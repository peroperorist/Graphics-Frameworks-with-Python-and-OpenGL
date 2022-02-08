from geometry.cylindricalGeometry import CylindricalGeometry

class PyramidGeometry(CylindricalGeometry):
    def __init__(self, radius=1, height=1, sides=4, heightSegments=4, closed=True):

        super().__init__(0, radius, height, sides, heightSegments, False, closed)

