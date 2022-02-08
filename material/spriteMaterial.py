from material.material import Material
from OpenGL.GL import *

class SpriteMaterial(Material):
    def __init__(self, texture, properties={}):
        
        vertexShaderCode = """
            uniform mat4 projectionMatrix;
            uniform mat4 viewMatrix;
            uniform mat4 modelMatrix;
            uniform bool billboard;
            uniform float tileNumber;
            uniform vec2 tileCount;
            in vec3 vertexPosition;
            in vec2 vertexUV;
            out vec2 UV;

            void main()
            {
                mat4 mvMatrix = viewMatrix * modelMatrix;
                if(billboard)
                {
                    mvMatrix[0][0] = 1;
                    mvMatrix[0][1] = 0;
                    mvMatrix[0][2] = 0;
                    mvMatrix[1][0] = 0;
                    mvMatrix[1][1] = 1;
                    mvMatrix[1][2] = 0;
                    mvMatrix[2][0] = 0;
                    mvMatrix[2][1] = 0;
                    mvMatrix[2][2] = 1;
                }
                gl_Position = projectionMatrix * mvMatrix * vec4(vertexPosition, 1.0);

                UV = vertexUV;
                if (tileNumber > -1.0)
                {
                    vec2 tileSize = 1.0 / tileCount;
                    float columnIndex = mod(tileNumber, tileCount[0]);
                    float rowIndex = floor(tileNumber / tileCount[0]);
                    vec2 tileOffset = vec2(columnIndex / tileCount[0], 1.0 - (rowIndex + 1.0) / tileCount[1] );
                    UV = UV * tileSize + tileOffset;
                }
            }
        """

        fragmentShaderCode = """
            uniform vec3 baseColor;
            uniform sampler2D texture;
            in vec2 UV;
            out vec4 fragColor;

            void main()
            {
                vec4 color = vec4(baseColor, 1) * texture2D(texture, UV);
                if(color.a < 0.1)
                    discard;

                fragColor = color;
            }
        """

        super().__init__(vertexShaderCode, fragmentShaderCode)
        self.addUniform("vec3", "baseColor", [1.0, 1.0, 1.0])
        self.addUniform("sampler2D", "texture", [texture.textureRef, 1])
        self.addUniform("bool", "billboard", False)
        self.addUniform("float", "tileNumber", -1)
        self.addUniform("vec2", "tileCount", [1,1])
        self.locateUniforms()

        # render both sides?
        self.settings["doubleSide"] = True
        self.setProperties(properties)

    
    def updateRenderSettings(self):
        if self.settings["doubleSide"]:
            glDisable(GL_CULL_FACE)
        else:
            glEnable(GL_CULL_FACE)

