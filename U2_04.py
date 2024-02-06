import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

'''
Variables globales
'''
xMin,xMax,yMin,yMax = -10,10,-10,10
        
class Cuadrado:
    def __init__(self,lado):
        self.vertices = [[-lado/2,lado/2],
                         [lado/2,lado/2],
                         [lado/2,-lado/2],
                         [-lado/2,-lado/2]]
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()

class SenoX:
    def __init__(self):
        self.vertices = []
        incX = 0.5
        X = xMin
        while x<=xMax:
            y = math.sin(x)
            self.vertices.append([x,y])
            x += incX
    def trazar(self):
        glBegin(GL_LINE_STRIP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()
        

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

    objeto1 = SenoX()
    
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        
        glColor(0,0,0)#RGB
        glBegin(GL_LINES)
        glVertex2f(xMin,0)
        glVertex2f(xMax,0)
        glVertex2f(0,yMin)
        glVertex2f(0,yMax)
        glEnd()

        glColor(1,0,0)
        objeto1.trazar()
       
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
