# Contrato de la interfaz web

Las respuestas de error deben ser comprensibles y no deben incluir información sensible.

## Materias

- `GET /api/materias`: devuelve las materias registradas.
- `POST /api/materias`: recibe `nombre` y `color`; valida campos, límites y duplicados.
- `DELETE /api/materias/{materia_id}`: informa la cantidad de tareas asociadas y exige
  confirmación antes de eliminar la materia y sus tareas.

## Tareas

- `GET /api/tareas`: devuelve tareas ordenadas por entrega y acepta filtros opcionales por
  `materia_id` y `completada`; incluye indicadores vencido y urgente.
- `POST /api/tareas`: recibe materia, título, descripción opcional y fecha; valida la
  existencia de la materia y los límites.
- `PATCH /api/tareas/{tarea_id}`: permite cambiar el estado de completitud.

## Interfaz estática

- `GET /`: entrega la interfaz HTML, usable en celulares y computadoras, con estados de
  validación, confirmación y ausencia de resultados.
