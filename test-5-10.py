from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from core.texture import Texture
from geometry.rectangleGeometry import RectangleGeometry
from geometry.boxGeometry import BoxGeometry
from material.textureMaterial import TextureMaterial
from extras.movementRig import MovementRig
from extras.gridHelper import GridHelper

# render a basic scene
class Test(Base):

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera( aspectRatio=800/600)
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.setPosition( [0, 0.5, 3] )
        self.scene.add( self.rig )

        crateGeometry = BoxGeometry()
        crateMaterial = TextureMaterial( Texture("images/crate.png"))
        crate = Mesh(crateGeometry, crateMaterial)
        self.scene.add( crate )

        grid = GridHelper( gridColor=[1, 1, 1], centerColor=[1, 1, 0])
        grid.rotateX( -3.14/2 )
        self.scene.add( grid )

        # HUD Layer
        self.hudScene = Scene()
        self.hudCamera = Camera()
        self.hudCamera.setOrthographic(0,800, 0,600, 1, -1)
        labelGeo1 = RectangleGeometry(width=600, height=80, position=[0, 600], alignment=[0, 1])
        labelMat1 = TextureMaterial( Texture("images/crate-sim.png") )
        label1 = Mesh(labelGeo1, labelMat1)
        self.hudScene.add( label1 )
        
        labelGeo2 = RectangleGeometry(width=400, height=80, position=[800, 0], alignment=[1, 0])
        labelMat2 = TextureMaterial( Texture("images/version-1.png") )
        label2 = Mesh(labelGeo2, labelMat2)
        self.hudScene.add( label2 )

    def update(self):
        #self.mesh.rotateY( 0.0514 )
        #self.mesh.rotateX( 0.0337 )
        self.rig.update( self.input, self.deltaTime )
        self.renderer.render( self.scene, self.camera )
        self.renderer.render( self.hudScene, self.hudCamera, clearColor=False)
    

# instantiate this class and run the program
Test( screenSize=[800, 600] ).run()


        