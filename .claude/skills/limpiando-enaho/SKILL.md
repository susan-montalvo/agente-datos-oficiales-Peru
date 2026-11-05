---
name: limpiando-enaho
description: Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO del INEI y arma una base de personas con pobreza y factor de expansión. Úsala cuando pidan limpiar, unir o analizar la ENAHO, o calcular pobreza por región, departamento, área, sexo o edad.
argument-hint: [año]
allowed-tools: Bash(uv run *)
---

# Limpiar la ENAHO

1. Si faltan los zip en datos/, pide al usuario bajarlos del INEI desde el navegador (código 966 = 2024):
   proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip y 966-Modulo02.zip
2. Corre exactamente, desde la raíz del repo: `uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio <año>`
   donde <año> es el año del pedido en cuatro dígitos; si no dice año, usa 2024.
   No escribas otro script de limpieza ni cambies filtros, llaves o factores.
3. Lee salidas/validacion.txt. Si dice VALIDACIÓN FALLIDA o la pobreza difiere del INEI en más de 0.1 puntos, detente y muestra el archivo.
4. Responde con salidas/personas_<año>.parquet. Toda cifra va ponderada con facpob07; pobre es `pobreza <= 2`, nunca un promedio del código.
5. Antes de usar una variable que no está en la base, lee [reference.md](reference.md).
