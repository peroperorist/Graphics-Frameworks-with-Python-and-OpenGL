from geometry.cylindricalGeometry import CylindricalGeometry

class CylinderGeometry(CylindricalGeometry):
    def __init__(self, radius=1, height=1, radialSegments=32, heightSegments=4, closed=True):
        
        super().__init__(radius, radius, height, radialSegments, heightSegments, closed, closed)

