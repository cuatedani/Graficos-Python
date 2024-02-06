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

class Prisma:
    def __init__(self):
        self.vertices = np.array([[0,10,0],
                                 [-5,0,-5],
                                 [5,0,-5],
                                 [5,0,5],
                                 [-5,0,5],
                                 [-5,0,-5]],dtype=np.float32)

    def trazar(self):
        glBegin(GL_TRIANGLE_FAN)
        for vertice in self.vertices:
            glVertex3fv(vertice)
        glEnd()

    def trasladar(self,tx=0,ty=0,tz=0):
        T = np.array([[1,0,0,tx],
                      [0,1,0,ty],
                      [0,0,1,tz],
                      [0,0,0,1]],dtype=np.float32)
        self.transformar(T)

    def escalar(self,sx=1,sy=1,sz=1):
        S = np.array([[sx,0,0,0],
                      [0,sy,0,0],
                      [0,0,sz,0],
                      [0,0,0,1]],dtype=np.float32)
        self.transformar(S)

    def rotarX(self,t=0):
        t = np.radians(t)
        R = np.array([[1,0,0,0],
                      [0,np.cos(t),-np.sin(t),0],
                      [0,np.sin(t),np.cos(t),0],
                      [0,0,0,1]],dtype=np.float32)
        self.transformar(R)
        
    def rotarY(self,t=0):
        t = np.radians(t)
        R = np.array([[np.cos(t),0,np.sin(t),0],
                       [0,1,0,0],
                       [-np.sin(t),0,np.cos(t),0],
                       [0,0,0,1]],dtype=np.float32)
        self.transformar(R)
        
    def rotarZ(self,t=0):
        t = np.radians(t)
        R = np.array([[np.cos(t),-np.sin(t),0,0],
                      [np.sin(t),np.cos(t),0,0],
                      [0,0,1,0],
                      [0,0,0,1]],dtype=np.float32)
        self.transformar(R)

class Anillo:
    def __init__(self):
        self.vertices_aro = np.array(np.genfromtxt('anillo_aro.csv', delimiter=','),dtype=np.float32)
        self.vertices_piedra = np.array(np.genfromtxt('anillo_piedra.csv', delimiter=','),dtype=np.float32)
        
    def trazar(self):
        glColor(0.5,0.5,0.5)
        glBegin(GL_QUAD_STRIP)
        for v in self.vertices_aro:
            glVertex3fv(v)
        glEnd()
        
        glColor(1,0,1)
        glBegin(GL_TRIANGLE_FAN)
        for v in self.vertices_piedra:
            glVertex3fv(v)
        glEnd()

    def trasladar(self,tx=0,ty=0,tz=0):
        T = np.array([[1,0,0,tx],
                      [0,1,0,ty],
                      [0,0,1,tz],
                      [0,0,0,1]],dtype=np.float32)
        self.transformar(T)

    def escalar(self,sx=1,sy=1,sz=1):
        S = np.array([[sx,0,0,0],
                      [0,sy,0,0],
                      [0,0,sz,0],
                      [0,0,0,1]],dtype=np.float32)
        self.transformar(S)

    def rotarX(self,t=0):
        t = np.radians(t)
        R = np.array([[1,0,0,0],
                      [0,np.cos(t),-np.sin(t),0],
                      [0,np.sin(t),np.cos(t),0],
                      [0,0,0,1]],dtype=np.float32)
        self.transformar(R)
        
    def rotarY(self,t=0):
        t = np.radians(t)
        R = np.array([[np.cos(t),0,np.sin(t),0],
                       [0,1,0,0],
                       [-np.sin(t),0,np.cos(t),0],
                       [0,0,0,1]],dtype=np.float32)
        self.transformar(R)
        
    def rotarZ(self,t=0):
        t = np.radians(t)
        R = np.array([[np.cos(t),-np.sin(t),0,0],
                      [np.sin(t),np.cos(t),0,0],
                      [0,0,1,0],
                      [0,0,0,1]],dtype=np.float32)
        self.transformar(R)

    def transformar(self,M):
        #Aro
        i=0
        while i < len(self.vertices_aro):
            x,y,z = self.vertices_aro[i]
            P = np.array([[x],
                          [y],
                          [z],
                          [1]],dtype=np.float32)
            Pp = np.dot(M,P)
            self.vertices_aro[i][0] = Pp[0][0]
            self.vertices_aro[i][1] = Pp[1][0]
            self.vertices_aro[i][2] = Pp[2][0]
            i += 1

        i=0
        #Piedra
        while i < len(self.vertices_piedra):
            x,y,z = self.vertices_piedra[i]
            P = np.array([[x],
                          [y],
                          [z],
                          [1]],dtype=np.float32)
            Pp = np.dot(M,P)
            self.vertices_piedra[i][0] = Pp[0][0]
            self.vertices_piedra[i][1] = Pp[1][0]
            self.vertices_piedra[i][2] = Pp[2][0]
            i += 1
             
def main():
    if not glfw.init():
        return

    window = glfw.create_window(500,500,"19400588",None,None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glClearColor(1,1,1,0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10,10,-10,10,1,30)#Paralelo
    #glFrustum(-3,3,-3,3,1,30)#Perspectiva

    pris =  Prisma()

    x,y,z = 5,5,8

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(x,y,z,0,0,0,0,1,0)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)#3D
        glEnable(GL_DEPTH_TEST)#Para dibujar lo oculto a la vista
        glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)#Relleno GL_FILL, GL_LINE

        glLineWidth(1)
        dibuja_ejes()

        glColor(0,0,0)
        pris.trazar()

        
        
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
















