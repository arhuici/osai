[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14976979.svg)](https://doi.org/10.5281/zenodo.14976979)

Autor: Romero Huici, Ángel
# Proyecto Análisis de Artículos
Este repositorio contiene el primer proyecto asociado al curso de Artificial Intelligence And Open Science In Research Software Engineering de 2025.

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

## Requisitos
- Docker
- Docker Compose

## Instalación y Ejecución
1. Clonar este repositorio y navegar a la aplicación:  
``` git clone https://github.com/arhuici/osai ```  
``` cd osai/app ```  
2. Introducir artículos a analizar en la carpeta `/articles` del proyecto.
3. Construir y levantar contenedores (los scripts se ejecutan automáticamente):  
```docker compose up --build python_app grobid```


## Transferir Resultados y Otros Comandos
Se puede requerir abrir una terminal en la carpeta `/app` del proyecto.
- Transferir resultados a máquina local
    - Wordcloud:  
```docker cp python_app:/app/persistent/results/wordcloud.png ./python/results```
    - Figuras:  
```docker cp python_app:/app/persistent/results/figures.png ./python/results```
    - Links:  
```docker cp python_app:/app/persistent/results/links.json ./python/results```

- Ejecutar scripts manualmente:
    - Wordcloud:  
```docker exec -it python_app python /app/scripts/s_wordcloud.py```
    - Figuras:  
```docker exec -it python_app python /app/scripts/s_figures.py```
    - Links:  
```docker exec -it python_app python /app/scripts/s_links.py```
- Terminar aplicación:  
    - Eliminar contenedores (manteniendo el volumen creado):  
```docker compose down```
    - Eliminar contenedores y volumen:  
```docker compose down -v```


## Citación del Repositorio
Romero Huici, Á. (2025). arhuici/osai. https://github.com/arhuici/osai

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

## Referencias
Garijo, D., Mao, A., Dharmala, H., Diwanji, C., Wang, J., Kelley, A., & García, M. A. (2025). SOMEF: Software metadata extraction framework (0.9.8). Zenodo. https://doi.org/10.5281/zenodo.14865582