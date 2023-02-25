from material.material import Material

class BrightFilterEffect(Material):
    def __init__(self, threshold=2.4):
        
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
            uniform float threshold;
            out vec4 fragColor;
            
            void main()
            {
                vec4 color = texture2D(texture, UV);
                if(color.r + color.g + color.b < threshold)
                    discard;
                
                fragColor = color;
            }
        """

        super().__init__(vertexShaderCode, fragmentShaderCode)
        
        self.addUniform("Sampler2D", "texture", [None, 1])
        self.addUniform("float", "threshold", threshold)

        self.locateUniforms()

