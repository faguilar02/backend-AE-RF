from typing import List, Optional, Union, Literal
from pydantic import BaseModel, Field

CanalUso = Literal["online", "pos", "atm", "transf"]
Dispositivo = Literal["mobile", "desktop", "unknown"]

class PredictRequest(BaseModel):
    """Schema de entrada para predicción individual."""
    id_transaccion: Union[int, str]
    fecha: str
    monto_operacion: float
    canal_uso: CanalUso
    dispositivo: Dispositivo
    ubigeo_distrito: Optional[int] = None
    ubigeo_provincia: Optional[int] = None
    bill_lat: Optional[float] = None
    bill_lon: Optional[float] = None
    merch_lat: Optional[float] = None
    merch_long: Optional[float] = None
    ship_lat: Optional[float] = None
    ship_long: Optional[float] = None
    dist1: Optional[float] = None
    dist2: Optional[float] = None

class PredictBatchRequest(BaseModel):
    """Schema de entrada para predicción en batch."""
    items: List[PredictRequest]

class PredictResponse(BaseModel):
    """Schema de salida para predicción individual."""
    id_transaccion: Union[int, str]
    anomaly_score: float
    threshold: float
    label_pred: Literal[0, 1]
    channel_used: CanalUso
    model: dict = Field(default={"name": "ae_per_channel", "version": "0.0.0-dry-run"})
    distances: Optional[dict] = None
    feature_flags: Optional[dict] = None
    explanations: Optional[list] = None
    timing_ms: Optional[int] = None
    warnings: Optional[List[str]] = None
    errors: Optional[List[str]] = None

class PredictBatchResponse(BaseModel):
    """Schema de salida para predicción en batch."""
    items: List[PredictResponse]
