from material.material import Material

class DepthMaterial(Material):
    def __init__(self):

        vertexShaderCode = """
          in vec3 vertexPosition;
          uniform mat4 projectionMatrix;
          uniform mat4 viewMatrix;
          uniform mat4 modelMatrix;

          void main()
          {
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
          }
        """

        fragmentShaderCode = """
          out vec4 fragColor;

          void main()
          {
            float z = gl_FragCorrd.z;
            fragColor = vec4(z, z, z, 1);
          }
        """

        super().__init__(vertexShaderCode, fragmentShaderCode)
        self.locateUniforms()

    