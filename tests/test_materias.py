from fastapi.testclient import TestClient

from app.main import app
from app.routes import materias


def cliente(base_temporal, monkeypatch):
    monkeypatch.setattr(materias, "DATABASE_PATH", base_temporal)
    return TestClient(app)


def test_crear_y_listar_materias(base_temporal, monkeypatch):
    response = cliente(base_temporal, monkeypatch).post("/api/materias", json={"nombre": "  Cálculo  ", "color": "#123456"})
    assert response.status_code == 201
    assert response.json()["nombre"] == "Cálculo"
    assert cliente(base_temporal, monkeypatch).get("/api/materias").json() == [response.json()]


def test_rechaza_vacios_duplicados_y_limites(base_temporal, monkeypatch):
    api = cliente(base_temporal, monkeypatch)
    assert api.post("/api/materias", json={"nombre": " ", "color": "#123456"}).status_code == 422
    assert api.post("/api/materias", json={"nombre": "Historia", "color": ""}).status_code == 422
    assert api.post("/api/materias", json={"nombre": "Historia", "color": "#123456"}).status_code == 201
    assert api.post("/api/materias", json={"nombre": " historia ", "color": "#654321"}).status_code == 409
    assert api.post("/api/materias", json={"nombre": "a" * 61, "color": "#123456"}).status_code == 422
    assert api.post("/api/materias", json={"nombre": "Arte", "color": "12345678"}).status_code == 422


def test_eliminacion_informa_confirma_y_aplica_cascada(base_temporal, monkeypatch):
    api = cliente(base_temporal, monkeypatch)
    materia = api.post("/api/materias", json={"nombre": "Física", "color": "#123456"}).json()
    with materias.conectar(base_temporal) as conexion:
        conexion.execute("INSERT INTO tareas (materia_id, titulo, fecha_entrega) VALUES (?, ?, ?)", (materia["id"], "Laboratorio", "2026-11-01T10:00:00"))
        conexion.commit()
    aviso = api.delete(f"/api/materias/{materia['id']}")
    assert aviso.status_code == 200
    assert aviso.json()["tareas_afectadas"] == 1
    assert api.get("/api/materias").json()
    borrado = api.delete(f"/api/materias/{materia['id']}?confirmar=true")
    assert borrado.json()["tareas_eliminadas"] == 1
    assert api.get("/api/materias").json() == []
