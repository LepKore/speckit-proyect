"""Creación y consulta del estado de recordatorios asociados a tareas."""

import sqlite3
from datetime import datetime
from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.database import conectar
from app.models import Tarea
from app.recordatorios import programar_recordatorio

router = APIRouter(prefix="/api/tareas", tags=["tareas"])
DATABASE_PATH = Path(__file__).parents[2] / "organizador.db"


def validar_fecha(valor: str) -> datetime:
    try:
        return datetime.fromisoformat(valor.replace("Z", "+00:00"))
    except (ValueError, AttributeError) as exc:
        raise HTTPException(
            status_code=422, detail="La fecha de entrega debe tener formato ISO válido."
        ) from exc


@router.post("", status_code=201)
def crear_tarea(tarea: Tarea) -> dict:
    entrega = validar_fecha(tarea.fecha_entrega)
    try:
        with conectar(DATABASE_PATH) as conexion:
            if conexion.execute(
                "SELECT 1 FROM materias WHERE id = ?", (tarea.materia_id,)
            ).fetchone() is None:
                raise HTTPException(status_code=404, detail="La materia no existe.")
            cursor = conexion.execute(
                """INSERT INTO tareas
                   (materia_id, titulo, descripcion, fecha_entrega, completada)
                   VALUES (?, ?, ?, ?, ?)""",
                (
                    tarea.materia_id,
                    tarea.titulo,
                    tarea.descripcion,
                    entrega.isoformat(),
                    int(tarea.completada),
                ),
            )
            tarea_id = cursor.lastrowid
            if not tarea.completada:
                programar_recordatorio(conexion, tarea_id, entrega)
    except sqlite3.IntegrityError as exc:
        raise HTTPException(status_code=400, detail="No fue posible guardar la tarea.") from exc
    return {**tarea.model_dump(), "id": tarea_id, "fecha_entrega": entrega.isoformat()}


@router.get("/{tarea_id}/recordatorio")
def obtener_recordatorio(tarea_id: int) -> dict:
    with conectar(DATABASE_PATH) as conexion:
        tarea = conexion.execute(
            "SELECT fecha_entrega FROM tareas WHERE id = ?", (tarea_id,)
        ).fetchone()
        if tarea is None:
            raise HTTPException(status_code=404, detail="La tarea no existe.")
        fila = conexion.execute(
            """SELECT id, tarea_id, fecha_entrega, fecha_aviso, estado, emitido_en
               FROM recordatorios WHERE tarea_id = ? AND fecha_entrega = ?""",
            (tarea_id, tarea["fecha_entrega"]),
        ).fetchone()
    if fila is None:
        return {"tarea_id": tarea_id, "estado": "no_programado"}
    return dict(fila)
