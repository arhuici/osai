# Guía de Instalación y Uso
## Requisitos
- Docker
- Docker Compose

## Instalación y Ejecución
1. Clonar el repositorio y navegar a la aplicación:  
``` git clone https://github.com/arhuici/osai ```  
``` cd osai/app ```
2. Introducir artículos a analizar en la carpeta `/articles` del proyecto.
3. Construir y levantar contenedores (los scripts se ejecutan automáticamente):  
```docker compose up --build python_app grobid```


## Transferir Resultados y Otros Comandos
Se puede requerir abrir una terminal en la carpeta `/app` del proyecto.  
- Transferir resultados a máquina local:  
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