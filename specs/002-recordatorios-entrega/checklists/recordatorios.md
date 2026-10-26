# Calidad de requisitos: Recordatorios de entrega

**Propósito**: Revisar que los requisitos de recordatorios sean completos, claros,
consistentes y listos para implementación por el autor.
**Creada**: 2026-10-26
**Funcionalidad**: [spec.md](../spec.md)

**Nota**: Esta lista personalizada fue generada para validar la calidad de los requisitos,
no el funcionamiento de la implementación.
**Propiedad de la revisión**: El autor es responsable de revisar esta lista y marcar `[x]`
solo cuando el criterio de calidad del requisito esté satisfecho.
**Semántica de marcadores**: `[x]` significa que el requisito fue revisado y es claro,
completo o consistente; no significa que la implementación esté terminada.

## Completitud de requisitos

- [ ] CHK001 ¿Están documentados los requisitos para programar un recordatorio al crear una tarea pendiente con al menos 24 horas restantes? [Completeness, Spec §RF-001]
- [ ] CHK002 ¿Están definidos los requisitos de integración con crear, completar, reabrir, cambiar fecha y eliminar tareas existentes? [Completeness, Spec §RF-005–RF-006; Gap]
- [ ] CHK003 ¿Están descritos el contenido del aviso, su relación con la tarea y el acceso de regreso a la tarea? [Completeness, Spec §RF-003; Spec §API]
- [ ] CHK004 ¿Están especificados el estado del recordatorio, su persistencia y su transición durante reinicios? [Completeness, Spec §RF-010–RF-011; Data model §Ciclo de vida]

## Claridad y consistencia temporal

- [ ] CHK005 ¿La expresión “exactamente 24 horas antes” define con precisión el instante de referencia y la zona horaria local? [Clarity, Spec §RF-002; Research §Cálculo temporal]
- [ ] CHK006 ¿La regla de “al menos 24 horas” es consistente entre programación, creación exacta en el límite y procesamiento del aviso? [Consistency, Spec §RF-001; Spec §Casos límite]
- [ ] CHK007 ¿Está claramente diferenciada la ausencia de aviso atrasado cuando faltan menos de 24 horas de la emisión normal en el instante válido? [Clarity, Spec §RF-007; Spec §Casos límite]
- [ ] CHK008 ¿Está definido cómo se normalizan fechas con y sin zona horaria, cambios de horario y relojes locales inválidos? [Ambiguity, Spec §Supuestos; Data model §Validación; Gap]
- [ ] CHK009 ¿La especificación define qué ocurre si el reloj del dispositivo cambia después de programar un recordatorio? [Edge Case, Spec §Supuestos; Gap]

## Idempotencia y ciclo de vida

- [ ] CHK010 ¿El identificador “tarea más fecha de entrega” está definido sin ambigüedad para fechas equivalentes representadas en distintos formatos? [Clarity, Research §Idempotencia; Data model §Validación]
- [ ] CHK011 ¿Está especificado qué transición ocurre al emitir un recordatorio y qué datos se conservan para impedir duplicados? [Completeness, Spec §RF-004; Data model §Ciclo de vida]
- [ ] CHK012 ¿Son consistentes las reglas para cancelar al completar, reprogramar al cambiar fecha y crear un nuevo aviso al reabrir una tarea? [Consistency, Spec §RF-005–RF-006; Spec §Casos límite]
- [ ] CHK013 ¿Está definido el comportamiento cuando varias tareas tienen el mismo momento de aviso? [Coverage, Spec §Casos límite]
- [ ] CHK014 ¿Están documentados los resultados esperados para una tarea vencida, completada o eliminada antes del aviso? [Coverage, Spec §RF-005–RF-007; Data model §Ciclo de vida]

## Escenarios de error y recuperación

- [ ] CHK015 ¿Están definidos mensajes comprensibles y estados visibles para permisos concedidos, rechazados, no decididos y API de notificaciones no disponible? [Completeness, Spec §RF-008–RF-009; Gap]
- [ ] CHK016 ¿Está especificado qué información conserva la aplicación cuando falla la emisión, se pierde la conexión o el navegador no puede mostrar avisos? [Recovery, Spec §RF-009; Spec §Casos límite; Gap]
- [ ] CHK017 ¿Está definido si una falla al procesar un aviso permite reintento, evita duplicados y conserva la tarea sin bloquear otras tareas? [Recovery, Spec §RF-009–RF-011; Gap]
- [ ] CHK018 ¿Son consistentes los requisitos de cancelación explícita y cancelación automática para no confundir borrar un recordatorio con borrar una tarea? [Consistency, Spec §API; Spec §RF-005]

## Criterios de aceptación y alcance

- [ ] CHK019 ¿Los criterios SC-001–SC-005 permiten evaluar objetivamente programación, emisión única, cancelación, reprogramación y permisos rechazados? [Measurability, Spec §SC-001–SC-005]
- [ ] CHK020 ¿El criterio SC-006 define cómo se medirá que el usuario entiende el estado y encuentra la tarea desde el aviso? [Clarity, Spec §SC-006]
- [ ] CHK021 ¿La especificación distingue qué comportamiento es obligatorio del navegador y qué comportamiento debe mantenerse cuando las notificaciones locales no están disponibles? [Clarity, Spec §Supuestos; Spec §RF-008–RF-009]
- [ ] CHK022 ¿Las restricciones de no usar cuentas, servicios remotos, sincronización y preferencias avanzadas están alineadas con todos los requisitos? [Consistency, Spec §Supuestos; Plan §Contexto técnico]

## Notas

- Marcar `[x]` solo después de confirmar que el requisito está completo, claro y sin ambigüedades.
- Mantener sin marcar los elementos que requieran aclaración o revisión del autor.
- Esta lista evalúa la redacción de requisitos, no el código ni la ejecución de pruebas.
- `/speckit.implement` puede leer el estado de esta lista, pero no debe modificar sus marcadores.
- `checklists/requirements.md` mantiene un ciclo independiente administrado por
  `/speckit.specify` y `/speckit.clarify`.
