# Tareas: Organizador de tareas académicas

**Entrada**: Documentos de diseño en `specs/001-organizador-tareas/`

**Prerrequisitos**: `plan.md`, `spec.md`, `research.md`, `data-model.md` y `contracts/api.md`.

**Pruebas**: Incluidas porque `RF-016` exige pruebas automatizadas con pytest.

## Fase 1: Preparación

- [X] T001 Crear la estructura `app/`, `app/routes/`, `app/static/` y `tests/` en la raíz del proyecto.
- [X] T002 Crear `pyproject.toml` con Python 3.12, FastAPI, servidor ASGI y pytest.
- [X] T003 [P] Crear `app/__init__.py` y `app/routes/__init__.py`.
- [X] T004 [P] Crear `tests/conftest.py` con una base SQLite temporal aislada por prueba.
- [X] T005 [P] Crear `README.md` con instalación, ejecución y pruebas en español.

## Fase 2: Fundamentos

- [X] T006 Implementar `app/database.py` con conexión SQLite, tablas `materias` y `tareas`, relación por `materia_id` y borrado en cascada.
- [X] T007 Implementar `app/models.py` con validaciones: nombre de materia 1–60, color máximo 7, título 1–120 y descripción máximo 500 caracteres.
- [X] T008 [P] Crear `tests/test_models.py` para campos obligatorios, límites, espacios externos y duplicidad normalizada.
- [X] T009 Implementar `app/main.py` con FastAPI, registro de rutas y archivos estáticos desde `app/static/`.
- [X] T010 Implementar `app/routes/errores.py` o el manejador común de errores con mensajes comprensibles y sin información sensible.
- [X] T011 [P] Crear `tests/test_database.py` para tablas, persistencia y aislamiento de la base temporal.

**Punto de control**: La aplicación arranca, crea su almacenamiento y ejecuta las pruebas fundamentales.

## Fase 3: Historia de usuario 1 - Registrar materias (Prioridad P1) 🎯 MVP

**Objetivo**: Crear, listar y eliminar materias, validando datos y confirmando el borrado de tareas asociadas.

**Prueba independiente**: Registrar una materia válida, rechazar valores inválidos y confirmar que el borrado avisa y elimina sus tareas.

- [X] T012 [P] [US1] Crear pruebas de contrato para `GET /api/materias` y `POST /api/materias` en `tests/test_materias.py`.
- [X] T013 [P] [US1] Crear pruebas para nombre vacío, nombre duplicado, color vacío y límites en `tests/test_materias.py`.
- [X] T014 [P] [US1] Crear pruebas de eliminación con tareas, aviso de cantidad, cancelación y confirmación en `tests/test_materias.py`.
- [X] T015 [US1] Implementar creación y listado de materias en `app/routes/materias.py` con normalización de espacios y duplicados sin distinguir mayúsculas.
- [X] T016 [US1] Implementar en `app/routes/materias.py` la consulta que informa cuántas tareas serán eliminadas y exige confirmación.
- [X] T017 [US1] Implementar en `app/routes/materias.py` el borrado confirmado de una materia y sus tareas, conservando datos si se cancela.
- [X] T018 [US1] Crear en `app/static/index.html` el formulario y listado de materias con mensajes y confirmación accesible.
- [X] T019 [US1] Implementar en `app/static/app.js` la creación, consulta y eliminación confirmada de materias según `contracts/api.md`.
- [X] T020 [P] [US1] Implementar en `app/static/styles.css` una presentación legible y responsiva para materias y confirmación.

**Punto de control**: US1 es un incremento MVP funcional y comprobable.

## Fase 4: Historia de usuario 2 - Crear y consultar tareas (Prioridad P1)

**Objetivo**: Crear tareas asociadas a materias y mostrar el listado ordenado con estados vencido y urgente.

**Prueba independiente**: Crear tareas con fechas distintas y comprobar orden, validación y clasificación temporal exacta.

- [ ] T021 [P] [US2] Crear pruebas de contrato para `GET /api/tareas` y `POST /api/tareas` en `tests/test_tareas.py`.
- [ ] T022 [P] [US2] Crear pruebas para título, descripción, fecha y materia inexistente en `tests/test_tareas.py`.
- [ ] T023 [P] [US2] Crear pruebas para fecha pasada, momento actual, exactamente 48 horas y tarea completada en `tests/test_tareas.py`.
- [ ] T024 [US2] Implementar creación y listado ordenado en `app/routes/tareas.py`, validando `materia_id`, título 1–120, descripción máximo 500 y fecha válida.
- [ ] T025 [US2] Implementar en `app/routes/tareas.py` la clasificación urgente: pendiente, no vencida y entrega entre ahora y 48 horas inclusivas.
- [ ] T026 [US2] Integrar en `app/static/index.html` el formulario de tarea con materia, título, descripción y fecha.
- [ ] T027 [US2] Implementar en `app/static/app.js` la creación y actualización del listado con orden y distintivos de estado.
- [ ] T028 [P] [US2] Implementar en `app/static/styles.css` estilos accesibles para tareas vencidas, urgentes, pendientes y completadas.

## Fase 5: Historia de usuario 3 - Completar y filtrar tareas (Prioridad P2)

**Objetivo**: Cambiar el estado y filtrar tareas por materia, estado o ambos.

**Prueba independiente**: Marcar tareas y comprobar cada combinación de filtros, incluida la lista sin resultados.

- [ ] T029 [P] [US3] Crear pruebas de contrato para `PATCH /api/tareas/{tarea_id}` y filtros en `tests/test_tareas.py`.
- [ ] T030 [P] [US3] Crear pruebas de filtros combinados por `materia_id` y `completada`, incluida lista vacía, en `tests/test_tareas.py`.
- [ ] T031 [US3] Implementar en `app/routes/tareas.py` el cambio persistente de `completada` y filtros opcionales.
- [ ] T032 [US3] Implementar en `app/static/index.html` controles accesibles de filtro y completitud.
- [ ] T033 [US3] Implementar en `app/static/app.js` filtros combinados, actualización de estado y mensaje sin resultados.
- [ ] T034 [P] [US3] Ajustar `app/static/styles.css` para diferenciar completadas y estados vacíos sin depender solo del color.

## Fase 6: Pulido y validación transversal

- [ ] T035 [P] Añadir en `tests/test_api.py` pruebas de `GET /` y archivos estáticos.
- [ ] T036 [P] Revisar `app/static/index.html` para teclado, etiquetas asociadas, foco visible y mensajes accesibles.
- [ ] T037 [P] Revisar `app/static/styles.css` para uso en celular y computadora.
- [ ] T038 Ejecutar los escenarios de `specs/001-organizador-tareas/quickstart.md` y actualizar `README.md` si procede.
- [ ] T039 [P] Revisar `specs/001-organizador-tareas/checklists/requirements.md` y `specs/001-organizador-tareas/checklists/ux.md`.
- [ ] T040 Ejecutar `pytest` desde la raíz y corregir fallos sin reducir cobertura de requisitos.

## Dependencias y orden

- Fase 1 no tiene dependencias.
- Fase 2 depende de Fase 1 y bloquea las historias.
- US1 y US2 dependen de Fase 2; pueden desarrollarse en paralelo con coordinación.
- US3 depende de las rutas y el listado de US2.
- Fase 6 depende de las historias que se entreguen.

## Oportunidades paralelas

- T003, T004 y T005 pueden ejecutarse en paralelo después de T001–T002.
- T008 y T011 pueden ejecutarse en paralelo después de T006–T007.
- T012–T014, T021–T023 y T029–T030 son grupos de pruebas paralelizables por historia.
- T020, T028 y T034 pueden ejecutarse en paralelo con backend, en archivos distintos.
- T035–T037 y T039 pueden ejecutarse en paralelo durante el pulido.

## Estrategia de implementación

1. Completar Fases 1 y 2.
2. Entregar US1 como MVP y validarla de forma independiente.
3. Añadir US2 y luego US3, validando cada historia antes de continuar.
4. Ejecutar Fase 6 y validar el quickstart completo.

## Notas

- Cada tarea usa el formato obligatorio `- [ ] T### [P?] [US?] descripción con ruta`.
- `[P]` solo identifica tareas paralelizables sin dependencia pendiente.
- Las pruebas deben escribirse antes de la implementación de cada historia.

## Phase 7: Convergence

- [ ] T041 Implementar `app/routes/tareas.py`, `tests/test_tareas.py` y el flujo de interfaz para crear, listar, validar y clasificar tareas según US2/AC1–AC5 y RF-003–RF-008 (missing).
- [ ] T042 Implementar el cambio de completitud, filtros combinados y sus pruebas en `app/routes/tareas.py`, `app/static/` y `tests/test_tareas.py` según US3/AC1–AC4 y RF-009–RF-010 (missing).
- [ ] T043 Añadir `tests/test_api.py` y pruebas de persistencia/reapertura que cubran los contratos HTTP y todas las funcionalidades principales según RF-016, CE-007 y la decisión de pruebas HTTP del plan (partial).
- [ ] T044 Completar la validación transversal de `app/static/` con estados vacíos, mensajes comprensibles, accesibilidad y responsividad verificables según RF-012, RF-015 y la Constitución V (partial).
