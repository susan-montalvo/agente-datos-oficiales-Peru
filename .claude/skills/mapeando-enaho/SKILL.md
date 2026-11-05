---
name: mapeando-enaho
description: Dibuja un mapa coroplético de la pobreza de la ENAHO del INEI por departamento del Perú y lo guarda en mapas/pobreza_departamento.png. Úsala cuando pidan un mapa, la distribución geográfica o la pobreza de los 25 departamentos.
argument-hint: [año]
allowed-tools: Bash(uv run *)
---

# Mapear la ENAHO

1. Si no existe salidas/personas_2024.parquet, usa primero la skill limpiando-enaho.
2. Si falta datos/peru_departamental_simple.geojson, bájalo de
   raw.githubusercontent.com/juaneladio/peru-geojson/master/peru_departamental_simple.geojson
3. Corre exactamente, desde la raíz del repo: `uv run ${CLAUDE_SKILL_DIR}/scripts/mapear.py --anio <año>`
   donde <año> es el año del pedido en cuatro dígitos; si no dice año, usa 2024.
   No escribas otro script de mapas.
4. Para 2024, el script compara por código los resultados con
   [referencias/pobreza_departamento_2024.csv](../../../referencias/pobreza_departamento_2024.csv),
   redondeados a un decimal. Comprueba los 25 códigos únicos y su cobertura entre ENAHO, GeoJSON
   y referencia. Si algún chequeo sale FALLA, detente y muestra la salida; no presentes ni generes
   un mapa con validaciones fallidas. El script une `ubigeo[:2]` con `FIRST_IDDP`, nunca por nombre;
   muestra los 25 departamentos, mantiene Lima (15) y Callao (07) separados, y usa una escala de un
   solo tono desde cero con leyenda «% de personas».
5. Responde con las cifras que imprime el script y la ruta del mapa. Se calculan como la sumaria
   (factor07 × mieperho): Cajamarca 45.0 %, Ica 6.0 %.
