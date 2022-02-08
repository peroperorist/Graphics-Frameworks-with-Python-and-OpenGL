from OpenGL.GL import *

class Uniform(object):

    def __init__(self, dataType, data):
        # type of dta:
        # int, bool, float, vec2, vec3, vec4
        self.dataType = dataType
        # data to be sent to uniform variable
        self.data = data
        # reference for variable location in program
        self.variableRef = None

    # get and store reference for program variable with given name
    def locateVariable(self, programRef, variableName):
        self.variableRef = glGetUniformLocation(programRef, variableName)

    # store data in uniform variable previously located
    def uploadData(self):
        # if the program does not reference the variable, then exit

        if self.variableRef == -1:
            return

        if self.dataType == "int":
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == "bool":
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == "float":
            glUniform1f(self.variableRef, self.data)
        elif self.dataType == "vec2":
            glUniform2f(self.variableRef, self.data[0], self.data[1])
        elif self.dataType == "vec3":
            glUniform3f(self.variableRef, self.data[0], self.data[1], self.data[2])
        elif self.dataType == "vec4":
            glUniform4f(self.variableRef, self.data[0], self.data[1], self.data[2], self.data[3])
        elif self.dataType == "mat4":
            glUniformMatrix4fv(self.variableRef, 1, GL_TRUE, self.data)
        elif self.dataType == "sampler2D":
            textureObjectRef, textureUnitRef = self.data
            # activate texture unit
            glActiveTexture( GL_TEXTURE0 + textureUnitRef )
            # associate texture object reference to currently active texture unit
            glBindTexture ( GL_TEXTURE_2D, textureObjectRef )
            # upload texture unit number (0...15) to uniform variable in shader
            glUniform1i (self.variableRef, textureUnitRef )
            
        

