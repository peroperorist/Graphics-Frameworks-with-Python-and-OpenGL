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
    # update for chapter 6-4
    def locateVariable(self, programRef, variableName):
        if self.dataType == "Light":
            self.variableRef = {}
            self.variableRef["lightType"] = glGetUniformLocation(programRef, variableName + ".lightType")
            self.variableRef["color"] = glGetUniformLocation(programRef, variableName + ".color")
            self.variableRef["direction"] = glGetUniformLocation(programRef, variableName + ".direction")
            self.variableRef["position"] = glGetUniformLocation(programRef, variableName + ".position")
            self.variableRef["attenuation"] = glGetUniformLocation(programRef, variableName + ".attenuation")
        
        # chapter 6-9
        elif self.dataType == "Shadow":
            self.variableRef = {}
            self.variableRef["lightDirection"] = glGetUniformLocation(progamRef, variableName + ".lightDirection")
            self.variableRef["projectionMatrix"] = glGetUniformLocation(programRef, variableName + ".projectionMatrix")
            self.variableRef["viewMatrix"] = glGetUniformLocation(programRef, variableName + ".viewMatrix")
            self.variableRef["depthTexture"] = glGetUniformLocation(programRef, variableName + ".depthTexture")
            self.variableRef["strength"] = glGetUniformLocation(programRef, variableName + ".strength")
            self.variableRef["bias"] = glGetUniformLocation(programRef, variableName + ".bias")
            
            
            

        else:
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
        elif self.dataType == "Light":
            glUniform1i( self.variableRef["lightType"], self.data.lightType)
            glUniform3f( self.variableRef["color"], self.data.color[0], self.data.color[1], self.data.color[2])
            direction = self.data.getDirection()
            glUniform3f( self.variableRef["direction"], direction[0], direction[1], direction[2] )
            position = self.data.getPosition()
            glUniform3f( self.variableRef["position"], position[0], position[1], position[2] )
            glUniform3f( self.variableRef["attenuation"], self.data.attenuation[0],self.data.attenuation[1],self.data.attenuation[2] )
            
        # chaper 6-9
        elif self.dataType == "Shadow":
            direction = self.data.lightSource.getDirection()
            glUniform3f( self.variableRef["lightDirection"], direction[0], direction[1], direction[2] )
            glUniformMatrix4fv( self.variableRef["projectionMatrix"], 1, GL_TRUE, self.data.camera.projectionMatrix)
            glUniformMatrix4fv( self.variableRef["viewMatrix"], 1, GL_TRUE, self.data.camera.viewMatrix)

            # configure depth texture
            textureObjectRef = self.data.renderTarget.texture.textureRef
            textureUnitRef = 15
            glActiveTexture( GL_TEXTURE0 + textureUnitRef )
            glBindTexture( GL_TEXTURE_2D, textureObjectRef )
            glUniform1i( self.variableRef["depthTexture"], textureUnitRef )
            glUniform1f( self.variableRef["strength"], self.data.strength )
            glUniform1f( self.variableRef["bias"], self.data.bias )

            

