FROM python:3.9-slim

WORKDIR /app

COPY src/message-service/ .

RUN pip install pika

CMD ["python", "publisher.py"]
