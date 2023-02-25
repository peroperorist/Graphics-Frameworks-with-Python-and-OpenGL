from light.light import Light

class DirectionalLight(Light):

    def __init__(self, color = [1, 1, 1], direction = [0, -1, 0]):
        
        super().__init__(Light.DIRECTIONAL)
        self.color = color
        self.setDirection( direction )
        