from material.material import Material

class PixelateEffect(Material):
    def __init__(self, pixelSize = 8, resolution = [512,512]):
        
        vertexShaderCode = """
            in vec2 vertexPosition;
            in vec2 vertexUV;
            out vec2 UV;

            void main()
            {
                gl_Position = vec4(vertexPosition, 0.0, 1.0);
                UV = vertexUV;
            }
        """

        fragmentShaderCode = """
            in vec2 UV;
            uniform sampler2D texture;
            uniform float pixelSize;
            uniform vec2 resolution;
            out vec4 fragColor;
            void main()
            {
                vec2 factor = resolution / pixelSize;
                vec2 newUV = floor( UV * factor ) / factor;
                vec4 color = texture2D(texture, newUV);
                fragColor = color;
            }
        """

        super().__init__(vertexShaderCode, fragmentShaderCode)
        self.addUniform("Sampler2D", "texture", [None, 1])
        self.addUniform("float", "pixelSize", pixelSize)
        self.addUniform("vec2", "resolution", resolution)
        self.locateUniforms()

