from OpenGL.GL import *  # Importa todas las funciones de OpenGL para gráficos 3D
from Mallas import *     # Importa las clases y funciones del archivo Mallas.py
import pygame            # Importa pygame para manejo de vectores

class Cubo(Malla):       # Define la clase Cubo que hereda de Malla

    def __init__(self, draw_type, position=pygame.Vector3(0, 0, 0), rotation=Rotation(0, pygame.Vector3(0, 1, 0)), scale=pygame.Vector3(1, 1, 1)):
        # Constructor de la clase Cubo, recibe tipo de dibujo, posición, rotación y escala
        vertices = [(0.5, -0.5, 0.5),      # Vértice 0
                   (-0.5, -0.5, 0.5),      # Vértice 1
                   (0.5, 0.5, 0.5),        # Vértice 2
                   (-0.5, 0.5, 0.5),       # Vértice 3
                   (0.5, 0.5, -0.5),       # Vértice 4
                   (-0.5, 0.5, -0.5),      # Vértice 5
                   (0.5, -0.5, -0.5),      # Vértice 6
                   (-0.5, -0.5, -0.5),     # Vértice 7
                   (0.5, 0.5, 0.5),        # Vértice 8 (repetido para facilitar dibujo)
                   (-0.5, 0.5, 0.5),       # Vértice 9
                   (0.5, 0.5, -0.5),       # Vértice 10
                   (-0.5, 0.5, -0.5),      # Vértice 11
                   (0.5, -0.5, -0.5),      # Vértice 12
                   (0.5, -0.5, 0.5),       # Vértice 13
                   (-0.5, -0.5, 0.5),      # Vértice 14
                   (-0.5, -0.5, -0.5),     # Vértice 15
                   (-0.5, -0.5, 0.5),      # Vértice 16
                   (-0.5, 0.5, 0.5),       # Vértice 17
                   (-0.5, 0.5, -0.5),      # Vértice 18
                   (-0.5, -0.5, -0.5),     # Vértice 19
                   (0.5, -0.5, -0.5),      # Vértice 20
                   (0.5, 0.5, -0.5),       # Vértice 21
                   (0.5, 0.5, 0.5),        # Vértice 22
                   (0.5, -0.5, 0.5)]       # Vértice 23

        triangles = [0, 2, 3, 0, 3, 1,     # Triángulos de la cara frontal
                     8, 4, 5, 8, 5, 9,     # Triángulos de la cara superior
                     10, 6, 7, 10, 7, 11,  # Triángulos de la cara trasera
                     12, 13, 14, 12, 14, 15, # Triángulos de la cara inferior
                     16, 17, 18, 16, 18, 19, # Triángulos de la cara izquierda
                     20, 21, 22, 20, 22, 23] # Triángulos de la cara derecha
        super().__init__(vertices, triangles, draw_type, position, rotation, scale) # Llama al constructor de Malla con los parámetros del cubo
