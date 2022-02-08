from geometry.parametricGeometry import ParametricGeometry

class PlaneGeometry(ParametricGeometry):
    def __init__(self, width=1, height=1, widthSegments=8, heightSegments=8):

        def S(u, v):
            return [u, v, 0]
        
        super().__init__(-width/2, width/2, widthSegments, -height/2, height/2, heightSegments, S)


