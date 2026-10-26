<!--
Sync Impact Report
- Version change: inexistente → 1.0.0
- Principios incorporados: cinco principios iniciales para el proyecto académico de la UPB.
- Secciones añadidas: Restricciones académicas y Flujo de desarrollo y calidad.
- Secciones eliminadas: ninguna.
- Pendientes: confirmar la fecha oficial de ratificación.
-->

# Constitución del Proyecto Académico UPB

## Principios Fundamentales

### I. Simplicidad Primero (YAGNI)
Las soluciones DEBEN implementar únicamente lo necesario para cumplir el objetivo
actual. El equipo NO DEBE introducir sobreingeniería, abstracciones especulativas,
funcionalidades no solicitadas ni dependencias innecesarias. Toda complejidad adicional
DEBE justificarse por una necesidad verificable.

### II. Pruebas Obligatorias
Toda funcionalidad DEBE contar con pruebas automatizadas antes de considerarse terminada.
Las pruebas DEBEN cubrir el comportamiento esperado y los casos relevantes de error.
Una funcionalidad sin pruebas automatizadas no cumple el criterio de finalización.

### III. Código Legible
El código DEBE utilizar nombres claros y funciones pequeñas, con una responsabilidad
comprensible. La documentación DEBE explicar las decisiones o comportamientos no
obvios, no repetir lo que ya expresa el código. La legibilidad DEBE priorizarse sobre
la brevedad extrema.

### IV. Validación de Entradas
Todo dato proporcionado por el usuario DEBE validarse antes de procesarse, almacenarse
o enviarse a otro componente. La validación DEBE rechazar datos inválidos de forma
controlada y comunicar errores comprensibles sin exponer información sensible.

### V. Accesibilidad y Diseño Responsivo
La interfaz DEBE ser utilizable en celulares y computadoras, adaptándose a sus
distintos tamaños de pantalla. Las funcionalidades DEBEN diseñarse con criterios de
accesibilidad, incluyendo navegación clara, contenido comprensible y controles
utilizables por personas con diferentes capacidades.

## Restricciones Académicas

El proyecto DEBE mantener un alcance coherente con sus objetivos académicos y permitir
que sus decisiones técnicas sean explicables y verificables. Las entregas DEBEN
identificar sus supuestos, limitaciones y evidencias de validación. El contenido de
los documentos del proyecto DEBE estar escrito en español.

## Flujo de Desarrollo y Calidad

Cada cambio DEBE revisarse contra estos principios antes de darse por terminado. El
trabajo DEBE avanzar mediante incrementos pequeños y verificables. La revisión DEBE
comprobar, como mínimo, la existencia de pruebas automatizadas, la validación de
entradas y el funcionamiento de la interfaz en celular y computadora cuando aplique.

## Gobernanza

Esta constitución es la referencia obligatoria para las decisiones de diseño,
implementación y revisión del proyecto. Toda modificación DEBE documentar el motivo,
el impacto y la fecha del cambio. Las enmiendas requieren revisión del equipo
responsable del proyecto y DEBEN actualizar la versión siguiendo estas reglas:

- **MAJOR**: eliminación o redefinición incompatible de un principio.
- **MINOR**: adición de un principio o ampliación sustancial de las obligaciones.
- **PATCH**: aclaraciones, correcciones de redacción o cambios no semánticos.

Las revisiones de calidad DEBEN verificar el cumplimiento de la constitución. Cuando
una excepción sea necesaria, DEBE registrarse su justificación, alcance y aprobación.

**Versión**: 1.0.0 | **Ratificada**: TODO(RATIFICATION_DATE): confirmar fecha oficial | **Última modificación**: 2026-10-26
