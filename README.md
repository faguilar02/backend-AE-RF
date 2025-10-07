# Backend AE-RF — FastAPI

API backend para predicción de anomalías en transacciones financieras usando Autoencoders y Random Forest.

## 🚀 Inicio Rápido

### Desarrollo Local (sin Docker)

1. **Crear entorno virtual e instalar dependencias:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. **Ejecutar servidor de desarrollo:**
   ```powershell
   python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

3. **Verificar endpoints:**
   - Health: http://localhost:8000/api/health
   - Docs: http://localhost:8000/docs (Swagger UI)

### Desarrollo con Docker

1. **Construir imagen:**
   ```powershell
   docker build -t backend-ae-rf:latest .
   ```

2. **Ejecutar contenedor:**
   ```powershell
   docker run --rm -p 8000:8000 backend-ae-rf:latest
   ```

3. **O usar Docker Compose (recomendado):**
   ```powershell
   docker-compose up --build
   ```

4. **Detener:**
   ```powershell
   docker-compose down
   ```

## 📡 Endpoints

### Base URL: `http://localhost:8000`

- **GET** `/api/health` — Health check
- **POST** `/api/predict` — Predicción individual
- **POST** `/api/predict/batch` — Predicción en batch

### Ejemplo de llamada (PowerShell):

```powershell
$json = @{
  id_transaccion = "TX001"
  fecha = "2025-10-07T10:30:00"
  monto_operacion = 150.50
  canal_uso = "online"
  dispositivo = "mobile"
  dist1 = 5.2
  dist2 = 3.1
} | ConvertTo-Json

Invoke-RestMethod -Uri http://localhost:8000/api/predict `
  -Method Post `
  -Body $json `
  -ContentType 'application/json'
```

### Ejemplo con curl:

```bash
curl -X POST http://localhost:8000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "id_transaccion": "TX001",
    "fecha": "2025-10-07T10:30:00",
    "monto_operacion": 150.50,
    "canal_uso": "online",
    "dispositivo": "mobile",
    "dist1": 5.2,
    "dist2": 3.1
  }'
```

## 🔧 Configuración

Variables de entorno (`.env` o configuradas en docker-compose):

- `APP_NAME`: Nombre de la aplicación
- `API_PREFIX`: Prefijo de rutas (default: `/api`)
- `CORS_ORIGINS`: Lista de orígenes permitidos para CORS

### CORS Configurado para:
- ✅ Desarrollo local: `http://localhost:4200` (Angular)
- ✅ Desarrollo alternativo: `http://localhost:3000`
- ✅ Producción: `https://frontend-ae-rf.vercel.app`

Para modificar orígenes CORS, edita `app/core/config.py` o usa variables de entorno.

## 📦 Estructura del Proyecto

```
fastapi-ae-rf/
├── app/
│   ├── main.py              # Entrada principal
│   ├── api/
│   │   └── routes/          # Endpoints
│   │       ├── health.py
│   │       └── predict.py
│   ├── core/
│   │   ├── config.py        # Configuración
│   │   └── logging.py       # Setup de logs
│   ├── schemas/
│   │   └── predict.py       # Modelos Pydantic
│   └── services/
│       └── predict_service.py  # Lógica de negocio
├── tests/                   # Tests unitarios
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🧪 Testing

```powershell
pytest tests/ -v
```

## 🚢 Despliegue en Producción

### Opción 1: VM/VPS con Docker

```bash
# En el servidor
git clone <repo>
cd fastapi-ae-rf
docker-compose up -d
```

### Opción 2: Cloud Platforms

- **Railway / Render**: Conectar repo, detecta Dockerfile automáticamente
- **Azure Container Instances**: `az container create --resource-group myRG --name backend-ae-rf --image <registry>/backend-ae-rf:latest --ports 8000`
- **AWS ECS / Fargate**: Subir imagen a ECR y crear servicio
- **Heroku**: Usar buildpack o container stack

### Opción 3: Kubernetes

```yaml
# deployment.yaml ejemplo
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-ae-rf
spec:
  replicas: 3
  selector:
    matchLabels:
      app: backend-ae-rf
  template:
    metadata:
      labels:
        app: backend-ae-rf
    spec:
      containers:
      - name: api
        image: backend-ae-rf:latest
        ports:
        - containerPort: 8000
```

## 🔐 Seguridad

- Restringir CORS en producción (editar `app/core/config.py`)
- Usar secretos para credenciales (no hardcodear en código)
- Configurar rate limiting y autenticación según necesidad
- Habilitar HTTPS con reverse proxy (nginx/Traefik)

## 📝 Notas

- Modo DRY-RUN activo: respuestas con valores fijos (sin modelo entrenado)
- Para integrar modelo real, editar `app/services/predict_service.py`

## 📄 Licencia

MIT
