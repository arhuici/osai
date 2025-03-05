# Pruebas realizadas

## Descripción

El proyecto contiene tres conjuntos de pruebas unitarias realizadas sobre cada uno de los tres scripts.

### Wordcloud

Se realizan pruebas en los siguientes escenarios sobre el método `get_abstracts()`:  
- El artículo tiene un abstract.  
- El artículo tiene más de un abstract.  
- El artículo no tiene abstract.  
- El servicio Grobid envía un error en la conversión.  

Se realizan pruebas en los siguientes escenarios sobre el método `draw_wordcloud()`:  
- Se han procesado abstracts de varios artículos.  
- No se han procesado abstracts de ningún artículo.  


### Figuras
Se realizan pruebas en los siguientes escenarios sobre el método `get_n_figures()`:  
- Hay figuras en el artículo.  
- No hay figuras en el artículo.  

Se realizan pruebas en los siguientes escenarios sobre el método `draw_figures()`:  
- Se han encontrado figuras en varios artículos.  
- No se han encontrado figuras en ningún artículo.  


### Links
Se realizan pruebas en los siguientes escenarios sobre el método `get_links()`:  
- Hay links en el artículo.  
- No hay links en el artículo.  

## Ejecución

1. Preparar entorno:  
    - Seguir la guía de Instalación.  
2. Ejecutar tests:  
    - Test Wordcloud:  
```docker exec -it python_app python -m unittest /app/scripts/test_wordcloud.py```
    - Test Figuras:  
```docker exec -it python_app python -m unittest /app/scripts/test_figures.py```
    - Test Links:  
```docker exec -it python_app python -m unittest /app/scripts/test_links.py```

Los resultados de los tests se mostrarán impresos en pantalla.