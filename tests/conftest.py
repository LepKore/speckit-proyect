"""Fixtures de pruebas con bases SQLite aisladas."""

import pytest

from app.database import conectar, inicializar_base


@pytest.fixture
def base_temporal(tmp_path):
    ruta = tmp_path / "prueba.sqlite3"
    inicializar_base(ruta)
    return ruta


@pytest.fixture
def conexion(base_temporal):
    with conectar(base_temporal) as conexion:
        yield conexion
