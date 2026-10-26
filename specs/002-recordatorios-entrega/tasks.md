# Tareas: Recordatorios de entrega

**Entrada**: Documentos de diseño en `specs/002-recordatorios-entrega/`

**Prerrequisitos**: `plan.md`, `spec.md`, `research.md`, `data-model.md` y `contracts/`.

**Pruebas**: Incluidas porque RF-012 y la constitución exigen pruebas automatizadas.

## Fase 1: Setup (infraestructura compartida)

**Propósito**: Preparar la estructura y configuración para ampliar la aplicación existente.

- [X] T001 Verificar en `app/` y `tests/` la estructura existente y documentar el punto de integración de recordatorios en `specs/002-recordatorios-entrega/plan.md`.
- [X] T002 [P] Actualizar `pyproject.toml` para conservar FastAPI, SQLite, pytest y las dependencias de pruebas HTTP sin añadir dependencias frontend nuevas.
- [X] T003 [P] Crear `tests/test_recordatorios.py` y `tests/test_api.py` con fixtures SQLite temporales reutilizables para la nueva funcionalidad.

## Fase 2: Foundational (prerrequisitos bloqueantes)

**Propósito**: Añadir persistencia, fechas y utilidades comunes antes de implementar historias.

**Punto de control**: La base puede crear y consultar recordatorios, y las pruebas de fundamentos pasan.

- [X] T004 Implementar en `app/database.py` la tabla `recordatorios` con `tarea_id`, `fecha_entrega`, `fecha_aviso`, `estado` (`pendiente`, `emitido` o `cancelado`) y `emitido_en` opcional, con relación a tareas y cascada al eliminar.
- [X] T005 [P] Implementar en `app/models.py` los modelos de recordatorio y validadores: `tarea_id` obligatorio, fechas válidas y comparables en zona horaria local, y estados limitados a `pendiente`, `emitido` y `cancelado`.
- [ ] T006 [P] Crear en `tests/test_recordatorios.py` pruebas unitarias para calcular `fecha_entrega - 24 horas`, rechazar fechas inválidas y garantizar como máximo un recordatorio pendiente por tarea y fecha.
- [ ] T007 Implementar en `app/recordatorios.py` las funciones de cálculo, programación, cancelación y reprogramación usando la identidad tarea más fecha de entrega; no crear avisos atrasados cuando falten menos de 24 horas.
- [ ] T008 Implementar en `app/main.py` la inicialización de la tabla de recordatorios y la integración del ciclo de procesamiento local sin bloquear el arranque.
- [ ] T009 [P] Crear en `tests/test_api.py` una prueba de arranque, persistencia y cascada de recordatorios al eliminar una tarea.

## Fase 3: Historia de usuario 1 - Recibir recordatorio de tarea pendiente (Prioridad: P1) 🎯 MVP

**Objetivo**: Programar y emitir una única notificación local 24 horas antes de cada tarea pendiente elegible.

**Prueba independiente**: Crear una tarea pendiente con más de 24 horas restantes, procesar exactamente su `fecha_aviso` y comprobar un aviso único con materia, título y fecha de entrega.

### Pruebas de US1

- [ ] T010 [P] [US1] Crear en `tests/test_recordatorios.py` pruebas de programación para tareas pendientes con al menos 24 horas restantes y ausencia de programación con menos de 24 horas.
- [ ] T011 [P] [US1] Crear en `tests/test_recordatorios.py` pruebas de emisión exacta en `fecha_aviso`, contenido de materia/título/fecha y no duplicación al procesar dos veces.
- [ ] T012 [P] [US1] Crear en `tests/test_api.py` pruebas de contrato para `GET /api/recordatorios/estado`, `POST /api/recordatorios/procesar` y `GET /api/tareas/{tarea_id}/recordatorio`.

### Implementación de US1

- [ ] T013 [US1] Implementar en `app/routes/recordatorios.py` los endpoints de estado, procesamiento idempotente y consulta por tarea según `contracts/api.md`.
- [ ] T014 [US1] Implementar en `app/routes/tareas.py` la creación de tareas con programación automática cuando la fecha de entrega esté al menos 24 horas en el futuro.
- [ ] T015 [US1] Integrar en `app/main.py` las rutas de recordatorios y el servicio local de procesamiento periódico mientras la aplicación esté ejecutándose.
- [ ] T016 [US1] Implementar en `app/static/app.js` la solicitud de procesamiento y la notificación del navegador con materia, título, fecha de entrega y enlace de regreso a la tarea.
- [ ] T017 [US1] Actualizar `app/static/index.html` para mostrar el estado del recordatorio junto a cada tarea y un mensaje claro cuando exista una notificación emitida.

**Punto de control**: US1 funciona de forma independiente y emite como máximo un recordatorio identificable por tarea y fecha.

## Fase 4: Historia de usuario 2 - Evitar recordatorios innecesarios (Prioridad: P1)

**Objetivo**: Cancelar o reemplazar recordatorios cuando cambie el estado o la fecha de una tarea.

**Prueba independiente**: Completar una tarea antes del aviso, modificar una fecha y crear una tarea con menos de 24 horas restantes; comprobar cancelación, reprogramación y ausencia de aviso atrasado.

### Pruebas de US2

- [ ] T018 [P] [US2] Crear en `tests/test_recordatorios.py` pruebas de cancelación al completar una tarea, incluyendo completar y reabrir antes del aviso.
- [ ] T019 [P] [US2] Crear en `tests/test_recordatorios.py` pruebas de reprogramación al cambiar la fecha, invalidando el recordatorio anterior y evitando duplicados.
- [ ] T020 [P] [US2] Crear en `tests/test_api.py` pruebas de `PATCH /api/tareas/{tarea_id}` para cambios de estado/fecha y de `DELETE /api/tareas/{tarea_id}/recordatorio`.

### Implementación de US2

- [ ] T021 [US2] Implementar en `app/routes/tareas.py` la creación, modificación y completitud de tareas con cancelación o reprogramación transaccional del recordatorio.
- [ ] T022 [US2] Implementar en `app/routes/recordatorios.py` la cancelación explícita por tarea y la invalidación de recordatorios cuya fecha de entrega cambió.
- [ ] T023 [US2] Implementar en `app/recordatorios.py` la regla de no emitir tareas vencidas, completadas o creadas/modificadas con menos de 24 horas restantes.
- [ ] T024 [US2] Actualizar `app/static/app.js` para reflejar cancelaciones, reprogramaciones y estados sin generar avisos duplicados.
- [ ] T025 [US2] Añadir en `tests/test_recordatorios.py` una prueba de persistencia tras reinicio y reprocesamiento idempotente.

**Punto de control**: ningún cambio de estado o fecha produce recordatorios obsoletos o duplicados.

## Fase 5: Historia de usuario 3 - Uso responsable de notificaciones (Prioridad: P2)

**Objetivo**: Comunicar disponibilidad de notificaciones y mantener operativas las tareas si el permiso no está disponible.

**Prueba independiente**: Rechazar el permiso, crear y consultar una tarea, y comprobar que la tarea se conserva con un mensaje comprensible y sin error bloqueante.

### Pruebas de US3

- [ ] T026 [P] [US3] Crear en `tests/test_api.py` pruebas de `GET /api/recordatorios/estado` para permisos concedidos, rechazados y API no disponible.
- [ ] T027 [P] [US3] Crear en `tests/test_recordatorios.py` pruebas de degradación cuando no hay permiso, conexión o disponibilidad del navegador, sin impedir operaciones de tareas.

### Implementación de US3

- [ ] T028 [US3] Implementar en `app/routes/recordatorios.py` respuestas de disponibilidad sin información sensible y sin bloquear la creación o consulta de tareas.
- [ ] T029 [US3] Implementar en `app/static/app.js` la consulta del permiso, solicitud explícita mediante `Notification.requestPermission()` y mensajes para `granted`, `denied` y `default`.
- [ ] T030 [US3] Actualizar `app/static/index.html` con un control accesible para activar notificaciones y un estado visible de disponibilidad.
- [ ] T031 [US3] Añadir en `app/static/styles.css` estilos responsivos y distinguibles sin depender únicamente del color para estados de recordatorio y permiso.

**Punto de control**: las tareas siguen funcionando aunque las notificaciones sean rechazadas o no estén disponibles.

## Fase 6: Pulido y validación transversal

**Propósito**: Validar la integración completa sin reducir cobertura ni alterar los checklists de requisitos.

- [ ] T032 [P] Completar en `tests/test_api.py` pruebas de `GET /`, archivos estáticos, mensajes de error y compatibilidad con las rutas existentes de tareas.
- [ ] T033 [P] Revisar `app/static/index.html` y `app/static/app.js` para teclado, foco visible, etiquetas, contenido comprensible y enlace de la notificación a la tarea.
- [ ] T034 [P] Revisar `app/static/styles.css` para uso legible en celular y computadora y estados distinguibles sin depender solo del color.
- [ ] T035 Ejecutar los seis escenarios de `specs/002-recordatorios-entrega/quickstart.md` y registrar los resultados en `README.md` si procede.
- [ ] T036 Ejecutar `pytest` desde la raíz y corregir fallos sin reducir la cobertura de RF-001–RF-012.
- [ ] T037 Revisar `specs/002-recordatorios-entrega/checklists/requirements.md` sin modificar marcadores automáticamente y documentar cualquier pendiente.

## Dependencias y orden de ejecución

- Fase 1 no tiene dependencias.
- Fase 2 depende de Fase 1 y bloquea las historias.
- US1 y US2 son P1; US2 depende de las rutas y programación base de US1, aunque sus pruebas de reglas pueden prepararse en paralelo.
- US3 depende de los endpoints y la interfaz de recordatorios de US1.
- Fase 6 depende de las historias implementadas.

### Oportunidades de paralelismo

- T002 y T003 pueden ejecutarse en paralelo.
- T005, T006 y T009 pueden prepararse en paralelo después de T004.
- En US1, T010–T012 pueden ejecutarse en paralelo y antes de T013–T017.
- En US2, T018–T020 pueden ejecutarse en paralelo y antes de T021–T025.
- En US3, T026 y T027 pueden ejecutarse en paralelo.
- T032–T034 pueden ejecutarse en paralelo después de las historias.

## Estrategia de implementación

1. Completar Setup y Foundational.
2. Implementar US1 como MVP: programación, procesamiento idempotente y notificación local.
3. Validar US1 independientemente.
4. Añadir US2 para cancelar y reprogramar sin romper US1.
5. Añadir US3 para permisos y degradación responsable.
6. Ejecutar la validación transversal y los escenarios de quickstart.
