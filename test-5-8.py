from typing import Mapping
from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from core.matrix import Matrix
from core.texture import Texture
from extras.textTexture import TextTexture
from extras.movementRig import MovementRig
from geometry.rectangleGeometry import RectangleGeometry
from geometry.boxGeometry import BoxGeometry
from material.textureMaterial import TextureMaterial

# render a basic scene
class Test(Base):

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera( aspectRatio=800/600)
        # self.camera.setPosition( [0, 0, 4])

        self.rig = MovementRig()
        self.rig.add( self.camera )
        self.rig.setPosition( [0, 1, 5] )
        self.scene.add( self.rig )

        labelTexture = TextTexture(text=" This is a Crate. ", 
                              systemFontName="Arial Bold",
                              fontSize = 40,
                              fontColor = [0, 0, 200],
                              imageWidth = 256,
                              imageHeight = 128, 
                              alignHorizontal = 0.5,
                              alignVertical = 0.5,
                              imageBorderWidth = 4,
                              imageBorderColor = [255, 0, 0])

        
        labelMaterial = TextureMaterial(labelTexture)
        labelGeometry = RectangleGeometry(width=1, height=0.5)
        labelGeometry.applyMatrix( Matrix.makeRotationY(3.14) )
        self.label = Mesh(labelGeometry, labelMaterial)
        self.label.setPosition( [0, 1, 0] )
        self.scene.add(self.label)

        crateGeometry = BoxGeometry()
        crateTexture = Texture("images/crate.png")
        crateMaterial = TextureMaterial(crateTexture)
        crate = Mesh( crateGeometry, crateMaterial)
        self.scene.add( crate )
        

    def update(self):
        #self.mesh.rotateY( 0.0514 )
        #self.mesh.rotateX( 0.0337 )
        self.rig.update( self.input, self.deltaTime )
        self.label.lookAt( self.camera.getWorldPosition())

        self.renderer.render( self.scene, self.camera)
    

# instantiate this class and run the program
Test( screenSize=[800, 600] ).run()


        