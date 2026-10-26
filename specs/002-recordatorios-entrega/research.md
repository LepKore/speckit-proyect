# Investigación técnica: Recordatorios de entrega

## Decisión: recordatorios locales sin servicio remoto

Se procesarán desde el servidor local existente y se mostrarán mediante las capacidades
estándar de notificación del navegador. El alcance no incluye cuentas, sincronización ni
proveedores externos.

## Decisión: cálculo temporal

El momento del aviso será exactamente `fecha_entrega - 24 horas`, usando la zona horaria local
normalizada por la aplicación. Esto permite probar el límite exacto y evitar avisos atrasados.

## Decisión: idempotencia y estados

Cada recordatorio se identifica por tarea y fecha de entrega. Sus estados serán `pendiente`,
`emitido` y `cancelado`, para evitar duplicados después de reinicios.

## Decisión: permisos y degradación

El permiso de notificaciones será opcional para crear, consultar, completar o modificar tareas.
La interfaz comunicará su disponibilidad sin bloquear el flujo principal.
