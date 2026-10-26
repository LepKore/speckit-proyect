"""Punto de entrada para las pruebas HTTP de recordatorios."""

import pytest

from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def cliente_api():
    """Cliente HTTP reutilizable para las pruebas de contrato."""
    return TestClient(app)
