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
- `data/`: datos de trabajo; no guardar credenciales ni datos descargados en Git.
- `outputs/`: graficos, resultados e informes generados.

El proyecto debe documentar las fuentes oficiales, los pasos de procesamiento y
los resultados para que el analisis pueda reproducirse.

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
