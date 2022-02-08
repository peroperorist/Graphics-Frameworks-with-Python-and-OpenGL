from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.rectangleGeometry import RectangleGeometry
from material.material import Material

# render a basic scene
class Test(Base):

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera( aspectRatio=800/600)
        self.camera.setPosition( [0, 0, 1.5])

        vsCode = """
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        in vec3 vertexPosition;
        in vec2 vertexUV;
        out vec2 UV;

        void main()
        {
            vec4 pos = vec4(vertexPosition, 1.0);
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * pos;
            UV = vertexUV;
        }


        """

        fsCode = """
        // return a random value in [0, 1]
        float random(vec2 UV)
        {
            return fract(235711.0 * sin(14.337 * UV.x + 42.418 * UV.y));
        }

        in vec2 UV;
        out vec4 fragColor;
        void main()
        {
            float r = random(UV);
            fragColor = vec4(r, r, r, 1);
        }
        """


        geometry = RectangleGeometry()
        material = Material( vsCode, fsCode)
        material.locateUniforms()

        self.mesh = Mesh( geometry, material )
        self.scene.add( self.mesh )

    def update(self):
        #self.mesh.rotateY( 0.0514 )
        #self.mesh.rotateX( 0.0337 )
        
        self.renderer.render( self.scene, self.camera)
    

# instantiate this class and run the program
Test( screenSize=[800, 600] ).run()


        