from geometry.geometry import Geometry
import numpy


class ParametricGeometry(Geometry):
    def __init__(self, uStart, uEnd, uResolution, vStart, vEnd, vResolution, surfaceFunction):
        super().__init__()
        # generate set of points on function
        deltaU = (uEnd - uStart) / uResolution
        deltaV = (vEnd - vStart) / vResolution
        positions = []
        
        for uIndex in range(uResolution+1):
            vArray = []
            for vIndex in range(vResolution+1):
                u = uStart + uIndex * deltaU
                v = vStart + vIndex * deltaV
                vArray.append( surfaceFunction(u, v) )
            positions. append(vArray)
        
        uvs = []
        uvData = []

        for uIndex in range(uResolution+1):
            vArray = []
            for vIndex in range(vResolution+1):
                u = uIndex/uResolution
                v = vIndex/vResolution
                vArray.append( [u, v] )
            uvs.append(vArray)


        # chapter 6-3
        def calcNormal(P0, P1, P2):
            v1 = numpy.array(P1) - numpy.array(P0)
            v2 = numpy.array(P2) - numpy.array(P0)
            normal = numpy.cross( v1, v2 )
            
            # Runtime warning: invalid value encountered in true_divide
            # norml = [0., 0., 0.]
            #print(normal)
            normal = normal / numpy.linalg.norm(normal)
            #print(normal)
            
            return normal
        
        
        vertexNormals = []
        for uIndex in range(uResolution + 1):
            vArray = []
            for vIndex in range(vResolution + 1):
                u = uStart + uIndex * deltaU
                v = vStart + vIndex * deltaV
                h = 0.0001
                P0 = surfaceFunction(u, v)
                P1 = surfaceFunction(u+h, v)
                P2 = surfaceFunction(u, v+h)
                normalVector = calcNormal(P0, P1, P2)
                vArray.append( normalVector )
            vertexNormals.append(vArray)


        # store vertex data
        positionData = []
        colorData = []

        # default vertex colors
        C1, C2, C3 = [1, 0, 0], [0, 1, 0], [0, 0, 1]
        C4, C5, C6 = [0, 1, 1], [1, 0, 1], [1, 1, 0]

        # chapter 6-3
        vertexNormalData = []
        faceNormalData = []

        # group vertex data into triangles
        # note: .copy() is necessary to avoid storing references
        for xIndex in range(uResolution):
            for yIndex in range(vResolution):
                # position data
                pA = positions[xIndex+0][yIndex+0]
                pB = positions[xIndex+1][yIndex+0]
                pD = positions[xIndex+0][yIndex+1]
                pC = positions[xIndex+1][yIndex+1]
                positionData += [ pA.copy(), pB.copy(), pC.copy(), pA.copy(), pC.copy(), pD.copy() ]

                # color data
                colorData += [C1,C2,C3, C4,C5,C6]

                #uv coordinates
                uvA = uvs[xIndex+0][yIndex+0]
                uvB = uvs[xIndex+1][yIndex+0]
                uvD = uvs[xIndex+0][yIndex+1]
                uvC = uvs[xIndex+1][yIndex+1]
                uvData += [uvA,uvB,uvC, uvA,uvC,uvD]

                # chapter 6-3
                # vertex normal vectors
                nA = vertexNormals[xIndex+0][yIndex+0]
                nB = vertexNormals[xIndex+1][yIndex+0]
                nD = vertexNormals[xIndex+0][yIndex+1]
                nC = vertexNormals[xIndex+1][yIndex+1]
                vertexNormalData += [nA,nB,nC, nA,nC,nD]

                # face normal vectors
                fn0 = calcNormal(pA, pB, pC)
                fn1 = calcNormal(pA, pC, pD)
                faceNormalData += [fn0,fn0,fn0, fn1,fn1,fn1]




        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.addAttribute("vec2", "vertexUV", uvData)

        # chapter 6-3
        self.addAttribute("vec3", "vertexNormal", vertexNormalData)
        self.addAttribute("vec3", "faceNormal", faceNormalData)

        self.countVertices()


        



        