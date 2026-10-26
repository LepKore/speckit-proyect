# speckit-proyect

## Organizador de tareas académicas UPB

Aplicación local para organizar materias y tareas académicas.

## Instalación

Con Python 3.12:

```text
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[test]"
```

## Ejecución

```text
uvicorn app.main:app --reload
```

## Pruebas

```text
pytest
```
