import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

'''
GOMEZ GONZALEZ JUAN DANIEL
'''
xMin,xMax,yMin,yMax,zMin,zMax = -10,10,-10,10,-10,10
            
class Ejes:
    def __init__(self):
        self.vertices = np.array([[-10,0,0],
                                 [10,0,0],
                                 [0,-10,0],
                                 [0,10,0],
                                 [0,0,-10],
                                 [0,0,10]],dtype=np.float32)
        
    def trazar(self):   
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex3fv(vertice)
        glEnd()
        
    def transformar(self,M): 
        i = 0
        while i < len(self.vertices):
            x,y,z = self.vertices[i][0],self.vertices[i][1],self.vertices[i][2]            P = np.matrix([[x],
                           [y],
                           [z],
                           [1]],dtype=np.float32)
            Pp = M*P
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            self.vertices[i][1] = Pp[2][0]
            i += 1
        
def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(500,500,"19400588",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)

    glClearColor(1,1,1,0)
    #gluOrtho2D(xMin,xMax,yMin,yMax)

    #Declaraciones
    Eje=Ejes()
    M = np.matrix([1,0,0,0],
                  [0,1,0,0],
                  [0,0,1,0],
                  [0,0,0,1])
    #Declaraciones
    
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        
        glBegin(GL_LINES)
        Eje.Trazar
        glEnd()

        
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
