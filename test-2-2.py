from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *

# render a single point
class Test(Base):

    def initialize(self):
        print("Initializing program...")

        ### initialize program ###

        # vertex shader code
        vsCode = """
        void main(){
            gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
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
        glPointSize(10)
    
    def update(self):
        # select program to use when rendering
        glUseProgram(self.programRef)
        # renders geometric objects using selected program
        glDrawArrays(GL_POINTS, 0, 1)


# instantiate this class and run the program
Test().run()

