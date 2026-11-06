# Agente de datos oficiales del Perú

Proyecto de la Tarea 4 del curso Python Intermedio: un agente de investigación
socioeconómica que combina series del BCRP, microdatos ENAHO del INEI, un
servidor MCP, Skills de Claude Code y análisis reproducible.

## Contenido

1. [Objetivo](#1-objetivo)
2. [Arquitectura del agente](#2-arquitectura-del-agente)
3. [Herramientas MCP](#3-herramientas-mcp-parte-1)
4. [Skills ENAHO](#4-skills-enaho-parte-2)
5. [Fuentes y descarga de datos](#5-fuentes-y-descarga-de-datos)
6. [Instalación con uv](#6-instalación-con-uv)
7. [Conectar el MCP a Claude Code](#7-conectar-el-mcp-a-claude-code)
8. [Reproducir el procesamiento y las pruebas](#8-reproducir-el-procesamiento-y-las-pruebas)
9. [Resultados de la evaluación](#9-resultados-de-la-evaluación-parte-4)
10. [Limitaciones y problemas encontrados](#10-limitaciones-y-problemas-encontrados)
11. [Ejemplo de una ejecución completa](#11-ejemplo-de-una-ejecución-completa-parte-3)
12. [Evidencias del uso de IA](#12-evidencias-del-uso-de-ia)

## 1. Objetivo

Construir un agente que responda preguntas socioeconómicas sobre el Perú con
datos oficiales y cálculos verificables, y no con el conocimiento previo del
modelo. El agente consulta las series del BCRP mediante un servidor MCP,
procesa los microdatos de la ENAHO 2024 mediante Skills, y produce cifras,
gráficos, mapas e informes con su fuente y su procedimiento.

## 2. Arquitectura del agente

```text
             Pregunta en lenguaje natural
                         │
                         ▼
                ┌─────────────────┐
                │   Claude Code   │  interpreta, planifica y combina resultados
                └────────┬────────┘
          ┌──────────────┴───────────────┐
          ▼                              ▼
 Servidor MCP `bcrp`               Skills ENAHO (.claude/skills/)
 (mcp/server.py)                   limpiando-enaho → base de personas
 buscar_series · serie             graficando-enaho → figuras/
 resumen · comparar_series         mapeando-enaho  → mapas/
 recurso bcrp://serie/{codigo}
 prompt informe
          │                              │
          ▼                              ▼
 API oficial del BCRP              Microdatos INEI (módulos 02 y 34)
          └──────────────┬───────────────┘
                         ▼
     Respuesta con cifras, fuentes, gráficos, mapas e informe
```

| Carpeta | Contenido |
|---|---|
| `mcp/` | Servidor MCP (`server.py`) y sus pruebas (`test_server.py`, `test_comparar_series.py`) |
| `.claude/skills/` | Las tres Skills ENAHO con su `SKILL.md` y sus scripts |
| `datos/` | Microdatos ENAHO (no se versionan), GeoJSON departamental y CSV del PBI 2024 |
| `referencias/` | Pobreza departamental 2024 de referencia, para validar el mapa |
| `salidas/` | Validación de la limpieza (`validacion.txt`); la base Parquet no se versiona |
| `figuras/`, `mapas/` | Gráficos y mapa generados por las Skills |
| `scripts/` | Análisis de la Parte 3 y exportador de las evidencias de IA |
| `outputs/parte-3/`, `informes/` | Indicadores, figuras e informe final de la Parte 3 |
| `evaluacion/` | Preguntas, resultados y comparación de la Parte 4 |
| `evidencias/` | Evidencias de ejecución de cada parte |
| `evidencias_ia/` | Conversaciones con los asistentes de IA |

## 3. Herramientas MCP (Parte 1)

El servidor sigue el contrato de la Sesión 04 y toma como referencia el
[proyecto MCP del BCRP](https://github.com/susan-montalvo/mcp-bcrp). Consulta
metadatos y observaciones en la API oficial del BCRP. El catálogo descargado se
guarda en `mcp/data/` y no se versiona.

| Componente | Tipo | Qué hace |
|---|---|---|
| `buscar_series` | Herramienta | Busca series por texto y, si se indica, por frecuencia |
| `serie` | Herramienta | Devuelve las observaciones de una serie en un intervalo, con el código, el período y el enlace oficial |
| `resumen` | Herramienta | Calcula en Python estadísticas del intervalo: primer y último valor, promedio, mínimo, máximo, cambio y variación porcentual |
| `comparar_series` | Herramienta propia | Alinea dos series de la misma frecuencia por períodos coincidentes y calcula su correlación. La correlación describe asociación y no demuestra causalidad |
| `bcrp://serie/{codigo}` | Recurso | Ficha con los metadatos oficiales de una serie |
| `informe` | Prompt | Plantilla para un informe breve con cifras verificables y sus fuentes |

Fechas aceptadas: `YYYY-MM` (mensual), `YYYY-T1` (trimestral), `YYYY-MM-DD`
(diaria) y `YYYY` (anual).

**Verificación:**

- **Acceso del cliente MCP:** un cliente FastMCP por `stdio` enumeró las
  herramientas y la plantilla del recurso, leyó la ficha de `PN01273PM` y
  ejecutó el prompt `informe`.
- **Funcionamiento desde Claude Code:** en una consulta del IPC de Lima
  Metropolitana a 12 meses (`2025-12` a `2026-09`), Claude Code llamó al
  servidor `bcrp` y mostró las observaciones, el resumen, el código, el período
  y el enlace oficial
  ([captura](evidencias/parte-1/integracion-claude-code-bcrp.png)).
- **Pruebas automatizadas:** `uv run pytest -q` terminó con **10 passed**: las 8
  pruebas originales y 2 pruebas adicionales para `comparar_series`, una con un
  caso válido y otra con un caso inválido
  ([salida](evidencias/parte-1/pruebas-automatizadas-10.txt) y
  [captura](evidencias/parte-1/pruebas-automatizadas-10.png)).

Ejemplo de solicitud con la herramienta propia: «Compara las series mensuales
PN01273PM y [segundo código] entre 2020-01 y 2024-12 e informa la correlación,
los períodos coincidentes y las fuentes».

## 4. Skills ENAHO (Parte 2)

Las tres Skills de `.claude/skills/` son copias independientes de las
desarrolladas en `skills-enaho`. Sus scripts usan las dependencias de
`pyproject.toml` y se ejecutan desde la raíz del repositorio con `uv run`.

| Skill | Qué hace | Salida |
|---|---|---|
| `limpiando-enaho` | Lee los módulos 02 y 34 (Stata), une personas y hogares, conserva a los residentes habituales, aplica `facpob07` y valida contra la pobreza oficial | `salidas/personas_2024.parquet` y `salidas/validacion.txt` |
| `graficando-enaho` | Grafica la pobreza (o la pobreza extrema) por área, departamento, sexo o grupo de edad, con título, unidades y fuente | `figuras/*.png` |
| `mapeando-enaho` | Hace un mapa coroplético de las 25 unidades territoriales, unido por código de ubigeo y cotejado con la referencia | `mapas/pobreza_departamento.png` |

Validación de la limpieza 2024: 33,691 hogares, 108,664 residentes habituales,
pobreza de 27.58 % (Sumaria) frente al 27.6 % oficial del INEI, y
`VALIDACIÓN OK` ([salidas/validacion.txt](salidas/validacion.txt)). El mapa
aprobó los 25 cotejos con la referencia.

**Activación y coordinación:** en sesiones nuevas de Claude Code y en lenguaje
natural, se probó lo siguiente
([evidencias](evidencias/parte-2/coordinacion-skills-2024/)):

- [Limpieza individual](evidencias/parte-2/coordinacion-skills-2024/limpiando-individual.txt):
  se activó `limpiando-enaho` y terminó con `VALIDACIÓN OK`.
- [Gráfico sin base procesada](evidencias/parte-2/coordinacion-skills-2024/graficando-sin-base.txt):
  se activó `graficando-enaho`, que llamó a `limpiando-enaho` y luego generó el
  gráfico por área (39.4 % rural, 24.7 % urbana).
- [Mapa sin base procesada](evidencias/parte-2/coordinacion-skills-2024/mapeando-sin-base.txt):
  se activó `mapeando-enaho`, que llamó a `limpiando-enaho` y generó el mapa
  tras aprobar los 25 cotejos.

Para estas pruebas se apartó temporalmente el Parquet existente y después se
restauró byte por byte. Las ejecuciones por área, departamento, sexo y edad
están en [evidencias de graficando-enaho](evidencias/parte-2/graficando-enaho/).

## 5. Fuentes y descarga de datos

| Fuente | Datos | Enlace |
|---|---|---|
| BCRP | Series estadísticas (API) | <https://estadisticas.bcrp.gob.pe/estadisticas/series/api/> |
| INEI | ENAHO 2024 (código 966), módulo 02: características de los miembros del hogar | [966-Modulo02.zip](https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip) |
| INEI | ENAHO 2024 (código 966), módulo 34: sumaria (pobreza) | [966-Modulo34.zip](https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip) |
| INEI | Portal de microdatos | <https://proyectos.inei.gob.pe/microdatos/> |

Los ZIP de la ENAHO se guardan en `datos/` sin descomprimir y no se versionan.
El GeoJSON departamental (`datos/`) y la referencia de pobreza 2024
(`referencias/`) sí están incluidos.

## 6. Instalación con uv

Requiere Python 3.12 y [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/susan-montalvo/agente-datos-oficiales-Peru.git
cd agente-datos-oficiales-Peru
uv sync --group dev
```

`uv` crea el entorno en `.venv` con las versiones fijadas en `uv.lock`. Para
ejecutar comandos dentro del entorno, se antepone `uv run`.

## 7. Conectar el MCP a Claude Code

El archivo [`.mcp.json`](.mcp.json) registra el servidor `bcrp`:

```json
{
  "mcpServers": {
    "bcrp": {
      "command": "uv",
      "args": ["run", "--project", ".", "python", "mcp/server.py"]
    }
  }
}
```

1. Abrir Claude Code en la raíz del repositorio (`claude`).
2. Aprobar el servidor `bcrp` cuando Claude Code lo solicite, o revisarlo con
   `/mcp`.
3. Preguntar, por ejemplo: «¿Cuál fue la variación interanual del PBI en mayo
   de 2024 según la serie PN01728AM?».

Las Skills de `.claude/skills/` se cargan automáticamente al abrir Claude Code
en la raíz del repositorio.

## 8. Reproducir el procesamiento y las pruebas

```bash
# Pruebas del servidor MCP (10 pruebas)
uv run pytest -q

# Servidor MCP de forma manual (Claude Code lo inicia con .mcp.json)
uv run python mcp/server.py

# Skills ENAHO (requieren los ZIP del INEI en datos/)
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area --anio 2024
uv run .claude/skills/mapeando-enaho/scripts/mapear.py --anio 2024

# Análisis e indicadores de la Parte 3
uv run python scripts/parte3_analisis.py
```

La limpieza debe terminar con `VALIDACIÓN OK` antes de los otros pasos. Las
opciones de `graficar.py --por` son `area`, `departamento`, `sexo` y `edad`.

## 9. Resultados de la evaluación (Parte 4)

Se ejecutaron las mismas 10 preguntas (4 BCRP, 4 ENAHO y 2 combinadas) con
Claude Code (`claude-opus-5-5`) en dos configuraciones:

| Métrica | Modo A: sin MCP ni Skills | Modo B: con MCP y Skills |
|---|---:|---:|
| Respuestas correctas | 2 / 10 | 2 / 10 |
| Correctas si se acepta el redondeo (sensibilidad) | 6 / 10 | 6 / 10 |
| Tiempo total / promedio por pregunta | 409.4 s / 40.9 s | 174.3 s / 17.4 s |
| Fuente ENAHO | Repositorio de GitHub de terceros (el INEI no respondió) | Microdatos oficiales del INEI |

MCP y Skills no cambiaron la cantidad de aciertos. Los errores comunes se deben
al redondeo frente a tolerancias muy estrictas (P01–P03 y P10) y a un filtro de
población distinto al de las respuestas esperadas (P05–P08). Sí redujeron el
tiempo en 57 % y aseguraron fuentes oficiales y evidencias reproducibles.

- Preguntas, respuestas esperadas y tolerancias: [evaluacion/preguntas.csv](evaluacion/preguntas.csv)
- Resultados por pregunta y modo: [evaluacion/resultados.csv](evaluacion/resultados.csv)
- Análisis y conclusión: [evaluacion/comparacion.md](evaluacion/comparacion.md)
- Vista lado a lado: [evaluacion/matriz_comparacion.md](evaluacion/matriz_comparacion.md)
- Respuestas y evidencias de cada modo: [evidencias/parte-4/](evidencias/parte-4/)

## 10. Limitaciones y problemas encontrados

- **Microdatos:** no se versionan por su tamaño. Para reproducir, hay que
  descargarlos del INEI. Durante la evaluación, el sitio del INEI no respondió
  en el Modo A.
- **Filtro de población:** `limpiando-enaho` conserva a los residentes
  habituales (108,664 personas). Las respuestas esperadas de la evaluación usan
  `p204 = 1` (109,842 personas), que reproduce la pobreza de la Sumaria. Esa
  diferencia explica los errores de P05–P08 y es una mejora pendiente de la
  Skill.
- **Tolerancias de la evaluación:** se definieron antes de ejecutar y son más
  estrictas que la precisión con que el agente reporta, por lo que penalizan
  el redondeo.
- **Diseño de la evaluación:** se hizo una sola sesión por modo con las 10
  preguntas, no una por pregunta, así que el tiempo es un promedio por modo. El
  Modo A consultó resultados de otro proyecto público para validarse. El
  criterio de interpretación de las preguntas combinadas se definió después de
  ver las respuestas. Hubo un primer intento del Modo B con otro modelo, que se
  descartó. El detalle está en [comparacion.md](evaluacion/comparacion.md).
- **Uso del MCP en el Modo B:** el MCP se llamó con un cliente FastMCP por
  `stdio` porque la sesión se abrió fuera del repositorio. Las Skills se
  ejecutaron con sus scripts.
- **Asistente de la Parte 3:** la ejecución integrada de la Parte 3 (MCP y
  Skills en una misma ejecución) se hizo con el agente de GitHub Copilot en
  VS Code (`gpt-6-luna`), no con Claude Code. Fue un error involuntario: la
  estudiante trabajaba en el panel de chat de VS Code y no se dio cuenta de que
  ese chat era Copilot y no Claude Code. Lo notó al preparar la Parte 4, como
  consta al final de la
  [conversación de planificación](evidencias_ia/evaluacion/02_2026-11-05_parte-4-planificacion.md)
  («donde estoy ahorita, en claude code, o en copilot de vs code?»). La
  ejecución usó el mismo servidor MCP y las mismas Skills del repositorio.
- **Análisis descriptivo:** el informe y la herramienta `comparar_series`
  describen asociaciones y no estiman efectos causales.

## 11. Ejemplo de una ejecución completa (Parte 3)

**Pregunta de investigación:** ¿Cómo evolucionó la actividad económica del
Perú durante 2024 y cómo se distribuyó territorialmente la pobreza monetaria
entre sus departamentos en ese mismo año?

1. **Plan:** el agente interpretó la pregunta y preparó el
   [plan de análisis](PLAN_ANALISIS_PARTE_3.md).
2. **BCRP mediante el MCP:** `serie` y `resumen` sobre `PN01728AM`
   (2024-01 a 2024-12) → [datos/pbi_interanual_mensual_2024.csv](datos/pbi_interanual_mensual_2024.csv).
3. **ENAHO mediante las Skills:** `limpiando-enaho` (validación OK) →
   `graficando-enaho --por departamento` → `mapeando-enaho` (25 cotejos
   aprobados).
4. **Integración:** [scripts/parte3_analisis.py](scripts/parte3_analisis.py)
   generó el gráfico del PBI, el ranking departamental y el resumen
   ([reproduccion.txt](outputs/parte-3/reproduccion.txt)).
5. **Resultado:** el [informe final](informes/informe_final.md), con estos
   hallazgos:
   - El PBI interanual fue irregular: −0.41 % en marzo, 5.71 % en mayo y 5.07 %
     en diciembre, con un promedio de 3.48 %.
   - La pobreza departamental fue de 45.0 % en Cajamarca y 6.0 % en Ica, una
     brecha de 39.0 puntos porcentuales.
   - Cajamarca, Loreto, Puno, Pasco y Huánuco superaron o rondaron el 39 %.
6. **Verificación manual:** se contrastaron las afirmaciones numéricas con la
   API del BCRP y con el CSV procesado
   ([capturas](evidencias/parte-3/verificacion-resultados/)).

Productos: [outputs/parte-3/](outputs/parte-3/) (gráfico BCRP, gráfico ENAHO,
mapa, ranking y validación del mapa).

## 12. Evidencias del uso de IA

Las conversaciones completas con los asistentes, exportadas desde sus
registros locales y sin datos personales, están en
[`evidencias_ia/`](evidencias_ia/). Están organizadas en `mcp/`, `skills/`,
`integracion/` y `evaluacion/`, y el índice está en
[evidencias_ia/README.md](evidencias_ia/README.md).

| Asistente | Uso |
|---|---|
| GitHub Copilot en VS Code (`gpt-6-luna`) | Entorno, Parte 1 (servidor MCP), Parte 2 (integración de Skills), Parte 3 (agente e informe) y planificación de la Parte 4 |
| Claude Code (`claude-opus-5-5`) | Desarrollo inicial de las Skills, pruebas de activación y coordinación, diseño de la evaluación, ejecuciones Modo A y Modo B, y documentación de la Parte 4 |

Las conversaciones se exportaron con
[scripts/exportar_evidencias_ia.py](scripts/exportar_evidencias_ia.py).
