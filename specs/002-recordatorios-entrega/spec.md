# Especificación de funcionalidad: Recordatorios de entrega

**Rama de funcionalidad**: `002-recordatorios-entrega`

**Creada**: 2026-10-26

**Estado**: Borrador

**Entrada**: Descripción del usuario: "Agregar recordatorios: el estudiante recibe una notificación un día antes de la fecha de entrega de cada tarea pendiente."

## Escenarios de usuario y pruebas

### Historia de usuario 1 - Recibir recordatorio de tarea pendiente (Prioridad: P1)

Como estudiante, quiero recibir una notificación un día antes de la fecha de entrega de
cada tarea pendiente para recordar oportunamente mis obligaciones académicas.

**Por qué esta prioridad**: Reduce el riesgo de olvidar entregas sin exigir que el estudiante
revise continuamente la aplicación.

**Prueba independiente**: Crear una tarea pendiente con una fecha futura, avanzar el reloj
hasta exactamente un día antes y comprobar que se muestra una única notificación con la
materia, el título y la fecha de entrega.

**Escenarios de aceptación**:

1. **Dado** que existe una tarea pendiente con fecha de entrega futura, **cuando** llega el
   momento exacto de 24 horas antes, **entonces** el estudiante recibe una notificación
   identificable con la información de la tarea.
2. **Dado** que una tarea pendiente tiene recordatorio programado, **cuando** el estudiante
   abre la notificación, **entonces** puede volver a la aplicación y consultar la tarea.
3. **Dado** que el estudiante ya recibió el recordatorio, **cuando** vuelve a consultar la
   tarea, **entonces** no recibe otra notificación por la misma entrega.

---

### Historia de usuario 2 - Evitar recordatorios innecesarios (Prioridad: P1)

Como estudiante, quiero que los recordatorios se ajusten al estado y a la fecha de mis
tareas para no recibir avisos que ya no son relevantes.

**Por qué esta prioridad**: Un aviso incorrecto o repetido reduce la confianza en todos los
recordatorios.

**Prueba independiente**: Completar una tarea antes del momento del recordatorio y comprobar
que no se notifica; crear una tarea con menos de 24 horas restantes y comprobar que no genera
un recordatorio atrasado.

**Escenarios de aceptación**:

1. **Dado** que una tarea tiene recordatorio pendiente, **cuando** se marca como completada
   antes del momento del aviso, **entonces** el recordatorio se cancela.
2. **Dado** que una tarea se crea o modifica cuando faltan menos de 24 horas para su entrega,
   **cuando** se guarda, **entonces** no se envía un recordatorio atrasado.
3. **Dado** que una tarea ya está vencida o completada, **cuando** llega cualquier momento
   posterior, **entonces** no se envía recordatorio.

---

### Historia de usuario 3 - Permitir el uso responsable de notificaciones (Prioridad: P2)

Como estudiante, quiero saber si las notificaciones están disponibles y poder continuar
usando mis tareas si las rechazo o el dispositivo no las permite.

**Por qué esta prioridad**: El recordatorio es una ayuda y no debe impedir la organización
normal de las tareas.

**Prueba independiente**: Rechazar el permiso de notificaciones y comprobar que la tarea se
guarda, que el estado se comunica claramente y que la aplicación sigue funcionando.

**Escenarios de aceptación**:

1. **Dado** que no se ha concedido permiso para notificaciones, **cuando** el estudiante
   crea una tarea, **entonces** la aplicación informa que el recordatorio no podrá mostrarse
   y conserva la tarea.
2. **Dado** que las notificaciones no están disponibles, **cuando** el estudiante consulta
   la tarea, **entonces** puede ver su fecha y estado sin errores bloqueantes.

### Casos límite

- Una tarea creada exactamente 24 horas antes de la entrega conserva un recordatorio para el
  momento de creación, sin enviarlo inmediatamente por estar atrasado.
- Una tarea creada con menos de 24 horas restantes no recibe un recordatorio atrasado.
- Cambiar la fecha de entrega reemplaza el recordatorio anterior por uno basado en la nueva
  fecha, siempre que la tarea siga pendiente y falten al menos 24 horas.
- Completar y volver a abrir una tarea antes del momento del aviso no debe enviar el aviso
  mientras permanezca completada.
- Reabrir una tarea pendiente con al menos 24 horas restantes debe permitir un nuevo
  recordatorio para la entrega actual, sin duplicar avisos para la misma fecha.
- Si el dispositivo está sin conexión o no permite notificaciones, la aplicación conserva la
  tarea y muestra el estado de disponibilidad de los recordatorios.
- El estudiante puede tener varias tareas con el mismo momento de recordatorio y debe poder
  distinguirlas por materia y título.

## Requisitos

### Requisitos funcionales

- **RF-001**: El sistema DEBE programar un recordatorio para cada tarea pendiente cuya fecha
  de entrega esté al menos 24 horas en el futuro.
- **RF-002**: El sistema DEBE emitir el recordatorio exactamente 24 horas antes de la fecha
  de entrega, según la hora local del dispositivo.
- **RF-003**: La notificación DEBE identificar la materia, el título y la fecha de entrega de
  la tarea.
- **RF-004**: El sistema DEBE emitir como máximo un recordatorio por cada tarea y fecha de
  entrega.
- **RF-005**: El sistema DEBE cancelar o invalidar el recordatorio cuando la tarea se marque
  como completada antes de su emisión.
- **RF-006**: El sistema DEBE recalcular el recordatorio cuando cambie la fecha de entrega,
  el estado o la tarea vuelva a estar pendiente.
- **RF-007**: El sistema NO DEBE emitir recordatorios atrasados para tareas creadas o
  modificadas cuando falten menos de 24 horas para la entrega.
- **RF-008**: El sistema DEBE solicitar o reconocer el permiso requerido para mostrar
  notificaciones y comunicar claramente si no está disponible.
- **RF-009**: La falta de permiso, conexión o disponibilidad de notificaciones NO DEBE
  impedir crear, consultar, completar o modificar tareas.
- **RF-010**: El sistema DEBE conservar la configuración y el estado de los recordatorios al
  cerrar y volver a abrir la aplicación en el mismo dispositivo.
- **RF-011**: El sistema DEBE evitar duplicados cuando se reprocese una tarea o se reinicie
  la aplicación.
- **RF-012**: La funcionalidad DEBE contar con pruebas automatizadas para programación,
  cancelación, reprogramación, duplicados y casos de disponibilidad.

### Entidades principales

- **Tarea**: Obligación académica existente, con fecha de entrega y estado de completitud.
- **Recordatorio**: Aviso asociado a una tarea y a una fecha de entrega concreta; registra el
  momento previsto, el estado de programación y si ya fue emitido.
- **Permiso de notificaciones**: Estado visible de disponibilidad de avisos en el dispositivo.

## Criterios de éxito

### Resultados medibles

- **SC-001**: El 100 % de las tareas pendientes con al menos 24 horas restantes recibe un
  único aviso en el momento definido de 24 horas antes durante las pruebas.
- **SC-002**: El 100 % de las tareas completadas antes del aviso no genera una notificación.
- **SC-003**: El 100 % de los cambios de fecha probados reemplaza el aviso anterior sin
  duplicarlo.
- **SC-004**: El estudiante puede identificar materia, título y fecha de entrega desde cada
  notificación sin abrir otra pantalla.
- **SC-005**: En el 100 % de las pruebas con permisos rechazados, la aplicación conserva las
  operaciones de tareas y muestra un mensaje comprensible.
- **SC-006**: Al menos el 90 % de los usuarios de prueba entiende el estado de los
  recordatorios y puede consultar la tarea desde el aviso en el primer intento.

## Supuestos

- La aplicación usa notificaciones locales del dispositivo o navegador y solicita el permiso
  correspondiente; no requiere cuentas ni un servicio remoto.
- La zona horaria y el reloj del dispositivo determinan el momento de 24 horas antes.
- La aplicación no envía recordatorios atrasados cuando la tarea se crea o modifica dentro
  de las 24 horas previas a la entrega.
- El estudiante puede seguir usando todas las funciones de tareas aunque rechace permisos.
- Los recordatorios pertenecen al mismo dispositivo que conserva las tareas.
- Las preferencias avanzadas de repetición, posponer, canales de sonido y sincronización entre
  dispositivos están fuera del alcance de esta versión.
