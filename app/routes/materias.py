"""Operaciones de materias."""

import sqlite3
from pathlib import Path

from fastapi import APIRouter, HTTPException, Query

from app.database import conectar
from app.models import Materia, normalizar_nombre


router = APIRouter(prefix="/api/materias", tags=["materias"])
DATABASE_PATH = Path(__file__).parents[2] / "organizador.db"


def _materia(fila: sqlite3.Row) -> dict:
    return {"id": fila["id"], "nombre": fila["nombre"], "color": fila["color"]}


@router.get("")
def listar_materias() -> list[dict]:
    with conectar(DATABASE_PATH) as conexion:
        filas = conexion.execute("SELECT id, nombre, color FROM materias ORDER BY nombre").fetchall()
    return [_materia(fila) for fila in filas]


@router.post("", status_code=201)
def crear_materia(materia: Materia) -> dict:
    try:
        with conectar(DATABASE_PATH) as conexion:
            cursor = conexion.execute(
                "INSERT INTO materias (nombre, nombre_normalizado, color) VALUES (?, ?, ?)",
                (materia.nombre, normalizar_nombre(materia.nombre), materia.color),
            )
            materia_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Ya existe una materia con ese nombre.")
    return {"id": materia_id, "nombre": materia.nombre, "color": materia.color}


@router.delete("/{materia_id}")
def eliminar_materia(materia_id: int, confirmar: bool = Query(False)) -> dict:
    with conectar(DATABASE_PATH) as conexion:
        materia = conexion.execute("SELECT id, nombre FROM materias WHERE id = ?", (materia_id,)).fetchone()
        if materia is None:
            raise HTTPException(status_code=404, detail="La materia no existe.")
        cantidad = conexion.execute("SELECT COUNT(*) AS total FROM tareas WHERE materia_id = ?", (materia_id,)).fetchone()["total"]
        if not confirmar:
            return {"requiere_confirmacion": True, "materia_id": materia_id, "nombre": materia["nombre"], "tareas_afectadas": cantidad}
        conexion.execute("DELETE FROM materias WHERE id = ?", (materia_id,))
    return {"eliminada": True, "materia_id": materia_id, "tareas_eliminadas": cantidad}
