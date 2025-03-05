FROM python:3.12

WORKDIR /app

COPY articles /app/persistent/articles
COPY scripts /app/scripts
COPY results /app/persistent/results

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

RUN pip3 install -r /app/scripts/requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]