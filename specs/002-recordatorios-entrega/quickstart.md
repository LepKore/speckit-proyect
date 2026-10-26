# Guía rápida de validación: Recordatorios de entrega

## Prerrequisitos

- Python 3.12 y dependencias instaladas.
- Permiso de notificaciones disponible para las pruebas de interfaz.

## Pruebas

```text
pytest
```

Se espera cobertura de cálculo de 24 horas, límite exacto, cancelación, reprogramación,
duplicados, persistencia y permisos rechazados.

## Ejecución

```text
uvicorn app.main:app --reload
```

## Escenarios manuales

1. Crear una tarea con más de 24 horas hasta la entrega y verificar el recordatorio pendiente.
2. Procesar el momento exacto de 24 horas antes y verificar un único aviso identificable.
3. Completar antes del aviso y verificar cancelación.
4. Cambiar la fecha y verificar que no se duplica el aviso.
5. Crear con menos de 24 horas y verificar que no hay aviso atrasado.
6. Rechazar permiso y verificar que las tareas siguen funcionando.

Consultar [data-model.md](data-model.md) y [contracts/api.md](contracts/api.md).
