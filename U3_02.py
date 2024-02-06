import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

def dibuja_ejes():
     
    glBegin(GL_LINES)
    glColor(1,0,0)
    glVertex3i(-10,0,0)
    glVertex3i(10,0,0)
    glColor(0,1,0) 
    glVertex3i(0,-10,0)
    glVertex3i(0,10,0)
    glColor(0,0,1) 
    glVertex3i(0,0,-10)
    glVertex3i(0,0,10)
    glEnd()  

def main():
    if not glfw.init():
        return

    window = glfw.create_window(500,500,"3D",None,None)
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    glClearColor(1,1,1,0) 

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10,10,-10,10,1,30)#paralelo

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(5,5,8,0,0,0,0,1,0)
      
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        dibuja_ejes()
        glBegin(GL_LINE_STRIP)
        glVertex3i(0,0,)
        glVertex3i(3,0,0)
        glVertex3i(3,2,0)
        glVertex3i(3,2,-1)
        glEnd()

        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()
