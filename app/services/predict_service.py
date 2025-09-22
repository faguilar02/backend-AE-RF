from typing import Any

class PredictService:
    """Capa de dominio/servicio. Una responsabilidad: manejar predicciones.
    Por ahora solo confirma recepción (dummy)."""

    def predict(self, payload: Any) -> dict:
        # Aquí luego cargarás el modelo, preprocesarás, etc.
        return {
            "success": True,
            "message": "Predict endpoint operativo",
            "received": payload,
        }
