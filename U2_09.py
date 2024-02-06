import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

'''
Variables globales
'''
xMin,xMax,yMin,yMax = -20,20,-20,20

class Circunferencia:
    def __init__(self,r=1):
        self.vertices = []
        for theta in np.linspace(0,2*np.pi):
            self.vertices.append([r*np.cos(theta),r*np.sin(theta)])
            
    def trazar(self):
        glBegin(GL_LINE_STRIP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()
        
    def trasladar(self,tx=0,ty=0):
        i = 0
        while i < len(self.vertices):
            self.vertices[i][0] += tx
            self.vertices[i][1] += ty
            i += 1

    def rotar(self,theta=0): #grados
        theta = np.radians(theta)
        i = 0
        while i < len(self.vertices):
            x = self.vertices[i][0]
            y = self.vertices[i][1]
            self.vertices[i][0] = x*np.cos(theta) - y*np.sin(theta)
            self.vertices[i][1] = x*np.sin(theta) + y*np.cos(theta)
            i += 1
            
class Cuadrado:
    def __init__(self,lado=1):
        self.vertices = [[-lado/2,lado/2],
                         [lado/2,lado/2],
                         [lado/2,-lado/2],
                         [-lado/2,-lado/2]]
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

    def rotar(self,theta=0): #grados
        theta = np.radians(theta)
        i = 0
        while i < len(self.vertices):
            x = self.vertices[i][0]
            y = self.vertices[i][1]
            self.vertices[i][0] = x*np.cos(theta) - y*np.sin(theta)
            self.vertices[i][1] = x*np.sin(theta) + y*np.cos(theta)
            i += 1   
        
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

    n = 2 # numero de objetos
    r = 1 # radio de la circunferencia "imaginaria"

    objetos = []
    for i in range(n):
        objetos.append(Cuadrado(1))

    for objeto in objetos:
        objeto.rotar(45)

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
        for objeto in objetos:
            objeto.trazar()

            
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
