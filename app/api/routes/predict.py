from fastapi import APIRouter, Depends
from app.schemas.predict import (
    PredictRequest,
    PredictResponse,
    PredictBatchRequest,
    PredictBatchResponse,
)
from app.services.predict_service import PredictService

router = APIRouter(prefix="/predict", tags=["predict"])

def get_predict_service() -> PredictService:
    """Punto de inyección de dependencias (reemplazable en tests)."""
    return PredictService()


@router.post("", response_model=PredictResponse)
async def predict(
    body: PredictRequest,
    service: PredictService = Depends(get_predict_service),
):
    """
    Predicción individual (DRY-RUN).
    
    Ejemplo curl:
    ```bash
    curl -X POST http://localhost:8000/api/predict \
      -H "Content-Type: application/json" \
      -d '{
        "id_transaccion": "TX001",
        "fecha": "2025-10-07T10:30:00",
        "monto_operacion": 150.50,
        "canal_uso": "online",
        "dispositivo": "mobile",
        "ubigeo_distrito": 150101,
        "dist1": 5.2,
        "dist2": 3.1
      }'
    ```
    
    Ejemplo PowerShell:
    ```powershell
    $json = @{
      id_transaccion = "TX001"
      fecha = "2025-10-07T10:30:00"
      monto_operacion = 150.50
      canal_uso = "online"
      dispositivo = "mobile"
      ubigeo_distrito = 150101
      dist1 = 5.2
      dist2 = 3.1
    } | ConvertTo-Json
    Invoke-RestMethod -Uri http://localhost:8000/api/predict -Method Post -Body $json -ContentType 'application/json'
    ```
    """
    return service.dry_run_predict(body)


@router.post("/batch", response_model=PredictBatchResponse)
async def predict_batch(
    body: PredictBatchRequest,
    service: PredictService = Depends(get_predict_service),
):
    """
    Predicción en batch (DRY-RUN).
    
    Ejemplo curl:
    ```bash
    curl -X POST http://localhost:8000/api/predict/batch \
      -H "Content-Type: application/json" \
      -d '{
        "items": [
          {
            "id_transaccion": "TX001",
            "fecha": "2025-10-07T10:30:00",
            "monto_operacion": 150.50,
            "canal_uso": "online",
            "dispositivo": "mobile",
            "dist1": 5.2
          },
          {
            "id_transaccion": "TX002",
            "fecha": "2025-10-07T11:00:00",
            "monto_operacion": 99.99,
            "canal_uso": "pos",
            "dispositivo": "unknown"
          }
        ]
      }'
    ```
    
    Ejemplo PowerShell:
    ```powershell
    $json = @{
      items = @(
        @{
          id_transaccion = "TX001"
          fecha = "2025-10-07T10:30:00"
          monto_operacion = 150.50
          canal_uso = "online"
          dispositivo = "mobile"
          dist1 = 5.2
        },
        @{
          id_transaccion = "TX002"
          fecha = "2025-10-07T11:00:00"
          monto_operacion = 99.99
          canal_uso = "pos"
          dispositivo = "unknown"
        }
      )
    } | ConvertTo-Json -Depth 3
    Invoke-RestMethod -Uri http://localhost:8000/api/predict/batch -Method Post -Body $json -ContentType 'application/json'
    ```
    """
    responses = [service.dry_run_predict(item) for item in body.items]
    return PredictBatchResponse(items=responses)
