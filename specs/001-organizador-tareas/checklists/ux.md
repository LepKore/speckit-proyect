# Experiencia de usuario y validación de datos: Organizador de tareas académicas

**Propósito**: Revisar la completitud, claridad y consistencia de los requisitos de
experiencia de usuario y validación de datos.
**Creada**: 2026-10-26
**Funcionalidad**: [spec.md](../spec.md)

**Nota**: Esta lista personalizada fue generada por `/speckit.checklist` a partir del
contexto de la funcionalidad y sus requisitos.
**Propiedad de la revisión**: Es un artefacto de revisión de calidad de requisitos. El
revisor marca `[x]` únicamente cuando el criterio de calidad está satisfecho.
**Semántica de marcadores**: `[x]` significa que se revisó y aprobó la calidad del
requisito; no significa que la implementación esté terminada.

## Completitud de requisitos de experiencia de usuario

- [ ] CHK001 ¿Están definidos los requisitos de interacción para registrar materias, crear tareas, completar tareas, filtrar y eliminar materias? [Completitud, Spec §Historias de usuario]
- [ ] CHK002 ¿Se especifican estados vacíos y mensajes comprensibles tanto para listas sin datos como para filtros sin resultados? [Completitud, Spec §Casos límite, RF-012]
- [ ] CHK003 ¿Está definido el comportamiento visible antes, durante y después de confirmar o cancelar la eliminación de una materia con tareas? [Cobertura, Spec §RF-013–RF-014]
- [ ] CHK004 ¿Se describen requisitos de accesibilidad para todos los controles y textos de la interfaz, no solo la navegación general? [Cobertura, Spec §RF-015]
- [ ] CHK005 ¿Están definidos los requisitos de presentación para diferenciar de forma comprensible tareas vencidas, urgentes, pendientes y completadas? [Completitud, Spec §RF-006–RF-009]

## Claridad y consistencia de la experiencia

- [ ] CHK006 ¿La expresión “controles y textos comprensibles” está concretada con criterios observables de accesibilidad y contenido? [Claridad, Spec §RF-015]
- [ ] CHK007 ¿La especificación define cómo se comunican al estudiante los límites de 60, 7, 120 y 500 caracteres? [Claridad, Spec §RF-005]
- [ ] CHK008 ¿Es consistente la regla de “urgente” en historias, casos límite, requisitos y criterios de éxito, incluyendo tareas completadas y el límite exacto de 48 horas? [Consistencia, Spec §RF-008, CE-004]
- [ ] CHK009 ¿La especificación distingue sin ambigüedad entre una tarea vencida y una tarea urgente en todos los estados posibles? [Claridad, Spec §RF-007–RF-008]
- [ ] CHK010 ¿El requisito de orden ascendente por fecha define cómo se resuelven dos tareas con la misma fecha de entrega? [Ambigüedad, Spec §RF-006]
- [ ] CHK011 ¿La experiencia de un usuario sin inicio de sesión y con un único usuario por dispositivo está descrita sin implicar funciones de cuenta o sincronización? [Consistencia, Spec §Supuestos]

## Calidad de validación de datos

- [ ] CHK012 ¿Cada campo obligatorio tiene una regla explícita para valores vacíos, espacios externos, formato inválido y valores fuera de límite? [Completitud, Spec §RF-002–RF-005]
- [ ] CHK013 ¿La especificación define si los límites de longitud cuentan caracteres antes o después de quitar espacios externos? [Claridad, Spec §RF-005]
- [ ] CHK014 ¿Está definido el formato válido del color y la relación entre el límite de 7 caracteres y los valores aceptados? [Ambigüedad, Spec §RF-001, RF-005]
- [ ] CHK015 ¿Se especifica un mensaje o criterio de error distinto para nombre duplicado, campo vacío, longitud excedida, fecha inválida y materia inexistente? [Completitud, Spec §RF-002–RF-004, RF-012]
- [ ] CHK016 ¿Está definido qué ocurre con los datos introducidos cuando una validación falla, para evitar pérdida o almacenamiento parcial? [Cobertura, Spec §RF-004, RF-012]
- [ ] CHK017 ¿Las reglas de validación son coherentes entre la especificación, el modelo de datos y el contrato de la interfaz? [Consistencia, Spec §RF-002–RF-005; data-model.md; contracts/api.md]

## Criterios de aceptación y escenarios límite

- [ ] CHK018 ¿Los criterios de éxito permiten evaluar objetivamente la facilidad de registrar materias y tareas sin depender de una tecnología concreta? [Medibilidad, Spec §CE-001–CE-002]
- [ ] CHK019 ¿Están cubiertos los escenarios de fecha exactamente actual, exactamente 48 horas, vencida y completada para evitar ambigüedad temporal? [Cobertura, Spec §Casos límite, RF-008]
- [ ] CHK020 ¿Está definido el comportamiento de la interfaz cuando la materia seleccionada para una tarea deja de existir? [Caso límite, Gap]
- [ ] CHK021 ¿Se especifica cómo se informa la cantidad de tareas que serán eliminadas y qué ocurre si la confirmación se cancela? [Claridad, Spec §RF-013–RF-014]
- [ ] CHK022 ¿Los requisitos describen criterios verificables para que la interfaz conserve legibilidad y uso en celular y computadora? [Medibilidad, Spec §RF-015, CE-005]

## Notas

- Marcar `[x]` solo después de confirmar que el requisito está completo, claro y sin
  ambigüedades.
- Mantener sin marcar los elementos que requieran aclaración o revisión del responsable.
- `/speckit.implement` puede leer el estado de esta lista, pero no debe modificar sus
  marcadores.
- `checklists/requirements.md` mantiene un ciclo independiente administrado por
  `/speckit.specify` y `/speckit.clarify`.
