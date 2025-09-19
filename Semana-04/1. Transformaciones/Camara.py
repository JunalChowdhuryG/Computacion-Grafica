import pygame                           # Importa la librería pygame para manejo de vectores y eventos
from OpenGL.GLU import *                # Importa funciones de OpenGL para manejo de cámara
from math import *                      # Importa todas las funciones matemáticas

class Camara:                           # Define la clase Camara
    def __init__(self):                 # Constructor de la clase Camara
        self.eye = pygame.math.Vector3(0, 0, 0)         # Posición de la cámara (punto de vista)
        self.up = pygame.math.Vector3(0, 1, 0)          # Vector hacia arriba de la cámara
        self.right = pygame.math.Vector3(1, 0, 0)       # Vector hacia la derecha de la cámara
        self.forward = pygame.math.Vector3(0, 0, 1)     # Vector hacia adelante de la cámara
        self.look = self.eye + self.forward             # Punto al que la cámara está mirando
        self.yaw = -90                                 # Ángulo de giro horizontal (yaw)
        self.pitch = 0                                 # Ángulo de giro vertical (pitch)
        self.last_mouse = pygame.math.Vector2(0, 0)    # Última posición del mouse
        self.mouse_sensitivityX = 0.1                  # Sensibilidad del mouse en X
        self.mouse_sensitivityY = 0.1                  # Sensibilidad del mouse en Y

    def rotatate(self, yaw, pitch):                    # Método para rotar la cámara
        self.yaw += yaw                               # Actualiza el ángulo yaw
        self.pitch += pitch                           # Actualiza el ángulo pitch

        if self.pitch > 89.0:                         # Limita el pitch máximo
            self.pitch = 89.0

        if self.pitch < -89.0:                        # Limita el pitch mínimo
            self.pitch = 89.0

        self.forward.x = cos(radians(self.yaw)) * cos(radians(self.pitch)) # Calcula componente X del vector forward
        self.forward.y = sin(radians(self.pitch))                          # Calcula componente Y del vector forward
        self.forward.z = sin(radians(self.yaw)) * cos(radians(self.pitch)) # Calcula componente Z del vector forward
        self.forward = self.forward.normalize()                            # Normaliza el vector forward
        self.right = self.forward.cross(pygame.math.Vector3(0, 1, 0)).normalize() # Calcula y normaliza el vector right
        self.up = self.right.cross(self.forward).normalize()               # Calcula y normaliza el vector up

    def update(self, w, h):                        # Método para actualizar la cámara según el mouse y teclado
        if pygame.mouse.get_visible():             # Si el mouse está visible, no actualiza la cámara
            return

        mouse_pos = pygame.mouse.get_pos()         # Obtiene la posición actual del mouse
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos) # Calcula el cambio de posición del mouse

        pygame.mouse.set_pos(w / 2, h / 2)         # Centra el mouse en la ventana

        self.last_mouse = pygame.mouse.get_pos()   # Actualiza la última posición del mouse

        self.rotatate(-mouse_change.x * self.mouse_sensitivityX, mouse_change.y * self.mouse_sensitivityY) # Rota la cámara según el movimiento del mouse

        keys = pygame.key.get_pressed()            # Obtiene el estado de las teclas
        if keys[pygame.K_DOWN]:                    # Si se presiona la flecha abajo
            self.eye -= self.forward * self.mouse_sensitivityX # Mueve la cámara hacia atrás
        if keys[pygame.K_UP]:                      # Si se presiona la flecha arriba
            self.eye += self.forward * self.mouse_sensitivityX # Mueve la cámara hacia adelante
        if keys[pygame.K_RIGHT]:                   # Si se presiona la flecha derecha
            self.eye += self.right * self.mouse_sensitivityX   # Mueve la cámara a la derecha
        if keys[pygame.K_LEFT]:                    # Si se presiona la flecha izquierda
            self.eye -= self.right * self.mouse_sensitivityX   # Mueve la cámara a la izquierda

        self.look = self.eye + self.forward        # Actualiza el punto al que mira la cámara
        gluLookAt(self.eye.x, self.eye.y, self.eye.z,      # Establece la vista de la cámara en OpenGL
                  self.look.x, self.look.y, self.look.z,
                  self.up.x, self.up.y, self.up.z)