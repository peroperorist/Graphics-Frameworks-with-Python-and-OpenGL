from material.basicMaterial import BasicMaterial
from OpenGL.GL import *

class PointMaterial(BasicMaterial):

    def __init__(self, properties={}):
        super().__init__()

        # render vertices as points 
        self.settings["drawStyle"] = GL_POINTS
        # width and height of points, in pixels
        self.settings["pointSize"] = 8
        # draw points as rounded
        self.settings["roundedPoints"] = False

        self.setProperties(properties)
    
    def updateRenderSettings(self):
        glPointSize(self.settings["pointSize"])
        if self.settings["roundedPoints"]:
            glEnable(GL_POINT_SMOOTH)
        else:
            glDisable(GL_POINT_SMOOTH)
    
    
