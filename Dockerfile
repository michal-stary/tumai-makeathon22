FROM python:3.8-slim

WORKDIR /app

COPY ./src/requirements.txt /app/src/requirements.txt
RUN pip install --upgrade pip && pip install -r src/requirements.txt

# copy processing and serving
COPY ./src /app/src

ENV PYTHONPATH "${PYTHONPATH}:/app/src/reg_score"


EXPOSE 8080
CMD python3 src/service.py 8080