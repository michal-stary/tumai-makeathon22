FROM python:3.8-slim

WORKDIR /app

# copy processing and serving
COPY ./src /app/src

RUN pip install --upgrade pip && pip install -r src/requirements.txt

EXPOSE 8080
CMD python3 src/service.py 8080