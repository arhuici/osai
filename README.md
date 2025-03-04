# Proyecto Análisis de Artículos
Este repositorio contiene el primer proyecto asociado al curso de Artificial Intelligence And Open Science In Research Software Engineering de 2025.

La aplicación que contiene utiliza Docker para montar dos contenedores: uno con GROBID y otro con un entorno Python. Esta aplicación permite analizar artículos científicos y extraer información mediante tres scripts.

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
1. Clonar este repositorio:  
``` git clone https://github.com/arhuici/osai ```
2. Introducir Artículos a analizar en la carpeta `/articles` del proyecto.
2. Construir y levantar contenedores:  
```docker compose up -d --build```
3. Ejecutar scripts:
    - Wordcloud:  
```docker exec -it python_app python /app/scripts/s_links.py```
    - Figuras:  
```docker exec -it python_app python /app/scripts/s_figures.py```
    - Links:  
```docker exec -it python_app python /app/scripts/s_links.py```

4. Transferir resultados a local (Opcional)
    - Wordcloud:  
```docker cp python_app:/app/persistent/results/wordcloud.png .```
    - Figuras:  
```docker cp python_app:/app/persistent/results/figures.png .```
    - Links:  
```docker cp python_app:/app/persistent/results/links.json .```

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.