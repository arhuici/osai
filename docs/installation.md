## Requisitos
- Docker
- Docker Compose

## Instalación y Ejecución
1. Clonar el repositorio:  
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