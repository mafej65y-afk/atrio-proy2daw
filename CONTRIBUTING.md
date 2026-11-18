# Cómo contribuir

Este documento recoge cómo trabaja el Grupo 4 en el repositorio. Lo que no está en el repositorio no cuenta como evidencia.

## Flujo de trabajo

1. **Incidencia.** Toda tarea nace como una incidencia (*issue*) en el tablero, con responsable.
2. **Rama.** Una rama por tarea, creada desde `main`:
   - `feature/<n.º-incidencia>-descripcion-corta` para funcionalidades
   - `fix/<n.º-incidencia>-descripcion-corta` para correcciones
   - `docs/<n.º-incidencia>-descripcion-corta` para documentación
3. **Commits.** Pequeños y con mensaje claro, siguiendo [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/). Mensajes en español:
   - `docs: añade análisis DAFO a la propuesta`
   - `feat: crea el recorrido por estancias`
   - `fix: corrige el contraste del botón de consulta`
4. **Pull request.** Con descripción y enlace a la incidencia (`Closes #12`). Se usa la plantilla del repositorio.
5. **Revisión.** Al menos otra persona del equipo revisa y aprueba la PR.
6. **Merge a `main`.** `main` está protegida: no se admiten commits directos.
7. **Etiqueta.** Una versión por hito: `v0.1-propuesta`, `v0.2-diseno`, `v0.3-funcional`, `v0.4-mvp`, `v1.0-final`.

## Idiomas

- Código (nombres de variables, funciones, clases y tablas): inglés.
- Comentarios, commits, incidencias, manuales y memoria: español.

## Reglas del proyecto

- Solo datos ficticios, generados con *seeders*. Nada de datos personales reales.
- Ninguna credencial en el código: se usan variables de entorno (`.env`, que no se sube).
- Dependencias con licencia libre o permisiva, listadas en la documentación.
- El uso de IA se declara en `docs/declaracion-uso-ia.md`. Cada integrante debe poder explicar lo que entrega.

## Tablero

Columnas: **Pendiente** → **En curso** → **En revisión** → **Hecho**. Cada tarjeta tiene responsable y hito.
