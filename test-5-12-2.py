from core.base import Base
from core.renderTarget import RenderTarget
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from core.texture import Texture
from geometry.sphereGeometry import SphereGeometry
from geometry.rectangleGeometry import RectangleGeometry
from material.textureMaterial import TextureMaterial
from extras.movementRig import MovementRig
from extras.postprocessor import Postprocessor
from effects.tintEffect import TintEffect
from effects.colorReduceEffect import ColorReduceEffect
from effects.pixelateEffect import PixelateEffect
from effects.invertEffect import InvertEffect
from effects.vignetteEffect import vignetteEffect
from OpenGL.GL import *
from material.surfaceMaterial import SurfaceMaterial

# render a basic scene
class Test(Base):

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer(clearColor=[0, 0, 0])
        self.scene = Scene()
        self.camera = Camera( aspectRatio=800/600)
        #elf.camera.setPosition( [0, 0, 4])

        self.rig = MovementRig()
        self.rig.add( self.camera )
        self.scene.add( self.rig )
        self.rig.setPosition( [0, 1, 4] )
        skyGeometry = SphereGeometry(radius=50)
        skyMaterial = TextureMaterial( Texture("images/sky-earth.jpg"))
        sky = Mesh( skyGeometry, skyMaterial)
        self.scene.add(sky)

        sphereGeometry = SphereGeometry()
        sphereMaterial = TextureMaterial( Texture("images/grid.png"))
        self.sphere = Mesh( sphereGeometry, sphereMaterial)
        self.sphere.setPosition([0,1,0])
        self.scene.add(self.sphere)



        grassGeometry = RectangleGeometry(width=100, height=100)
        grassMaterial = TextureMaterial( Texture("images/grass.jpg"), {"repeatUV": [50, 50]})
        grass = Mesh ( grassGeometry, grassMaterial)
        grass.rotateX(-3.14/2)
        self.scene.add(grass)
        

        
        self.postprocessor = Postprocessor(self.renderer, self.scene, self.camera)
        #err = glGetError()
        #if ( err != GL_NO_ERROR ):
        #    print('GLERROR: ', gluErrorString( err ))
        
        #self.postprocessor.addEffect( TintEffect(tintColor=[0, 1, 0]))
        #err = glGetError()
        #if ( err != GL_NO_ERROR ):
        #    print('GLERROR: ', gluErrorString( err ))
        #self.postprocessor.addEffect( ColorReduceEffect(levels=5))
        self.postprocessor.addEffect( PixelateEffect(resolution=[800, 600]))
        
        
        #self.postprocessor.addEffect( InvertEffect() )
        #self.postprocessor.addEffect( vignetteEffect())
      
    

    def update(self):
        #self.mesh.rotateY( 0.0514 )
        #self.mesh.rotateX( 0.0337 )
        self.rig.update(self.input, self.deltaTime)
        self.sphere.rotateY( 0.01337 )
        #self.renderer.render( self.scene, self.camera)
        self.postprocessor.render()
        

# instantiate this class and run the program
Test( screenSize=[800, 600] ).run()


        