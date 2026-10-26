import pytest
from pydantic import ValidationError

from app.models import Materia, Tarea, normalizar_nombre


def test_materia_normaliza_nombre_y_valida_limites():
    materia = Materia(nombre="  Cálculo  ", color="#123456")
    assert materia.nombre == "Cálculo"

    with pytest.raises(ValidationError):
        Materia(nombre=" ", color="#123456")
    with pytest.raises(ValidationError):
        Materia(nombre="a" * 61, color="#123456")
    assert normalizar_nombre("  CÁLCULO ") == normalizar_nombre("cálculo")


def test_tarea_valida_campos_y_normaliza_texto():
    tarea = Tarea(materia_id=1, titulo="  Parcial  ", descripcion="  Repasar  ", fecha_entrega="2026-11-01T10:00:00")
    assert tarea.titulo == "Parcial"
    assert tarea.descripcion == "Repasar"

    with pytest.raises(ValidationError):
        Tarea(materia_id=1, titulo="a" * 121, fecha_entrega="2026-11-01T10:00:00")
    with pytest.raises(ValidationError):
        Tarea(materia_id=1, titulo="ok", descripcion="a" * 501, fecha_entrega="2026-11-01T10:00:00")
