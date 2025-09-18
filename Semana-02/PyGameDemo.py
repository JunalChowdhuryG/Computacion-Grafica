import pygame #iniciar ventana contexto
from pygame.locals import * # variable locales
from OpenGL.GL import * # opengl
from OpenGL.GLU import * #teclado + mouse

pygame.init()

screen_width = 1000 #ancho
screen_height = 800 #alto

#colocar el tamanio en 800x1000 y utilizar buffering de OpenGL
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in Python")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480) #640 px de ancho y 480px de alto


done = False
init_ortho()

while not done:
    for event in pygame.event.get(): #mientras no presionemos X de cerrar ventana
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #limitar pantalla
    glMatrixMode(GL_MODELVIEW) #cambiar el modo de vista
    glLoadIdentity() # iniciar las coordenadas
    glPointSize(5) #establecer tamanio de puntos

    glBegin(GL_POINTS) #inicializar puntos
    glVertex2i(100, 50) #dibuja punto en la coordenada 100,50
    glVertex2i(630, 450) #dibuja punto en la coordenada 630,450
    glEnd() #creacion de puntos

    pygame.display.flip() #actualizar la pantalla
    pygame.time.wait(100) #esperar 100ms al siguiente refresco de pantalla

pygame.quit()