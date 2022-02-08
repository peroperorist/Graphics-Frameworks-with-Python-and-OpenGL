from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from core.renderTarget import RenderTarget
from geometry.geometry import Geometry
from OpenGL.GL import *

class Postprocessor(object):
    
    def __init__(self, renderer, scene, camera, finalRenderTarget=None):
        self.renderer = renderer
        self.sceneList = [scene]
        self.cameraList = [camera]
        self.renderTargetList = [ finalRenderTarget ]
        self.finalRenderTarget = finalRenderTarget
        self.orthoCamera = Camera()
        self.orthoCamera.setOrthographic() 
        
        # aligned with clip space by default
        # generate a rectangle already aligned with clip space;
        # no matrix transformations will be applied
        self.rectangleGeo = Geometry()
        P0, P1, P2, P3 = [-1, -1], [1, -1], [-1, 1], [1, 1]
        T0, T1, T2, T3 = [ 0,  0], [1,  0], [ 0, 1], [1, 1]
        positionData = [P0,P1,P3, P0,P3,P2]
        uvData = [T0,T1,T3, T0,T3,T2]
        self.rectangleGeo.addAttribute("vec2", "vertexPosition", positionData)
        self.rectangleGeo.addAttribute("vec2", "vertexUV", uvData)
        self.rectangleGeo.countVertices()

    def addEffect(self, effect):
        postScene = Scene()
        resolution = self.renderer.windowSize
        target = RenderTarget(resolution)

        # change the previous entry in the render target list to this newly created render target
        self.renderTargetList[-1] = target
        # the effect in this render pass will use the texture that was written to in the previous render pass
        effect.uniforms["texture"].data[0] = target.texture.textureRef
        mesh = Mesh( self.rectangleGeo, effect )
        postScene.add( mesh )

        self.sceneList.append( postScene )
        self.cameraList.append( self.orthoCamera )
        self.renderTargetList.append( self.finalRenderTarget )


    def render(self):
        passes = len(self.sceneList)
        for n in range( passes ):
            scene = self.sceneList[n]
            camera = self.cameraList[n]
            target = self.renderTargetList[n]
            self.renderer.render( scene, camera, renderTarget=target)
            
        
        
