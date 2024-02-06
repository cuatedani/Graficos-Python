import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

def DDA(xi,yi,xf,yf):
    dx = xf-xi
    dy = yf-yi
    if(abs(dx) >= abs(dy)):
        pasos = abs(dx)
    else:
        pasos = abs(dy)
    ax=dx/pasos
    ay=dy/pasos
    x=xi
    y=yi
    i=0
    glBegin(GL_POINTS)
    while i<=pasos:
        glVertex2i(round(x),round(y)) 
        x=(x+ax)
        y=(y+ay)
        i=i+1
    glEnd()

def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(501,501,"Prueba GLFW",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)

    glClearColor(1,1,1,0)#RGB, 4to. Gamma
    gluOrtho2D(-250,250,-250,250)#xMin,xMax,yMin,yMax
    
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
        DDA(0,0,100,100)
        
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()

