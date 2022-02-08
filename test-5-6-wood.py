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

        float boxRandom(vec2 UV, float scale){
            vec2 iScaleUV = floor(scale * UV);
            return random(iScaleUV);
        }

        float smoothRandom(vec2 UV, float scale)
        {
            vec2 iScaleUV = floor(scale * UV);
            vec2 fScaleUV = fract(scale * UV);
            float a = random(iScaleUV);
            float b = random(round(iScaleUV + vec2(1, 0)));
            float c = random(round(iScaleUV + vec2(0, 1)));
            float d = random(round(iScaleUV + vec2(1, 1)));
            return mix ( mix(a, b, fScaleUV.x), mix(c, d, fScaleUV.x), fScaleUV.y);
        }

        // add smooth random values at different scales weighted (amplitudes) so that sum is approximately 1.0
        float fractalRandom(vec2 UV, float scale)
        {
            float value = 0.0;
            float amplitude = 0.5;

            for (int i = 0; i < 6; i++)
            {
                value += amplitude * smoothRandom(UV, scale);
                scale *= 2.0;
                amplitude *= 0.5;
            }
            return value;
        }


        in vec2 UV;
        out vec4 fragColor;
        void main()
        {
            float t = 80 * UV.y + 20 * fractalRandom(UV, 2);
            float r = clamp( 2 * abs(sin(t)), 0, 1);
            vec4 color1 = vec4(0.3, 0.2, 0.0, 1.0);
            vec4 color2 = vec4(0.6, 0.4, 0.2, 1.0);
            fragColor = mix(color1, color2, r);
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


        