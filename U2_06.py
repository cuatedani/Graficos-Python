import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
'''
Variables globales
'''
xMin,xMax,yMin,yMax = -10,10,-10,10
        
class Circunferencia:
    def __init__(self,r):
        self.vertices = []
        for theta in np.linspace(0,2*np.pi):
            self.vertices.append([r*np.cos(theta),r*np.sin(theta)])
    def trazar(self):
        glBegin(GL_LINE_STRIP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()

    def trasladar (self):
    
def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(600,600,"Prueba GLFW",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)

    glClearColor(1,1,1,0)#RGB, 4to. Gamma
    gluOrtho2D(xMin,xMax,yMin,yMax)#xMin,xMax,yMin,yMax

    objeto1 = Circunferencia(10)
    
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        
        glColor(0,0,0)#RGB
        objeto1.trazar();

        glColor(1,0,0)
        objeto1.trazar()
       
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
