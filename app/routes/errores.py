"""Manejadores de errores HTTP sin detalles internos."""

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def manejar_validacion(request: Request, exc: RequestValidationError) -> JSONResponse:
    del request, exc
    return JSONResponse(status_code=422, content={"detail": "Los datos enviados no son válidos."})
