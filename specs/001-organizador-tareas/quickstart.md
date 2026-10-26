# Guía rápida de validación

## Prerrequisitos

- Python 3.12 instalado.
- Dependencias instaladas desde el archivo de dependencias del proyecto.

## Pruebas

Desde la raíz del proyecto:

```text
pytest
```

Se espera que pasen las pruebas de validaciones, persistencia, filtros, eliminación en
cascada y clasificación temporal.

## Ejecución

```text
uvicorn app.main:app --reload
```

Abrir la dirección local mostrada por el servidor.

## Validación manual mínima

1. Registrar una materia y crear dos tareas con fechas diferentes.
2. Verificar orden, estados vencido/urgente, completitud y filtros.
3. Intentar valores vacíos o sobre los límites y comprobar los mensajes.
4. Eliminar una materia con tareas: cancelar y confirmar, verificando ambos resultados.
5. Cerrar y reabrir la aplicación para comprobar la persistencia.

Consultar [data-model.md](data-model.md) para reglas y [contracts/api.md](contracts/api.md)
para rutas.
