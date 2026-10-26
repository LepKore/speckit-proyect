"""Pruebas y fixtures base para la funcionalidad de recordatorios."""

import pytest

from app.database import conectar


@pytest.fixture
def conexion_recordatorios(conexion):
    """Expone la conexión SQLite aislada para las pruebas de recordatorios."""
    return conexion


def test_tabla_recordatorios_disponible(conexion_recordatorios):
    tabla = conexion_recordatorios.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'recordatorios'"
    ).fetchone()
    assert tabla[0] == "recordatorios"
