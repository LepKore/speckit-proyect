"""Punto de entrada FastAPI y entrega de archivos estáticos."""

import asyncio
from contextlib import asynccontextmanager, suppress
from pathlib import Path

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.database import inicializar_base
from app.recordatorios import procesar_recordatorios
from app.routes.errores import manejar_validacion
from app.routes.materias import router as materias_router
from app.routes.recordatorios import router as recordatorios_router
from app.routes.tareas import router as tareas_router


BASE_DIR = Path(__file__).parent
DATABASE_PATH = BASE_DIR.parent / "organizador.db"
INTERVALO_RECORDATORIOS_SEGUNDOS = 60


async def procesar_recordatorios_periodicamente() -> None:
    """Procesa recordatorios en segundo plano sin bloquear peticiones HTTP."""
    while True:
        await asyncio.to_thread(procesar_recordatorios, DATABASE_PATH)
        await asyncio.sleep(INTERVALO_RECORDATORIOS_SEGUNDOS)


@asynccontextmanager
async def ciclo_vida(app: FastAPI):
    inicializar_base(DATABASE_PATH)
    tarea_recordatorios = asyncio.create_task(procesar_recordatorios_periodicamente())
    app.state.tarea_recordatorios = tarea_recordatorios
    try:
        yield
    finally:
        tarea_recordatorios.cancel()
        with suppress(asyncio.CancelledError):
            await tarea_recordatorios


app = FastAPI(title="Organizador de tareas UPB", lifespan=ciclo_vida)
app.add_exception_handler(RequestValidationError, manejar_validacion)
app.include_router(materias_router)
app.include_router(recordatorios_router)
app.include_router(tareas_router)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/")
async def inicio() -> FileResponse:
    return FileResponse(BASE_DIR / "static" / "index.html")
