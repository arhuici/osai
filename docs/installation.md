## Requisitos
- Docker
- Docker Compose

## Instalación y Ejecución
1. Clonar el repositorio:  
``` git clone https://github.com/arhuici/osai ```
2. Introducir Artículos a analizar en la carpeta `/articles` del proyecto.
3. Construir y levantar contenedores:  
```docker compose up -d --build python_app grobid```
4. Ejecutar scripts:
    - Wordcloud:  
```docker exec -it python_app python /app/scripts/s_wordcloud.py```
    - Figuras:  
```docker exec -it python_app python /app/scripts/s_figures.py```
    - Links:  
```docker exec -it python_app python /app/scripts/s_links.py```

5. Transferir resultados a local (Opcional)
    - Wordcloud:  
```docker cp python_app:/app/persistent/results/wordcloud.png ./python/results```
    - Figuras:  
```docker cp python_app:/app/persistent/results/figures.png ./python/results```
    - Links:  
```docker cp python_app:/app/persistent/results/links.json ./python/results```

### Comandos adicionales
6. Terminar aplicación:  
    - Eliminar contenedores (manteniendo el volumen creado):  
```docker compose down```

    - Eliminar contenedores y volumen:  
```docker compose down -v```