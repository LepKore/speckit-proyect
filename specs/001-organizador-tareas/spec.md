# Especificación de funcionalidad: Organizador de tareas académicas

**Rama de funcionalidad**: `001-organizador-tareas`

**Creada**: 2026-10-26

**Estado**: Borrador

**Entrada**: Descripción del usuario: "Aplicación para estudiantes de la UPB que permite organizar materias y tareas académicas en un solo dispositivo, sin inicio de sesión."

## Clarificaciones

### Sesión 2026-10-26

- P: ¿Qué debe ocurrir con las tareas asociadas cuando se elimina una materia? → R: Se elimina la materia junto con todas sus tareas asociadas, previa indicación clara de que existen tareas que también serán eliminadas.
- P: ¿Qué límites máximos de longitud deben tener los campos de materias y tareas? → R: Nombre de materia: 60 caracteres; color: 7 caracteres; título de tarea: 120 caracteres; descripción: 500 caracteres.
- P: ¿Cómo debe calcularse que una tarea es “urgente”? → R: Una tarea pendiente, no vencida y con vencimiento entre el momento actual y las próximas 48 horas exactas se marca como urgente.

## Escenarios de usuario y pruebas

### Historia de usuario 1 - Registrar materias (Prioridad: P1)

Como estudiante, quiero registrar mis materias con un nombre y un color para identificar
rápidamente a qué materia pertenece cada tarea.

**Por qué esta prioridad**: Las materias son la base para organizar y filtrar las tareas.

**Prueba independiente**: Se puede registrar una materia y comprobar que aparece con su
nombre y color en la lista de materias.

**Escenarios de aceptación**:

1. **Dado** que no existe una materia con el nombre indicado, **cuando** registro un
   nombre y un color válidos, **entonces** la materia aparece en la lista.
2. **Dado** que intento guardar una materia sin nombre o sin color, **cuando** confirmo
   el formulario, **entonces** el sistema muestra un error y no la registra.

---

### Historia de usuario 2 - Crear y consultar tareas (Prioridad: P1)

Como estudiante, quiero crear tareas asociadas a una materia y consultar un listado
ordenado por fecha de entrega para saber qué debo hacer primero.

**Por qué esta prioridad**: Permite gestionar el trabajo académico diario, que es el
objetivo principal de la aplicación.

**Prueba independiente**: Se pueden crear dos tareas con fechas distintas y comprobar
que se muestran ordenadas de la más próxima a la más lejana.

**Escenarios de aceptación**:

1. **Dado** que existe una materia, **cuando** creo una tarea con título y fecha válidos,
   **entonces** la tarea aparece asociada a esa materia.
2. **Dado** que creo tareas con distintas fechas, **cuando** consulto el listado,
   **entonces** se ordenan de acuerdo con la fecha de entrega ascendente.
3. **Dado** que una tarea tiene fecha anterior al momento actual, **cuando** consulto
   el listado, **entonces** se destaca como vencida.
4. **Dado** que una tarea vence dentro de las próximas 48 horas, **cuando** consulto
   el listado, **entonces** se identifica como urgente.
5. **Dado** que el título está vacío, la fecha es inválida o no se selecciona materia,
   **cuando** intento guardar la tarea, **entonces** el sistema muestra un error y no
   la registra.

---

### Historia de usuario 3 - Completar y filtrar tareas (Prioridad: P2)

Como estudiante, quiero marcar tareas como completadas y filtrarlas por materia o estado
para concentrarme en el trabajo pendiente.

**Por qué esta prioridad**: Ayuda a controlar el avance y reduce la cantidad de tareas
visibles cuando la lista crece.

**Prueba independiente**: Se puede completar una tarea y comprobar que cambia de estado
y que los filtros por materia y estado devuelven solo los resultados correspondientes.

**Escenarios de aceptación**:

1. **Dado** que existe una tarea pendiente, **cuando** la marco como completada,
   **entonces** su estado cambia a completada.
2. **Dado** que existen tareas de varias materias, **cuando** filtro por una materia,
   **entonces** solo aparecen tareas de esa materia.
3. **Dado** que existen tareas pendientes y completadas, **cuando** filtro por estado,
   **entonces** solo aparecen tareas del estado seleccionado.
4. **Dado** que combino un filtro de materia y uno de estado, **cuando** consulto el
   listado, **entonces** se cumplen ambos filtros simultáneamente.

### Casos límite

- No se permite registrar nombres de materia vacíos ni duplicados ignorando mayúsculas,
  minúsculas y espacios externos.
- No se permite registrar tareas sin título, materia o fecha de entrega.
- El nombre de materia no puede superar 60 caracteres; el color no puede superar 7;
  el título de tarea no puede superar 120; y la descripción no puede superar 500.
- Una fecha exactamente 48 horas después del momento actual se considera urgente.
- Una tarea vencida no se considera urgente aunque su vencimiento esté dentro de las
  próximas 48 horas en términos de fecha.
- Una tarea completada no se considera urgente, aunque su fecha de entrega esté dentro
  de las próximas 48 horas.
- Si un filtro no encuentra resultados, se muestra un mensaje claro y no una lista
  ambigua o rota.
- Los datos permanecen disponibles al cerrar y volver a abrir la aplicación en el mismo
  dispositivo.
- Al eliminar una materia con tareas asociadas, se informa cuántas tareas serán eliminadas
  y se solicita confirmación antes de borrar la materia y sus tareas.

## Requisitos

### Requisitos funcionales

- **RF-001**: El sistema DEBE permitir registrar materias con nombre y color.
- **RF-002**: El sistema DEBE validar que el nombre de la materia no esté vacío ni
  duplicado.
- **RF-003**: El sistema DEBE permitir crear tareas con materia, título, descripción
  opcional y fecha de entrega.
- **RF-004**: El sistema DEBE validar todos los datos introducidos antes de guardarlos.
- **RF-005**: El sistema DEBE limitar y validar la longitud máxima del nombre de materia
  a 60 caracteres, del color a 7, del título de tarea a 120 y de la descripción a 500.
- **RF-006**: El sistema DEBE mostrar las tareas ordenadas por fecha de entrega ascendente.
- **RF-007**: El sistema DEBE destacar las tareas vencidas.
- **RF-008**: El sistema DEBE identificar como urgentes únicamente las tareas pendientes,
  no vencidas y cuyo vencimiento esté entre el momento actual y las próximas 48 horas
  exactas, incluyendo el límite de 48 horas.
- **RF-009**: El sistema DEBE permitir marcar una tarea como completada y conservar su
  estado hasta que el estudiante lo cambie.
- **RF-010**: El sistema DEBE permitir filtrar tareas por materia, por estado o por ambos.
- **RF-011**: El sistema DEBE conservar las materias y tareas en el mismo dispositivo
  sin requerir inicio de sesión.
- **RF-012**: El sistema DEBE mostrar mensajes comprensibles para errores de validación y
  estados sin resultados.
- **RF-013**: Al solicitar la eliminación de una materia con tareas asociadas, el sistema
  DEBE indicar claramente que esas tareas también serán eliminadas y solicitar confirmación.
- **RF-014**: Tras la confirmación, el sistema DEBE eliminar la materia y todas sus tareas
  asociadas; si se cancela, DEBE conservarlas sin cambios.
- **RF-015**: La interfaz DEBE funcionar en celular y computadora y ser navegable con
  controles y textos comprensibles.
- **RF-016**: La funcionalidad DEBE contar con pruebas automatizadas para los flujos
  principales, validaciones, clasificación temporal y filtros.

### Entidades principales

- **Materia**: Representa una asignatura del estudiante; contiene nombre y color.
- **Tarea**: Representa una obligación académica; contiene materia, título, descripción
  opcional, fecha de entrega y estado de completitud.

## Criterios de éxito

### Resultados medibles

- **CE-001**: Un estudiante puede registrar una materia válida en menos de 30 segundos.
- **CE-002**: Un estudiante puede crear una tarea válida en menos de 60 segundos.
- **CE-003**: El 100 % de las tareas visibles se presenta en orden ascendente de fecha
  de entrega.
- **CE-004**: El 100 % de las tareas vencidas y urgentes se identifica correctamente
  según las reglas de tiempo definidas.
- **CE-005**: Al menos el 90 % de los usuarios de prueba puede encontrar las tareas
  pendientes de una materia usando los filtros en el primer intento.
- **CE-006**: Las materias y tareas creadas siguen disponibles después de cerrar y
  reabrir la aplicación en el mismo dispositivo.
- **CE-007**: Todas las funcionalidades principales tienen pruebas automatizadas antes
  de la entrega.

## Supuestos

- La primera versión tiene un único usuario por dispositivo y no incluye registro,
  inicio de sesión ni sincronización entre dispositivos.
- El estudiante proporciona fechas de entrega válidas y comprensibles para su dispositivo.
- El estado inicial de toda tarea nueva es pendiente.
- La zona horaria del dispositivo determina el momento actual y el cálculo de 48 horas.
- La eliminación de una materia elimina también todas sus tareas asociadas, únicamente
  después de una confirmación explícita del estudiante.
- La aplicación se usa principalmente para la organización personal del estudiante y no
  sustituye los sistemas oficiales de la UPB.
