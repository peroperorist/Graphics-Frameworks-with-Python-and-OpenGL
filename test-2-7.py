from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *

# animate trianble moving across screen
class Test(Base):

    def initialize(self):
        print("Initializing program...")

        ### initialize program ###

        # vertex shader code
        vsCode = """
        in vec3 position;
        uniform vec3 translation;
        void main(){
            vec3 pos = position + translation;
            gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
        }
        """

        # fragment shader code
        fsCode = """
        uniform vec3 baseColor;
        out vec4 fragColor;
        void main(){
            fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
        }
        """

        # send code to GPU and compile; store program refrence
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
        # specify color used when clearly
        glClearColor(0.0, 0.0, 0.0, 1.0)

        ### render settings (optional) ###
        # set point width and height
        #glPointSize(10)
        # set line width
        #glLineWidth(4)



        ### set up vertex array object ###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        ### set up Vertex attribute ###
        positionData = [[0.0, 0.2, 0.0],
                       [0.2, -0.2, 0.0],
                       [-0.2, -0.2, 0.0]]

        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")
        
        ### set up uniforms ###
        self.translation = Uniform("vec3", [-0.5, 0.0, 0.0])
        self.translation.locateVariable(self.programRef, "translation")

        self.baseColor = Uniform("vec3", [1.0, 0.0, 0.0])
        self.baseColor.locateVariable(self.programRef, "baseColor")
        
    def update(self):
        # increase x coordinate of tlanslation
        self.translation.data[0] += 0.01
        # if triangle passes off-screen on the right, change translation so it reappears on the left
        if self.translation.data[0] > 1.2:
            self.translation.data[0] = -1.2

        ### render scene ###
        # reset color buffr with specified color
        glClear(GL_COLOR_BUFFER_BIT)
        # select program to use when rendering
        glUseProgram(self.programRef)
        # draw the first triangle
        self.translation.uploadData()
        self.baseColor.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

# instantiate this class and run the program
Test().run()

