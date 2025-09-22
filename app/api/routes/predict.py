from fastapi import APIRouter, Depends
from app.schemas.predict import PredictRequest, PredictResponse
from app.services.predict_service import PredictService

router = APIRouter(prefix="/predict", tags=["predict"])

def get_predict_service() -> PredictService:
    # Punto de inyección de dependencias (reemplazable en tests)
    return PredictService()

@router.post("", response_model=PredictResponse)
async def predict(
    body: PredictRequest,
    service: PredictService = Depends(get_predict_service),
):
    result = service.predict(body.payload)
    return PredictResponse(**result)
