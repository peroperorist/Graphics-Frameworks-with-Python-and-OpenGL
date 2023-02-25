from material.material import Material

class AdditiveBlendEffect(Material):
    def __init__(self, blendTexture=None, originalStrength=1, blendStrength=1):
        
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
            uniform sampler2D blendTexture;
            uniform float originalStrength;
            uniform float blendStrength;
            out vec4 fragColor;
            
            void main()
            {
                vec4 originalColor = texture2D(texture, UV);
                vec4 blendColor = texture2D(blendTexture, UV);
                vec4 color = originalStrength * originalColor + blendStrength * blendColor;

                fragColor = color;
            }
        """

        super().__init__(vertexShaderCode, fragmentShaderCode)
        self.addUniform("Sampler2D", "texture", [None, 1])
        self.addUniform("sampler2D", "blendTexture", [blendTexture.textureRef, 2])
        self.addUniform("float", "originalStrength", originalStrength)
        self.addUniform("float", "blendStrength", blendStrength)
        

        self.locateUniforms()

