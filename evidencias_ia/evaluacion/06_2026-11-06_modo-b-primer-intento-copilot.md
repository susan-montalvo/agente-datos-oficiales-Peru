# Modo B: primer intento con GitHub Copilot (descartado)

- **Sesión:** `1de4297b` · GitHub Copilot (agente de VS Code)
- **Carpeta de trabajo inicial:** `~/Documents/GitHub/Modo B`
- **Modelo:** gpt-6-luna
- **Mensajes de la usuaria:** 1 a 2 de 2 de la sesión
- **Inicio:** 2026-11-06 09:22:39 · **Fin:** 2026-11-06 09:28:42 (hora de Lima)

> Exportación del registro local de GitHub Copilot. Se omiten las instrucciones de sistema, los hooks y los permisos; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-11-06 09:22:39

responde las 10 preguntas formuladas en el csv, utiliza el mcp y las skillas desarrolladas de la carpeta agente-datos-oficiales-Peru ubicada en carpeta git hub de mi computadora, escribe las respuesta en una columna a la derecha de las preguntas en el csv, documenta el procedimiento en un read me

## 🤖 Copilot · 2026-11-06 09:22:47

Voy a localizar el CSV y la carpeta de agente indicada, y revisar qué MCP está disponible para consultar fuentes oficiales.

**Herramienta `bash`** — Localiza el CSV y la carpeta de skills

```bash
pwd && ls -la && find .. -maxdepth 4 -type d -iname 'agente-datos-oficiales-Peru' -print
```

**Herramienta `tool_search_tool`** — MCP tools to query official Peruvian government data APIs, datasets, or web search via agente-datos-oficiales-Peru

```json
{
 "query": "MCP tools to query official Peruvian government data APIs, datasets, or web search via agente-datos-oficiales-Peru"
}
```

<details><summary>Resultado</summary>

```
["github-mcp-server-actions_get","github-mcp-server-get_copilot_space","github-mcp-server-search_repositories","github-mcp-server-search_code","github-mcp-server-search_issues"]
```

</details>

<details><summary>Resultado</summary>

```
~/Documents/GitHub/Modo B
total 8
drwxr-xr-x   3 susanmontalvo  staff    96 Nov  6 09:12 .
drwxr-xr-x@ 18 susanmontalvo  staff   576 Nov  6 09:10 ..
-rw-r--r--@  1 susanmontalvo  staff  1861 Nov  5 21:47 preguntas.csv
../agente-datos-oficiales-Peru
<shellId: 0 completed with exit code 0>
```

</details>

**Herramienta `view`** — view the file at ~/Documents/GitHub/Modo B/preguntas.csv.

```json
{
 "path": "~/Documents/GitHub/Modo B/preguntas.csv"
}
```

**Herramienta `bash`** — Inspecciona skills y configuración disponibles

```bash
find '~/Documents/GitHub/agente-datos-oficiales-Peru' -maxdepth 3 -type f -print
```

**Herramienta `bash`** — Revisa estructura del agente local

```bash
ls -la '~/Documents/GitHub/agente-datos-oficiales-Peru' && find '~/Documents/GitHub' -maxdepth 2 -type d -print
```

<details><summary>Resultado</summary>

```
pregunta_id,pregunta
P01,"Según la serie mensual PN01728AM del BCRP, ¿cuál fue la variación interanual del PBI en mayo de 2024?"
P02,"Según la serie mensual PN01273PM del BCRP, ¿cuál fue la variación porcentual de 12 meses del IPC de Lima Metropolitana (inflación interanual) en diciembre de 2024?"
P03,"Según la serie mensual PN01210PM del BCRP (tipo de cambio bancario promedio, S/ por US$), ¿cuál fue el promedio simple de los 12 meses de 2024?"
P04,"Según la serie mensual PD04722MM del BCRP, ¿en cuántos puntos porcentuales varió la tasa de referencia de la política monetaria entre enero de 2024 y diciembre de 2024?"
P05,"Según los microdatos de la ENAHO 2024 (Módulos 02 y 34), ¿qué porcentaje de las personas menores de 18 años (0 a 17 años) se encontraba en situación de pobreza monetaria?"
P06,"Según los microdatos de la ENAHO 2024 (Módulos 02 y 34), ¿qué porcentaje de los niños y niñas de 0 a 4 años se encontraba en situación de pobreza monetaria extrema?"
P07,"Según los microdatos de la ENAHO 2024 (Módulos 02 y 34), ¿qué porcentaje de las mujeres se encontraba en situación de pobreza monetaria?"
P08,"Según los microdatos de la ENAHO 2024 (Módulos 02 y 34), ¿cuántos puntos porcentuales más alta fue la pobreza monetaria de las personas de 0 a 17 años que la de las personas de 60 años a más?"
P09,"Combinando ENAHO y BCRP: si la pobreza monetaria pasó de 29.0 % (2023) a 27.6 % (2024), ¿cuál es el cociente entre esa variación (en puntos porcentuales) y el promedio simple de las variaciones interanuales mensuales del PBI de 2024 (serie PN01728AM)?"
P10,Combinando ENAHO y BCRP: ¿a cuántos dólares equivale la línea de pobreza monetaria promedio de 2024 (Módulo 34 de la ENAHO) usando el tipo de cambio bancario promedio de 2024 (promedio simple de los 12 meses de la serie PN01210PM)?

```

</details>

<details><summary>Resultado</summary>

```
Output too large to read at once (10.8 KB). Saved to: /var/folders/xq/9y7gptwn01s29w73bn8qj9c40000gn/T/1793974973951-copilot-tool-output-623-6adda11b-3685-4a2c-8849-c2f557b94c93.txt
Consider using tools like rg (for searching), head/tail (for viewing start/end), view with view_range (for specific sections), or jq (for JSON) to examine portions of the output.

Preview (first 500 chars):
~/Documents/GitHub/agente-datos-oficiales-Peru/datos/pbi_interanual_mensual_2024.csv
~/Documents/GitHub/agente-datos-oficiales-Peru/datos/966-Modulo34.zip
~/Documents/GitHub/agente-datos-oficiales-Peru/datos/966-Modulo02/enaho01-2024-200.dta
~/Documents/GitHub/agente-datos-oficiales-Peru/datos/966-Modulo34/sumaria-2024.dta
~/Documents/GitHub/agente-datos-oficiales-Peru/datos/peru_departamental_simple.g
<shellId: 1 completed with exit code 0>
```

</details>

<details><summary>Resultado</summary>

```
total 408
drwxr-xr-x@ 27 susanmontalvo  staff     864 Nov  5 19:59 .
drwxr-xr-x@ 18 susanmontalvo  staff     576 Nov  6 09:10 ..
-rw-r--r--@  1 susanmontalvo  staff    8196 Nov  6 09:16 .DS_Store
drwxr-xr-x@  4 susanmontalvo  staff     128 Nov  4 18:06 .claude
drwxr-xr-x@ 13 susanmontalvo  staff     416 Nov  5 20:52 .git
-rw-r--r--@  1 susanmontalvo  staff     155 Nov  4 18:07 .gitignore
-rw-r--r--@  1 susanmontalvo  staff     136 Nov  4 11:42 .mcp.json
drwxr-xr-x@  6 susanmontalvo  staff     192 Nov  4 13:50 .pytest_cache
-rw-r--r--@  1 susanmontalvo  staff       5 Nov  4 10:26 .python-version
drwxr-xr-x@  9 susanmontalvo  staff     288 Nov  4 10:58 .venv
-rw-r--r--@  1 susanmontalvo  staff    2306 Nov  5 18:26 PLAN_ANALISIS_PARTE_3.md
-rw-r--r--@  1 susanmontalvo  staff    8327 Nov  5 19:59 README.md
drwxr-xr-x@  8 susanmontalvo  staff     256 Nov  5 17:02 datos
drwxr-xr-x@  6 susanmontalvo  staff     192 Nov  6 09:11 evaluacion
drwxr-xr-x@  6 susanmontalvo  staff     192 Nov  5 17:51 evidencias
drwxr-xr-x@  3 susanmontalvo  staff      96 Nov  5 19:59 evidencias_ia
drwxr-xr-x@  7 susanmontalvo  staff     224 Nov  5 13:02 figuras
drwxr-xr-x@  3 susanmontalvo  staff      96 Nov  5 17:19 informes
drwxr-xr-x@  3 susanmontalvo  staff      96 Nov  4 18:07 mapas
drwxr-xr-x@  8 susanmontalvo  staff     256 Nov  6 09:16 mcp
drwxr-xr-x@  3 susanmontalvo  staff      96 Nov  5 17:02 outputs
-rw-r--r--@  1 susanmontalvo  staff     805 Nov  4 11:42 pyproject.toml
drwxr-xr-x@  3 susanmontalvo  staff      96 Nov  4 18:06 referencias
drwxr-xr-x@  4 susanmontalvo  staff     128 Nov  5 13:40 salidas
drwxr-xr-x@  3 susanmontalvo  staff      96 Nov  5 17:02 scripts
drwxr-xr-x@  4 susanmontalvo  staff     128 Nov  4 11:44 src
-rw-r--r--@  1 susanmontalvo  staff  163694 Nov  4 11:44 uv.lock
~/Documents/GitHub
~/Documents/GitHub/Registro oficial Cusco
~/Documents/GitHub/Registro oficial Cusco/PDF
~/Documents/GitHub/Incendios-en_Peru_reel
~/Documents/GitHub/Incendios-en_Peru_reel/.sox-runtime
~/Documents/GitHub/Incendios-en_Peru_reel/salidas
~/Documents/GitHub/Incendios-en_Peru_reel/__pycache__
~/Documents/GitHub/Incendios-en_Peru_reel/.venv
~/Documents/GitHub/Incendios-en_Peru_reel/.git
~/Documents/GitHub/Incendios-en-Peru
~/Documents/GitHub/Incendios-en-Peru/datos
~/Documents/GitHub/Incendios-en-Peru/.git
~/Documents/GitHub/produccion-editorial-peru
~/Documents/GitHub/produccion-editorial-peru/datos
~/Documents/GitHub/produccion-editorial-peru/.venv-reel
~/Documents/GitHub/produccion-editorial-peru/reel
~/Documents/GitHub/produccion-editorial-peru/web
~/Documents/GitHub/produccion-editorial-peru/docs
~/Documents/GitHub/produccion-editorial-peru/.venv
~/Documents/GitHub/produccion-editorial-peru/scripts
~/Documents/GitHub/produccion-editorial-peru/.git
~/Documents/GitHub/whatsapp-mcp
~/Documents/GitHub/whatsapp-mcp/whatsapp-bridge
~/Documents/GitHub/whatsapp-mcp/.git
~/Documents/GitHub/whatsapp-mcp/whatsapp-mcp-server
~/Documents/GitHub/Diplomado-Su-2026
~/Documents/GitHub/Diplomado-Su-2026/tarea_1
~/Documents/GitHub/Diplomado-Su-2026/.pytest_cache
~/Documents/GitHub/Diplomado-Su-2026/.claude
~/Documents/GitHub/Diplomado-Su-2026/tarea_2
~/Documents/GitHub/Diplomado-Su-2026/.git
~/Documents/GitHub/skills-enaho
~/Documents/GitHub/skills-enaho/datos
~/Documents/GitHub/skills-enaho/salidas
~/Document
… [salida recortada: 3,754 caracteres más]
```

</details>

**Herramienta `bash`** — Lista skills y código MCP relevantes

```bash
find '~/Documents/GitHub/agente-datos-oficiales-Peru/.claude' '~/Documents/GitHub/agente-datos-oficiales-Peru/mcp' '~/Documents/GitHub/agente-datos-oficiales-Peru/src' '~/Documents/GitHub/agente-datos-oficiales-Peru/scripts' -type f -print
```

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/.mcp.json.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/.mcp.json"
}
```

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/README.md.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/README.md",
 "view_range": [
  1,
  180
 ]
}
```

**Herramienta `bash`** — Identifica microdatos y series disponibles

```bash
find '~/Documents/GitHub/agente-datos-oficiales-Peru/datos' -maxdepth 3 -type f -print
```

<details><summary>Resultado</summary>

```
~/Documents/GitHub/agente-datos-oficiales-Peru/datos/pbi_interanual_mensual_2024.csv
~/Documents/GitHub/agente-datos-oficiales-Peru/datos/966-Modulo34.zip
~/Documents/GitHub/agente-datos-oficiales-Peru/datos/966-Modulo02/enaho01-2024-200.dta
~/Documents/GitHub/agente-datos-oficiales-Peru/datos/966-Modulo34/sumaria-2024.dta
~/Documents/GitHub/agente-datos-oficiales-Peru/datos/peru_departamental_simple.geojson
~/Documents/GitHub/agente-datos-oficiales-Peru/datos/966-Modulo02.zip
<shellId: 3 completed with exit code 0>
```

</details>

<details><summary>Resultado</summary>

```
~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/settings.local.json
~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/mapeando-enaho/scripts/mapear.py
~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/mapeando-enaho/SKILL.md
~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/graficando-enaho/scripts/graficar.py
~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/graficando-enaho/SKILL.md
~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/limpiando-enaho/reference.md
~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/limpiando-enaho/scripts/limpiar.py
~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/limpiando-enaho/SKILL.md
~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/test_comparar_series.py
~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/server.py
~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/.DS_Store
~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/__pycache__/test_server.cpython-312-pytest-9.2.0.pyc
~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/__pycache__/server.cpython-312.pyc
~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/__pycache__/test_comparar_series.cpython-312-pytest-9.2.0.pyc
~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/test_server.py
~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/data/catalogo_bcrp.csv
~/Documents/GitHub/agente-datos-oficiales-Peru/src/agente_datos_oficiales_peru/__init__.py
~/Documents/GitHub/agente-datos-oficiales-Peru/src/agente_datos_oficiales_peru/__pycache__/__init__.cpython-312.pyc
~/Documents/GitHub/agente-datos-oficiales-Peru/src/agente_datos_oficiales_peru.egg-info/PKG-INFO
~/Documents/GitHub/agente-datos-oficiales-Peru/src/agente_datos_oficiales_peru.egg-info/SOURCES.txt
~/Documents/GitHub/agente-datos-oficiales-Peru/src/agente_datos_oficiales_peru.egg-info/requires.txt
~/Documents/GitHub/agente-datos-oficiales-Peru/src/agente_datos_oficiales_peru.egg-info/top_level.txt
~/Documents/GitHub/agente-datos-oficiales-Peru/src/agente_datos_oficiales_peru.egg-info/dependency_links.txt
~/Documents/GitHub/agente-datos-oficiales-Peru/scripts/parte3_analisis.py
<shellId: 4 completed with exit code 0>
```

</details>

<details><summary>Resultado</summary>

```
{
  "mcpServers": {
    "bcrp": {
      "command": "uv",
      "args": ["run", "--project", ".", "python", "mcp/server.py"]
    }
  }
}

```

</details>

<details><summary>Resultado</summary>

```
# Agente de datos oficiales del Peru

Proyecto de la Tarea 4: un agente de investigacion socioeconomica que combina
series del BCRP, microdatos ENAHO del INEI, herramientas MCP y analisis
reproducible.

## Preparar el entorno

Requiere Python 3.12 y [uv](https://docs.astral.sh/uv/).

'''bash
uv sync --group dev
uv run pytest
'''

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

Los ZIP de microdatos ENAHO deben descargarse del [INEI, módulo 34](https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip)
y [módulo 02](https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip)
(código INEI 966 para 2024) y guardarse en `datos/`. No se versionan. El GeoJSON
departamental y la referencia de pobreza 2024 están incluidos en `datos/` y
`referencias/`. Para procesar, graficar y mapear:

'''bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area --anio 2024
uv run .claude/skills/mapeando-enaho/scripts/mapear.py --anio 2024
'''

La limpieza debe pasar la validación antes de usar la base en los otros pasos.
Los productos se guardan en `salidas/`, `figuras/` y `mapas/`.

### Evidencias de `graficando-enaho`

La [transcripción de Claude Code](evidencias/parte-2/graficando-enaho/activacion-lenguaje-natural-2024.txt)
registra la solicitud en lenguaje natural, la activación de la Skill y la
ejecución del gráfico por área (39.4 % rural y 24.7 % urbana). Las salidas de
consola para departamento, sexo y edad están en
[ejecuciones-complementarias-2024.txt](evidencias/parte-2/graficando-enaho/ejecuciones-complementarias-2024.txt).
Los PNG verificables están versionados en
[figuras de evidencia](evidencias/parte-2/graficando-enaho/figuras/): área,
sexo, edad y departamento. No se incluyen los microdatos; para reproducir el
flujo completo, descárgalos de los enlaces oficiales indicados arriba.

### Invocación individual y coordinación de las tres Skills

Las [evidencias de coordinación](evidencias/parte-2/coordinacion-skills-2024/)
registran tres sesiones nuevas de Claude Code en lenguaje natural:

- [Limpieza individual](evidencias/parte-2/coordinacion-skills-2024/limpiando-individual.txt):
  se activó `limpiando-enaho` y terminó con `VALIDACIÓN OK`.
- [Gráfico sin base procesada](evidencias/parte-2/coordinacion-skills-2024/graficando-sin-base.txt):
  se activó `graficando-enaho`, luego `limpiando-enaho`, y finalmente se generó
  el gráfico por área.
- [Mapa sin base procesada](evidencias/parte-2/coordinacion-skills-2024/mapeando-sin-base.txt):
  se activó `mapeando-enaho`, luego `limpiando-enaho`, y se generó el mapa tras
  aprobar las 25 comparaciones con la referencia.

Las figuras de esas dos cadenas están en
[figuras de coordinación](evidencias/parte-2/coordinacion-skills-2024/figuras/).
Para ambas pruebas se apartó temporalmente el Parquet preexistente y se restauró
byte por byte al concluir. Los microdatos no s
… [salida recortada: 4,283 caracteres más]
```

</details>

## 🤖 Copilot · 2026-11-06 09:23:27

El CSV contiene 10 consultas de BCRP y ENAHO, y la carpeta indicada incluye servidor MCP local, microdatos y skills de procesamiento. Revisaré sus instrucciones y definiciones antes de calcular y registrar las respuestas.

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/server.py.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/server.py"
}
```

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/limpiando-enaho/SKILL.md.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/limpiando-enaho/SKILL.md"
}
```

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/limpiando-enaho/reference.md.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/limpiando-enaho/reference.md"
}
```

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/graficando-enaho/SKILL.md.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/graficando-enaho/SKILL.md"
}
```

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/mapeando-enaho/SKILL.md.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/mapeando-enaho/SKILL.md"
}
```

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/limpiando-enaho/scripts/limpiar.py.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/limpiando-enaho/scripts/limpiar.py"
}
```

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/test_server.py.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/test_server.py"
}
```

<details><summary>Resultado</summary>

```
File too large to read at once (13.7 KB). Consider using the grep tool to search within the file, or view with view_range to read specific sections.
```

</details>

<details><summary>Resultado</summary>

```
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

```

</details>

<details><summary>Resultado</summary>

```
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

```

</details>

<details><summary>Resultado</summary>

```
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

```

</details>

<details><summary>Resultado</summary>

```
# ENAHO · referencia

## Base salidas/personas_<año>.parquet

Una fila por residente habitual (108,664 en 2024).

| Variable | Qué es |
|---|---|
| conglome, vivienda, hogar, codperso | Llaves, como texto (conservan los ceros) |
| p203 | Parentesco con el jefe de hogar (1 = jefe) |
| p207 | Sexo: 1 hombre, 2 mujer |
| p208a | Edad en años |
| facpob07 | Factor de expansión de personas |
| ubigeo | Seis dígitos, texto |
| departamento | `ubigeo[:2]`; Lima es 15 y Callao 07 |
| estrato, dominio | Del marco muestral; urbano = estrato ≤ 5 |
| pobreza | 1 extremo, 2 no extremo, 3 no pobre |
| pobre, pobre_extremo | `pobreza <= 2` y `pobreza == 1` |
| mieperho, factor07 | Miembros del hogar y factor de hogares |

## Seis trampas

1. Ceros a la izquierda: conglome «015009», ubigeo «010101». Nunca convertir llaves a número.
2. Nombres rotos: el año llega como «aÑo»; el script lo normaliza a `anio`.
3. No todos son residentes: el módulo 200 trae 117,721 filas; residentes habituales, 108,664.
4. Uniones que duplican: siempre `validate="m:1"` al unir personas con hogares.
5. Encuestas no son personas: toda cifra se pondera (facpob07 en personas; factor07 × mieperho en la sumaria).
6. Códigos, no números: pobreza es categoría; pobre es `pobreza <= 2`.

## Cifras de referencia 2024

- Pobreza: 27.6 % (INEI); sumaria 27.58 %, personas 27.53 %. Extrema: 5.5 %.
- Cusco 18.5 %. Urbano 24.8 %, rural 39.3 % con la sumaria (24.7 % y 39.4 % con la base de personas y facpob07).
- Más pobres: Cajamarca 45.0 %, Loreto 43.0 %, Puno 39.9 %. Menos: Ica 6.0 %, Moquegua 11.0 %, Madre de Dios 11.1 %.

## Otras variables

Para variables fuera de la base, revisar el diccionario en datos/966-Modulo34/Diccionario2024.pdf
(o Modulo02) y agregarlas en `limpiar.py`, no en una limpieza aparte.

```

</details>

<details><summary>Resultado</summary>

```
"""Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO y arma una base de personas.

Uso: uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
"""

import argparse
import sys
import unicodedata
import zipfile
from pathlib import Path

import pandas as pd

LLAVES = ["conglome", "vivienda", "hogar"]
LLAVES_PERSONA = LLAVES + ["codperso"]
CODIGO_INEI = {2024: 966}  # código de la ENAHO en el portal de microdatos
POBREZA_INEI = {2024: 27.6}  # pobreza monetaria oficial, en %

RAIZ = Path.cwd()
DATOS = RAIZ / "datos"
SALIDAS = RAIZ / "salidas"


def normalizar(nombre: str) -> str:
    """Pasa a minúsculas y quita tildes: «aÑo» se vuelve «anio»."""
    nombre = nombre.lower().replace("ñ", "ni")
    return unicodedata.normalize("NFKD", nombre).encode("ascii", "ignore").decode()


def leer(codigo: int, modulo: str, archivo: str) -> pd.DataFrame:
    """1 · Leer: extrae el .dta del zip si hace falta y lo lee con códigos, no etiquetas."""
    carpeta = DATOS / f"{codigo}-Modulo{modulo}"
    ruta = carpeta / archivo
    if not ruta.exists():
        zip_ = DATOS / f"{codigo}-Modulo{modulo}.zip"
        if not zip_.exists():
            sys.exit(f"Falta {zip_}. Bájalo de proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/{zip_.name}")
        with zipfile.ZipFile(zip_) as z:
            z.extract(f"{carpeta.name}/{archivo}", DATOS)
    df = pd.read_stata(ruta, convert_categoricals=False)
    # 2 · Normalizar nombres
    df.columns = [normalizar(c) for c in df.columns]
    for c in LLAVES_PERSONA + ["ubigeo"]:
        if c in df.columns:
            df[c] = df[c].astype("string")
    return df


def ponderada(serie: pd.Series, peso: pd.Series) -> float:
    return 100 * (serie * peso).sum() / peso.sum()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--anio", type=int, default=2024)
    anio = parser.parse_args().anio
    if anio not in CODIGO_INEI:
        sys.exit(f"Año {anio} sin código INEI conocido. Agrégalo en CODIGO_INEI.")
    codigo = CODIGO_INEI[anio]

    sumaria = leer(codigo, "34", f"sumaria-{anio}.dta")
    miembros = leer(codigo, "02", f"enaho01-{anio}-200.dta")

    # 3 · Filtrar residentes habituales (definición del INEI)
    residente = ((miembros.p204 == 1) & (miembros.p205 == 2)) | ((miembros.p204 == 2) & (miembros.p206 == 1))
    personas = miembros.loc[residente, LLAVES_PERSONA + ["p203", "p207", "p208a", "facpob07"]]

    # 4 · Unir cada persona con su hogar
    columnas_hogar = LLAVES + ["ubigeo", "estrato", "dominio", "pobreza", "mieperho", "factor07"]
    base = personas.merge(sumaria[columnas_hogar], on=LLAVES, how="left", validate="m:1")

    # 5 · Construir variables
    base["departamento"] = base.ubigeo.str[:2]
    base["urbano"] = base.estrato <= 5
    base["pobre"] = base.pobreza <= 2
    base["pobre_extremo"] = base.pobreza == 1
    base["anio"] = anio

    # 6 · Validar
    pob_hogares = ponderada(sumaria.pobreza <= 2, sumaria.factor07 * sumaria.mieperho)
    ext_hogares = ponderada(sumaria.pobreza == 1, sumaria.factor07 * sumaria.mieperho)
    pob_personas = ponderada(base.pobre, base.facpob07)
    oficial = POBREZA_INEI.get(anio)
    chequeos = {
        "llaves de hogar únicas en la sumaria": not sumaria.duplicated(LLAVES).any(),
        "llaves de persona únicas": not personas.duplicated(LLAVES_PERSONA).any(),
        "la unión no perdió ni duplicó filas": len(base) == len(personas),
        "toda persona tiene hogar en la sumaria": base.pobreza.notna().all(),
        "ubigeo con 6 dígitos": base.ubigeo.str.len().eq(6).all(),
    }
    if oficial is not None:
        chequeos[f"pobreza difiere del INEI ({oficial} %) en menos de 0.1 puntos"] = abs(pob_hogares - oficial) < 0.1

    # 7 · Guardar
    SALIDAS.mkdir(exist_ok=True)
    base.to_parquet(SALIDAS / f"personas_{anio}.parquet", index=False)
    lineas = [
        f"ENAHO {anio} · validación",
        f"Hogares en la sumaria: {len(sumaria):,}",
        f"Filas en el módulo 200: {len(mi
… [salida recortada: 809 caracteres más]
```

</details>

<details><summary>Resultado</summary>

```
"""El contrato del servidor: si estas pruebas pasan, Claude Code y evaluar.py pueden usarlo.

    uv run pytest -q

Llaman al servidor en memoria, igual que lo haría Claude Code, y piden datos reales al BCRP.
"""
import asyncio

import pytest
from fastmcp import Client
from fastmcp.exceptions import ToolError

from server import mcp


async def _con_cliente(f):
    async with Client(mcp) as c:
        return await f(c)


def llamar(herramienta, **args):
    return asyncio.run(_con_cliente(lambda c: c.call_tool(herramienta, args))).data


def test_buscar_encuentra_el_ipc():
    r = llamar("buscar_series", texto="ipc 12 meses", limite=5)
    assert "PN01273PM" in [x["codigo"] for x in r]
    assert {"codigo", "nombre", "frecuencia"} <= r[0].keys()


def test_cuatro_herramientas_como_minimo():
    nombres = {t.name for t in asyncio.run(_con_cliente(lambda c: c.list_tools()))}
    assert {"buscar_series", "serie", "resumen"} <= nombres
    assert len(nombres) >= 4, "falta su herramienta propia"


def test_serie_mensual():
    r = llamar("serie", codigo="PN01271PM", desde="2025-01", hasta="2025-12")
    assert len(r["datos"]) == 12
    assert r["datos"][0]["periodo"] == "2025-01"
    assert r["datos"][2]["valor"] == pytest.approx(0.81, abs=0.01)   # IPC de Lima, marzo de 2025
    assert r["fuente"].startswith("https://estadisticas.bcrp.gob.pe")


def test_serie_diaria():
    r = llamar("serie", codigo="PD04638PD", desde="2026-10-01", hasta="2026-10-15")
    assert r["datos"][0]["periodo"] == "2026-10-01"
    assert r["datos"][-1] == {"periodo": "2026-10-15", "valor": pytest.approx(3.428, abs=0.001)}


def test_resumen_sin_cuentas_a_mano():
    r = llamar("resumen", codigo="PN01273PM", desde="2025-12", hasta="2026-09")
    assert r["primero"]["valor"] == pytest.approx(1.51, abs=0.01)
    assert r["ultimo"]["valor"] == pytest.approx(4.55, abs=0.01)
    assert r["maximo"]["periodo"] == "2026-09"
    assert {"cambio", "variacion_pct", "promedio", "minimo"} <= r.keys()


def test_codigo_inexistente_da_un_error_claro():
    with pytest.raises(ToolError, match="XX999"):
        llamar("serie", codigo="XX999", desde="2025-01", hasta="2025-02")


def test_un_recurso():
    async def contar(c):
        return len(await c.list_resources()) + len(await c.list_resource_templates())
    assert asyncio.run(_con_cliente(contar)) >= 1


def test_un_prompt():
    assert len(asyncio.run(_con_cliente(lambda c: c.list_prompts()))) >= 1

```

</details>

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/server.py.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/server.py",
 "view_range": [
  1,
  220
 ]
}
```

**Herramienta `bash`** — Comprueba resultados preexistentes de la skill

```bash
for f in 'salidas/personas_2024.parquet' 'salidas/validacion.txt'; do if [ -e "~/Documents/GitHub/agente-datos-oficiales-Peru/$f" ]; then ls -l "~/Documents/GitHub/agente-datos-oficiales-Peru/$f"; else printf 'MISSING %s\n' "$f"; fi; done
```

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/graficando-enaho/scripts/graficar.py.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/.claude/skills/graficando-enaho/scripts/graficar.py"
}
```

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/pyproject.toml.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/pyproject.toml"
}
```

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/datos/pbi_interanual_mensual_2024.csv.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/datos/pbi_interanual_mensual_2024.csv"
}
```

<details><summary>Resultado</summary>

```
"""MCP server for official Banco Central de Reserva del Peru time series."""

from __future__ import annotations

import re
import time
import unicodedata
from functools import lru_cache
from pathlib import Path
from typing import Any

import httpx
import pandas as pd
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError

CATALOG_URL = "https://estadisticas.bcrp.gob.pe/estadisticas/series/metadata"
API_URL = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"
CATALOG_PATH = Path(__file__).parent / "data" / "catalogo_bcrp.csv"
READ_ONLY = {"readOnlyHint": True, "openWorldHint": True}

mcp = FastMCP(
    "bcrp",
    instructions=(
        "Consulta series oficiales del BCRP. Busca primero el codigo con "
        "buscar_series, usa serie para observaciones y resumen para estadisticas. "
        "Cita siempre el codigo, el periodo y el enlace oficial; no estimes cifras."
    ),
)

_COLUMN_NAMES = {
    "Código de serie": "codigo",
    "Categoría de serie": "categoria",
    "Grupo de serie": "grupo",
    "Nombre de serie": "nombre",
    "Frecuencia": "frecuencia",
    "Fecha de actualización": "actualizada",
    "Fecha de inicio": "inicio",
}


def _sin_tildes(texto: str) -> str:
    normalizado = unicodedata.normalize("NFD", texto.casefold())
    return "".join(caracter for caracter in normalizado if unicodedata.category(caracter) != "Mn")


@lru_cache(maxsize=1)
def _catalogo() -> pd.DataFrame:
    """Load the official series catalog, downloading and caching it on first use."""
    try:
        if not CATALOG_PATH.exists():
            CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
            respuesta = httpx.get(CATALOG_URL, timeout=120)
            respuesta.raise_for_status()
            CATALOG_PATH.write_bytes(respuesta.content)
        catalogo = pd.read_csv(CATALOG_PATH, sep=";", encoding="latin-1", dtype=str).fillna("")
    except (httpx.HTTPError, OSError, pd.errors.ParserError, UnicodeError) as exc:
        raise ToolError(f"No se pudo cargar el catalogo oficial del BCRP: {exc}") from exc

    columnas_faltantes = set(_COLUMN_NAMES).difference(catalogo.columns)
    if columnas_faltantes:
        raise ToolError(
            "El catalogo del BCRP no contiene las columnas esperadas: "
            + ", ".join(sorted(columnas_faltantes))
        )

    catalogo = catalogo.rename(columns=_COLUMN_NAMES)
    catalogo["texto_busqueda"] = (
        catalogo["categoria"] + " " + catalogo["grupo"] + " " + catalogo["nombre"]
    ).map(_sin_tildes)
    return catalogo


def _ficha(codigo: str) -> dict[str, str]:
    filas = _catalogo()
    coincidencias = filas.loc[filas["codigo"] == codigo]
    if coincidencias.empty:
        raise ToolError(f"No existe el codigo de serie {codigo!r}. Buscalo con buscar_series.")

    fila = coincidencias.iloc[0]
    return {
        "codigo": fila["codigo"],
        "nombre": f"{fila['grupo']} - {fila['nombre']}",
        "categoria": fila["categoria"],
        "frecuencia": fila["frecuencia"],
        "inicio": fila["inicio"],
        "actualizada": fila["actualizada"],
    }


@mcp.tool(annotations=READ_ONLY)
def buscar_series(texto: str, frecuencia: str | None = None, limite: int = 10) -> list[dict[str, str]]:
    """Busca series BCRP por palabras clave, categoria, grupo o frecuencia.

    Todas las palabras de texto deben aparecer en los metadatos de la serie.
    Ejemplos: "ipc 12 meses", "tipo de cambio venta" o "reservas internacionales".
    """
    if not texto.strip():
        raise ToolError("El texto de busqueda no puede estar vacio.")
    if not 1 <= limite <= 50:
        raise ToolError("El limite debe ser un entero entre 1 y 50.")

    catalogo = _catalogo()
    coincidencias = pd.Series(True, index=catalogo.index)
    for palabra in _sin_tildes(texto).split():
        coincidencias &= catalogo["texto_busqueda"].str.contains(re.escape(palabra), na=False)
    if frecuencia:
        coincidencias &= catalogo["frecuencia"].str.casefold() == frecuencia.ca
… [salida recortada: 4,155 caracteres más]
```

</details>

<details><summary>Resultado</summary>

```
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "agente-datos-oficiales-peru"
version = "0.1.0"
description = "Agente de investigacion socioeconomica con datos oficiales del Peru"
readme = "README.md"
requires-python = ">=3.12,<3.13"
dependencies = [
    "fastmcp>=2,<4",
    "geopandas>=1.0",
    "httpx>=0.27",
    "matplotlib>=3.8",
    "numpy>=1.26,<3",
    "pandas>=2.2,<3",
    "plotly>=5.24",
    "pyarrow>=18",
    "pyproj>=3.6,<3.8",
    "pyreadstat>=1.3.6",
    "python-dotenv>=1.0",
    "requests>=2.32",
]

[dependency-groups]
dev = ["pytest>=8"]

[tool.setuptools.packages.find]
where = ["src"]

[tool.uv]
# cryptography 49+ no ofrece wheels para macOS Intel y requiere OpenSSL al compilar.
constraint-dependencies = ["cryptography<49"]

```

</details>

<details><summary>Resultado</summary>

```
periodo,variacion_interanual_pct
2024-01,1.83097461976354
2024-02,3.16241000807473
2024-03,-0.409690120959002
2024-04,5.52986981371346
2024-05,5.70691310837814
2024-06,0.370585322038706
2024-07,4.85868197288225
2024-08,3.97028100948149
2024-09,3.49053235679599
2024-10,3.83110341773776
2024-11,4.38200682962149
2024-12,5.06622215564914

```

</details>

<details><summary>Resultado</summary>

```
"""Grafica la pobreza de la ENAHO por grupo, desde la base de personas de limpiando-enaho.

Uso: uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area --anio 2024
"""

import argparse
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path.cwd()
SALIDAS = RAIZ / "salidas"
FIGURAS = RAIZ / "figuras"

COLOR = "#2a78d6"  # un solo color para todas las barras
TINTA = "#0b0b0b"
TINTA_SECUNDARIA = "#52514e"

DEPARTAMENTOS = {
    "01": "Amazonas", "02": "Áncash", "03": "Apurímac", "04": "Arequipa", "05": "Ayacucho",
    "06": "Cajamarca", "07": "Callao", "08": "Cusco", "09": "Huancavelica", "10": "Huánuco",
    "11": "Ica", "12": "Junín", "13": "La Libertad", "14": "Lambayeque", "15": "Lima",
    "16": "Loreto", "17": "Madre de Dios", "18": "Moquegua", "19": "Pasco", "20": "Piura",
    "21": "Puno", "22": "San Martín", "23": "Tacna", "24": "Tumbes", "25": "Ucayali",
}
EDADES = [0, 18, 30, 45, 60, 200]
GRUPOS_EDAD = ["0–17", "18–29", "30–44", "45–59", "60 y más"]

INDICADORES = {"pobre": "Pobreza monetaria", "pobre_extremo": "Pobreza extrema"}
NOMBRE_GRUPO = {"area": "área", "departamento": "departamento", "sexo": "sexo", "edad": "grupo de edad"}


def agrupar(base: pd.DataFrame, por: str) -> pd.Series:
    """Devuelve la etiqueta de grupo de cada persona."""
    if por == "area":
        return base.urbano.map({True: "Urbano", False: "Rural"})
    if por == "departamento":
        return base.departamento.map(DEPARTAMENTOS)
    if por == "sexo":
        return base.p207.map({1: "Hombre", 2: "Mujer"})
    return pd.cut(base.p208a, EDADES, right=False, labels=GRUPOS_EDAD).astype("string")


def ponderar(base: pd.DataFrame, grupo: pd.Series, indicador: str) -> pd.Series:
    """% de personas con el indicador, ponderado con facpob07."""
    peso = base.facpob07
    con = (base[indicador] * peso).groupby(grupo).sum()
    return (100 * con / peso.groupby(grupo).sum()).sort_values()


def graficar(valores: pd.Series, titulo: str, anio: int, ruta: Path) -> None:
    alto = 1.2 + 0.32 * len(valores)
    fig, ax = plt.subplots(figsize=(7, max(alto, 2.6)))
    barras = ax.barh(valores.index, valores.values, color=COLOR, height=0.7)
    ax.bar_label(barras, labels=[f"{v:.1f} %" for v in valores], padding=4, color=TINTA, fontsize=9)

    ax.set_xlim(0, valores.max() * 1.15)  # barras desde cero, con aire para el valor
    ax.margins(y=0.02)
    ax.set_xticks([])
    ax.tick_params(axis="y", length=0, labelcolor=TINTA, labelsize=10)
    for lado in ["top", "right", "bottom"]:
        ax.spines[lado].set_visible(False)
    ax.spines["left"].set_color(TINTA_SECUNDARIA)

    fig.suptitle(titulo, x=0.02, ha="left", fontsize=12, fontweight="bold", color=TINTA)
    ax.set_title("% de personas", loc="left", fontsize=9, color=TINTA_SECUNDARIA)
    fig.text(0.02, 0.01, f"Fuente: INEI, ENAHO {anio}", fontsize=8, color=TINTA_SECUNDARIA)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(ruta, dpi=200, facecolor="white")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--por", choices=list(NOMBRE_GRUPO), required=True)
    parser.add_argument("--indicador", choices=list(INDICADORES), default="pobre")
    parser.add_argument("--anio", type=int, default=2024)
    args = parser.parse_args()

    archivo = SALIDAS / f"personas_{args.anio}.parquet"
    if not archivo.exists():
        sys.exit(f"Falta {archivo}. Usa primero la skill limpiando-enaho.")
    base = pd.read_parquet(archivo)

    grupo = agrupar(base, args.por)
    if grupo.isna().any():
        sys.exit(f"{grupo.isna().sum()} personas sin grupo de {args.por}; revisa la base.")
    valores = ponderar(base, grupo, args.indicador)

    titulo = f"{INDICADORES[args.indicador]} por {NOMBRE_GRUPO[args.por]}, Perú {args.anio}"
    FIGURAS.mkdir(exist_ok=True)
    ruta = FIGURAS / f"{args.indicador.replace('pobre', 'pobreza')}_{args.por}_{args.
… [salida recortada: 324 caracteres más]
```

</details>

<details><summary>Resultado</summary>

```
-rw-r--r--@ 1 susanmontalvo  staff  481480 Nov  5 17:00 ~/Documents/GitHub/agente-datos-oficiales-Peru/salidas/personas_2024.parquet
-rw-r--r--@ 1 susanmontalvo  staff  549 Nov  5 17:00 ~/Documents/GitHub/agente-datos-oficiales-Peru/salidas/validacion.txt
<shellId: 5 completed with exit code 0>
```

</details>

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/server.py.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/mcp/server.py",
 "view_range": [
  221,
  420
 ]
}
```

**Herramienta `view`** — view the file at ~/Documents/GitHub/agente-datos-oficiales-Peru/salidas/validacion.txt.

```json
{
 "path": "~/Documents/GitHub/agente-datos-oficiales-Peru/salidas/validacion.txt"
}
```

**Herramienta `bash`** — Localiza referencias y salidas de evaluación relacionadas

```bash
find '~/Documents/GitHub/agente-datos-oficiales-Peru/referencias' -maxdepth 2 -type f -print && find '~/Documents/GitHub/agente-datos-oficiales-Peru/evaluacion' -maxdepth 2 -type f -print
```

<details><summary>Resultado</summary>

```
            raise ToolError(f"El BCRP respondio HTTP {status} al consultar {codigo}.") from exc
        except httpx.RequestError as exc:
            if intento < 2:
                time.sleep(2 * (intento + 1))
                continue
            raise ToolError(f"No se pudo consultar la API del BCRP: {exc}") from exc
        except ValueError as exc:
            if intento < 2:
                time.sleep(2 * (intento + 1))
                continue
            raise ToolError("El BCRP no devolvio JSON valido despues de tres intentos.") from exc

        periodos = payload.get("periods")
        if not isinstance(periodos, list):
            raise ToolError(f"La respuesta del BCRP no contiene periodos para {codigo}.")

        datos: list[dict[str, Any]] = []
        for periodo in periodos:
            valores = periodo.get("values", [])
            valor = valores[0] if valores else None
            if valor is None or str(valor).strip().casefold() in {"", "n.d.", "n.d", "nd"}:
                continue
            try:
                numero = float(str(valor).replace(",", "."))
            except ValueError as exc:
                raise ToolError(
                    f"El BCRP devolvio un valor no numerico para "
                    f"{periodo.get('name')!r}: {valor!r}."
                ) from exc
            datos.append({"periodo": _periodo_api(periodo["name"], frecuencia), "valor": numero})
        return tuple(datos)

    raise ToolError(f"No se pudieron descargar los datos de la serie {codigo}.")


@mcp.tool(annotations=READ_ONLY)
def serie(codigo: str, desde: str, hasta: str) -> dict[str, Any]:
    """Consulta observaciones BCRP en un intervalo inclusivo y devuelve la fuente reproducible.

    Usa YYYY-MM para series mensuales, YYYY-T1 para trimestrales, YYYY-MM-DD para
    diarias y YYYY para anuales.
    """
    ficha = _ficha(codigo)
    inicio = _fecha_api(desde, ficha["frecuencia"])
    fin = _fecha_api(hasta, ficha["frecuencia"])
    if _clave_fecha_api(inicio, ficha["frecuencia"]) > _clave_fecha_api(
        fin, ficha["frecuencia"]
    ):
        raise ToolError(f"El inicio {desde!r} debe ser anterior o igual al final {hasta!r}.")

    datos = _descargar(codigo, inicio, fin, ficha["frecuencia"])
    return {
        "codigo": ficha["codigo"],
        "nombre": ficha["nombre"],
        "frecuencia": ficha["frecuencia"],
        "datos": list(datos),
        "fuente": f"{API_URL}/{codigo}/json/{inicio}/{fin}",
    }


@mcp.tool(annotations=READ_ONLY)
def resumen(codigo: str, desde: str, hasta: str) -> dict[str, Any]:
    """Calcula extremos, cambio, variacion porcentual y promedio de una serie BCRP."""
    resultado = serie(codigo, desde, hasta)
    datos = resultado["datos"]
    if not datos:
        raise ToolError(f"No hay observaciones para {codigo} entre {desde} y {hasta}.")

    primero, ultimo = datos[0], datos[-1]
    cambio = ultimo["valor"] - primero["valor"]
    variacion = cambio / primero["valor"] * 100 if primero["valor"] else None
    return {
        "codigo": codigo,
        "nombre": resultado["nombre"],
        "frecuencia": resultado["frecuencia"],
        "periodo": {"desde": primero["periodo"], "hasta": ultimo["periodo"]},
        "primero": primero,
        "ultimo": ultimo,
        "cambio": cambio,
        "variacion_pct": variacion,
        "promedio": sum(punto["valor"] for punto in datos) / len(datos),
        "maximo": max(datos, key=lambda punto: punto["valor"]),
        "minimo": min(datos, key=lambda punto: punto["valor"]),
        "fuente": resultado["fuente"],
    }


@mcp.tool(annotations=READ_ONLY)
def comparar_series(codigo_a: str, codigo_b: str, desde: str, hasta: str) -> dict[str, Any]:
    """Alinea dos series BCRP por periodo y calcula su correlacion en observaciones coincidentes.

    Ambas series deben tener la misma frecuencia. La correlacion describe asociacion y
    no implica causalidad.
    """
    serie_a = serie(codigo_a, desde, hasta)
    serie_b = serie(codigo
… [salida recortada: 1,823 caracteres más]
```

</details>

<details><summary>Resultado</summary>

```
ENAHO 2024 · validación
Hogares en la sumaria: 33,691
Filas en el módulo 200: 117,721
Residentes habituales en la base: 108,664
Pobreza (sumaria, factor07 × mieperho): 27.58 %
Pobreza extrema (sumaria): 5.50 %
Pobreza (personas, facpob07): 27.53 %
Pobreza oficial INEI: 27.6 %

[OK] llaves de hogar únicas en la sumaria
[OK] llaves de persona únicas
[OK] la unión no perdió ni duplicó filas
[OK] toda persona tiene hogar en la sumaria
[OK] ubigeo con 6 dígitos
[OK] pobreza difiere del INEI (27.6 %) en menos de 0.1 puntos

VALIDACIÓN OK

```

</details>

<details><summary>Resultado</summary>

```
~/Documents/GitHub/agente-datos-oficiales-Peru/referencias/pobreza_departamento_2024.csv
~/Documents/GitHub/agente-datos-oficiales-Peru/evaluacion/comparacion.md
~/Documents/GitHub/agente-datos-oficiales-Peru/evaluacion/resultados.csv
~/Documents/GitHub/agente-datos-oficiales-Peru/evaluacion/.DS_Store
~/Documents/GitHub/agente-datos-oficiales-Peru/evaluacion/preguntas.csv
<shellId: 6 completed with exit code 0>
```

</details>

**Herramienta `bash`** — Consulta series BCRP usando el servidor MCP local

```bash
uv run --project '~/Documents/GitHub/agente-datos-oficiales-Peru' python - <<'PY'
import asyncio, json, os, sys
root = '~/Documents/GitHub/agente-datos-oficiales-Peru'
os.chdir(root)
sys.path.insert(0, root)
from fastmcp import Client
from mcp.server import mcp

async def main():
    async with Client(mcp) as client:
        calls = [
            ('PN01728AM', '2024-01', '2024-12'),
            ('PN01273PM', '2024-12', '2024-12'),
            ('PN01210PM', '2024-01', '2024-12'),
            ('PD04722MM', '2024-01', '2024-12'),
        ]
        results = {}
        for code, start, end in calls:
            results[code] = (await client.call_tool('serie', {'codigo': code, 'desde': start, 'hasta': end})).data
        print(json.dumps(results, ensure_ascii=False, indent=2))

asyncio.run(main())
PY
```

**Herramienta `bash`** — Identifica variables de pobreza y línea monetaria en ENAHO

```bash
uv run --project '~/Documents/GitHub/agente-datos-oficiales-Peru' python - <<'PY'
from pathlib import Path
import pyreadstat
p = Path('~/Documents/GitHub/agente-datos-oficiales-Peru/datos/966-Modulo34/sumaria-2024.dta')
_, meta = pyreadstat.read_dta(p, metadataonly=True)
for name, label in zip(meta.column_names, meta.column_labels):
    print(f'{name}\t{label}')
PY
unzip -l '~/Documents/GitHub/agente-datos-oficiales-Peru/datos/966-Modulo34.zip' | grep -iE 'diccionario|sumaria'
```

<details><summary>Resultado</summary>

```
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
ImportError: cannot import name 'mcp' from 'mcp.server' (~/Documents/GitHub/agente-datos-oficiales-Peru/.venv/lib/python3.12/site-packages/mcp/server/__init__.py)
<shellId: 7 completed with exit code 1>
```

</details>

<details><summary>Resultado</summary>

```
Output too large to read at once (10.4 KB). Saved to: /var/folders/xq/9y7gptwn01s29w73bn8qj9c40000gn/T/1793975050310-copilot-tool-output-623-8c5728b4-c92e-4e71-aac1-0e543c75e4f3.txt
Consider using tools like rg (for searching), head/tail (for viewing start/end), view with view_range (for specific sections), or jq (for JSON) to examine portions of the output.

Preview (first 500 chars):
aÑo	año de la encuesta
mes	mes de ejecucion de la encuesta
conglome	numero de conglomerado
vivienda	numero de seleccion de vivienda
hogar	numero secuencial del hogar
ubigeo	ubicacion geográfica
dominio	dominio geográfico
estrato	estrato geográfico
mieperho	total de miembros del hogar
totmieho	total de personas en el hogar
percepho	total de perceptores de ingresos
ia01hd	ingreso alquiler imputado de la vivienda
ia02hd	ingreso por transferencia de alquiler
ig03hd1	credito, compra casa, departament
<shellId: 8 completed with exit code 0>
```

</details>

**Herramienta `bash`** — Reintenta consulta BCRP mediante el servidor MCP

```bash
uv run --project '~/Documents/GitHub/agente-datos-oficiales-Peru' python - <<'PY'
import asyncio, json, os, sys
root = '~/Documents/GitHub/agente-datos-oficiales-Peru'
os.chdir(root)
sys.path.insert(0, os.path.join(root, 'mcp'))
from fastmcp import Client
from server import mcp

async def main():
    async with Client(mcp) as client:
        calls = [
            ('PN01728AM', '2024-01', '2024-12'),
            ('PN01273PM', '2024-12', '2024-12'),
            ('PN01210PM', '2024-01', '2024-12'),
            ('PD04722MM', '2024-01', '2024-12'),
        ]
        results = {}
        for code, start, end in calls:
            results[code] = (await client.call_tool('serie', {'codigo': code, 'desde': start, 'hasta': end})).data
        print(json.dumps(results, ensure_ascii=False, indent=2))

asyncio.run(main())
PY
```

**Herramienta `rg`** — pobreza|pobre|linea|linea|factor07|linpea|linea|limite

```json
{
 "pattern": "pobreza|pobre|linea|linea|factor07|linpea|linea|limite",
 "paths": "/var/folders/xq/9y7gptwn01s29w73bn8qj9c40000gn/T/1793975050310-copilot-tool-output-623-8c5728b4-c92e-4e71-aac1-0e543c75e4f3.txt",
 "output_mode": "content",
 "-n": true,
 "head_limit": 80
}
```

<details><summary>Resultado</summary>

```
/var/folders/xq/9y7gptwn01s29w73bn8qj9c40000gn/T/1793975050310-copilot-tool-output-623-8c5728b4-c92e-4e71-aac1-0e543c75e4f3.txt:156:linpe	linea de pobreza alimentaria
/var/folders/xq/9y7gptwn01s29w73bn8qj9c40000gn/T/1793975050310-copilot-tool-output-623-8c5728b4-c92e-4e71-aac1-0e543c75e4f3.txt:157:linea	linea de pobreza total
/var/folders/xq/9y7gptwn01s29w73bn8qj9c40000gn/T/1793975050310-copilot-tool-output-623-8c5728b4-c92e-4e71-aac1-0e543c75e4f3.txt:158:pobreza	pobreza
/var/folders/xq/9y7gptwn01s29w73bn8qj9c40000gn/T/1793975050310-copilot-tool-output-623-8c5728b4-c92e-4e71-aac1-0e543c75e4f3.txt:159:factor07	factor de expansion anual proyecciones cpv-2007
/var/folders/xq/9y7gptwn01s29w73bn8qj9c40000gn/T/1793975050310-copilot-tool-output-623-8c5728b4-c92e-4e71-aac1-0e543c75e4f3.txt:160:lineav	linea corriente de vulnerabilidad
/var/folders/xq/9y7gptwn01s29w73bn8qj9c40000gn/T/1793975050310-copilot-tool-output-623-8c5728b4-c92e-4e71-aac1-0e543c75e4f3.txt:161:pobrezav	pobreza y vulnerable con linea corriente
```

</details>

<details><summary>Resultado</summary>

```
{
  "PN01728AM": {
    "codigo": "PN01728AM",
    "nombre": "Producto bruto interno y demanda interna (variación porcentual interanual) - PBI",
    "frecuencia": "Mensual",
    "datos": [
      {
        "periodo": "2024-01",
        "valor": 1.83097461976354
      },
      {
        "periodo": "2024-02",
        "valor": 3.16241000807473
      },
      {
        "periodo": "2024-03",
        "valor": -0.409690120959002
      },
      {
        "periodo": "2024-04",
        "valor": 5.52986981371346
      },
      {
        "periodo": "2024-05",
        "valor": 5.70691310837814
      },
      {
        "periodo": "2024-06",
        "valor": 0.370585322038706
      },
      {
        "periodo": "2024-07",
        "valor": 4.85868197288225
      },
      {
        "periodo": "2024-08",
        "valor": 3.97028100948149
      },
      {
        "periodo": "2024-09",
        "valor": 3.49053235679599
      },
      {
        "periodo": "2024-10",
        "valor": 3.83110341773776
      },
      {
        "periodo": "2024-11",
        "valor": 4.38200682962149
      },
      {
        "periodo": "2024-12",
        "valor": 5.06622215564914
      }
    ],
    "fuente": "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01728AM/json/2024-1/2024-12"
  },
  "PN01273PM": {
    "codigo": "PN01273PM",
    "nombre": "Índice de precios Lima Metropolitana (var% 12 meses) - IPC",
    "frecuencia": "Mensual",
    "datos": [
      {
        "periodo": "2024-12",
        "valor": 1.96630270142824
      }
    ],
    "fuente": "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01273PM/json/2024-12/2024-12"
  },
  "PN01210PM": {
    "codigo": "PN01210PM",
    "nombre": "Tipo de cambio - promedio del periodo (S/ por US$) - Bancario - Promedio",
    "frecuencia": "Mensual",
    "datos": [
      {
        "periodo": "2024-01",
        "valor": 3.73980952380952
      },
      {
        "periodo": "2024-02",
        "valor": 3.82730952380952
      },
      {
        "periodo": "2024-03",
        "valor": 3.70955263157895
      },
      {
        "periodo": "2024-04",
        "valor": 3.71315909090909
      },
      {
        "periodo": "2024-05",
        "valor": 3.73097727272727
      },
      {
        "periodo": "2024-06",
        "valor": 3.78463157894737
      },
      {
        "periodo": "2024-07",
        "valor": 3.7644
      },
      {
        "periodo": "2024-08",
        "valor": 3.741325
      },
      {
        "periodo": "2024-09",
        "valor": 3.76821428571429
      },
      {
        "periodo": "2024-10",
        "valor": 3.75359090909091
      },
      {
        "periodo": "2024-11",
        "valor": 3.77885
      },
      {
        "periodo": "2024-12",
        "valor": 3.73489473684211
      }
    ],
    "fuente": "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01210PM/json/2024-1/2024-12"
  },
  "PD04722MM": {
    "codigo": "PD04722MM",
    "nombre": "Tasas de interés del Banco Central de Reserva - Tasa de Referencia de la Política Monetaria",
    "frecuencia": "Mensual",
    "datos": [
      {
        "periodo": "2024-01",
        "valor": 6.5
      },
      {
        "periodo": "2024-02",
        "valor": 6.25
      },
      {
        "periodo": "2024-03",
        "valor": 6.25
      },
      {
        "periodo": "2024-04",
        "valor": 6.0
      },
      {
        "periodo": "2024-05",
        "valor": 5.75
      },
      {
        "periodo": "2024-06",
        "valor": 5.75
      },
      {
        "periodo": "2024-07",
        "valor": 5.75
      },
      {
        "periodo": "2024-08",
        "valor": 5.5
      },
      {
        "periodo": "2024-09",
        "valor": 5.25
      },
      {
        "periodo": "2024-10",
        "valor": 5.25
      },
      {
        "periodo": "2024-11",
        "valor": 5.0
      },
      {
        "periodo": "2024-12",
        "valor": 5.0
      }
    ],
    "fuente": "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04722MM/json/2024-1/2024-1
… [salida recortada: 48 caracteres más]
```

</details>

**Herramienta `bash`** — Calcula indicadores ENAHO y cocientes de las series MCP

```bash
uv run --project '~/Documents/GitHub/agente-datos-oficiales-Peru' python - <<'PY'
from pathlib import Path
import pandas as pd
root = Path('~/Documents/GitHub/agente-datos-oficiales-Peru')
people = pd.read_parquet(root / 'salidas/personas_2024.parquet')

def rate(mask, condition):
    s = people.loc[mask]
    return 100 * (s['facpob07'] * condition.loc[s.index]).sum() / s['facpob07'].sum()

age = people['p208a']
poor = people['pobre'].astype(bool)
poverty = people['pobreza']
asks = {
    'P05_pobre_0_17_pct': rate(age.between(0, 17), poor),
    'P06_extrema_0_4_pct': rate(age.between(0, 4), poverty.eq(1)),
    'P07_mujeres_pobres_pct': rate(people['p207'].eq(2), poor),
    'P08_gap_0_17_vs_60_pp': rate(age.between(0, 17), poor) - rate(age.ge(60), poor),
}

sumaria = pd.read_stata(root / 'datos/966-Modulo34/sumaria-2024.dta', convert_categoricals=False)
line = pd.to_numeric(sumaria['linea'], errors='coerce')
fh = pd.to_numeric(sumaria['factor07'], errors='coerce')
size = pd.to_numeric(sumaria['mieperho'], errors='coerce')
valid = line.notna() & fh.notna() & size.notna()
asks['linea_mean_unweighted_soles'] = line[valid].mean()
asks['linea_mean_household_weighted_soles'] = (line[valid] * fh[valid]).sum() / fh[valid].sum()
person_weight = fh[valid] * size[valid]
asks['linea_mean_person_weighted_soles'] = (line[valid] * person_weight).sum() / person_weight.sum()

pbi = pd.read_csv(root / 'datos/pbi_interanual_mensual_2024.csv')
asks['PBI_mean_interannual_2024_pct'] = pbi['variacion_interanual_pct'].mean()
asks['P09_ratio_pp_over_PBI_mean'] = (27.6 - 29.0) / asks['PBI_mean_interannual_2024_pct']
fx = [3.73980952380952,3.82730952380952,3.70955263157895,3.71315909090909,3.73097727272727,3.78463157894737,3.7644,3.741325,3.76821428571429,3.75359090909091,3.77885,3.73489473684211]
asks['FX_mean_2024_soles_per_usd'] = sum(fx)/len(fx)
asks['P10_person_weighted_line_usd'] = asks['linea_mean_person_weighted_soles'] / asks['FX_mean_2024_soles_per_usd']
asks['P10_household_weighted_line_usd'] = asks['linea_mean_household_weighted_soles'] / asks['FX_mean_2024_soles_per_usd']
for key, value in asks.items():
    print(f'{key}={value:.12f}')
print(f'linea_valid_households={int(valid.sum())}, sumaria_households={len(sumaria)}, people_rows={len(people)}')
PY
```

<details><summary>Resultado</summary>

```
P05_pobre_0_17_pct=36.471431732178
P06_extrema_0_4_pct=9.962304115295
P07_mujeres_pobres_pct=27.675724029541
P08_gap_0_17_vs_60_pp=14.451309204102
linea_mean_unweighted_soles=414.713775634766
linea_mean_household_weighted_soles=452.039367675781
linea_mean_person_weighted_soles=454.385864257812
PBI_mean_interannual_2024_pct=3.482490874431
P09_ratio_pp_over_PBI_mean=-0.402011103684
FX_mean_2024_soles_per_usd=3.753892879452
P10_person_weighted_line_usd=121.043907165527
P10_household_weighted_line_usd=120.418823242188
linea_valid_households=33691, sumaria_households=33691, people_rows=108664
<shellId: 10 completed with exit code 0>
```

</details>

## 🤖 Copilot · 2026-11-06 09:25:04

Las consultas al servidor MCP del BCRP ya devolvieron los datos oficiales de 2024; la base ENAHO existente pasa las validaciones de la skill. Estoy contrastando los promedios y fórmulas finales antes de escribir las respuestas y el README.

**Herramienta `bash`** — Verifica promedios y cambios con herramientas resumen del MCP

```bash
uv run --project '~/Documents/GitHub/agente-datos-oficiales-Peru' python - <<'PY'
import asyncio, json, os, sys
root = '~/Documents/GitHub/agente-datos-oficiales-Peru'
os.chdir(root)
sys.path.insert(0, os.path.join(root, 'mcp'))
from fastmcp import Client
from server import mcp

async def main():
    async with Client(mcp) as client:
        out = {}
        for code in ('PN01728AM', 'PN01210PM', 'PD04722MM'):
            out[code] = (await client.call_tool('resumen', {'codigo': code, 'desde': '2024-01', 'hasta': '2024-12'})).data
        ipc = (await client.call_tool('serie', {'codigo': 'PN01273PM', 'desde': '2024-12', 'hasta': '2024-12'})).data
        print(json.dumps({'resumenes': out, 'ipc_dic_2024': ipc}, ensure_ascii=False, indent=2))

asyncio.run(main())
PY
```

<details><summary>Resultado</summary>

```
{
  "resumenes": {
    "PN01728AM": {
      "codigo": "PN01728AM",
      "nombre": "Producto bruto interno y demanda interna (variación porcentual interanual) - PBI",
      "frecuencia": "Mensual",
      "periodo": {
        "desde": "2024-01",
        "hasta": "2024-12"
      },
      "primero": {
        "periodo": "2024-01",
        "valor": 1.83097461976354
      },
      "ultimo": {
        "periodo": "2024-12",
        "valor": 5.06622215564914
      },
      "cambio": 3.2352475358855997,
      "variacion_pct": 176.69537856856877,
      "promedio": 3.4824908744314746,
      "maximo": {
        "periodo": "2024-05",
        "valor": 5.70691310837814
      },
      "minimo": {
        "periodo": "2024-03",
        "valor": -0.409690120959002
      },
      "fuente": "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01728AM/json/2024-1/2024-12"
    },
    "PN01210PM": {
      "codigo": "PN01210PM",
      "nombre": "Tipo de cambio - promedio del periodo (S/ por US$) - Bancario - Promedio",
      "frecuencia": "Mensual",
      "periodo": {
        "desde": "2024-01",
        "hasta": "2024-12"
      },
      "primero": {
        "periodo": "2024-01",
        "valor": 3.73980952380952
      },
      "ultimo": {
        "periodo": "2024-12",
        "valor": 3.73489473684211
      },
      "cambio": -0.004914786967409768,
      "variacion_pct": -0.13141810929459766,
      "promedio": 3.753892879452419,
      "maximo": {
        "periodo": "2024-02",
        "valor": 3.82730952380952
      },
      "minimo": {
        "periodo": "2024-03",
        "valor": 3.70955263157895
      },
      "fuente": "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01210PM/json/2024-1/2024-12"
    },
    "PD04722MM": {
      "codigo": "PD04722MM",
      "nombre": "Tasas de interés del Banco Central de Reserva - Tasa de Referencia de la Política Monetaria",
      "frecuencia": "Mensual",
      "periodo": {
        "desde": "2024-01",
        "hasta": "2024-12"
      },
      "primero": {
        "periodo": "2024-01",
        "valor": 6.5
      },
      "ultimo": {
        "periodo": "2024-12",
        "valor": 5.0
      },
      "cambio": -1.5,
      "variacion_pct": -23.076923076923077,
      "promedio": 5.6875,
      "maximo": {
        "periodo": "2024-01",
        "valor": 6.5
      },
      "minimo": {
        "periodo": "2024-11",
        "valor": 5.0
      },
      "fuente": "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04722MM/json/2024-1/2024-12"
    }
  },
  "ipc_dic_2024": {
    "codigo": "PN01273PM",
    "nombre": "Índice de precios Lima Metropolitana (var% 12 meses) - IPC",
    "frecuencia": "Mensual",
    "datos": [
      {
        "periodo": "2024-12",
        "valor": 1.96630270142824
      }
    ],
    "fuente": "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01273PM/json/2024-12/2024-12"
  }
}
<shellId: 11 completed with exit code 0>
```

</details>

**Herramienta `apply_patch`**

```json
"*** Begin Patch\n*** Update File: ~/Documents/GitHub/Modo B/preguntas.csv\n@@\n-pregunta_id,pregunta\n-P01,\"Según la serie mensual PN01728AM del BCRP, ¿cuál fue la variación interanual del PBI en mayo de 2024?\"\n-P02,\"Según la serie mensual PN01273PM del BCRP, ¿cuál fue la variación porcentual de 12 meses del IPC de Lima Metropolitana (inflación interanual) en diciembre de 2024?\"\n-P03,\"Según la serie mensual PN01210PM del BCRP (tipo de cambio bancario promedio, S/ por US$), ¿cuál fue el promedio simple de los 12 meses de 2024?\"\n-P04,\"Según la serie mensual PD04722MM del BCRP, ¿en cuántos puntos porcentuales varió la tasa de referencia de la política monetaria entre enero de 2024 y diciembre de 2024?\"\n-P05,\"Según los microdatos de la ENAHO 2024 (Módulos 02 y 34), ¿qué porcentaje de las personas menores de 18 años (0 a 17 años) se encontraba en situación de pobreza monetaria?\"\n-P06,\"Según los microdatos de la ENAHO 2024 (Módulos 02 y 34), ¿qué porcentaje de los niños y niñas de 0 a 4 años se encontraba en situación de pobreza monetaria extrema?\"\n-P07,\"Según los microdatos de la ENAHO 2024 (Módulos 02 y 34), ¿qué porcentaje de las mujeres se encontraba en situación de pobreza monetaria?\"\n-P08,\"Según los microdatos de la ENAHO 2024 (Módulos 02 y 34), ¿cuántos puntos porcentuales más alta fue la pobreza monetaria de las personas de 0 a 17 años que la de las personas de 60 años a más?\"\n-P09,\"Combinando ENAHO y BCRP: si la pobreza monetaria pasó de 29.0 % (2023) a 27.6 % (2024), ¿cuál es el cociente entre esa variación (en puntos porcentuales) y el promedio simple de las variaciones interanuales mensuales del PBI de 2024 (serie PN01728AM)?\"\n-P10,Combinando ENAHO y BCRP: ¿a cuántos dólares equivale la línea de pobreza monetaria promedio de 2024 (Módulo 34 de la ENAHO) usando el tipo de cambio bancario promedio de 2024 (promedio simple de los 12 meses de la serie PN01210PM)?\n+pregunta_id,pregunta,respuesta\n+P01,\"Según la serie mensual PN01728AM del BCRP, ¿cuál fue la variación interanual del PBI en mayo de 2024?\",\"5,71 % interanual (PN01728AM, mayo de 2024).\"\n+P02,\"Según la serie mensual PN01273PM del BCRP, ¿cuál fue la variación porcentual de 12 meses del IPC de Lima Metropolitana (inflación interanual) en diciembre de 2024?\",\"1,97 % (PN01273PM, diciembre de 2024).\"\n+P03,\"Según la serie mensual PN01210PM del BCRP (tipo de cambio bancario promedio, S/ por US$), ¿cuál fue el promedio simple de los 12 meses de 2024?\",\"S/ 3,7539 por US$ (promedio simple de 12 meses de PN01210PM).\"\n+P04,\"Según la serie mensual PD04722MM del BCRP, ¿en cuántos puntos porcentuales varió la tasa de referencia de la política monetaria entre enero de 2024 y diciembre de 2024?\",\"Disminuyó 1,50 puntos porcentuales: de 6,50 % en enero a 5,00 % en diciembre (PD04722MM).\"\n+P05,\"Según los microdatos de la ENAHO 2024 (Módulos 02 y 34), ¿qué porcentaje de las personas menores de 18 años (0 a 17 años) se encontraba en situación de pobreza monetaria?\",\"36,47 % de las personas de 0 a 17 años (ponderado con facpob07).\"\n+P06,\"Según los microdatos de la ENAHO 2024 (Módulos 02 y 34), ¿qué porcentaje de los niños y niñas de 0 a 4 años se encontraba en situación de pobreza monetaria extrema?\",\"9,96 % de las personas de 0 a 4 años (pobreza extrema; ponderado con facpob07).\"\n+P07,\"Según los microdatos de la ENAHO 2024 (Módulos 02 y 34), ¿qué porcentaje de las mujeres se encontraba en situación de pobreza monetaria?\",\"27,68 % de las mujeres (ponderado con facpob07).\"\n+P08,\"Según los microdatos de la ENAHO 2024 (Módulos 02 y 34), ¿cuántos puntos porcentuales más alta fue la pobreza monetaria de las personas de 0 a 17 años que la de las personas de 60 años a más?\",\"14,45 puntos porcentuales más alta (36,47 % en 0–17 años frente a 22,02 % en 60 años a más).\"\n+P09,\"Combinando ENAHO y BCRP: si la pobreza monetaria pasó de 29.0 % (2023) a 27.6 % (2024), ¿cuál es el cociente entre esa variación (en pu
… [salida recortada: 4,100 caracteres más]
```

<details><summary>Resultado</summary>

```
Added 1 file(s): ~/Documents/GitHub/Modo B/README.md
Modified 1 file(s): ~/Documents/GitHub/Modo B/preguntas.csv
```

</details>

**Herramienta `bash`** — Valida estructura del CSV y cifras ENAHO

```bash
python - <<'PY'
import csv
from pathlib import Path
import pandas as pd
root = Path('~/Documents/GitHub/Modo B')
with (root / 'preguntas.csv').open(encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 10, len(rows)
assert list(rows[0]) == ['pregunta_id', 'pregunta', 'respuesta']
assert [r['pregunta_id'] for r in rows] == [f'P{i:02}' for i in range(1, 11)]
assert all(r['respuesta'].strip() for r in rows)
people = pd.read_parquet('~/Documents/GitHub/agente-datos-oficiales-Peru/salidas/personas_2024.parquet')
for label, mask in [('0–17', people.p208a.between(0, 17)), ('60+', people.p208a.ge(60))]:
    s = people.loc[mask]
    pct = 100 * (s.facpob07 * s.pobre).sum() / s.facpob07.sum()
    print(f'{label} pobreza ponderada: {pct:.6f}%')
print(f'CSV verificado: {len(rows)} respuestas, 3 columnas, todas completas')
print(f'Readme presente: {(root / "README.md").is_file()}')
PY
```

<details><summary>Resultado</summary>

```
~/anaconda3/lib/python3.11/site-packages/pandas/core/arrays/masked.py:60: UserWarning: Pandas requires version '1.3.6' or newer of 'bottleneck' (version '1.3.5' currently installed).
  from pandas.core import (
<command with shellId: 12 is still running after 30 seconds. The command is still running. You will be automatically notified when it completes; if you need the command to complete end your response with no tool calls to wait for the notification. Use stop_bash to stop it.>
```

</details>

**Herramienta `read_bash`** — Waiting up to 30 seconds for command output

```json
{
 "shellId": "12",
 "delay": 30
}
```

<details><summary>Resultado</summary>

```
~/anaconda3/lib/python3.11/site-packages/pandas/core/arrays/masked.py:60: UserWarning: Pandas requires version '1.3.6' or newer of 'bottleneck' (version '1.3.5' currently installed).
  from pandas.core import (
0–17 pobreza ponderada: 36.471430%
60+ pobreza ponderada: 22.020125%
CSV verificado: 10 respuestas, 3 columnas, todas completas
Readme presente: True
<shellId: 12 completed with exit code 0>
```

</details>

## 🤖 Copilot · 2026-11-06 09:26:29

Completé las 10 respuestas en la columna `respuesta` y documenté las fuentes, ponderaciones y cálculos.

- [preguntas.csv](<~/Documents/GitHub/Modo B/preguntas.csv>)
- [README.md](<~/Documents/GitHub/Modo B/README.md>)

Verifiqué que el CSV contiene las 10 preguntas y respuestas. Las series del BCRP se consultaron mediante el MCP local; para ENAHO usé la base validada y los factores de expansión indicados por la skill.

## 🧑 Usuaria · 2026-11-06 09:28:32

en el read me especifica que lo hiciste tu

**Herramienta `view`** — view the file at ~/Documents/GitHub/Modo B/README.md.

```json
{
 "path": "~/Documents/GitHub/Modo B/README.md"
}
```

<details><summary>Resultado</summary>

```
# Respuestas sobre BCRP y ENAHO 2024

Este directorio contiene `preguntas.csv`, con las 10 respuestas añadidas en la
columna `respuesta`. Las cifras se calcularon con series oficiales del BCRP y
microdatos de la ENAHO 2024 del INEI.

## Procedimiento

### Series del BCRP

Se consultó el servidor MCP local `bcrp` del proyecto
`../agente-datos-oficiales-Peru/mcp/server.py`, usando las herramientas
`serie` y `resumen`. Las observaciones cubren enero-diciembre de 2024, excepto
el IPC, consultado para diciembre. Las series y fuentes oficiales son:

- PBI interanual, `PN01728AM`:
  <https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01728AM/json/2024-1/2024-12>
- IPC de Lima Metropolitana a 12 meses, `PN01273PM`:
  <https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01273PM/json/2024-12/2024-12>
- Tipo de cambio bancario promedio (S/ por US$), `PN01210PM`:
  <https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01210PM/json/2024-1/2024-12>
- Tasa de referencia, `PD04722MM`:
  <https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04722MM/json/2024-1/2024-12>

Para el tipo de cambio y el PBI se promediaron las 12 observaciones mensuales
sin ponderación. Para la tasa de referencia se restó el valor de enero al de
diciembre. Se mantuvo precisión completa en las operaciones y se redondeó la
respuesta a 2 decimales (4 para promedios y cocientes).

### ENAHO

Se emplearon los microdatos de los módulos 02 (personas) y 34 (sumaria), código
INEI 966, y la base de personas ya procesada por la skill
`../agente-datos-oficiales-Peru/.claude/skills/limpiando-enaho/`. La validación
de `../agente-datos-oficiales-Peru/salidas/validacion.txt` reporta
`VALIDACIÓN OK`: 108 664 residentes habituales, unión sin pérdidas ni
duplicaciones, y pobreza de la sumaria de 27,58 %, consistente con el 27,6 %
oficial del INEI.

Las proporciones de personas se calcularon con el factor de expansión
`facpob07`; se definió pobreza monetaria como `pobreza <= 2` y pobreza extrema
como `pobreza == 1`. Se filtraron las edades inclusivamente (0–17, 0–4 y
60 años a más); para mujeres se usó `p207 == 2`. La diferencia de edad se
calculó restando la tasa de pobreza del grupo de 60 años a más a la tasa de
0–17 años.

Para la línea de pobreza se usó la variable `linea` (línea de pobreza total)
del módulo 34. Al ser un umbral por persona registrado en cada hogar, su
promedio se ponderó por personas representadas (`factor07 × mieperho`), dando
S/ 454,39 por persona al mes. Para convertirlo a dólares se dividió entre el
promedio simple anual de `PN01210PM` (S/ 3,7539 por US$).

Los microdatos ENAHO se descargan del portal oficial del INEI:

- [Módulo 02, ENAHO 2024](https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip)
- [Módulo 34, ENAHO 2024](https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip)

## Cálculo de la pregunta combinada P09

La variación de pobreza es `27,6 − 29,0 = −1,4` puntos porcentuales. El
promedio de las 12 variaciones interanuales mensuales del PBI es 3,4825 %.
Por tanto, el cociente es `−1,4 ÷ 3,4825 = −0,4020` (adimensional).

## Archivos

- `preguntas.csv`: preguntas originales con la columna `respuesta` añadida.
- Este README: fuentes, definiciones, ponderaciones y operaciones utilizadas.

```

</details>

**Herramienta `apply_patch`**

```json
"*** Begin Patch\n*** Update File: ~/Documents/GitHub/Modo B/README.md\n@@\n Este directorio contiene `preguntas.csv`, con las 10 respuestas añadidas en la\n columna `respuesta`. Las cifras se calcularon con series oficiales del BCRP y\n microdatos de la ENAHO 2024 del INEI.\n \n+## Autoría\n+\n+Las consultas al MCP, los cálculos, las respuestas del CSV y este README fueron\n+preparados por un asistente de IA que utiliza Copilot SDK en VS Code, a solicitud\n+de la usuaria. Las fuentes y los datos empleados son los organismos oficiales\n+indicados a continuación.\n+\n ## Procedimiento\n*** End Patch"
```

<details><summary>Resultado</summary>

```
Modified 1 file(s): ~/Documents/GitHub/Modo B/README.md
```

</details>

## 🤖 Copilot · 2026-11-06 09:28:42

Actualicé el [README.md](<~/Documents/GitHub/Modo B/README.md>) para indicar que las consultas, cálculos, respuestas y documentación fueron preparados por un asistente de IA que utiliza Copilot SDK en VS Code, a solicitud tuya.
