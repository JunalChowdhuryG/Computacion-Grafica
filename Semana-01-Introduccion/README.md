# Semana 1: Introducción al Procesamiento de Imágenes

## Definición Básica de Imagen
- **Imagen digital**: Representación discreta de un espacio continuo. Se obtiene mediante dos procesos clave:
  - **Muestreo (Sampling)**: Discretización espacial, es decir, dividir el espacio continuo en una cuadrícula de píxeles (e.g., resolución de la imagen).
  - **Cuantización (Quantization)**: Discretización de los valores de intensidad o color, asignando valores finitos a rangos continuos (e.g., de infinito a 256 niveles en uint8).

Esto asume que el mundo real es continuo, pero un contrapunto escéptico: en física cuántica, el mundo es discreto a escalas subatómicas, aunque para imágenes prácticas, el modelo continuo es válido. Tu nota no menciona aliasing (efecto de muestreo insuficiente), que es una laguna común; lo agrego como completitud: si el muestreo es bajo, surge aliasing, distorsionando la imagen.

## Dominios de la Imagen
- **Dominio Espacial**: Representa la imagen en términos de posición (x, y). Aquí se aplican operaciones directas sobre píxeles.
- **Dominio de Frecuencia**: Representa la imagen en términos de frecuencias (e.g., via Transformada de Fourier). Útil para filtrado y compresión, ya que revela patrones repetitivos.

Perspectiva alternativa: Algunos frameworks (e.g., en machine learning) priorizan el dominio espacial para convoluciones en CNNs, mientras que el de frecuencia es clave en compresión como JPEG. Tu nota dice "Dominio -> Espacio | - Frecuencia", lo interpreto como jerarquía, pero en realidad son transformaciones mutuamente convertibles.

## Operaciones Básicas
- **Traslación**: Desplazamiento de la imagen en el plano (e.g., mover píxeles en x o y).
- **Rotación**: Giro de la imagen alrededor de un punto, usualmente el centro, usando matrices de transformación.

Agrego: Estas son transformaciones geométricas afines. Un escéptico podría notar que sin interpolación (e.g., bilineal), la rotación causa pérdida de información. Tu nota las menciona brevemente; las completo con que se representan matemáticamente como matrices 2x2 para 2D.

## Convoluciones
- **Definición**: Operación que aplica un kernel (filtro) sobre la imagen para transformar cada píxel basado en sus vecinos. No es solo "f(x) -> g(f(x))", que parece una composición de funciones; corrigo: En procesamiento de imágenes, la convolución 2D es $(f * g)(x,y) = \sum_{i,j} f(i,j) \cdot g(x-i, y-j)$, donde f es la imagen y g el kernel.
- Aplicaciones: Suavizado (blur), detección de bordes (e.g., Sobel), etc.

Contrapunto: En GPUs, convoluciones son eficientes vía FFT en dominio de frecuencia, cuestionando si siempre operar en espacial es óptimo. Completo esto porque tu nota es vaga.

## Métricas y Conceptos Adicionales
- **Reed-Solomon Error Correction**: Código de corrección de errores usado en almacenamiento y transmisión de datos (e.g., en CDs o QR codes con imágenes). Podría relacionarse con integridad de imágenes digitales; un escéptico diría que no es central en intro a gráficos, quizás sea de un tema de compresión o ruido.
- **Peak Signal to Noise Ratio (PSNR)**: Métrica de calidad de imagen, $PSNR = 10 \log_{10} \left( \frac{MAX^2}{MSE} \right)$, donde MAX es el valor máximo (e.g., 255 en uint8) y MSE el error cuadrático medio. Mide distorsión tras compresión o procesamiento.

## Modelos de Color y Dimensiones
- **RGB**: 3 canales (Rojo, Verde, Azul). Formatos: JPG, JPEG, etc. (compresión con pérdida).
- **RGBA**: 4 canales (RGB + Alpha para transparencia). Formato: PNG (compresión sin pérdida).
- **Escala de Grises**: 1 canal (intensidad).
- **Dimensiones**: Alto (height), Ancho (width), Canales (channels).  
Ejemplo de tu nota: `im.shape > (628, 1165)` → Alto: 628, Ancho: 1165, Canales: 1 (grises). Corrigo: En Python (e.g., con NumPy/OpenCV), es (alto, ancho, canales).

Perspectiva alternativa: Modelos como HSV o Lab son útiles para tareas específicas (e.g., segmentación), pero RGB es base para gráficos. Tu repetición de "3 RGB" y "4 RGBA" la elimino por redundancia.

## Tipos de Datos
- **uint8**: Entero sin signo de 8 bits, rango [0, 255]. Ideal para almacenamiento de imágenes (eficiente en memoria), pero puede causar overflow (después de 255, wrap-around a 0).
- **float32**: Flotante de 32 bits. Rango flexible, útil en GPUs para matrices normalizadas [0,1].
- **float64**: Flotante de 64 bits. Mayor precisión, pero más memoria; menos común en imágenes.

* **uint8** es estándar para visualización, pero floats evitan clipping en operaciones; un sesgo podría ser ignorar que floats consumen más VRAM en GPU.

## Distancias Métricas
- **Distancia de Minkowski**: Generalización de distancias, $d(p,q) = \left( \sum_{i=1}^n |p_i - q_i|^r \right)^{1/r}$, donde r ≥ 1 (a veces notado como p, pero uso r para evitar confusión).
  - r = 1: Distancia de Manhattan (suma de diferencias absolutas).
  - r = 2: Distancia Euclidiana (raíz de suma de cuadrados).
  - r → ∞: Distancia de Chebyshev (máximo de diferencias absolutas).

* Usada en clustering de píxeles o segmentación.

## Técnicas de Umbralización (Thresholding)
- **Definición**: Proceso para binarizar imágenes (e.g., convertir a blanco/negro) basado en un umbral t.
- **Técnicas**:
  - **Bruta (Global)**: Un t fijo para toda la imagen. Simple, pero falla en iluminaciones variables.
  - **Adaptativa**: t variable por regiones (e.g., media local). Mejor para imágenes no uniformes.
  - **Otsu**: Automático, maximiza varianza entre clases (fondo/objeto) via histograma. Asume bimodalidad.


## Sección Importante: Resolución y Explicaciones Detalladas
Como pediste "resolver y terminar" esta parte, la completo con demostraciones matemáticas, explicaciones y correcciones. Priorizo verdad: Tus suposiciones (e.g., p=inf es exactamente Chebyshev) son correctas, pero agrego pruebas para robustez. Investigé conceptualmente adaptive y Otsu (sin tools, basado en conocimiento estándar).

1. **Distancia de Minkowski y Chebyshev: Demostraciones**
   - **Fórmula General (Minkowski)**: Para dos puntos $\mathbf{p} = (p_1, \dots, p_n)$ y $\mathbf{q} = (q_1, \dots, q_n)$ en espacio n-dimensional:
     $$d_r(\mathbf{p}, \mathbf{q}) = \left( \sum_{i=1}^n |p_i - q_i|^r \right)^{1/r}, \quad r \geq 1$$
     - **Caso r=1 (Manhattan)**: $d_1 = \sum_{i=1}^n |p_i - q_i|$. Demostración simple: En 2D, es la suma de distancias horizontal y vertical, como caminos en una cuadrícula urbana.
     - **Caso r=2 (Euclidiana)**: $d_2 = \sqrt{\sum_{i=1}^n (p_i - q_i)^2}$. Derivada del teorema de Pitágoras; en imágenes, mide similitud de píxeles.
     - **Caso r→∞ (Chebyshev)**: Límite: $d_\infty = \max_{i=1}^n |p_i - q_i|$. Prueba: Cuando r crece, el término máximo domina la suma, ya que $(|a|^r + |b|^r)^{1/r} \approx \max(|a|, |b|)$ para r grande.
   - **Aplicación en Imágenes**: Útil en k-NN para clasificación de píxeles. Contrapunto: Manhattan es más rápida computacionalmente que Euclidiana en altas dimensiones.

2. **Umbralización y sus Técnicas**
   - **General**: Convierte imagen a binaria: píxel > t → 1 (objeto), else 0 (fondo).
   - **Bruta/Global**: t fijo. Falla en variaciones de luz; asumes uniformidad, que no siempre es cierta.
   - **Adaptativa**: Calcula t por ventana local (e.g., media - C). Prueba: En OpenCV, usa `cv2.adaptiveThreshold`. Perspectiva: Mejor para documentos escaneados, pero computacionalmente costosa.
   - **Otsu**: Método óptimo para histogramas bimodales. Algoritmo: Para cada t posible (0-255), calcula varianza entre clases $\sigma_b^2 = w_0 w_1 (\mu_0 - \mu_1)^2$, maximiza. Demostración: Asume distribución normal; maximizar $\sigma_b^2$ minimiza error de clasificación.

3. **Investigación sobre Adaptativa y Otsu**
   - **Adaptativa**: Variantes incluyen mean, Gaussian. Ejemplo: En una imagen con sombras, t global binariza mal; adaptativa ajusta por bloques. Laguna en tu nota: No considera tamaño de ventana (e.g., 11x11 píxeles). Contrapunto: Sensible a ruido; prefiltrado (e.g., Gaussian blur) ayuda.
   - **Otsu**: Basado en Nobuyuki Otsu (1979). Extensión: Multi-Otsu para >2 clases. Prueba en código: En Python con skimage, `threshold_otsu(img)`. Alternativa: Si histograma no bimodal, usa Ridler-Calvard o ML-based thresholding. Tu suposición "areas determinadas" es vaga; Otsu determina t global pero óptimo para separación.
