from material.material import Material

class TintEffect(Material):
    def __init__(self, tintColor=[1,0,0]):
        
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
            uniform vec3 tintColor;
            uniform sampler2D texture;
            out vec4 fragColor;
            void main()
            {
                vec4 color = texture2D(texture, UV);
                float gray = (color.r + color.g + color.b) / 3.0;
                fragColor = vec4(gray * tintColor, 1.0);
                
            }
        """

        super().__init__(vertexShaderCode, fragmentShaderCode)
        self.addUniform("Sampler2D", "texture", [None, 1])
        self.addUniform("vec3", "tintColor", tintColor)
        self.locateUniforms()

