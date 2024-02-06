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

#Juan Daniel Gomez Gonzalez
#NC: 19400588
class TrianguloEquilatero:
    def __init__(self,lado):
        lado = round(lado)
        self.radio = round(0.5773502692*lado)
        self.ap = round(0.2886751346*lado)
        self.ra_b = Recta(0,self.radio,-lado/2,-self.ap)
        self.rb_c = Recta(-lado/2,-self.ap,lado/2,-self.ap)
        self.rc_a = Recta(lado/2,-self.ap,0,self.radio)
    def trazar(self):
        self.ra_b.trazar()
        self.rb_c.trazar()
        self.rc_a.trazar()

class TrianguloInscrito:
    def __init__(self,radio):
        radio = round(radio)
        self.lado = round(1.73205050808*radio)
        self.tri = TrianguloEquilatero(self.lado)
        self.cir = Circunferencia(radio)
    def trazar(self):
        self.tri.trazar()
        self.cir.trazar()

class TrianguloCircunscrito:
    def __init__(self,lado):
        lado = round(lado)
        self.radio = round(0.2886751346*lado)
        self.tri = TrianguloEquilatero(lado)
        self.cir = Circunferencia(self.radio)
    def trazar(self):
        self.cir.trazar()
        self.tri.trazar()

def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(803,803,"Triangulo Inscrito",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)

    glClearColor(1,1,1,0)#RGB, 4to. Gamma
    gluOrtho2D(-250,250,-250,250)#xMin,xMax,yMin,yMax

    TriCir = TrianguloCircunscrito(115)
    
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
        TriCir.trazar()
       
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
