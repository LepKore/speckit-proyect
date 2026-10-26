# Investigación técnica

## Decisión: aplicación web en un solo proyecto FastAPI

**Decisión**: Usar Python 3.12 con FastAPI para servir la API y los archivos estáticos
HTML, CSS y JavaScript desde el mismo proyecto.

**Justificación**: Cumple el alcance académico, evita microservicios y mantiene una sola
forma de ejecutar y probar la aplicación.

**Alternativas consideradas**: Separar frontend y backend, usar un framework frontend o
crear varios servicios. Se descartan por añadir complejidad sin valor para esta versión.

## Decisión: SQLite como almacenamiento local

**Decisión**: Persistir materias y tareas en SQLite con relación entre ambas entidades.

**Justificación**: Es suficiente para un usuario por dispositivo y no requiere un servidor
de base de datos.

**Alternativas consideradas**: Archivos JSON y una base de datos servidor. JSON ofrece
menos garantías para relaciones y la base de datos servidor excede el alcance.

## Decisión: pruebas automatizadas con pytest

**Decisión**: Cubrir validaciones, reglas de fechas, persistencia y endpoints mediante
pytest.

**Justificación**: La constitución exige pruebas automatizadas y pytest permite validar
lógica y flujos HTTP de forma repetible.

## Decisión: cálculo de urgencia basado en el momento actual

Una tarea es urgente solo si está pendiente, no vencida y su entrega está entre el momento
actual y 48 horas después, incluyendo exactamente el límite superior.

## Decisión: eliminación explícita en cascada

Antes de eliminar una materia con tareas se informa cuántas tareas serán eliminadas y se
solicita confirmación. Confirmada la acción, se eliminan la materia y sus tareas.
