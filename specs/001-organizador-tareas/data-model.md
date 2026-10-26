# Modelo de datos

## Materia

Representa una asignatura del estudiante.

| Campo | Reglas |
|---|---|
| id | Identificador único generado por el sistema. |
| nombre | Obligatorio, de 1 a 60 caracteres tras quitar espacios externos; sin duplicados ignorando mayúsculas, minúsculas y espacios externos. |
| color | Obligatorio, máximo 7 caracteres. |

## Tarea

Representa una obligación académica asociada a una materia.

| Campo | Reglas |
|---|---|
| id | Identificador único generado por el sistema. |
| materia_id | Obligatorio; referencia a una materia existente. |
| titulo | Obligatorio, de 1 a 120 caracteres tras quitar espacios externos. |
| descripcion | Opcional, máximo 500 caracteres. |
| fecha_entrega | Obligatoria y válida; usa la zona horaria del dispositivo. |
| completada | Obligatoria; inicia como falso. |

## Relaciones y ciclo de vida

- Una materia puede tener cero o muchas tareas; cada tarea pertenece a una materia.
- Eliminar una materia elimina sus tareas después de confirmación.
- Una tarea pendiente puede pasar a completada.
- Una tarea es vencida si su fecha es anterior al momento actual.
- Una tarea es urgente si está pendiente, no vencida y vence entre ahora y ahora más 48
  horas, con intervalo inclusivo.
