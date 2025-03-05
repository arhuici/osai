
# Características del proyecto

## Características de los contenedores

### Docker Compose
- Genera dos contenedores: python_app y grobid. El primero se inicializa cuando el segundo está corriendo y en funcionamiento.  
- Los dos contenedores se despliegan en una misma red para su comunicación.  
- El contenedor python_app tiene enlazado un volumen para asegurar la persistencia de los resultados obtenidos con los scripts.

### Dockerfile grobid
Recoge la imagen de Docker Hub e instala curl para poder realizar la comprobación de salud en el Docker Compose.

### Dockerfile python_app
Recoge la imagen de Python, instala las librerías necesarias para el funcionamiento de los scripts y prepara el entorno de trabajo con las carpetas `/scripts` en la que se sitúan los tres scripts, `/articles` con los pdf de entrada y `/results` con los resultados de los scripts. Por último, se mantiene el contenedor en ejecución para poder lanzar los scripts de Python.  
Por último, llama al entrypoint que ejecuta los scripts de forma automática y mantiene el contenedor vivo para futuras conexiones.

### Volumen data_volume
Este volumen tiene las mismas carpetas `/articles` y `/results` del contenedor python_app, situadas en el subdirectorio `/peristent`.  
De esta forma, la persistencia se mantiene para los archivos de entrada y salida.

## Características de los scripts

### General
Cada uno de los tres scripts realiza las tareas de obtención de los artículos y conversión a XML mediante Grobid.  
De esta forma, cada uno de los scripts funcionaría como una aplicación independiente de los demás.  
Además los scripts van imprimiendo por pantalla resultados parciales con el fin de facilitar la verificación de su funcionamiento.

- Obtención de artículos:  
Se leen aquellos artículos que sean .pdf. Si no se encuentra ninguno, el programa acaba.  
No se realizan comprobaciones sobre si los archivos son artículos científicos o no.

- Conversión a XML con Grobid:  
Por cada uno de los pdfs encontrados, se envía una petición POST al servicio de Grobid para convertir el texto completo de cada uno de ellos a xml y así extraer lo correspondiente a cada script.  
Por ello, si la respuesta del servidor no es 200 o no se encuentra lo que se quiere buscar, no se procesa el texto del artículo en cuestión que haya dado error.  

### Wordcloud
Tras obtener los abstracts de los artículos mediante su etiqueta TEI se extraen las palabras clave y se crea la nube de palabras. Se obtiene un abstract por artículo, el primero en el caso de que hayan varios.
- Extracción de palabras clave:  
Se elimina del texto los caracteres especiales y se convierten a minúscula el resto de palabras.  
No se eliminan elementos como stopwords porque la implementación de wordcloud utilizada ya lo hace.
- Creación de nube de palabras:  
Con el texto tratado se genera la nube de palabras y se almacena en `results/wordcloud.png` para su visualización.

### Figuras
Tras obtener las figuras de los artículos mediante sus etiquetas TEI, se cuentan y se dibujan en un bar chart. Se obtienen todas las figuras de cada artículo.

- Bar chart:  
Se dibuja un gráfico con el número de figuras frente a un índice. El gráfico se almacena posteriormente en `results/figures.png` para su visualización.


### Links 
Tras obtener los links de cada artículo mediante una expresión regex, se guardan en un diccionario cuyas claves son índices, al igual que en el caso de las Figuras, y cuyos valores son las listas de links encontrados en cada archivo. Posteriormente, se almacena en un archivo json.  
De esta forma se pueden visualizar los links que se han encontrado por artículo.
- JSON:  
Se almacena el diccionario obtenido con todos los links para su visualización y análisis en `results/links.json`.

## Pruebas realizadas

El proyecto contiene tres conjuntos de pruebas unitarias realizadas sobre cada uno de los tres scripts.

Para información más detallada y como ejecutarlos, visita la web del proyecto.