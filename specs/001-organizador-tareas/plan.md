# Plan de implementación: Organizador de tareas académicas

**Rama**: `001-organizador-tareas` | **Fecha**: 2026-10-26 | **Especificación**: [spec.md](spec.md)

**Entrada**: `specs/001-organizador-tareas/spec.md`

## Resumen

Crear una aplicación local para organizar materias y tareas académicas, con ordenamiento,
filtros, estados vencido/urgente y eliminación confirmada en cascada. Se usará un único
proyecto FastAPI con frontend estático HTML, CSS y JavaScript, y SQLite como almacenamiento.
La investigación está en [research.md](research.md).

## Contexto técnico

**Lenguaje/Versión**: Python 3.12

**Dependencias principales**: FastAPI y pytest

**Almacenamiento**: SQLite

**Pruebas**: pytest para lógica, persistencia y contratos HTTP

**Plataforma objetivo**: Navegador web en celular y computadora, servido localmente

**Tipo de proyecto**: Aplicación web monolítica de un solo usuario por dispositivo

**Objetivos de rendimiento**: Respuesta inmediata para el uso local; no hay objetivo de
concurrencia multiusuario.

**Restricciones**: Sin Docker ni microservicios; sin inicio de sesión; documentos en
español; interfaz accesible y responsiva.

**Escala/Alcance**: Un usuario por dispositivo y dos entidades principales; sin
sincronización, autenticación ni eliminación independiente de tareas.

## Verificación de la constitución

*Puerta: debe aprobarse antes de investigar y después del diseño.*

- **Simplicidad**: APROBADO. Un solo proyecto FastAPI, SQLite y frontend sin frameworks.
- **Pruebas obligatorias**: APROBADO. pytest cubrirá flujos, validaciones y reglas.
- **Código legible**: APROBADO. Se mantendrán módulos pequeños y nombres claros.
- **Validación de entradas**: APROBADO. El modelo y los contratos definen límites y errores.
- **Accesibilidad y responsividad**: APROBADO. Se validará en celular y computadora.
- **Contenido académico**: APROBADO. Todos los documentos están en español.

## Estructura del proyecto

### Documentación de esta funcionalidad

```text
specs/001-organizador-tareas/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/api.md
└── tasks.md              # Se crea en /speckit.tasks
```

### Código fuente

```text
app/
├── main.py              # Aplicación FastAPI y archivos estáticos
├── database.py          # Conexión y creación de SQLite
├── models.py            # Entidades y validaciones
├── routes/
│   ├── materias.py      # Operaciones de materias
│   └── tareas.py        # Operaciones de tareas y filtros
└── static/
    ├── index.html
    ├── styles.css
    └── app.js

tests/
├── test_materias.py
├── test_tareas.py
└── test_api.py
```

**Decisión de estructura**: Un proyecto con `app/` para backend, rutas y archivos
estáticos, más `tests/` para pruebas. No se crean capas adicionales sin una necesidad
verificable.

## Seguimiento de complejidad

No hay violaciones de la constitución que justificar. La estructura propuesta evita
complejidad innecesaria y mantiene una sola aplicación.

## Verificación posterior al diseño

- **Simplicidad**: APROBADO; no se añadieron frameworks frontend, Docker ni servicios.
- **Pruebas obligatorias**: APROBADO; quickstart y estructura incluyen pruebas pytest.
- **Código legible**: APROBADO; responsabilidades separadas por módulos pequeños.
- **Validación de entradas**: APROBADO; límites y relaciones están documentados.
- **Accesibilidad y responsividad**: APROBADO; la interfaz está contratada para ambos
  tipos de dispositivo.
