# Stage 1: Builder (opcional para dependencias compiladas)
FROM python:3.10-slim as builder

WORKDIR /app

# Instalar dependencias del sistema si fueran necesarias (ej. gcc para algunas libs)
# RUN apt-get update && apt-get install -y --no-install-recommends build-essential

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.10-slim

WORKDIR /app

# Copiar dependencias desde builder
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiar código de la aplicación
COPY ./app ./app

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

# Exponer puerto
EXPOSE 8000

# Comando de inicio (producción con Gunicorn + Uvicorn workers)
CMD ["gunicorn", "app.main:app", \
     "--worker-class", "uvicorn.workers.UvicornWorker", \
     "--workers", "4", \
     "--bind", "0.0.0.0:8000", \
     "--log-level", "info", \
     "--access-logfile", "-", \
     "--error-logfile", "-"]
