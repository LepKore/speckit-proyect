"""Punto de entrada para las pruebas HTTP de recordatorios."""

import pytest

from fastapi.testclient import TestClient

import app.main as modulo_main
from app.database import conectar
from app.routes import materias, recordatorios, tareas


@pytest.fixture
def cliente_api(base_temporal, monkeypatch):
    """Cliente HTTP reutilizable para las pruebas de contrato."""
    monkeypatch.setattr(modulo_main, "DATABASE_PATH", base_temporal)
    monkeypatch.setattr(materias, "DATABASE_PATH", base_temporal)
    monkeypatch.setattr(recordatorios, "DATABASE_PATH", base_temporal)
    monkeypatch.setattr(tareas, "DATABASE_PATH", base_temporal)
    with TestClient(modulo_main.app) as cliente:
        yield cliente


def test_arranque_inicializa_ciclo_sin_bloquear(cliente_api):
    assert cliente_api.get("/").status_code == 200
    assert not modulo_main.app.state.tarea_recordatorios.done()


def test_recordatorios_persisten_y_se_eliminan_en_cascada(
    cliente_api, base_temporal
):
    del cliente_api
    entrega = "2030-11-02T10:00:00"
    with conectar(base_temporal) as conexion:
        conexion.execute(
            "INSERT INTO materias (nombre, nombre_normalizado, color) VALUES (?, ?, ?)",
            ("Calculo", "calculo", "#123456"),
        )
        materia_id = conexion.execute("SELECT id FROM materias").fetchone()["id"]
        cursor = conexion.execute(
            "INSERT INTO tareas (materia_id, titulo, fecha_entrega) VALUES (?, ?, ?)",
            (materia_id, "Parcial", entrega),
        )
        tarea_id = cursor.lastrowid
        conexion.execute(
            """
            INSERT INTO recordatorios
                (tarea_id, fecha_entrega, fecha_aviso, estado)
            VALUES (?, ?, ?, 'pendiente')
            """,
            (tarea_id, entrega, "2030-11-01T10:00:00"),
        )

    with conectar(base_temporal) as conexion:
        assert conexion.execute(
            "SELECT COUNT(*) AS total FROM recordatorios"
        ).fetchone()["total"] == 1
        conexion.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
        assert conexion.execute(
            "SELECT COUNT(*) AS total FROM recordatorios"
        ).fetchone()["total"] == 0


def test_contrato_estado_procesar_consulta_y_creacion_tarea(cliente_api):
    materia = cliente_api.post(
        "/api/materias", json={"nombre": "Calculo", "color": "#123456"}
    ).json()
    tarea = cliente_api.post(
        "/api/tareas",
        json={
            "materia_id": materia["id"],
            "titulo": "Parcial",
            "fecha_entrega": "2030-11-02T10:00:00",
        },
    )
    assert tarea.status_code == 201
    tarea_id = tarea.json()["id"]

    estado = cliente_api.get("/api/recordatorios/estado")
    assert estado.status_code == 200
    assert estado.json()["pendientes"] == 1
    detalle = cliente_api.get(f"/api/tareas/{tarea_id}/recordatorio")
    assert detalle.status_code == 200
    assert detalle.json()["estado"] == "pendiente"

    procesado = cliente_api.post(
        "/api/recordatorios/procesar",
        json={"ahora": "2030-11-01T10:00:00"},
    )
    assert procesado.status_code == 200
    assert procesado.json()["emitidos"][0]["materia"] == "Calculo"
    assert cliente_api.post(
        "/api/recordatorios/procesar",
        json={"ahora": "2030-11-01T10:00:00"},
    ).json()["emitidos"] == []
