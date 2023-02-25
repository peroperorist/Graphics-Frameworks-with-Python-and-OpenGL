from core.camera import Camera
from core.renderTarget import RenderTarget
from material.depthMaterial import DepthMaterial
from OpelGL.GL import *

class Shadow(object):

    def __init__(self, lightSource, strength=0.5, resolution=[512,512], cameraBounds=[-5,5, -5,5, 0,20], bias=0.01):

        super().__init__()

        # must be directiona light
        self.lightSource = lightSource

        # camera used to render scene from perspective of light
        self.camera = Camera()
        left, right, bottom, top, near, far = cameraBounds
        self.camera.setOrthographic(left, right, bottom, top, near, far)
        self.lightSource.add( self.camera )
        
        # target used during the shadow pass, contains depth texture
        self.renderTarget = RenderTarget( resolution, properties={"wrap": GL_CLAMP_TO_BORDER} )
        # render only depth data to target texture
        self.material = DepthMaterial()
        # controls darkness of shadow
        self.strength = strength
        # used to avoide visual artifacts due to rounding/sampling precision issues
        self.bias = bias

    def updateInternal(self):
        self.camera.updateViewMatrix()
        self.material.uniforms["viewMatrix"].data = self.camera.viewMatrix
        self.material.uniforms["projectionMatrix"].data = self.camera.projectionMatrix



