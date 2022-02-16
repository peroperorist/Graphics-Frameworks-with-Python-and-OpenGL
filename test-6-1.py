from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.boxGeometry import BoxGeometry
from material.surfaceMaterial import SurfaceMaterial
from core.texture import Texture

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
        self.camera.setPosition( [0, 0, 6])

        ambient = AmbientLight( color=[0.1, 0.1, 0.1] )
        self.scene.add( ambient )
        directional = DirectionalLight( color=[0.8, 0.8, 0.8], direction=[-1, -1, -2] )
        self.scene.add( directional )
        point = PointLight( color=[0.9, 0, 0], position=[1, 1, 0.8] )
        self.scene.add( point )

        sphereGeometry = SphereGeometry()
        flatMaterial = FlatMaterial( properties={ "baseColor" : [0.6, 0.2, 0.2] } )
        grid = Texture("images/grid.png")
        lambertMaterial = LambertMaterial( texture=grid )
        phongMaterial = PhongMaterial( properties={ "baseColor" : [0.5, 0.5, 1] } )
        
        sphere1 = Mesh(sphereGeometry, flatMaterial)
        sphere1.setPosition( [-2.2, 0, 0] )
        self.scene.add( sphere1 )

        sphere2 = Mesh(sphereGeometry, lambertMaterial)
        sphere2.setPosition( [0, 0, 0] )
        self.scene.add( sphere2 )

        sphere3 = Mesh(sphereGeometry, phongMaterial)
        sphere3.setPosition( [2.2, 0, 0] )
        self.scene.add( sphere3 )



    def update(self):
        #self.mesh.rotateY( 0.0514 )
        #self.mesh.rotateX( 0.0337 )
        
        self.renderer.render( self.scene, self.camera)
    

# instantiate this class and run the program
Test( screenSize=[800, 600] ).run()


        