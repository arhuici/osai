[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14976591.svg)](https://doi.org/10.5281/zenodo.14976591)

Autor: Romero Huici, Ángel
# Descripción
Esta se trata de la documentación del repositorio que contiene el primer proyecto asociado al curso de Artificial Intelligence And Open Science In Research Software Engineering de 2025.

La aplicación que contiene utiliza Docker para montar dos contenedores: uno con GROBID y otro con un entorno Python. Esta aplicación permite analizar artículos científicos y extraer información mediante tres scripts.

Los scripts se ejecutan automáticamente al levantar los contenedores pero se pueden volver a ejecutar de forma manual.


## Funcionalidades
- Wordcloud de keywords:  
Genera una nube de palabras a partir de los abstracts de los artículos. Devuelve un archivo .png
- Conteo de figuras:  
Crea una visualización con el número de figuras por artículo. Devuelve un archivo .png
- Lista de links:  
 Genera una lista por artículo de los links que contiene. Devuelve un archivo .json
- Resultados:  
 Los resultados de los scripts se almacenan en la carpeta `/results` asociada al volumen de Docker `data_volume`.

## Uso de la aplicación

Comprueba la guía de instalación.

## Referencias
Garijo, D., Mao, A., Dharmala, H., Diwanji, C., Wang, J., Kelley, A., & García, M. A. (2025). SOMEF: Software metadata extraction framework (0.9.8). Zenodo. https://doi.org/10.5281/zenodo.14865582