from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.rectangleGeometry import RectangleGeometry
from geometry.boxGeometry import BoxGeometry
from material.textureMaterial import TextureMaterial
from extras.textTexture import TextTexture

# render a basic scene
class Test(Base):

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera( aspectRatio=800/600)
        # self.camera.setPosition( [0, 0, 1.5])

        self.camera.setPosition( [0, 0, 1.5])


        # geometry = RectangleGeometry()
        geometry = BoxGeometry()
        message = TextTexture(text="Python Graphics", 
                              systemFontName="Impact",
                              fontSize = 32,
                              fontColor = [0, 0, 200],
                              imageWidth = 256,
                              imageHeight = 256, 
                              alignHorizontal = 0.5,
                              alignVertical = 0.5,
                              imageBorderWidth = 4,
                              imageBorderColor = [255, 0, 0])

        #material = SurfaceMaterial( {"useVertexColors": True} )
        material = TextureMaterial(message)
        self.mesh = Mesh( geometry, material )
        self.scene.add( self.mesh )

    def update(self):
        #self.mesh.rotateY( 0.0514 )
        #self.mesh.rotateX( 0.0337 )
        self.mesh.rotateY( 0.0257 )
        self.mesh.rotateX( 0.0169 )
        self.renderer.render( self.scene, self.camera)
    

# instantiate this class and run the program
Test( screenSize=[800, 600] ).run()


        