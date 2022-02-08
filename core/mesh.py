from core.object3D import Object3D
from OpenGL.GL import *

class Mesh(Object3D):
    def __init__(self, geometry, material):
        super().__init__()

        self.geometry = geometry
        self.material = material
        
        # should this object be rendered?
        self.visible = True

        # set up associations between attributes stored in geometry and shader program stored in material
        self.vaoRef = glGenVertexArrays(1)
        #self.geometry.attributes = {}
        glBindVertexArray(self.vaoRef)
        for variableName, attributeObject in geometry.attributes.items():
            attributeObject.associateVariable(material.programRef, variableName)
            

        # unbind this vertex array object
        glBindVertexArray(0)