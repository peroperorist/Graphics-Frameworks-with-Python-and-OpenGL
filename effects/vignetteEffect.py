from material.material import Material

class vignetteEffect(Material):
    def __init__(self, dimStart=0.4, dimEnd=1.0, dimColor=[0,0,0]):
        
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
            uniform float dimStart;
            uniform float dimEnd;
            uniform vec3 dimColor;
            out vec4 fragColor;

            void main()
            {
                vec4 color = texture2D(texture, UV);
                // calculate position in clip space from UV coordinates
                vec2 position = 2 * UV - vec2(1,1);
                // calculate distance (d) from center, which affects brightness
                float d = length(position);
                // calculate brightness (b) factor:
                // when d=dimStart, b=1; when d=dimEnd, b=0
                float b = (d - dimEnd)/(dimStart - dimEnd);
                // prevent oversaturation
                b = clamp(b, 0, 1);
                // mix the texture color and dim color
                fragColor = vec4( b * color.rgb + (1-b) * dimColor, 1);
            }
        """

        super().__init__(vertexShaderCode, fragmentShaderCode)
        self.addUniform("Sampler2D", "texture", [None, 1])
        self.addUniform("float", "dimStart", dimStart)
        self.addUniform("float", "dimEnd", dimEnd)
        self.addUniform("vec3", "dimColor", dimColor)
        
        self.locateUniforms()

