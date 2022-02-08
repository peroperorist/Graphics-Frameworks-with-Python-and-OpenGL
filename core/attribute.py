from OpenGL.GL import *
import numpy

class Attribute(object):

    def __init__(self, dataType, data):
        # type of elements in data array: int, float, ve2, vec3, vec4
        self.dataType = dataType

        # arrya of data to be stored in buffer
        self.data = data

        # reference of available bufer from GPU
        self.bufferRef = glGenBuffers(1)

        # upload data immediately
        self.uploadData()

    #uploda this data to a GPU buffer
    def uploadData(self):

        # convert data to numpy array format
        # convert numbers to 32 bit floats
        data = numpy.array(self.data).astype(numpy.float32)

        # select buffer used by the following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        # store data in currently bound buffer
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

    # associate varibale in program with this buffer
    def associateVariable(self, programRef, variableName):

        # get refrence for program variable with given name
        variableRef = glGetAttribLocation(programRef, variableName)
        #print(variableName, variableRef)
        # if the program does not reference the variable, then exit
        if variableRef == -1:
            return

        # select buffer used by the following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        # specify how data will be read from the currently bound buffer into the specified variable

        if self.dataType == "int":
            glVertexAttribPointer(variableRef, 1, GL_INT, False, 0, None)
        elif self.dataType == "float":
            glVertexAttribPointer(variableRef, 1, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec2":
            glVertexAttribPointer(variableRef, 2, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec3":
            glVertexAttribPointer(variableRef, 3, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec4":
            glVertexAttribPointer(variableRef, 4, GL_FLOAT, False, 0, None)
        else:
            raise Exception("Attribute " + variableName + " has unknown type " + self.dataType)

        # indicate that data will be streamed to this variable
        glEnableVertexAttribArray(variableRef)








