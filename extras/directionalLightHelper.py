from extras.gridHelper import GridHelper

class DirectionalLightHelper(GridHelper):

    def __init__(self, directionalLight):
        
        color = directionalLight.color
        super().__init__(size=1, divisions=4, gridColor=color, centerColor=[1, 1, 1])

        self.geometry.attributes["vertexPosition"].data += [[0, 0, 0], [0, 0, -10]]
        self.geometry.attributes["vertexColor"].data += [color, color]
        self.geometry.attributes["vertexPosition"].uploadData()
        self.geometry.attributes["vertexColor"].uploadData()
        
        self.geometry.countVertices()

