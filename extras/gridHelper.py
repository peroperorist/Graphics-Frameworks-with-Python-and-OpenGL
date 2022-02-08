from core.mesh import Mesh
from geometry.geometry import Geometry
from material.lineMaterial import LineMaterial

class GridHelper(Mesh):
    def __init__(self, size=10, divisions=10, gridColor=[0,0,0], centerColor=[0.5, 0.5, 0.5], lineWidth=1):
        geo = Geometry()

        positionData = []
        colorData = []

        # create range of values
        values = []
        deltaSize = size/divisions
        for n in range(divisions+1):
            values.append( -size/2 + n * deltaSize)

        #print(values)

        # add vertical lines
        for x in values:
            positionData.append( [x, -size/2, 0] )
            positionData.append( [x,  size/2, 0] )
            #print(x, ",", (-size/2))
            #print(x, ",", (size/2))
            
            if x == 0:
                colorData.append(centerColor)
                colorData.append(centerColor)
            else:
                colorData.append(gridColor)
                colorData.append(gridColor)
        
        # add horizontal lines
        for y in values:
            positionData.append( [-size/2, y, 0])
            positionData.append( [ size/2, y, 0])
            #print((-size/2), ",", y )
            #print((size/2), ",", y )
            if y == 0:
                colorData.append(centerColor)
                colorData.append(centerColor)
            else:
                colorData.append(gridColor)
                colorData.append(gridColor)
        
        geo.addAttribute("vec3", "vertexPosition", positionData)
        geo.addAttribute("vec3", "vertexColor", colorData)
        geo.countVertices()

        mat = LineMaterial({
            "useVertexColors": True,
            "lineWidth":       lineWidth,
            "lineType":        "segments"
        })

        #print(colorData)
        # initialize the mesh 
        super().__init__(geo, mat)