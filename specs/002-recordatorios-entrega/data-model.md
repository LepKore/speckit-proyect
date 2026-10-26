# Modelo de datos: Recordatorios de entrega

## Recordatorio

| Campo | Reglas |
|---|---|
| id | Identificador único generado por el sistema. |
| tarea_id | Obligatorio; referencia a una tarea existente. |
| fecha_entrega | Fecha normalizada que originó el aviso. |
| fecha_aviso | Exactamente 24 horas antes de la entrega. |
| estado | `pendiente`, `emitido` o `cancelado`. |
| emitido_en | Opcional; momento en que se emitió el aviso. |

## Ciclo de vida

- Una tarea pendiente con al menos 24 horas restantes crea un recordatorio.
- Completar la tarea cancela el recordatorio pendiente.
- Cambiar la fecha cancela el anterior y crea uno nuevo si corresponde.
- Emitir cambia el estado a `emitido` y no vuelve a procesarlo.
- Eliminar una tarea elimina sus recordatorios.

## Validación

- `tarea_id` debe existir.
- Las fechas deben ser válidas y comparables en la zona horaria local.
- No puede haber más de un recordatorio pendiente para una tarea y fecha.
