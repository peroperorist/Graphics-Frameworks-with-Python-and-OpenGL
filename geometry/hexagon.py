from geometry.polygonGeometry import PolygonGeometry

class HexagonGeometry(PolygonGeometry):
    def __init__(self, radius = 1):
        super().__init__(sides = 6, radius = radius)