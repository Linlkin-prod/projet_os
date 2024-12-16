FROM python:3.9-slim

WORKDIR /app

COPY server.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 12345

HEALTHCHECK --interval=30s --timeout=10s CMD nc -z localhost 12345 || exit 1

RUN chmod +x server.py

CMD ["python", "server.py"]
