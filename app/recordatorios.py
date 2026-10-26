"""Reglas de dominio y persistencia de los recordatorios locales."""

from __future__ import annotations

import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

from app.database import conectar


ANTICIPACION = timedelta(hours=24)


def _convertir_fecha(valor: datetime | str) -> datetime:
    """Convierte una fecha ISO sin perder su zona horaria, si fue informada."""
    if isinstance(valor, datetime):
        return valor
    if not isinstance(valor, str):
        raise ValueError("La fecha debe ser una fecha y hora válida.")
    try:
        return datetime.fromisoformat(valor.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("La fecha debe tener un formato ISO válido.") from exc


def _ahora_comparable(fecha: datetime, ahora: datetime | None) -> datetime:
    if ahora is None:
        return datetime.now().astimezone(fecha.tzinfo) if fecha.tzinfo else datetime.now()
    if (fecha.tzinfo is None) != (ahora.tzinfo is None):
        raise ValueError("Las fechas deben usar la misma zona horaria.")
    return ahora.astimezone(fecha.tzinfo) if fecha.tzinfo else ahora


def calcular_fecha_aviso(fecha_entrega: datetime | str) -> datetime:
    """Calcula el instante exacto de aviso: entrega menos 24 horas."""
    return _convertir_fecha(fecha_entrega) - ANTICIPACION


def programar_recordatorio(
    conexion: sqlite3.Connection,
    tarea_id: int,
    fecha_entrega: datetime | str,
    *,
    ahora: datetime | None = None,
) -> sqlite3.Row | None:
    """Programa un aviso elegible y conserva una sola fila por tarea y entrega."""
    entrega = _convertir_fecha(fecha_entrega)
    momento_actual = _ahora_comparable(entrega, ahora)
    aviso = calcular_fecha_aviso(entrega)

    tarea = conexion.execute(
        "SELECT completada FROM tareas WHERE id = ?", (tarea_id,)
    ).fetchone()
    if tarea is None:
        raise ValueError("La tarea no existe.")
    if tarea["completada"] or entrega - momento_actual < ANTICIPACION:
        return None

    entrega_iso = entrega.isoformat()
    conexion.execute(
        """
        INSERT INTO recordatorios
            (tarea_id, fecha_entrega, fecha_aviso, estado, emitido_en)
        VALUES (?, ?, ?, 'pendiente', NULL)
        ON CONFLICT(tarea_id, fecha_entrega) DO UPDATE SET
            fecha_aviso = excluded.fecha_aviso,
            estado = 'pendiente',
            emitido_en = NULL
        WHERE recordatorios.estado = 'cancelado'
        """,
        (tarea_id, entrega_iso, aviso.isoformat()),
    )
    return conexion.execute(
        "SELECT * FROM recordatorios WHERE tarea_id = ? AND fecha_entrega = ?",
        (tarea_id, entrega_iso),
    ).fetchone()


def cancelar_recordatorio(
    conexion: sqlite3.Connection,
    tarea_id: int,
    fecha_entrega: datetime | str | None = None,
) -> int:
    """Cancela recordatorios pendientes de una tarea sin borrar su historial."""
    parametros: list[object] = [tarea_id]
    condicion_fecha = ""
    if fecha_entrega is not None:
        condicion_fecha = " AND fecha_entrega = ?"
        parametros.append(_convertir_fecha(fecha_entrega).isoformat())
    cursor = conexion.execute(
        "UPDATE recordatorios SET estado = 'cancelado' "
        "WHERE tarea_id = ? AND estado = 'pendiente'" + condicion_fecha,
        parametros,
    )
    return cursor.rowcount


def reprogramar_recordatorio(
    conexion: sqlite3.Connection,
    tarea_id: int,
    fecha_entrega: datetime | str,
    *,
    ahora: datetime | None = None,
) -> sqlite3.Row | None:
    """Invalida avisos anteriores y programa la fecha de entrega vigente."""
    entrega = _convertir_fecha(fecha_entrega)
    conexion.execute(
        """
        UPDATE recordatorios
        SET estado = 'cancelado'
        WHERE tarea_id = ? AND estado = 'pendiente' AND fecha_entrega <> ?
        """,
        (tarea_id, entrega.isoformat()),
    )
    return programar_recordatorio(conexion, tarea_id, entrega, ahora=ahora)


def procesar_recordatorios(
    ruta_base: str | Path, *, ahora: datetime | None = None
) -> list[dict]:
    """Emite de forma idempotente los avisos vencidos que siguen siendo válidos."""
    momento_actual = ahora or datetime.now()
    ahora_iso = momento_actual.isoformat()
    emitidos: list[dict] = []

    with conectar(ruta_base) as conexion:
        filas = conexion.execute(
            """
            SELECT r.id, r.tarea_id, r.fecha_entrega, r.fecha_aviso,
                   t.titulo, t.completada, m.nombre AS materia
            FROM recordatorios AS r
            JOIN tareas AS t ON t.id = r.tarea_id
            JOIN materias AS m ON m.id = t.materia_id
            WHERE r.estado = 'pendiente' AND r.fecha_aviso <= ?
            ORDER BY r.fecha_aviso, r.id
            """,
            (ahora_iso,),
        ).fetchall()

        for fila in filas:
            entrega = _convertir_fecha(fila["fecha_entrega"])
            comparable = _ahora_comparable(entrega, momento_actual)
            if fila["completada"] or entrega <= comparable:
                conexion.execute(
                    "UPDATE recordatorios SET estado = 'cancelado' WHERE id = ?",
                    (fila["id"],),
                )
                continue
            actualizado = conexion.execute(
                """
                UPDATE recordatorios
                SET estado = 'emitido', emitido_en = ?
                WHERE id = ? AND estado = 'pendiente'
                """,
                (ahora_iso, fila["id"]),
            )
            if actualizado.rowcount:
                emitidos.append(
                    {
                        "recordatorio_id": fila["id"],
                        "tarea_id": fila["tarea_id"],
                        "materia": fila["materia"],
                        "titulo": fila["titulo"],
                        "fecha_entrega": fila["fecha_entrega"],
                    }
                )
    return emitidos
