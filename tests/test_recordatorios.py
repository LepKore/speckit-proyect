"""Pruebas unitarias para la funcionalidad de recordatorios."""

from datetime import datetime, timedelta

import pytest

from app.recordatorios import (
    calcular_fecha_aviso,
    procesar_recordatorios,
    programar_recordatorio,
)


@pytest.fixture
def conexion_recordatorios(conexion):
    """Expone la conexión SQLite aislada para las pruebas de recordatorios."""
    return conexion


def test_tabla_recordatorios_disponible(conexion_recordatorios):
    tabla = conexion_recordatorios.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'recordatorios'"
    ).fetchone()
    assert tabla[0] == "recordatorios"


def crear_tarea(conexion, fecha_entrega: datetime) -> int:
    conexion.execute(
        "INSERT INTO materias (nombre, nombre_normalizado, color) VALUES (?, ?, ?)",
        ("Calculo", "calculo", "#123456"),
    )
    materia_id = conexion.execute("SELECT id FROM materias").fetchone()["id"]
    cursor = conexion.execute(
        "INSERT INTO tareas (materia_id, titulo, fecha_entrega) VALUES (?, ?, ?)",
        (materia_id, "Parcial", fecha_entrega.isoformat()),
    )
    return cursor.lastrowid


def test_calcula_fecha_aviso_exactamente_24_horas_antes():
    entrega = datetime(2026, 11, 2, 10, 30)
    assert calcular_fecha_aviso(entrega) == datetime(2026, 11, 1, 10, 30)


@pytest.mark.parametrize("fecha", ["fecha-invalida", "2026-99-10T10:00:00", None])
def test_rechaza_fechas_invalidas(fecha):
    with pytest.raises(ValueError, match="fecha"):
        calcular_fecha_aviso(fecha)


def test_programacion_es_unica_por_tarea_y_fecha(conexion_recordatorios):
    ahora = datetime(2026, 10, 26, 9)
    entrega = ahora + timedelta(days=2)
    tarea_id = crear_tarea(conexion_recordatorios, entrega)

    primero = programar_recordatorio(
        conexion_recordatorios, tarea_id, entrega, ahora=ahora
    )
    segundo = programar_recordatorio(
        conexion_recordatorios, tarea_id, entrega, ahora=ahora
    )

    assert primero["id"] == segundo["id"]
    total = conexion_recordatorios.execute(
        "SELECT COUNT(*) AS total FROM recordatorios WHERE estado = 'pendiente'"
    ).fetchone()["total"]
    assert total == 1


def test_programa_con_al_menos_24_horas_y_omite_avisos_atrasados(
    conexion_recordatorios,
):
    ahora = datetime(2026, 10, 26, 9)
    tarea_exacta = crear_tarea(conexion_recordatorios, ahora + timedelta(hours=24))
    programado = programar_recordatorio(
        conexion_recordatorios,
        tarea_exacta,
        ahora + timedelta(hours=24),
        ahora=ahora,
    )
    assert programado is not None
    assert programado["fecha_aviso"] == ahora.isoformat()

    conexion_recordatorios.execute(
        "INSERT INTO materias (nombre, nombre_normalizado, color) VALUES (?, ?, ?)",
        ("Fisica", "fisica", "#654321"),
    )
    materia_id = conexion_recordatorios.execute(
        "SELECT id FROM materias WHERE nombre_normalizado = 'fisica'"
    ).fetchone()["id"]
    entrega_cercana = ahora + timedelta(hours=23, minutes=59)
    cursor = conexion_recordatorios.execute(
        "INSERT INTO tareas (materia_id, titulo, fecha_entrega) VALUES (?, ?, ?)",
        (materia_id, "Laboratorio", entrega_cercana.isoformat()),
    )
    assert (
        programar_recordatorio(
            conexion_recordatorios,
            cursor.lastrowid,
            entrega_cercana,
            ahora=ahora,
        )
        is None
    )


def test_emite_en_fecha_aviso_con_detalle_y_sin_duplicados(conexion_recordatorios):
    ahora = datetime(2026, 10, 26, 9)
    entrega = ahora + timedelta(days=2)
    tarea_id = crear_tarea(conexion_recordatorios, entrega)
    programar_recordatorio(conexion_recordatorios, tarea_id, entrega, ahora=ahora)
    conexion_recordatorios.commit()
    ruta = conexion_recordatorios.execute("PRAGMA database_list").fetchone()[2]

    assert procesar_recordatorios(ruta, ahora=ahora + timedelta(hours=23, minutes=59)) == []
    avisos = procesar_recordatorios(ruta, ahora=ahora + timedelta(days=1))
    assert avisos == [{
        "recordatorio_id": 1,
        "tarea_id": tarea_id,
        "materia": "Calculo",
        "titulo": "Parcial",
        "fecha_entrega": entrega.isoformat(),
    }]
    assert procesar_recordatorios(ruta, ahora=ahora + timedelta(days=1)) == []
