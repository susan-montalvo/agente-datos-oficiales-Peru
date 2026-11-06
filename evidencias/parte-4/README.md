# Evidencias de la Parte 4: ejecuciones de la evaluación

Esta carpeta guarda una copia sin cambios de las dos ejecuciones de las 10
preguntas de [`evaluacion/preguntas.csv`](../../evaluacion/preguntas.csv). La
comparación y los resultados están en
[`evaluacion/comparacion.md`](../../evaluacion/comparacion.md) y
[`evaluacion/resultados.csv`](../../evaluacion/resultados.csv).

| Carpeta | Configuración | Contenido |
|---|---|---|
| [`modo-a/`](modo-a/) | Sin MCP ni Skills | `preguntas.csv` con la columna `respuesta` y `README.md` con la búsqueda de datos, la metodología y las advertencias |
| [`modo-b/`](modo-b/) | Con MCP y Skills | `preguntas.csv` con la columna `respuesta`, `README.md` con el procedimiento y `evidencias/`: respuestas del MCP (`mcp_respuestas.json`), cálculos (`calculos.json`), validación ENAHO (`validacion.txt`), scripts y figuras de las Skills |

## Origen

Las dos ejecuciones se hicieron el 6 de noviembre de 2026 en sesiones de Claude
Code abiertas en carpetas fuera de este repositorio. Así el Modo A no tenía
acceso al MCP, a las Skills ni a los archivos de evaluación.

- `GitHub/Modo A` → copiada en `modo-a/`
- `GitHub/Modo B` → copiada en `modo-b/`. Durante la ejecución, esta carpeta se
  llamaba `Modo B firme`.

Se copiaron sin modificar, salvo los archivos `.DS_Store` de macOS. Por eso las
rutas relativas de los README (por ejemplo, `../agente-datos-oficiales-Peru/` o
`../Modo B/evidencias/scripts/…`) se refieren a la ubicación original. Desde
este repositorio, los scripts del Modo B están en
[`modo-b/evidencias/scripts/`](modo-b/evidencias/scripts/).

Las conversaciones completas de las dos sesiones están en
[`evidencias_ia/`](../../evidencias_ia/).
