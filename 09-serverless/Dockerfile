FROM python:3.9-slim

RUN pip install --no-cache-dir numpy pillow tflite-runtime flask requests

COPY lambda_function.py /app/lambda_function.py
COPY model_2024_hairstyle.tflite /app/model_2024_hairstyle.tflite


WORKDIR /app

CMD ["python", "-m", "http.server", "8080"]
