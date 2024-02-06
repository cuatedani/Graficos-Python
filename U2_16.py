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
   
    def rotarrespecto(self,t=0,xr=1,yr=1):
        self.trasladar(-xr,-yr)
        self.rotar(t)
        self.trasladar(xr,yr)

    def escalarrespecto(self,sx=0,sy=0,xf=0,yf=0):
        self.trasladar(-xf,-yf)
        self.escalar(sx,sy)
        self.trasladar(xf,yf)

    def trasladar(self,tx=0,ty=0):
        T = np.matrix([[1,0,tx],
                       [0,1,ty],
                       [0,0,1]],dtype=np.float32)
        self.transformar(T)
    def rotar(self,t=0): #grados
        t = np.radians(t)
        R = np.matrix([[np.cos(t),-np.sin(t),0],
                       [np.sin(t),np.cos(t),0],
                       [0,0,1]],dtype=np.float32)
        self.transformar(R)

    def escalar(self,sx=1,sy=1): 
        S = np.matrix([[sx,0,0],
                       [0,sy,0],
                       [0,0,1]],dtype=np.float32)
        self.transformar(S)
    def transformar(self,M): 
        i = 0
        while i < len(self.vertices):
            x,y = self.vertices[i][0],self.vertices[i][1]
            P = np.matrix([[x],
                           [y],
                           [1]],dtype=np.float32)
            Pp = M*P
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1
    def rotarXY(self,t,xr=0,yr=0): #grados
        t = np.radians(t)
        M = np.matrix([[np.cos(t),-np.sin(t),xr*(1-np.cos(t))+yr*np.sin(t)],
                       [np.sin(t),np.cos(t),yr*(1-np.cos(t))-xr*np.sin(t)],
                       [0,0,1]],dtype=np.float32)
        print(M)
        self.transformar(M)
    def escalarXY(self,sx=1,sy=1,xf=0,yf=0): 
        S = np.matrix([[sx,0,xf*(1-sx)],
                       [0,sy,yf*(1-sy)],
                       [0,0,1]],dtype=np.float32)
        self.transformar(S)
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
        '''
        objeto1.trasladar(-0.5,-0.5)
        objeto1.rotar(5)
        objeto1.trasladar(0.5,0.5)
        '''
        objeto1.rotarXY(5,0.5,0.5)
        objeto1.escalarXY(1.05,1.05,0.5,0.5)
        '''
        objeto1.trasladar(-0.5,-0.5)
        objeto1.escalar(1.01,1.01)
        objeto1.trasladar(0.5,0.5)
        '''
        
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
