"""Endpoints HTTP para consultar y procesar recordatorios locales."""

from datetime import datetime
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.database import conectar
from app.recordatorios import procesar_recordatorios

router = APIRouter(prefix="/api/recordatorios", tags=["recordatorios"])
DATABASE_PATH = Path(__file__).parents[2] / "organizador.db"


class SolicitudProcesamiento(BaseModel):
    ahora: datetime | None = None


@router.get("/estado")
def estado_recordatorios() -> dict:
    with conectar(DATABASE_PATH) as conexion:
        pendientes = conexion.execute(
            "SELECT COUNT(*) AS total FROM recordatorios WHERE estado = 'pendiente'"
        ).fetchone()["total"]
    return {"disponible": True, "pendientes": pendientes}


@router.post("/procesar")
def procesar(solicitud: SolicitudProcesamiento | None = None) -> dict:
    try:
        emitidos = procesar_recordatorios(
            DATABASE_PATH, ahora=solicitud.ahora if solicitud else None
        )
    except (OSError, ValueError):
        raise HTTPException(
            status_code=503, detail="No fue posible procesar los recordatorios."
        )
    return {"emitidos": emitidos}
