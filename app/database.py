"""Persistencia SQLite mínima para materias y tareas."""

import sqlite3
from pathlib import Path


SCHEMA = """
CREATE TABLE IF NOT EXISTS materias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    nombre_normalizado TEXT NOT NULL UNIQUE,
    color TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    materia_id INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    fecha_entrega TEXT NOT NULL,
    completada INTEGER NOT NULL DEFAULT 0 CHECK (completada IN (0, 1)),
    FOREIGN KEY (materia_id) REFERENCES materias (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS recordatorios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarea_id INTEGER NOT NULL,
    fecha_entrega TEXT NOT NULL,
    fecha_aviso TEXT NOT NULL,
    estado TEXT NOT NULL CHECK (estado IN ('pendiente', 'emitido', 'cancelado')),
    emitido_en TEXT,
    UNIQUE (tarea_id, fecha_entrega),
    FOREIGN KEY (tarea_id) REFERENCES tareas (id) ON DELETE CASCADE
);
"""


def conectar(ruta: str | Path) -> sqlite3.Connection:
    """Abre una conexión con claves como atributos y cascada habilitada."""
    conexion = sqlite3.connect(ruta)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def inicializar_base(ruta: str | Path) -> None:
    """Crea las tablas necesarias si todavía no existen."""
    with conectar(ruta) as conexion:
        conexion.executescript(SCHEMA)
