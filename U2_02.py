import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

class Recta:
    def __init__(self,xi,yi,xf,yf): #Constructor
        self.xi = round(xi)
        self.xf = round(xf)
        self.yi = round(xi)
        self.yf = round(yf)
    def trazar(self): #Metodo de la clase
        dx = self.xf-self.xi
        dy = self.yf-self.yi
        if(abs(dx) >= abs(dy)):
            pasos = abs(dx)
        else:
            pasos = abs(dy)
        ax=dx/pasos
        ay=dy/pasos
        x=self.xi
        y=self.yi
        i=0
        glBegin(GL_POINTS)
        while i<=pasos:
            glVertex2i(round(x),round(y)) 
            x=(x+ax)
            y=(y+ay)
            i=i+1
        glEnd()
class Cuadrado:
    def __init__(self,lado):
        lado = round(lado)
        self.r1_2 = Recta(-lado/2,lado/2,lado/2,lado/2)
        self.r3_4 = Recta(-lado/2,-lado/2,lado/2,-lado/2)
        self.r3_1 = Recta(-lado/2,-lado/2,-lado/2,lado/2)
        self.r4_2 = Recta(lado/2,-lado/2,lado/2,lado/2)
    def trazar(self):
        self.r1_2.trazar()
        self.r3_4.trazar()
        self.r3_1.trazar()
        self.r4_2.trazar()

class Circunferencia:
    def __init__(self,radio):
        self.r = round(radio)
    def trazar(self):
     
        xi,xf = 0,self.r
        x = xi
        glBegin(GL_POINTS)
        while x<=xf:
            y = round(+ math.sqrt(self.r**2 - x**2))
            glVertex2i(x,y)
            glVertex2i(x,y)
            glVertex2i(-x,y)
            glVertex2i(-x,-y)
            glVertex2i(x,-y)
            x += 1
        yi,yf = 0,self.r
        y = yi
        while y<=yf:
            x = round(+ math.sqrt(self.r**2 - y**2))
            glVertex2i(x,y)
            glVertex2i(x,y)
            glVertex2i(-x,y)
            glVertex2i(-x,-y)
            glVertex2i(x,-y)
            y += 1
        glEnd()

def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(503,503,"Prueba GLFW",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)

    glClearColor(1,1,1,0)#RGB, 4to. Gamma
    gluOrtho2D(-250,250,-250,250)#xMin,xMax,yMin,yMax

    recta1 = Recta(-100,-10,200,5)#Objeto recta1
    recta2 = Recta(-100,0,200,250)#Objeto recta2
    
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        
        glColor(0,0,0)#RGB
        glBegin(GL_POINTS)
        i = -250
        while i<=250:
            glVertex2i(i,0)
            glVertex2i(0,i)
            i += 1
        glEnd()

        glColor(1,0,0)
        recta1.trazar()
        glColor(0,0,1)
        recta2.trazar()

       
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()


