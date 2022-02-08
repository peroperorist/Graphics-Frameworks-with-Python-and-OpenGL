from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *

# render two triangles with different positions and colors 

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

        ### render settings (optional) ###
        # set point width and height
        glPointSize(10)
        # set line width
        glLineWidth(4)

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
        self.translation1 = Uniform("vec3", [-0.5, 0.0, 0.0])
        self.translation1.locateVariable(self.programRef, "translation")

        self.translation2 = Uniform("vec3", [0.5, 0.0, 0.0])
        self.translation2.locateVariable(self.programRef, "translation")

        self.baseColor1 = Uniform("vec3", [1.0, 0.0, 0.0])
        self.baseColor1.locateVariable(self.programRef, "baseColor")
        self.baseColor2 = Uniform("vec3", [0.0, 0.0, 1.0])
        self.baseColor2.locateVariable(self.programRef, "baseColor")

    def update(self):
        # select program to use when rendering
        glUseProgram(self.programRef)
        # draw the first triangle
        self.translation1.uploadData()
        self.baseColor1.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)
        
        # draw the second triangle
        self.translation2.uploadData()
        self.baseColor2.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

# instantiate this class and run the program
Test().run()

