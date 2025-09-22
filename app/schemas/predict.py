from pydantic import BaseModel, Field
from typing import Any, Optional

class PredictRequest(BaseModel):
    # coloca aquí los campos que enviará tu frontend (por ahora cualquiera)
    payload: Optional[Any] = Field(default=None, description="Datos de entrada")

class PredictResponse(BaseModel):
    success: bool = True
    message: str = "Predict endpoint operativo"
    received: Optional[Any] = None
