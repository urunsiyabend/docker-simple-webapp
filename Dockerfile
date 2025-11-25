# Dockerfile
FROM python:3.12-slim

# Daha öngörülebilir runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Bağımlılıklar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodu
COPY app/ ./app

# 8080'de dinle
EXPOSE 8080

# Flask uygulamasını çalıştır
CMD ["python", "app/app.py"]
