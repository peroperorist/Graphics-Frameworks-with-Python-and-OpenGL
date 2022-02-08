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

        ### render settings (optional) ###
        # set point width and height
        glLineWidth(4)

        ### set up vertex array object - triangle ###
        self.vaoTri = glGenVertexArrays(1)
        glBindVertexArray(self.vaoTri)

        ### set up Vertex attribute ###
        positionDataTri = [[-0.5, 0.8, 0.0],
                       [-0.2, 0.2, 0.0],
                       [-0.8, 0.2, 0.0]]

        self.vertexCountTri = len(positionDataTri)
        positionAttributeTri = Attribute("vec3", positionDataTri)
        positionAttributeTri.associateVariable(self.programRef, "position")
        
        # set up vertex array object - square ###
        self.vaoSquare = glGenVertexArrays(1)
        glBindVertexArray(self.vaoSquare)
        positionDataSquare = [[0.8, 0.8, 0.0],
                              [0.8, 0.2, 0.0],
                              [0.2, 0.2, 0.0],
                              [0.2, 0.8, 0.0]]

        self.vertexCountSquare = len(positionDataSquare)
        positionAttributeSquare = Attribute("vec3", positionDataSquare)
        positionAttributeSquare.associateVariable(self.programRef, "position")


    def update(self):
        # select program to use when rendering
        glUseProgram(self.programRef)
        # renders geometric objects using selected program
        #glDrawArrays(GL_LINE_LOOP, 0, self.vertexCount)
        #glDrawArrays(GL_LINES, 0, self.vertexCount)
        #glDrawArrays(GL_LINE_STRIP, 0, self.vertexCount)

        # draw the triangle
        glBindVertexArray(self.vaoTri)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCountTri)
        # draw the square
        glBindVertexArray(self.vaoSquare)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCountSquare)
        

# instantiate this class and run the program
Test().run()

