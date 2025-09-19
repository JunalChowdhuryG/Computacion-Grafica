from OpenGL.GL import *  # Importa todas las funciones de OpenGL para gráficos 3D
from Mallas import *     # Importa las clases y funciones del archivo Mallas.py
import pygame            # Importa pygame para manejo de vectores

class LeerMalla(Malla):  # Define la clase LeerMalla que hereda de Malla

    def __init__(self, file_name, draw_type, position=pygame.Vector3(0, 0, 0), rotation=Rotation(0, pygame.Vector3(0, 1, 0)), scale=pygame.Vector3(1, 1, 1) ):
        self.file_name = file_name      # Guarda el nombre del archivo de la malla
        vertices, triangles = self.cargar_dibujo()  # Carga los vértices y triángulos desde el archivo
        self.tipo_dibujo = draw_type    # Guarda el tipo de dibujo
        super().__init__(vertices, triangles, draw_type, position, rotation, scale) # Llama al constructor de Malla con los datos cargados

    def cargar_dibujo(self):            # Método para cargar los datos de la malla desde el archivo
        vertices = []                   # Lista para almacenar los vértices
        triangulos = []                 # Lista para almacenar los triángulos
        with open(self.file_name) as f: # Abre el archivo de la malla
            linea = f.readline()        # Lee la primera línea del archivo
            while linea:                # Mientras haya líneas en el archivo
                if linea[:2] == "v ":   # Si la línea define un vértice
                    vx, vy, vz = [float(value) for value in linea[2:].split()] # Extrae las coordenadas del vértice
                    vertices.append((vx, vy, vz)) # Agrega el vértice a la lista
                if linea[:2] == "f ":   # Si la línea define una cara (triángulo)
                    t1, t2, t3, *r = [value for value in linea[2:].split()] # Extrae los índices de los vértices
                    triangulos.append([int(value) for value in t1.split('/')][0] - 1) # Agrega el primer índice (ajustado a base 0)
                    triangulos.append([int(value) for value in t2.split('/')][0] - 1) # Agrega el segundo índice (ajustado a base 0)
                    triangulos.append([int(value) for value in t3.split('/')][0] - 1) # Agrega el tercer índice (ajustado a base 0)
                linea = f.readline()    # Lee la siguiente línea del archivo
        return vertices, triangulos     # Devuelve las listas de vértices y triángulos

