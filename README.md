# Agente de datos oficiales del Peru

Proyecto de la Tarea 4: un agente de investigacion socioeconomica que combina
series del BCRP, microdatos ENAHO del INEI, herramientas MCP y analisis
reproducible.

## Preparar el entorno

Requiere Python 3.12 y [uv](https://docs.astral.sh/uv/).

```bash
uv sync --group dev
uv run pytest
```

`uv` crea el entorno local en `.venv` y conserva las versiones resueltas en
`uv.lock`. Para ejecutar comandos dentro del entorno, antepon `uv run`.

## Estructura

- `src/agente_datos_oficiales_peru/`: codigo del proyecto.
- `mcp/server.py`: servidor MCP de series oficiales del BCRP.
- `mcp/test_server.py` y `mcp/test_comparar_series.py`: pruebas del servidor.
- `.claude/skills/`: Skills locales para limpiar, graficar y mapear la ENAHO.
- `datos/`: insumos ENAHO y GeoJSON; los microdatos descargados no se versionan.
- `salidas/`, `figuras/` y `mapas/`: resultados generados por las Skills.

El proyecto debe documentar las fuentes oficiales, los pasos de procesamiento y
los resultados para que el analisis pueda reproducirse.

## Parte 2: Skills para procesar y analizar ENAHO

Las tres Skills de `.claude/skills/` son copias independientes de las desarrolladas
en `skills-enaho`: `limpiando-enaho`, `graficando-enaho` y `mapeando-enaho`.
Sus scripts usan las dependencias ya declaradas en `pyproject.toml` y se ejecutan
desde la raíz de este repositorio con `uv run`.

Los ZIP de microdatos ENAHO deben estar en `datos/` (código INEI 966 para 2024).
No se versionan. El GeoJSON departamental y la referencia de pobreza 2024 están
incluidos en `datos/` y `referencias/`. Para procesar, graficar y mapear:

```bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area --anio 2024
uv run .claude/skills/mapeando-enaho/scripts/mapear.py --anio 2024
```

La limpieza debe pasar la validación antes de usar la base en los otros pasos.
Los productos se guardan en `salidas/`, `figuras/` y `mapas/`.

## Parte 1: servidor MCP del BCRP

El servidor sigue el contrato de la Sesion 04 y toma como referencia el
[proyecto MCP del BCRP](https://github.com/susan-montalvo/mcp-bcrp). Busca
metadatos y observaciones en la API oficial del BCRP; el catalogo descargado se
guarda localmente en `mcp/data/` y no se versiona.

```bash
uv sync --group dev
uv run python mcp/server.py
```

Claude Code inicia el servidor con la configuracion local de `.mcp.json`.
Sus herramientas `buscar_series`, `serie`, `resumen` y `comparar_series`
devuelven el codigo, el periodo y la fuente oficial. Las fechas aceptadas son
`YYYY-MM` (mensual), `YYYY-T1` (trimestral), `YYYY-MM-DD` (diaria) y `YYYY`
(anual).

### Verificación de recursos, prompt e integración

- **Acceso del cliente MCP (paso 2):** verificado con un cliente FastMCP por
  `stdio`. El cliente enumeró las herramientas y la plantilla
  `bcrp://serie/{codigo}`, leyó la ficha de `PN01273PM` y encontró y ejecutó el
  prompt `informe`.
- **Funcionamiento desde Claude Code (paso 3):** demostrado desde Claude Code.
  En la consulta de IPC de Lima Metropolitana a 12 meses para `2025-12` a
  `2026-09`, Claude Code llamó al servidor `bcrp`, presentó las observaciones y
  el resumen calculado, y mostró el código de serie, el período y el enlace
  oficial del BCRP.

### Herramienta propia: `comparar_series`

Se agrego `comparar_series` como herramienta de analisis adicional. Recibe dos
codigos de serie y un intervalo, alinea las observaciones por periodos
coincidentes y calcula su correlacion en Python. Ambas series deben tener la
misma frecuencia y al menos dos periodos coincidentes. La respuesta incluye
los pares comparados, la cantidad de periodos, la correlacion y las fuentes
oficiales. La correlacion describe asociacion y no demuestra causalidad.

Desde Claude Code se puede solicitar, por ejemplo: «Compara las series
mensuales PN01273PM y [segundo codigo] entre 2020-01 y 2024-12 e informa la
correlacion, los periodos coincidentes y las fuentes».

## Estado verificado y evidencias

- **Pruebas automatizadas:** `uv run pytest -q` terminó con `10 passed`.
  La [salida de pytest](evidencias/parte-1/pruebas-automatizadas-10.txt) y la
  [captura de la ejecución](evidencias/parte-1/pruebas-automatizadas-10.png)
  están guardadas en el repositorio.
- **Integración MCP:** la [captura de Claude Code](evidencias/parte-1/integracion-claude-code-bcrp.png)
  documenta la consulta al servidor BCRP.
- **Skills ENAHO:** las tres Skills se integraron como copias independientes.
  Se ejecutó el flujo de limpieza, gráfico por área y mapa para 2024: la
  limpieza terminó con `VALIDACIÓN OK` (108,664 residentes), el gráfico
  informó 39.4 % de pobreza rural y 24.7 % urbana, y el mapa aprobó las
  comparaciones de los 25 departamentos con la referencia.
- Los microdatos y los resultados generados se excluyen de Git; se generan
  localmente al ejecutar los comandos de la Parte 2.
