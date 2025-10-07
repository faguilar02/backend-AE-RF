import time
from app.schemas.predict import PredictRequest, PredictResponse

class PredictService:
    """Capa de dominio/servicio. Maneja predicciones con modo DRY-RUN."""

    def dry_run_predict(self, req: PredictRequest) -> PredictResponse:
        """
        Modo DRY-RUN: valida schema y devuelve payload fijo sin procesar modelo.
        
        Args:
            req: PredictRequest validado por Pydantic
            
        Returns:
            PredictResponse con valores por defecto (anomaly_score=0, label_pred=0)
        """
        # Devuelve una respuesta fija en modo DRY-RUN según la petición del usuario.
        # Ignora el contenido de `req` y retorna los valores solicitados.
        return PredictResponse(
            id_transaccion=123456,
            anomaly_score=0.0,
            threshold=0.0,
            label_pred=0,
            channel_used="online",
            model={"name": "ae_per_channel", "version": "0.0.0-dry-run"},
            distances={"dist1": -1.0, "dist2": 2.84},
            feature_flags={"dist1_missing": 1, "dist2_missing": 0, "dt_unknown": 0},
            explanations=[],
            timing_ms=4,
            warnings=["dry-run: no se procesó el modelo"],
            errors=[],
        )
