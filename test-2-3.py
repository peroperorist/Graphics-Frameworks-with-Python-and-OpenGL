from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *

# render a single point
class Test(Base):

    def initialize(self):
        print("Initializing program...")

        ### initialize program ###

        # vertex shader code
        vsCode = """
        in vec3 position;
        void main(){
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """

        # fragment shader code
        fsCode = """
        out vec4 fragColor;
        void main(){
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        # send code to GPU and compile; store program refrence
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        ### set up vertex array object ###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        ### render settings (optional) ###
        # set point width and height
        glLineWidth(4)

        ### set up Vertex attribute ###
        positionData = [[0.8, 0.0, 0.0],
                       [0.4, 0.6, 0.0],
                       [-0.4, 0.6, 0.0],
                       [-0.8, 0.0, 0.0],
                       [-0.4, -0.6, 0.0],
                       [0.4, -0.6, 0.0]]

        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")
        
    def update(self):
        # select program to use when rendering
        glUseProgram(self.programRef)
        # renders geometric objects using selected program
        #glDrawArrays(GL_LINE_LOOP, 0, self.vertexCount)
        #glDrawArrays(GL_LINES, 0, self.vertexCount)
        #glDrawArrays(GL_LINE_STRIP, 0, self.vertexCount)
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)


# instantiate this class and run the program
Test().run()

