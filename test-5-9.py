from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from core.texture import Texture
from geometry.rectangleGeometry import RectangleGeometry
from material.spriteMaterial import SpriteMaterial
from extras.movementRig import MovementRig
from extras.gridHelper import GridHelper

from math import floor

# render a basic scene
class Test(Base):

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera( aspectRatio=800/600)
        self.camera.setPosition( [0, 0, 1.5])
        
        self.rig = MovementRig()
        self.rig.add( self.camera )
        self.rig.setPosition( [0, 0.5, 3] )
        self.scene.add( self.rig )
        
        geometry = RectangleGeometry()
        tileSet = Texture("images/rolling-ball.png")
        spriteMaterial = SpriteMaterial(tileSet, 
            {"billboard"  : 1, 
             "tileCount"  : [4, 4],
             "tileNumber" : 0
            })

        #self.tilesPerSecond = 8
        self.tilesPerSecond = 4

        self.sprite = Mesh(geometry, spriteMaterial)
        self.scene.add( self.sprite )
        
        
        grid = GridHelper(size=20, gridColor=[1,1,1], centerColor=[0,1,0])
        #grid = GridHelper()
        grid.rotateX(-3.14/2)
        self.scene.add( grid )


    def update(self):
        #self.mesh.rotateY( 0.0514 )
        #self.mesh.rotateX( 0.0337 )
        tileNumber = floor(self.time * self.tilesPerSecond )
        self.sprite.material.uniforms["tileNumber"].data = tileNumber
        self.rig.update( self.input, self.deltaTime)
        self.renderer.render( self.scene, self.camera)
    

# instantiate this class and run the program
Test( screenSize=[800, 600] ).run()


        