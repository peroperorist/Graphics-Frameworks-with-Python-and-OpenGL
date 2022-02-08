from OpenGL.GL import *
from core.mesh import Mesh
import pygame

class Renderer(object):

    def __init__(self, clearColor=[0, 0, 0]):
        glEnable(GL_DEPTH_TEST)
        # required for antialiasing
        glEnable(GL_MULTISAMPLE)
        glClearColor(clearColor[0], clearColor[1], clearColor[2], 1)
        

        # glEnable(GL_ALPHA_TEST)
        # Alpha blending
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.windowSize = pygame.display.get_surface().get_size()


    #def render(self, scene, camera):
    def render(self, scene, camera, clearColor=True, clearDepth=True, renderTarget=None):  # Chapter 5-8

        
        # activate render target
        if (renderTarget == None):
            # set render target to window
            glBindFramebuffer(GL_FRAMEBUFFER, 0)
            glViewport(0,0, self.windowSize[0], self.windowSize[1])
            
        else:
            # set render target properties
            glBindFramebuffer(GL_FRAMEBUFFER, renderTarget.framebufferRef)
            glViewport(0,0, renderTarget.width, renderTarget.height)
            
        # clear color and depth buffers
        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if clearColor:
            glClear(GL_COLOR_BUFFER_BIT)
        if clearDepth:
            glClear(GL_DEPTH_BUFFER_BIT)
        
        
        #glEnable(GL_BLEND)
        #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)



        # update camera view (calculate inverse)
        camera.updateViewMatrix()

        # extract list of all Mesh objects in scene
        descendantList = scene.getDescendantList()
        meshFilter = lambda x : isinstance(x, Mesh)
        meshList = list( filter( meshFilter, descendantList) )

        for mesh in meshList:
            # if this object is not visible, continue to next object in list
            if not mesh.visible:
                continue
            
            glUseProgram( mesh.material.programRef )
            # bind VAO
            glBindVertexArray(mesh.vaoRef)
            
            # update uniform values stored outside of material
            mesh.material.uniforms["modelMatrix"].data = mesh.getWorldMatrix()
            mesh.material.uniforms["viewMatrix"].data = camera.viewMatrix
            mesh.material.uniforms["projectionMatrix"].data = camera.projectionMatrix

            # update uniforms stored in material
            for variableName, uniformObject in mesh.material.uniforms.items():
                uniformObject.uploadData()

            # update render settings
            mesh.material.updateRenderSettings()
            
            glDrawArrays( mesh.material.settings["drawStyle"], 0, mesh.geometry.vertexCount)



