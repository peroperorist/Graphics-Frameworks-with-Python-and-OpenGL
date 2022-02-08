from core.base import Base
from core.camera import Camera
from core.mesh import Mesh
from core.renderer import Renderer
from core.scene import Scene
from core.texture import Texture
from geometry.rectangleGeometry import RectangleGeometry
from material.textureMaterial import TextureMaterial


# render a basic scene
class Test(Base):

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera( aspectRatio=800/600)
        self.camera.setPosition( [0, 0, 2])

        geometry = RectangleGeometry()
        grid = Texture("images/grid.png")
        #material = SurfaceMaterial( {"useVertexColors": True} )
        material = TextureMaterial(grid)
        self.mesh = Mesh( geometry, material )
        self.scene.add( self.mesh )

    def update(self):    
        self.renderer.render( self.scene, self.camera)
    
# instantiate this class and run the program
Test( screenSize=[800, 600] ).run()


        