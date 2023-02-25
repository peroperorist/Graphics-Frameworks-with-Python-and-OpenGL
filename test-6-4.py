from math import sinh
from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from core.texture import Texture
from core.renderTarget import RenderTarget
from geometry.sphereGeometry import SphereGeometry
from geometry.rectangleGeometry import RectangleGeometry
from material.textureMaterial import TextureMaterial
from material.surfaceMaterial import SurfaceMaterial
from extras.movementRig import MovementRig
from extras.postprocessor import Postprocessor
from effects.brightFilterEffect import BrightFilterEffect
from effects.horizontalBlurEffect import HorizontalBlurEffect
from effects.verticalBlurEffect import VerticalBlurEffect
from effects.additiveBlendEffect import AdditiveBlendEffect

# render a basic scene
class Test(Base):

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer(clearColor=[0,0,0])
        self.scene = Scene()
        self.camera = Camera( aspectRatio=800/600)
        self.camera.setPosition( [0, 0, 4])

        self.rig = MovementRig()
        self.rig.add( self.camera )
        self.scene.add( self.rig )
        #self.rig.setPosition( [0, 1, 4] )
        self.rig.setPosition( [0, 1, 3] )
        skyGeometry = SphereGeometry(radius=50)
        skyMaterial = TextureMaterial( Texture("images/sky-earth.jpg"))
        sky = Mesh( skyGeometry, skyMaterial)
        self.scene.add (sky)

        sphereGeometry = SphereGeometry()
        sphereMaterial = TextureMaterial( Texture("images/grid.png"))
        self.sphere = Mesh( sphereGeometry, sphereMaterial)
        self.sphere.setPosition([0,1,0])
        self.scene.add (self.sphere)



        grassGeometry = RectangleGeometry(width=100, height=100)
        grassMaterial = TextureMaterial( Texture("images/grass.jpg"), {"repeatUV": [50, 50]})
        grass = Mesh ( grassGeometry, grassMaterial)
        grass.rotateX(-3.14/2)
        self.scene.add(grass)
        
        # glow scene
        self.glowScene = Scene()
        redMaterial = SurfaceMaterial({"baseColor": [1, 0, 0 ]})
        glowSphere = Mesh(sphereGeometry, redMaterial)
        glowSphere.transform = self.sphere.transform
        self.glowScene.add( glowSphere )

        #glow postprocessing
        glowTarget = RenderTarget( resolution=[800, 600] )
        self.glowPass = Postprocessor(self.renderer, self.glowScene, self.camera, glowTarget)
        self.glowPass.addEffect( HorizontalBlurEffect(textureSize=[800, 600], blurRadius=50) )
        self.glowPass.addEffect( VerticalBlurEffect(textureSize=[800, 600], blurRadius=50) )
        
        # combining results of glow effect with main scene
        self.comboPass = Postprocessor(self.renderer, self.scene, self.camera) 
        self.comboPass.addEffect( AdditiveBlendEffect(glowTarget.texture, originalStrength=1, blendStrength=3) )
        

        
    def update(self):
        #self.mesh.rotateY( 0.0514 )
        #self.mesh.rotateX( 0.0337 )
        self.rig.update(self.input, self.deltaTime)
        self.glowPass.render()
        self.comboPass.render()

# instantiate this class and run the program
Test( screenSize=[800, 600] ).run()


        