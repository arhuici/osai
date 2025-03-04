FROM python:3.12

WORKDIR /app

COPY articles /app/persistent/articles
COPY scripts /app/scripts
COPY results /app/persistent/results

RUN pip3 install -r /app/scripts/requirements.txt

CMD tail -f /dev/null