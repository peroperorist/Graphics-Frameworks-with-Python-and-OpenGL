from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *

# render shapes with vertex colors
class Test(Base):

    def initialize(self):
        print("Initializing program...")

        ### initialize program ###

        # vertex shader code
        vsCode = """
        in vec3 position;
        in vec3 vertexColor;
        out vec3 color;
        void main(){
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
            color = vertexColor;
        }
        """

        # fragment shader code
        fsCode = """
        in vec3 color;
        out vec4 fragColor;
        void main(){
            fragColor = vec4(color.r, color.g, color.b, 1.0);
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
        positionData = [[0.8, 0.0, 0.0],
                       [0.4, 0.6, 0.0],
                       [-0.4, 0.6, 0.0],
                       [-0.8, 0.0, 0.0],
                       [-0.4, -0.6, 0.0],
                       [0.4, -0.6, 0.0]]

        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")
        
        colorData = [[1.0, 0.0, 0.0],
                       [1.0, 0.5, 0.0],
                       [1.0, 1.0, 0.0],
                       [0.0, 1.0, 0.0],
                       [0.0, 0.0, 1.0],
                       [0.5, 0.0, 1.0]]

        colorAttribute = Attribute("vec3", colorData)
        colorAttribute.associateVariable(self.programRef, "vertexColor")
        

        


    def update(self):
        # select program to use when rendering
        glUseProgram(self.programRef)
        # renders geometric objects using selected program
        #glDrawArrays(GL_POINTS, 0, self.vertexCount)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)
        
        

# instantiate this class and run the program
Test().run()

