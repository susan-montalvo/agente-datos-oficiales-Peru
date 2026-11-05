---
name: graficando-enaho
description: Grafica la pobreza de la ENAHO del INEI en barras, por área (urbano y rural), departamento, sexo o grupo de edad, y guarda un PNG en figuras/. Úsala cuando pidan un gráfico, una figura o una comparación visual de la pobreza o la pobreza extrema en el Perú.
argument-hint: [area|departamento|sexo|edad]
allowed-tools: Bash(uv run *)
---

# Graficar la ENAHO

1. Si no existe salidas/personas_2024.parquet, usa primero la skill limpiando-enaho.
2. Corre exactamente, desde la raíz del repo:
   `uv run ${CLAUDE_SKILL_DIR}/scripts/graficar.py --por <grupo> --anio 2024`
   donde <grupo> es area, departamento, sexo o edad, según el pedido (urbano y rural = area).
   Para pobreza extrema agrega `--indicador pobre_extremo`. No escribas otro script de gráficos.
3. Reglas que el script ya cumple y que no se cambian: ponderar con facpob07; barras desde cero
   y ordenadas; un solo color con el valor escrito en cada barra; título con qué y cuándo;
   nota «Fuente: INEI, ENAHO 2024»; PNG a 200 dpi.
4. Responde con las cifras que imprime el script y la ruta del PNG en figuras/.
5. Las cifras salen de la base de personas: urbano 24.7 % y rural 39.4 %. La sumaria da 24.8 % y 39.3 %.
