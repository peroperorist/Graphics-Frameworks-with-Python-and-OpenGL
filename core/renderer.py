from OpenGL.GL import *
from core.mesh import Mesh
from light.light import Light
from light.shadow import Shadow
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

        # chapter 6-9
        self.shadowsEnabled = False

        self.windowSize = pygame.display.get_surface().get_size()

    # chapter 6-9
    def enableShadows(self, shadowLight, strength=0.5, resolution=[512, 512]):
        self.shadowsEnabled = True
        self.shadowObject = Shadow(shadowLight, strength=strength, resolution=resolution)


    #def render(self, scene, camera):
    def render(self, scene, camera, clearColor=True, clearDepth=True, renderTarget=None):  # Chapter 5-8

        # chater 6-9
        # filter descendents
        descendentList = scene.getDescendentList()
        meshFilter = lambda x : isinstance(x, Mesh)
        meshList = list( filter( meshFilter, descendentList))

        ## shadow pass
        if self.shadowsEnabled:
            # set render target properties
            glBindFramebuffer(GL_FRAMEBUFFER, self.shadowObject.renderTarget.framebufferRef)
            glViewport(0, 0, self.shadowObject.renderTarget.width, self.shadowObject.renderTarget.height )

            # set default color to white, used when no objects present to cast shadows
            glClearColor(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT)
            glClear(GL_DEPTH_BIT)

            # everything in the scene gets rendered with depthMaterial, so only need to call glUseProgram & set matrices once
            glUseProgram( self.shadowObject.material.programRef)
            self.shadowObject.updateInternal()

            for mesh in meshList:
                # skip invisible meshes
                if not mesh.visible:
                    continue
                
                # only triangle-based meshes cast shadows
                if mesh.material.settings["drawStyle"] != GL_TRIANGLES:
                    continue

                #bind VAO
                glBindVertexArray( mesh.vaoRef )
                
                # update transform data
                self.shadowObject.material.uniforms["modelMatrix"].data = mesh.getWorldMatrix()

                # update uniforms (matrix data) stored in shadow material
                for varName, unifObj in self.shadowObject.material.uniforms.items():
                    glDrawArrays( GL_TRIANGLES, 0, mesh.geometry.vertexCount )
                


        
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

        # chapter 6-5, light
        lightFileter = lambda x : isinstance(x, Light)
        lightList = list( filter( lightFileter, descendantList ) )
        # scenes support 4 lights; precisely 4 must be present
        while len(lightList) < 4 :
            lightList.append( Light() )




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

            # chapter 6-5
            # if material uses light data, add lights from list
            if "light0" in mesh.material.uniforms.keys():
                for lightNumber in range(4):
                    lightName = "light" + str(lightNumber)
                    lightObject = lightList[lightNumber]
                    mesh.material.uniforms[lightName].data = lightObject
            
            # add camera position if needed (specular lighting)
            if "viewPosition" in mesh.material.uniforms.keys():
                mesh.material.uniforms["viewPosition"].data = camera.getWorldPosition()
            
            # chapter 6-9
            # add shadow data if enabled and used by shader
            if self.shadowsEnabled and "shadow0" in mesh.material.uniforms.keys():
                mesh.material.uniforms["shadow0"].data = self.shadowObject


            # update uniforms stored in material
            for variableName, uniformObject in mesh.material.uniforms.items():
                uniformObject.uploadData()

            # update render settings
            mesh.material.updateRenderSettings()
            
            glDrawArrays( mesh.material.settings["drawStyle"], 0, mesh.geometry.vertexCount)





