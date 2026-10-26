# Plan de implementación: Recordatorios de entrega

**Rama**: `002-recordatorios-entrega` | **Fecha**: 2026-10-26 | **Especificación**: [spec.md](spec.md)

**Entrada**: Especificación en `specs/002-recordatorios-entrega/spec.md`.

## Resumen

Añadir recordatorios locales para tareas pendientes, calculados 24 horas antes de la entrega.
Se reutilizarán FastAPI, SQLite y la interfaz HTML/CSS/JS existentes. El estado será
persistentemente idempotente y se recalculará al crear, modificar o completar una tarea.

## Contexto técnico

**Lenguaje/Versión**: Python 3.12 y JavaScript del navegador

**Dependencias principales**: FastAPI, SQLite, pytest y APIs estándar de notificaciones del navegador

**Almacenamiento**: SQLite para recordatorios y estado de emisión; estado del permiso en el navegador

**Pruebas**: pytest para reglas, persistencia y contratos HTTP; pruebas de interfaz para permisos

**Plataforma objetivo**: Aplicación web local en navegador de celular o computadora

**Tipo de proyecto**: Aplicación web monolítica de un usuario por dispositivo

**Objetivos de rendimiento**: Procesar recordatorios sin bloquear las operaciones de tareas

**Restricciones**: Sin cuentas, servicios remotos, sincronización ni dependencias frontend nuevas; documentos en español

**Escala/Alcance**: Un dispositivo, un usuario y un aviso por tarea y fecha de entrega

## Decisiones de investigación

- El aviso se calcula como `fecha_entrega - 24 horas`, usando la zona horaria local.
- El servidor local procesará recordatorios pendientes periódicamente mientras esté ejecutándose.
- La interfaz solicitará permiso del navegador y seguirá funcionando si se rechaza.
- La identidad de un recordatorio será tarea más fecha de entrega; cambiar la fecha invalida el anterior.
- Los estados `pendiente`, `emitido` y `cancelado` evitan duplicados después de reinicios.

## Constitution Check

*Puerta: debe aprobarse antes de investigar y después del diseño.*

- **Simplicidad**: APROBADO. Se reutiliza la aplicación existente y no se añade servicio remoto.
- **Pruebas obligatorias**: APROBADO. Se cubrirán cálculo, estados, persistencia, duplicados y permisos.
- **Código legible**: APROBADO. Cálculo, almacenamiento y presentación tendrán responsabilidades separadas.
- **Validación de entradas**: APROBADO. Se validarán fechas, estados y referencias a tareas.
- **Accesibilidad y responsividad**: APROBADO. El estado del permiso tendrá mensajes comprensibles.
- **Contenido académico**: APROBADO. Documentación y mensajes estarán en español.

## Estructura del proyecto

### Documentación

```text
specs/002-recordatorios-entrega/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/api.md
└── tasks.md
```

### Código fuente

```text
app/
├── database.py
├── models.py
├── routes/
│   ├── tareas.py
│   └── recordatorios.py
└── static/
    ├── index.html
    ├── app.js
    └── styles.css

tests/
├── test_recordatorios.py
└── test_api.py
```

**Decisión de estructura**: Mantener el monolito existente y añadir solo el módulo de
recordatorios, su persistencia y pruebas.

**Punto de integración**: `app/database.py` conserva las tablas existentes y añade
`recordatorios` con una FK a `tareas`; `app/models.py` contiene el modelo y la validación
temporal. Las rutas y el servicio de procesamiento se incorporarán en las fases posteriores.

## Complejidad

No hay violaciones de la constitución que justificar.

## Verificación posterior al diseño

- **Simplicidad**: APROBADO; no se añaden servicios externos ni frameworks nuevos.
- **Pruebas obligatorias**: APROBADO; se cubren transiciones y casos límite.
- **Código legible**: APROBADO; responsabilidades separadas.
- **Validación de entradas**: APROBADO; se validan fechas, estados y referencias.
- **Accesibilidad y responsividad**: APROBADO; permiso y estado tendrán mensajes accesibles.
