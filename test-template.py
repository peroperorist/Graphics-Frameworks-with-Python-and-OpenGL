from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.boxGeometry import BoxGeometry
from core.texture import Texture
from geometry.rectangleGeometry import RectangleGeometry
from material.surfaceMaterial import SurfaceMaterial

# chapter 6
from geometry.sphereGeometry import SphereGeometry
from light.ambientLight import AmbientLight
from light.directionalLight import DirectionalLight
from light.pointLight import PointLight
from material.flatMaterial import FlatMaterial
from material.lambertMaterial import LambertMaterial
from material.phongtMaterial import PhongMaterial



# render a basic scene
class Test(Base):

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera( aspectRatio=800/600)
        self.camera.setPosition( [0, 0, 4])

        geometry = BoxGeometry()
        #material = SurfaceMaterial( {"useVertexColors": True} )
        material = SurfaceMaterial( 
            {"useVertexColors": True,
             "wireframe":       True,
             "lineWidth":       8} )
        
        self.mesh = Mesh( geometry, material )
        self.scene.add( self.mesh )

    def update(self):
        #self.mesh.rotateY( 0.0514 )
        #self.mesh.rotateX( 0.0337 )
        
        self.renderer.render( self.scene, self.camera)
    

# instantiate this class and run the program
Test( screenSize=[800, 600] ).run()


        