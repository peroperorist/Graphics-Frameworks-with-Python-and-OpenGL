from light.light import Light

class PointLight(Light):

    def __init__(self, color = [1,1,1], position = [0,0,0], attenuation = [1,0,0.1] ):

        super().__init__(Light.POINT)
        self.color = color
        self.setPosition( position )
        self.attenuation = attenuation

