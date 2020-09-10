import sys
import ctypes
import sdl2
from OpenGL import GL as gl

from kaalia import (
    __title__ as TITLE,
    __version__ as VERISON)


def sdl2_die(msg):
    sys.stderr.write(f"{msg}: {sdl2.SDL_GetError()}")
    sdl2.SDL_Quit()
    sys.exit(1)


class kaaliaMain(object):
    def __init__(self):
        self.quit = False
        self.screen_width = 1280
        self.screen_height = 1024
        self.title = f"{TITLE} Ver:{VERISON}".encode('utf8')

    def onInit(self):
        if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) < 0:
            sdl2_die("Unable to initialize SDL")

        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 4)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 6)
        sdl2.SDL_GL_SetAttribute(
            sdl2.SDL_GL_CONTEXT_PROFILE_MASK,
            sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 32)
        self.window = sdl2.SDL_CreateWindow(
            self.title,
            sdl2.SDL_WINDOWPOS_CENTERED,
            sdl2.SDL_WINDOWPOS_CENTERED,
            self.screen_width,
            self.screen_height,
            sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
        if not self.window:
            sdl2_die("Unable to create window")
        self.glcontext = sdl2.SDL_GL_CreateContext(self.window)
        sdl2.SDL_GL_SetSwapInterval(1)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_CULL_FACE)
        gl.glEnable(gl.GL_BLEND)
        self.event = sdl2.SDL_Event()

    def onEvent(self, e):
        if e.type == sdl2.SDL_QUIT:
            self.quit = True
        if e.key.keysym.sym == sdl2.SDLK_ESCAPE:
            self.quit = True

    def onQuit(self):
        sdl2.SDL_GL_DeleteContext(self.glcontext)
        sdl2.SDL_DestroyWindow(self.window)
        sdl2.SDL_Quit()

    def GameMainandLoop(self):
        while not self.quit:
            gl.glClearColor(0, 0, 0, 1.0)
            while sdl2.SDL_PollEvent(ctypes.byref(self.event)) != 0:
                self.onEvent(self.event)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
            sdl2.SDL_GL_SwapWindow(self.window)

    def run(self):
        self.onInit()
        self.GameMainandLoop()
        self.onQuit()
        return 0
