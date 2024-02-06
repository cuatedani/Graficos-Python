import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

'''
Variables globales
'''
xMin,xMax,yMin,yMax = -10,10,-10,10
            
class Cruz:
    def __init__(self):
        self.vertices = np.array([[0.5,1.5],
                         [0.5,0.5],
                         [1.5,0.5],
                         [1.5,-0.5],
                         [0.5,-0.5],
                         [0.5,-2.5],
                         [-0.5,-2.5],
                         [-0.5,-0.5],
                         [-1.5,-0.5],
                         [-1.5,0.5],
                         [-0.5,0.5],
                         [-0.5,1.5]],dtype=np.float32)
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()
    def trasladar(self,tx=0,ty=0):
        T = np.matrix([[tx],[ty]],dtype=np.float32)
        i = 0
        while i < len(self.vertices):
            P = np.matrix([[self.vertices[i][0]],[self.vertices[i][1]]],dtype=np.float32)
            Pp = T + P
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1
            
    def rotar(self,t=0): #grados
        t = np.radians(t)
        R = np.matrix([[np.cos(t),-np.sin(t)],
                       [np.sin(t),np.cos(t)]],dtype=np.float32)
        i = 0
        while i < len(self.vertices):
            P = np.matrix([ [self.vertices[i][0]],[self.vertices[i][1]] ],dtype=np.float32)
            Pp = R*P
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1

    def escalar(self,sx=1,sy=1): 
        S = np.matrix([[sx,0],
                       [0,sy]],dtype=np.float32)
        i = 0
        while i < len(self.vertices):
            P = np.matrix([[self.vertices[i][0]],[self.vertices[i][1]]],dtype=np.float32)
            Pp = S*P
            self.vertices[i] = Pp
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

    objeto1 = Cruz()
    objeto1.trasladar(6,6)
    
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

        time.sleep(0.1)
        objeto1.trasladar(-6,-6)
        objeto1.rotar(5)
        objeto1.trasladar(6,6)
        
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
