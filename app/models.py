"""Modelos y validaciones de dominio."""

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


def normalizar_nombre(valor: str) -> str:
    """Forma usada para comparar nombres sin espacios externos ni mayúsculas."""
    return valor.strip().casefold()


def texto_requerido(valor: str, *, maximo: int, campo: str) -> str:
    valor = valor.strip()
    if not valor:
        raise ValueError(f"{campo} es obligatorio")
    if len(valor) > maximo:
        raise ValueError(f"{campo} no puede superar {maximo} caracteres")
    return valor


class Materia(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int | None = None
    nombre: str = Field(min_length=1, max_length=60)
    color: str = Field(min_length=1, max_length=7)

    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls, valor: str) -> str:
        return texto_requerido(valor, maximo=60, campo="El nombre")

    @field_validator("color")
    @classmethod
    def validar_color(cls, valor: str) -> str:
        valor = valor.strip()
        if not valor:
            raise ValueError("El color es obligatorio")
        if len(valor) > 7:
            raise ValueError("El color no puede superar 7 caracteres")
        return valor


class Tarea(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int | None = None
    materia_id: int
    titulo: str = Field(min_length=1, max_length=120)
    descripcion: str | None = Field(default=None, max_length=500)
    fecha_entrega: str
    completada: bool = False

    @field_validator("titulo")
    @classmethod
    def validar_titulo(cls, valor: str) -> str:
        return texto_requerido(valor, maximo=120, campo="El título")

    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, valor: str | None) -> str | None:
        if valor is None:
            return None
        valor = valor.strip()
        if len(valor) > 500:
            raise ValueError("La descripción no puede superar 500 caracteres")
        return valor or None


class EstadoRecordatorio(StrEnum):
    PENDIENTE = "pendiente"
    EMITIDO = "emitido"
    CANCELADO = "cancelado"


class Recordatorio(BaseModel):
    """Recordatorio persistido para una fecha concreta de entrega."""

    model_config = ConfigDict(from_attributes=True)
    id: int | None = None
    tarea_id: int = Field(gt=0)
    fecha_entrega: datetime
    fecha_aviso: datetime
    estado: EstadoRecordatorio = EstadoRecordatorio.PENDIENTE
    emitido_en: datetime | None = None

    @field_validator("fecha_entrega", "fecha_aviso", "emitido_en")
    @classmethod
    def validar_fecha(cls, valor: datetime | None) -> datetime | None:
        if valor is None:
            return None
        return valor

    @model_validator(mode="after")
    def validar_periodo(self) -> "Recordatorio":
        if self.fecha_aviso >= self.fecha_entrega:
            raise ValueError("La fecha de aviso debe ser anterior a la entrega")
        return self
