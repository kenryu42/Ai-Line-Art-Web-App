FROM python:3.7

RUN apt-get update
RUN apt-get install -y cmake

COPY . app/
WORKDIR /app

RUN pip install -r requirements.txt

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
