# **Semana 2: Transformaciones y Modelos de Color en Procesamiento de Imágenes**

Esta sección extiende los conceptos introducidos en la Semana 1, enfocándose en transformaciones geométricas, convoluciones, filtros específicos y modelos de color avanzados. Se presenta una integración ordenada de teoría y práctica, con explicaciones matemáticas, conceptos clave y ejemplos de código en Python utilizando bibliotecas como OpenCV (cv2) y NumPy. Los ejemplos prácticos asumen un entorno con estas bibliotecas instaladas y se basan en imágenes

## **Transformaciones Geométricas**

Las transformaciones geométricas modifican la posición, tamaño o orientación de los píxeles en una imagen sin alterar sus valores de intensidad. Estas se representan mediante matrices afines o proyectivas, permitiendo operaciones como traslación, escalado y rotación. En el contexto de OpenCV, se aplican matrices de transformación para mapear coordenadas originales a nuevas posiciones.

### **Teoría**
- **Traslación**: Desplaza la imagen en los ejes x e y. Matemáticamente, para un píxel (x, y), la nueva posición es (x + tx, y + ty), donde tx y ty son los desplazamientos. La matriz afín es:
  $$\begin{bmatrix}
  1 & 0 & tx \\
  0 & 1 & ty \\
  0 & 0 & 1
  \end{bmatrix}$$
- **Escalado**: Cambia el tamaño de la imagen multiplicando las coordenadas por factores sx (horizontal) y sy (vertical). La matriz es:
  $$\begin{bmatrix}
  sx & 0 & 0 \\
  0 & sy & 0 \\
  0 & 0 & 1
  \end{bmatrix}$$
  Un escalado uniforme (sx = sy) preserva la relación de aspecto.
- **Rotación**: Gira la imagen alrededor de un punto (usualmente el centro) por un ángulo θ. La matriz de rotación en sentido antihorario es:
  $$\begin{bmatrix}
  \cos\theta & -\sin\theta & 0 \\
  \sin\theta & \cos\theta & 0 \\
  0 & 0 & 1
  \end{bmatrix}$$
  Para rotación en sentido horario, se invierten los signos de los términos con seno: cosθ y sinθ en la primera fila, -sinθ y cosθ en la segunda. Para composiciones, se combinan matrices (e.g., rotación seguida de traslación para centrar la imagen).

Estas transformaciones pueden causar artefactos si no se aplica interpolación (e.g., bilineal o bicúbica). En casos avanzados, como corrección de perspectiva, se usa una transformación proyectiva (homografía) con una matriz 3x3 general.

### **Práctica**
Ejemplos de código para transformaciones básicas y perspectiva. Asume importaciones previas: `import cv2`, `import numpy as np`, `import matplotlib.pyplot as plt`.

```python
# Ejemplo de traslación
img = cv2.imread('Imagenes/centro1.jpg')
rows, cols = img.shape[:2]
M = np.float32([[1, 0, 100], [0, 1, 50]])  # Traslación: tx=100, ty=50
img_translated = cv2.warpAffine(img, M, (cols, rows))

plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(img_translated, cv2.COLOR_BGR2RGB))
plt.show()

# Ejemplo de escalado
M = np.float32([[1.5, 0, 0], [0, 1.5, 0]])  # Escalado uniforme por 1.5
img_scaled = cv2.warpAffine(img, M, (int(cols*1.5), int(rows*1.5)))

plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(img_scaled, cv2.COLOR_BGR2RGB))
plt.show()

# Ejemplo de rotación (antihorario)
center = (cols/2, rows/2)
angle = 45  # Grados
M = cv2.getRotationMatrix2D(center, angle, 1.0)  # Anti-horario
img_rotated = cv2.warpAffine(img, M, (cols, rows))

plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(img_rotated, cv2.COLOR_BGR2RGB))
plt.show()

# Rotación en sentido horario: cambiar angle a -45
M_clockwise = cv2.getRotationMatrix2D(center, -angle, 1.0)
img_rotated_clockwise = cv2.warpAffine(img, M_clockwise, (cols, rows))

plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(img_rotated_clockwise, cv2.COLOR_BGR2RGB))
plt.show()
```

Para transformación de perspectiva (ejemplo proporcionado):
```python
img = cv2.imread('IMG_4928.jpg')
img = img[:,:,::-1]  # Convertir a RGB
plt.imshow(img)

puntos = np.float32([[230, 980], [1770, 580], [2800, 2650], [600, 3380]])

imgDibujo = img.copy()
cv2.circle(imgDibujo, (230, 980), 30, (255,0,0), -1)
cv2.circle(imgDibujo, (1770, 580), 30, (255,0,0), -1)
cv2.circle(imgDibujo, (2800, 2650), 30, (255,0,0), -1)
cv2.circle(imgDibujo, (600, 3380), 30, (255,0,0), -1)

pts = puntos.reshape((-1,1,2))
cv2.polylines(imgDibujo, [pts.astype(np.int32)], True, (0,255,0), thickness=10)

plt.figure(figsize=(10,10))
plt.imshow(imgDibujo)
plt.show()

width = 500
height = 700

target = np.float32([[0,0], [width,0], [width,height], [0,height]])

matrix = cv2.getPerspectiveTransform(puntos, target)
result = cv2.warpPerspective(img, matrix, (width, height))

plt.figure(figsize=(10,10))
plt.imshow(result)
plt.show()
```

## **Espacios de Color y Conversiones**

Los espacios de color representan la información cromática de manera estructurada. RGB es aditivo (basado en luz), mientras que CMYK es sustractivo (basado en tinta). HSI (Hue-Saturation-Intensity) es intuitivo para humanos, separando intensidad de color.

### **Teoría**
- **Espectro de Color y Mezcla**: El espectro visible abarca longitudes de onda de ~400-700 nm. La mezcla aditiva (RGB) combina rojo, verde y azul para formar colores; la sustractiva (CMYK) resta luz con cian, magenta, amarillo y negro.
- **XYZ**: Espacio de color CIE 1931, basado en percepción humana, con coordenadas tricromáticas para representar todos los colores visibles.
- **RGB**: Tres canales (Rojo, Verde, Azul). Normalizado: valores en [0,1]. Decimal (e.g., (255,0,0)) vs. hexadecimal (e.g., #FF0000).
- **CMYK**: Cuatro canales (Cian, Magenta, Amarillo, Negro) para impresión.
- **HSI (Hue-Saturation-Intensity)**: 
  - **Hue (Matiz)**: Ángulo relacionado con la longitud de onda dominante (0-360°).
  - **Saturation (Saturación)**: Pureza del color (0-1; 0=gris, 1=puro).
  - **Intensity (Intensidad o Brillo)**: Media acromática de intensidad (0-1).
  RGB y CMYK no son intuitivos para humanos; HSI lo es, con intensidad en eje vertical.
- **Equivalencia y Conversiones**:
  - **RGB → HSI**:
    $$I = \frac{R + G + B}{3}, \quad S = 1 - \frac{3 \min(R,G,B)}{R+G+B}, \quad H = \cos^{-1}\left( \frac{(R-G) + (R-B)}{2\sqrt{(R-G)^2 + (R-B)(G-B)}} \right)$$
    Ajustar H basado en canales dominantes.
  - **HSI → RGB**: Dependiente del sector de H (e.g., para H en [0,120°]: R = I(1 + S cos H / cos(60°-H)), etc.).
- **Diagrama de Cromaticidad**: Representa colores en plano xy (CIE), ignorando brillo.
- **Gamut**: Rango de colores representables. Monitores (RGB) cubren ~72% NTSC; impresoras (CMYK) menos, debido a limitaciones físicas.

### **Práctica**
Ejemplos de conversiones y manipulación.

```python
# Lectura y conversión BGR a RGB
img = cv2.imread('Imagenes/centro1.jpg')  # Formato BGR por defecto en cv2
print(img.shape)  # (alto, ancho, canales)

plt.figure(figsize=(10,10))
plt.imshow(img)  # Muestra incorrecta sin conversión
plt.show()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Forma 1
# Alternativas: img = img[:,:,[2,1,0]] o img[:,:,::-1]

plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()

print(img[50,50,:])  # Valor RGB en píxel (50,50)

# Conversión a escala de grises
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# Alternativa: imgGray = cv2.imread('Imagenes/centro1.jpg', 0)

print(imgGray.shape)
plt.figure(figsize=(10,10))
plt.imshow(imgGray, cmap='gray')
plt.show()

# Conversión a HSV y detección de color (amarillo)
imgHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

amarillo = np.uint8([[[0, 0, 255]]])  # RGB amarillo
amarilloHSV = cv2.cvtColor(amarillo, cv2.COLOR_RGB2HSV)
print(amarilloHSV)  # Ejemplo: [[[30, 255, 255]]]

lower_amarillo = np.array([15, 90, 0])
upper_amarillo = np.array([40, 255, 255])

mask = cv2.inRange(imgHSV, lower_amarillo, upper_amarillo)
res = cv2.bitwise_and(img, img, mask=mask)

plt.figure(figsize=(10,10))
plt.imshow(res)
plt.show()
```

Para unión de canales (e.g., partes separadas):
```python
# Suponiendo parte_roja, parte_verde, parte_azul como matrices 2D
imagen_unida = np.dstack((parte_roja, parte_verde, parte_azul))
plt.imshow(imagen_unida)
plt.show()
```

## **Convoluciones de Imágenes**

La convolución aplica un kernel sobre la imagen para transformar píxeles basados en vecinos, revelando características como bordes o suavizado.

### **Teoría**
La convolución 2D es: $(f * g)(x,y) = \sum_{i,j} f(i,j) \cdot g(x-i, y-j)$, donde f es la imagen y g el kernel. En frecuencia, es multiplicación vía FFT para eficiencia.

### **Práctica**
- **Filtro de Promedio (Suavizado)**: Kernel uniforme (e.g., 3x3: 1/9 en todos).
```python
kernel_avg = np.ones((3,3), np.float32) / 9
img_avg = cv2.filter2D(img, -1, kernel_avg)

plt.imshow(img_avg)
plt.show()
```
- **Filtro Laplaciano (Detección de Bordes)**: Kernel: $$\begin{bmatrix} 0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0 \end{bmatrix}$$
```python
kernel_lap = np.array([[0,1,0], [1,-4,1], [0,1,0]])
img_lap = cv2.filter2D(imgGray, -1, kernel_lap)

plt.imshow(img_lap, cmap='gray')
plt.show()
```