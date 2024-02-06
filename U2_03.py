import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

class Recta:
    def __init__(self,xi,yi,xf,yf): #Constructor
        self.xi = xi
        self.xf = xf
        self.yi = yi
        self.yf = yf
    def trazar(self): #Metodo
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
        x=0
        y=self.r
        DPK=3-2*self.r
        glBegin(GL_POINTS)
        while x<=y:
            glVertex2i(x,y)
            glVertex2i(-x,y)
            glVertex2i(x,-y)
            glVertex2i(-x,-y)
            glVertex2i(y,x)
            glVertex2i(-y,x)
            glVertex2i(y,-x)
            glVertex2i(-y,-x)
            if DPK>=0:
                 DPK = DPK+4*(x-y)+10
                 y= y-1
            else:
                DPK = DPK+4*x+6
            x+=1
        glEnd()

class CuadradoInscrito:
    def __init__(self,radio):
        radio = round(radio)
        lado = round(2*radio)
        self.cua = Cuadrado(lado)
        self.cir = Circunferencia(radio)
    def trazar(self):
        self.cua.trazar()
        self.cir.trazar()
        
class CuadradoCircunscrito:
    def __init__(self,radio):
        radio = round(radio)
        lado = round(1.4142135623730951*radio) #math.rqrt(2)
        self.cua = Cuadrado(lado)
        self.cir = Circunferencia(radio)
    def trazar(self):
        self.cua.trazar()
        self.cir.trazar()

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

    objeto1 = CuadradoInscrito(80)
    objeto2 = CuadradoCircunscrito(60)
    
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
        objeto1.trazar()
        glColor(0,0,1)
        objeto2.trazar()
      
       
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
