# Evidencias de uso de IA

Esta carpeta reúne las conversaciones con asistentes de IA usadas para
desarrollar y evaluar el proyecto, exportadas a Markdown (opción B de la pauta).
Cada archivo corresponde a una sesión, o a un tramo de una sesión larga. Incluye
la herramienta, el modelo, la carpeta de trabajo, las horas de inicio y fin, las
instrucciones de la usuaria, las respuestas del asistente y las herramientas que
ejecutó con sus resultados.

## Asistentes utilizados

| Asistente | Modelo | Uso |
|---|---|---|
| GitHub Copilot (agente de VS Code) | `gpt-6-luna` | Entorno del proyecto, Parte 1 (servidor MCP), Parte 2 (adaptación e integración de las Skills), Parte 3 (agente e informe), planificación de la Parte 4 y un primer intento del Modo B, que se descartó |
| Claude Code | `claude-opus-5-5` | Desarrollo inicial de las Skills, pruebas de activación y coordinación, diseño de las preguntas y respuestas esperadas, ejecuciones Modo A y Modo B, y documentación de la Parte 4 |

## Índice (orden cronológico dentro de cada carpeta)

| Carpeta | Archivo | Asistente | Contenido |
|---|---|---|---|
| `mcp/` | [01_2026-10-28_prueba-mcp-bcrp-ipc.md](mcp/01_2026-10-28_prueba-mcp-bcrp-ipc.md) | Claude Code | Antecedente (Sesión 04): búsqueda de series del IPC e inflación con el MCP `bcrp` |
| `mcp/` | [02_2026-10-28_prueba-mcp-bcrp-recurso.md](mcp/02_2026-10-28_prueba-mcp-bcrp-recurso.md) | Claude Code | Antecedente (Sesión 04): lectura del recurso `bcrp://serie/PN01273PM` |
| `mcp/` | [03_2026-11-04_entorno-y-parte-1-servidor-mcp.md](mcp/03_2026-11-04_entorno-y-parte-1-servidor-mcp.md) | Copilot | Entorno del proyecto y Parte 1: `server.py`, herramienta propia `comparar_series`, conexión con Claude Code, 8 pruebas originales y 2 adicionales |
| `skills/` | [01_2026-10-31_entorno-skills.md](skills/01_2026-10-31_entorno-skills.md) | Claude Code | Preparación del entorno para las Skills ENAHO |
| `skills/` | [02_2026-10-31_desarrollo-skills.md](skills/02_2026-10-31_desarrollo-skills.md) | Claude Code | Desarrollo de `limpiando-enaho`, `graficando-enaho` y `mapeando-enaho` |
| `skills/` | [03_2026-10-31_pruebas-activacion-skills.md](skills/03_2026-10-31_pruebas-activacion-skills.md) | Claude Code | 15 sesiones de prueba: activación de las Skills con preguntas en lenguaje natural |
| `skills/` | [04_2026-11-04_parte-2-adaptacion-e-integracion-skills.md](skills/04_2026-11-04_parte-2-adaptacion-e-integracion-skills.md) | Copilot | Parte 2: validación del mapa, integración de las Skills al repositorio, revisión de requisitos, activación y coordinación |
| `skills/` | [05_2026-11-05_pruebas-coordinacion-skills.md](skills/05_2026-11-05_pruebas-coordinacion-skills.md) | Claude Code | 7 sesiones de prueba: invocación individual y coordinación de las tres Skills en este repositorio |
| `integracion/` | [01_2026-11-05_parte-3-agente-e-informe.md](integracion/01_2026-11-05_parte-3-agente-e-informe.md) | Copilot | Parte 3: pregunta de investigación, plan de análisis, ejecución con MCP y Skills, informe final y verificación manual |
| `evaluacion/` | [01_2026-11-04_traslado-preguntas.md](evaluacion/01_2026-11-04_traslado-preguntas.md) | Claude Code | Traslado de `preguntas.csv` a una carpeta temporal fuera del repositorio |
| `evaluacion/` | [02_2026-11-05_parte-4-planificacion.md](evaluacion/02_2026-11-05_parte-4-planificacion.md) | Copilot | Planificación de la Parte 4: plantillas, cómo evitar la contaminación y cómo usar sesiones independientes |
| `evaluacion/` | [03_2026-11-05_diseno-preguntas-y-respuestas-esperadas.md](evaluacion/03_2026-11-05_diseno-preguntas-y-respuestas-esperadas.md) | Claude Code | Diseño de las 10 preguntas y cálculo independiente de las respuestas esperadas y tolerancias |
| `evaluacion/` | [04_2026-11-05_resultados-y-comparacion.md](evaluacion/04_2026-11-05_resultados-y-comparacion.md) | Claude Code | Registro de resultados, criterios de corrección, `comparacion.md` y organización de las evidencias de la Parte 4 |
| `evaluacion/` | [05_2026-11-06_modo-a-sin-mcp-ni-skills.md](evaluacion/05_2026-11-06_modo-a-sin-mcp-ni-skills.md) | Claude Code | Ejecución completa del Modo A (sin MCP ni Skills) |
| `evaluacion/` | [06_2026-11-06_modo-b-primer-intento-copilot.md](evaluacion/06_2026-11-06_modo-b-primer-intento-copilot.md) | Copilot | Primer intento del Modo B con Copilot. Se descartó porque usaba otro modelo que el Modo A |
| `evaluacion/` | [07_2026-11-06_modo-b-con-mcp-y-skills.md](evaluacion/07_2026-11-06_modo-b-con-mcp-y-skills.md) | Claude Code | Ejecución completa del Modo B (con MCP y Skills) que se usó en la evaluación |

Las respuestas generadas por cada modo están en
[`evidencias/parte-4/`](../evidencias/parte-4/), y la comparación en
[`evaluacion/comparacion.md`](../evaluacion/comparacion.md).

## Cómo se exportaron

Las sesiones se convirtieron desde los registros locales de cada herramienta
con [`scripts/exportar_evidencias_ia.py`](../scripts/exportar_evidencias_ia.py):

- Claude Code: `~/.claude/projects/…/*.jsonl`.
- GitHub Copilot: `~/.copilot/session-state/<sesión>/events.jsonl`.

La sesión principal de Copilot (`43cf96d4`, 205 mensajes del 4 y 5 de
noviembre) se dividió en cuatro archivos según la parte de la tarea. En git
aparece como "Agent host session 8dba87ff".

- **Datos ocultos:** correos, rutas con el nombre de usuario, carpetas
  temporales y enlaces privados de claude.ai. Antes de publicar se buscaron
  claves API, tokens y contraseñas, y no se encontró ninguno.
- **Contenido omitido:** las instrucciones de sistema, los hooks y permisos de
  Copilot, y el razonamiento interno de los modelos. Las salidas de herramientas
  de más de 4,000 caracteres se recortan, y el recorte se indica.
- **Sesiones excluidas:** conversaciones personales sin relación con el
  proyecto, que estaban en las mismas carpetas de registros.
