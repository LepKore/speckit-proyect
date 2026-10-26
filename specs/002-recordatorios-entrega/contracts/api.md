# Contrato de la interfaz de recordatorios

Las respuestas de error deben ser comprensibles y no incluir información sensible.

## Estado y procesamiento

- `GET /api/recordatorios/estado`: devuelve disponibilidad de notificaciones y cantidad de
  recordatorios pendientes.
- `POST /api/recordatorios/procesar`: procesa avisos cuyo momento llegó y devuelve los avisos
  emitidos. Debe ser idempotente.

## Recordatorio de una tarea

- `GET /api/tareas/{tarea_id}/recordatorio`: devuelve el recordatorio de la fecha actual.
- `DELETE /api/tareas/{tarea_id}/recordatorio`: cancela el recordatorio sin eliminar la tarea.

## Integración

- `POST /api/tareas`: programa un recordatorio si la tarea pendiente tiene al menos 24 horas.
- `PATCH /api/tareas/{tarea_id}`: cancela o reprograma según el nuevo estado o fecha.

## Interfaz

- Muestra disponibilidad de notificaciones y solicita permiso sin bloquear tareas.
- El aviso identifica materia, título y fecha, y permite volver a la tarea.
