import sys
import ctypes

import sdl2
from OpenGL import GL as gl
# from OpenGL.GL import shaders

from kaalia import (
    __title__ as TITLE,
    __version__ as VERISON)


class kaaliaMain(object):
    def __init__(self):
        self.quit = False
        self.window_width = 1280
        self.window_height = 1024
        self.title = f"{TITLE} Ver:{VERISON}".encode('utf8')

    def onInit(self):
        sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 2)
        sdl2.SDL_GL_SetAttribute(
            sdl2.SDL_GL_CONTEXT_PROFILE_MASK,
            sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
        sdl2.SDL_GL_SetSwapInterval(1)
        self.window = sdl2.SDL_CreateWindow(
            self.title,
            sdl2.SDL_WINDOWPOS_CENTERED,
            sdl2.SDL_WINDOWPOS_CENTERED,
            self.window_width,
            self.window_height,
            sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
        if not self.window:
            sys.stderr.write("Error: Could not create window\n")
            return False
        self.glcontext = sdl2.SDL_GL_CreateContext(self.window)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_CULL_FACE)
        gl.glEnable(gl.GL_BLEND)
        gl.glClearColor(0, 0, 0, 1.0)
        return True

    def GameMainandLoop(self):
        sdl2.SDL_UpdateWindowSurface(self.window)
        event = sdl2.SDL_Event()
        while not self.quit:
            while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
                if event.type == sdl2.SDL_QUIT:
                    self.quit = True
                if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                    self.quit = True
            gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
            sdl2.SDL_GL_SwapWindow(self.window)

    def onQuit(self):
        sdl2.SDL_DestroyWindow(self.window)
        sdl2.SDL_Quit()

    def run(self):
        if self.onInit():
            self.GameMainandLoop()
        self.onQuit()
        return 0
