# Semana 1: Introducción al Procesamiento de Imágenes

## Definición Básica de Imagen
- **Imagen digital**: Representación discreta de un espacio continuo. Se obtiene mediante dos procesos clave:
  - **Muestreo (Sampling)**: Discretización espacial, que divide el espacio continuo en una cuadrícula de píxeles, determinando la resolución de la imagen.
  - **Cuantización (Quantization)**: Discretización de los valores de intensidad o color, asignando un número finito de niveles a rangos continuos, como por ejemplo de un espectro infinito a 256 niveles en formato uint8.

Este enfoque se basa en el modelo continuo del mundo real, aunque en física cuántica se reconoce una discreción a escalas subatómicas. Para aplicaciones prácticas en imágenes, el modelo continuo resulta adecuado. Es importante considerar el efecto de aliasing, que surge cuando el muestreo es insuficiente y provoca distorsiones en la imagen, como patrones no deseados.

## Dominios de la Imagen
- **Dominio Espacial**: Representa la imagen en términos de posiciones coordenadas (x, y), permitiendo operaciones directas sobre los píxeles individuales.
- **Dominio de Frecuencia**: Representa la imagen en términos de componentes de frecuencia, típicamente mediante la Transformada de Fourier. Este dominio es particularmente útil para tareas como el filtrado de ruido y la compresión de datos, al revelar patrones repetitivos y variaciones en la imagen.

Ambos dominios son complementarios y se pueden convertir mutuamente mediante transformaciones. En contextos como el aprendizaje automático, las redes convolucionales (CNN) suelen operar en el dominio espacial, mientras que técnicas de compresión como JPEG aprovechan el dominio de frecuencia para mayor eficiencia.

## Operaciones Básicas
- **Traslación**: Desplazamiento de la imagen en el plano cartesiano, ajustando las posiciones de los píxeles en las direcciones x o y.
- **Rotación**: Giro de la imagen alrededor de un punto de referencia, comúnmente el centro, utilizando matrices de transformación geométrica.

Estas operaciones forman parte de las transformaciones afines en dos dimensiones, representadas matemáticamente por matrices de 2x2. Para preservar la calidad, es esencial aplicar métodos de interpolación, como el bilineal, ya que sin ellos puede ocurrir pérdida de información o artefactos visuales.

## Convoluciones
- **Definición**: Operación matemática que aplica un kernel (o filtro) sobre la imagen para modificar cada píxel en función de sus valores vecinos. En el contexto del procesamiento de imágenes en dos dimensiones, la convolución se define como $(f * g)(x,y) = \sum_{i,j} f(i,j) \cdot g(x-i, y-j)$, donde $f$ representa la imagen y $g$ el kernel.
- Aplicaciones: Incluyen el suavizado (blur) para reducir ruido, la detección de bordes mediante kernels como Sobel, y el realce de características específicas.

En entornos computacionales avanzados, como GPUs, las convoluciones pueden optimizarse mediante la Transformada Rápida de Fourier (FFT) en el dominio de frecuencia, lo que cuestiona la necesidad de operar siempre en el dominio espacial para todas las tareas.

## Métricas y Conceptos Adicionales
- **Reed-Solomon Error Correction**: Código de corrección de errores empleado en el almacenamiento y transmisión de datos digitales, como en códigos QR o discos compactos, para mantener la integridad de las imágenes ante posibles corrupciones.
- **Peak Signal to Noise Ratio (PSNR)**: Métrica cuantitativa de la calidad de una imagen, calculada como $PSNR = 10 \log_{10} \left( \frac{MAX^2}{MSE} \right)$, donde $MAX$ es el valor máximo posible de intensidad (por ejemplo, 255 en uint8) y $MSE$ el error cuadrático medio. Esta métrica evalúa la distorsión introducida por procesos como la compresión o el filtrado.

## Modelos de Color y Dimensiones
- **RGB**: Compuesto por tres canales (Rojo, Verde, Azul), comúnmente almacenado en formatos como JPG o JPEG, que utilizan compresión con pérdida.
- **RGBA**: Incluye cuatro canales (RGB más Alpha para transparencia), típicamente en formatos como PNG, con compresión sin pérdida.
- **Escala de Grises**: Representado por un solo canal de intensidad.
- **Dimensiones**: Definidas por el alto (height), ancho (width) y número de canales (channels). Por ejemplo, en bibliotecas como NumPy u OpenCV en Python, la forma de una imagen se expresa como (alto, ancho, canales), tal como (628, 1165) para una imagen en escala de grises con un canal implícito.

Otros modelos de color, como HSV o Lab, ofrecen ventajas en tareas específicas como la segmentación, aunque RGB permanece como base estándar para la mayoría de las aplicaciones gráficas.

## Tipos de Datos
- **uint8**: Entero sin signo de 8 bits, con rango [0, 255]. Es eficiente en términos de memoria y estándar para el almacenamiento y visualización de imágenes, aunque susceptible a overflow, donde valores superiores a 255 se envuelven a 0.
- **float32**: Flotante de 32 bits, con rango flexible y útil para operaciones normalizadas en [0,1], especialmente en aceleradores como GPUs.
- **float64**: Flotante de 64 bits, que proporciona mayor precisión numérica, aunque consume más recursos de memoria y es menos común en el procesamiento de imágenes rutinario.

Los tipos flotantes evitan problemas de recorte en cálculos intermedios, pero requieren consideración del consumo de recursos en entornos con limitaciones de hardware.

## Distancias Métricas
- **Distancia de Minkowski**: Generalización de métricas de distancia, definida como $d(p,q) = \left( \sum_{i=1}^n |p_i - q_i|^r \right)^{1/r}$, donde $r \geq 1$.
  - $r = 1$: Distancia de Manhattan, suma de diferencias absolutas.
  - $r = 2$: Distancia Euclidiana, raíz cuadrada de la suma de diferencias al cuadrado.
  - $r \to \infty$: Distancia de Chebyshev, máximo de las diferencias absolutas.

Estas distancias se aplican en algoritmos como el clustering de píxeles o la segmentación de imágenes, donde la elección de $r$ influye en la sensibilidad a dimensiones específicas.

## Técnicas de Umbralización (Thresholding)
- **Definición**: Proceso de binarización de imágenes, que convierte los valores de píxeles en dos categorías (por ejemplo, blanco y negro) basándose en un valor umbral $t$. Matemáticamente, para un píxel con intensidad $I(x,y)$, si $I(x,y) > t$, se asigna 1 (objeto); de lo contrario, 0 (fondo). Esta técnica es fundamental en la segmentación inicial de imágenes, facilitando la detección de objetos o regiones de interés.
- **Técnicas**:
  - **Bruta (Global)**: Utiliza un umbral $t$ fijo para toda la imagen. Es computacionalmente simple y efectivo en escenarios con iluminación uniforme, pero puede fallar en imágenes con variaciones de contraste o sombras, ya que no adapta a condiciones locales. Por ejemplo, en una imagen con gradientes de luz, un $t$ global podría clasificar incorrectamente regiones oscuras como fondo.
  - **Adaptativa**: Calcula umbrales variables según regiones locales de la imagen, como la media o mediana de una ventana deslizante (por ejemplo, de tamaño 11x11 píxeles). Esto mejora el rendimiento en imágenes no uniformes, ajustándose a cambios en la iluminación. Variantes incluyen el método de media (donde $t = \mu - C$, con $\mu$ como media local y $C$ una constante) o el gaussiano, que pondera los píxeles cercanos con una distribución normal. Sin embargo, requiere selección cuidadosa del tamaño de ventana para evitar artefactos como halos en bordes.
  - **Otsu**: Método automático que selecciona $t$ óptimo maximizando la varianza entre clases (fondo y objeto) a partir del histograma de la imagen. Asume una distribución bimodal y calcula, para cada $t$ posible (de 0 a 255), la varianza entre clases $\sigma_b^2 = w_0 w_1 (\mu_0 - \mu_1)^2$, donde $w_0, w_1$ son las probabilidades de cada clase y $\mu_0, \mu_1$ sus medias. El $t$ que maximiza $\sigma_b^2$ minimiza el error de clasificación intra-clase. Es eficiente para histogramas bimodales, pero puede suboptimizarse en distribuciones multimodales o con ruido significativo.

Estas técnicas se combinan frecuentemente con preprocesamiento, como filtrado gaussiano, para mitigar ruido y mejorar la precisión.

## Sección Importante: Resolución y Explicaciones Detalladas
Esta sección proporciona demostraciones matemáticas y explicaciones detalladas para conceptos clave, asegurando una comprensión robusta basada en principios establecidos.

1. **Distancia de Minkowski y Chebyshev: Demostraciones**
   - **Fórmula General (Minkowski)**: Para dos puntos $\mathbf{p} = (p_1, \dots, p_n)$ y $\mathbf{q} = (q_1, \dots, q_n)$ en un espacio n-dimensional:
     $$d_r(\mathbf{p}, \mathbf{q}) = \left( \sum_{i=1}^n |p_i - q_i|^r \right)^{1/r}, \quad r \geq 1$$
     - **Caso r=1 (Manhattan)**: $d_1 = \sum_{i=1}^n |p_i - q_i|$. En un plano 2D, equivale a la distancia recorrida en ejes perpendiculares, similar a la navegación en una cuadrícula urbana. Demostración: Para puntos (0,0) y (3,4), $d_1 = 3 + 4 = 7$.
     - **Caso r=2 (Euclidiana)**: $d_2 = \sqrt{\sum_{i=1}^n (p_i - q_i)^2}$. Derivada del teorema de Pitágoras; en imágenes, mide la similitud directa entre vectores de píxeles. Ejemplo: Para los mismos puntos, $d_2 = \sqrt{9 + 16} = 5$.
     - **Caso r→∞ (Chebyshev)**: $d_\infty = \max_{i=1}^n |p_i - q_i|$. Prueba matemática: A medida que $r$ aumenta, el término mayor en la suma domina, ya que $\left( a^r + b^r \right)^{1/r} \to \max(a, b)$ para $a > b > 0$. En el ejemplo, $d_\infty = \max(3,4) = 4$.
   - **Aplicación en Imágenes**: Empleadas en algoritmos como k-vecinos más cercanos (k-NN) para clasificación de píxeles en segmentación. La distancia de Manhattan es computacionalmente más eficiente en dimensiones altas, mientras que la Euclidiana captura similitudes geométricas más intuitivas.

2. **Umbralización y sus Técnicas**
   - **General**: La umbralización transforma una imagen de intensidades continuas en una binaria, facilitando análisis posteriores como el conteo de objetos o la detección de formas. Es sensible al ruido, por lo que se recomienda un prefiltrado (por ejemplo, mediana o gaussiano) para estabilizar los resultados.
   - **Bruta/Global**: Aplicable cuando la imagen presenta un contraste bimodal claro y uniforme. Limitaciones: En presencia de variaciones de iluminación, puede generar falsos positivos o negativos. Ejemplo práctico: En una imagen médica de rayos X con fondo uniforme, un $t=128$ podría separar tejidos efectivamente.
   - **Adaptativa**: Ideal para imágenes con iluminaciones heterogéneas, como documentos escaneados o fotografías al aire libre. El cálculo local reduce errores en regiones variables, pero introduce parámetros como el tamaño de ventana (demasiado pequeño genera ruido; demasiado grande, pierde detalles locales) y la constante de ajuste $C$. En implementaciones como OpenCV, funciones como `cv2.adaptiveThreshold(img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=11, C=2)` permiten personalización.
   - **Otsu**: Proporciona un enfoque no supervisado, optimizando la separación de clases mediante análisis de histograma. Extensión: Para imágenes multimodales, se puede aplicar Multi-Otsu, que encuentra múltiples umbrales. Demostración numérica: Suponga un histograma con picos en 50 y 200; Otsu selecciona $t \approx 125$ para maximizar la varianza entre clases. En Python con scikit-image, se invoca como `from skimage.filters import threshold_otsu; t = threshold_otsu(img)`.

3. **Investigación sobre Adaptativa y Otsu**
   - **Adaptativa**: Desarrollada para abordar limitaciones de métodos globales, esta técnica se basa en el análisis local de vecindades. Variantes clave incluyen: (i) Adaptativa por media, que usa la media local menos una constante; (ii) Adaptativa gaussiana, que aplica pesos gaussianos para priorizar píxeles centrales, reduciendo sensibilidad al ruido periférico. En aplicaciones reales, como el procesamiento de imágenes satelitales con sombras variables, el método adaptativo supera al global al preservar detalles en áreas de bajo contraste. Consideraciones prácticas: El tamaño de ventana debe ser impar y mayor que el ruido esperado (por ejemplo, 3x3 para ruido mínimo, 31x31 para variaciones amplias). Limitaciones: Alto costo computacional en imágenes grandes, aunque optimizable con procesamiento paralelo. Alternativas incluyen métodos basados en aprendizaje automático, como redes neuronales para umbrales dinámicos, que incorporan contexto semántico.
   - **Otsu**: Propuesto por Nobuyuki Otsu en 1979, este algoritmo asume que la imagen se compone de dos clases gaussianas y busca minimizar la varianza intra-clase (equivalente a maximizar la inter-clase). Prueba detallada: El histograma se normaliza como probabilidades $p(i)$; para un umbral $t$, $w_0 = \sum_{i=0}^t p(i)$, $\mu_0 = \sum_{i=0}^t i p(i) / w_0$, y análogamente para $w_1, \mu_1$. La varianza $\sigma_b^2$ se evalúa exhaustivamente para $t=1$ a $254$, seleccionando el máximo. En casos no bimodales, como histogramas uniformes, Otsu puede fallar, sugiriendo preprocesamiento como ecualización de histograma. Extensiones: Otsu 2D incorpora información espacial (gradientes), mejorando robustez al ruido. En bibliotecas como MATLAB o Python (con OpenCV: `ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)`), es de implementación directa. Perspectiva comparativa: Otsu es más rápido que adaptativo para imágenes grandes, pero menos flexible en escenarios no uniformes; una combinación (Otsu local) integra lo mejor de ambos.