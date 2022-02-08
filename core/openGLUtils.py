from OpenGL.GL import *

#static methods to load and compile OpenGL shaders and link to create programs
class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):

        #specify required OpenGL/GLSL version
        shaderCode = '#version 330\n' + shaderCode

        #create empty shader object and return reference value
        shaderRef = glCreateShader(shaderType)

        #stores the source code in the shader
        glShaderSource(shaderRef, shaderCode)
        # compiles source code previously stored in the shader object
        glCompileShader(shaderRef)

        # queries whether shader compile was sucdessful
        compileSuccess = glGetShaderiv(shaderRef, GL_COMPILE_STATUS)

        if not compileSuccess:
            # retrieve error message
            errorMessage = glGetShaderInfoLog(shaderRef)
            # free memory used to store shader program
            glDeleteShader(shaderRef)
            # convert byte string to character string
            errorMessage = '\n' + errorMessage.decode('utf-8')

            # raise exception: halt program and print error message
            raise Exception(errorMessage)

        # compilation was successful: return shader reference value
        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):
        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL_FRAGMENT_SHADER)

        # create empty program object and store reference to it
        programRef = glCreateProgram()

        # attach previously compiled shader programs
        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)

        # link vertex shader to fragment shader
        glLinkProgram(programRef)

        # queries whether program link was successful
        linkSuccess = glGetProgramiv(programRef, GL_LINK_STATUS)

        if not linkSuccess:
            # retrieve error message
            errorMessage = glGetProgramInfoLog(programRef)
            # free memory used to store program
            glDeleteProgram(programRef)
            # convert byte string to character string
            errorMessage = '\n' + errorMessage.decode('utf-8')
            # raise exception: halt aplication and print error message
            raise Exception(errorMessage)

        # linking was successful, return program refrence value

        return programRef

    @staticmethod
    def printSystemInfo():
        print(" Vendor: " + glGetString(GL_VENDOR).decode('utf-8'))
        print(" Renderer: " + glGetString(GL_RENDERER).decode('utf-8'))
        print(" OpenGL version supported: " + glGetString(GL_VERSION).decode('utf-8'))
        print(" GLSL version supported: " + glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8'))
        




