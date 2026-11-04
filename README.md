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
- `tests/`: pruebas automatizadas.
- `data/`: datos de trabajo; no guardar credenciales ni datos descargados en Git.
- `outputs/`: graficos, resultados e informes generados.

El proyecto debe documentar las fuentes oficiales, los pasos de procesamiento y
los resultados para que el analisis pueda reproducirse.
