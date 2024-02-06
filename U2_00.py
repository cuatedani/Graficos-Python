import glfw

def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(400,400,"Prueba GLFW",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)
    
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
