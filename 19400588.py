import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

#Juan Daniel Gomez Gonzalez
'''Variables Globales'''
xMin,xMax,yMin,yMax = -10,10,-10,10
class TrianguloEquilatero:
    def __init__(self,lado):
        self.radio = 0.5773502692*lado
        self.ap = self.radio*0.5
        self.vertices = [[0,self.radio],
                         [-lado/2,-self.ap],
                         [lado/2,-self.ap]]
        
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()

    def trasladar(self,tx=0,ty=0):
        i = 0
        while i < len(self.vertices):
            self.vertices[i][0] += tx
            self.vertices[i][1] += ty
            i += 1

    def rotar(self,theta=0):
        theta = np.radians(theta)
        i = 0
        while i < len(self.vertices):
            x = self.vertices[i][0]
            y = self.vertices[i][1]
            self.vertices[i][0] = x*np.cos(theta) - y*np.sin(theta)
            self.vertices[i][1] = x*np.sin(theta) + y*np.cos(theta)
            i += 1
            
    def escalar(self,sx=1,sy=1):
        i = 0
        while i < len(self.vertices):
            self.vertices[i][0] *= sx
            self.vertices[i][1] *= sy
            i += 1
        
def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(600,600,"19400588",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)

    glClearColor(1,1,1,0)
    gluOrtho2D(xMin,xMax,yMin,yMax)


    r = 7
    n = 20
    
    Triangulos = []
    for i in range(n):
        Triangulos.append(TrianguloEquilatero(1))

    theta = 270
    incTheta = 360/20
    for Triangulo in Triangulos:
        Triangulo.rotar(theta)
        theta += incTheta

    theta = 0
    incTheta = 2*np.pi/n
    for Triangulo in Triangulos:
        Triangulo.trasladar(r*np.cos(theta),r*np.sin(theta))
        theta += incTheta

    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        
        glColor(0,0,0)
        glBegin(GL_LINES)
        glVertex2f(xMin,0)
        glVertex2f(xMax,0)
        glVertex2f(0,yMin)
        glVertex2f(0,yMax)
        glEnd()

        glColor(1,0,0)
        for Triangulo in Triangulos:
            Triangulo.trazar()
            
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
