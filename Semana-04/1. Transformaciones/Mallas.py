from OpenGL.GL import *  # Importa todas las funciones de OpenGL para dibujar gráficos 3D
import pygame            # Importa la librería pygame para manejo de vectores y gráficos

class Rotation:          # Define una clase para representar una rotación
    def __init__(self, angle, axis):  # Constructor que recibe el ángulo y el eje de rotación
        self.angle = angle            # Guarda el ángulo de rotación
        self.axis = axis              # Guarda el eje de rotación (Vector3)

class Malla:             # Define una clase para representar una malla 3D

    def __init__(self, vertices, traingles, draw_type, translation, rotation, scale):
        self.vertices = vertices      # Guarda la lista de vértices de la malla
        self.triangles = traingles    # Guarda la lista de índices que forman triángulos
        self.draw_type = draw_type    # Tipo de dibujo (por ejemplo, GL_TRIANGLES)
        self.translation = translation# Vector de traslación de la malla
        self.rotation = rotation      # Objeto Rotation para la rotación de la malla
        self.scale = scale            # Vector de escala de la malla

    def draw(self, move=pygame.Vector3(0, 0, 0)):  # Método para dibujar la malla, opcionalmente moviéndola
        glPushMatrix()                 # Guarda la matriz actual para no afectar otras transformaciones

        glTranslatef(move.x, move.y, move.z)  # Aplica una traslación adicional (movimiento)
        glTranslatef(self.translation.x, self.translation.y, self.translation.z)  # Aplica la traslación de la malla
        glScalef(self.scale.x, self.scale.y, self.scale.z)  # Aplica la escala de la malla
        glRotatef(self.rotation.angle, self.rotation.axis.x, self.rotation.axis.y, self.rotation.axis.z)  # Aplica la rotación

        for t in range(0, len(self.triangles) , 3):  # Itera sobre los triángulos de la malla (de 3 en 3)
            glBegin(self.draw_type)                  # Inicia el dibujo con el tipo especificado
            glVertex3fv(self.vertices[self.triangles[t]])       # Dibuja el primer vértice del triángulo
            glVertex3fv(self.vertices[self.triangles[t + 1]])   # Dibuja el segundo vértice del triángulo
            glVertex3fv(self.vertices[self.triangles[t + 2]])   # Dibuja el tercer vértice del triángulo
            glEnd()                                 # Finaliza el dibujo del triángulo
        glPopMatrix()                               # Restaura la matriz original para no afectar otros objetos