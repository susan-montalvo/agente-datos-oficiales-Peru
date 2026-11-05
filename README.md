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
uv run pytest -q
uv run python mcp/server.py
```

Claude Code puede iniciar el servidor con la configuracion local de `.mcp.json`.
Sus herramientas `buscar_series`, `serie`, `resumen` y `comparar_series`
devuelven el codigo, el periodo y la fuente oficial. Las fechas aceptadas son
`YYYY-MM` (mensual), `YYYY-T1` (trimestral), `YYYY-MM-DD` (diaria) y `YYYY`
(anual).
