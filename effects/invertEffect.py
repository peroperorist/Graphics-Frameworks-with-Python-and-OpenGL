from material.material import Material

class InvertEffect(Material):
    def __init__(self):
        
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
            out vec4 fragColor;
            void main()
            {
                vec4 color = texture2D(texture, UV);
                vec4 invert = vec4(1 - color.r, 1 - color.g, 1 - color.b, 1);
                fragColor = invert;
            }
        """

        super().__init__(vertexShaderCode, fragmentShaderCode)
        self.addUniform("Sampler2D", "texture", [None, 1])
        self.locateUniforms()

