#!/bin/bash

echo "Running s_links.py..."
python /app/scripts/s_links.py

echo "Running s_figures.py..."
python /app/scripts/s_figures.py

echo "Running s_wordcloud.py..."
python /app/scripts/s_wordcloud.py

tail -f /dev/null
