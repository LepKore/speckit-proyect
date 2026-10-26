"""Punto de entrada FastAPI y entrega de archivos estáticos."""

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.database import inicializar_base
from app.routes.errores import manejar_validacion
from app.routes.materias import router as materias_router


BASE_DIR = Path(__file__).parent
DATABASE_PATH = BASE_DIR.parent / "organizador.db"


@asynccontextmanager
async def ciclo_vida(app: FastAPI):
    inicializar_base(DATABASE_PATH)
    yield


app = FastAPI(title="Organizador de tareas UPB", lifespan=ciclo_vida)
app.add_exception_handler(RequestValidationError, manejar_validacion)
app.include_router(materias_router)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/")
async def inicio() -> FileResponse:
    return FileResponse(BASE_DIR / "static" / "index.html")
