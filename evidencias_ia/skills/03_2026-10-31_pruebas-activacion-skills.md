# Pruebas de activación de las Skills en lenguaje natural

Reúne 15 sesiones cortas e independientes, en orden cronológico.

---

## Sesión bb5ba63a

- **Sesión:** `bb5ba63a` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:14:08 · **Fin:** 2026-10-31 10:14:25 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:14:09

¿Cuál fue la pobreza en Cusco en 2024?

**Herramienta `Skill`**

```json
{
 "skill": "limpiando-enaho",
 "args": "Calcular la pobreza en Cusco en 2024"
}
```

<details><summary>Resultado</summary>

```
Execute skill: limpiando-enaho
```

</details>

**Herramienta `Bash`** — List project files and skills

```bash
ls -la && ls -R .claude salidas | head -50 && cat pyproject.toml
```

<details><summary>Resultado</summary>

```
total 440
drwxr-xr-x@ 15 susanmontalvo  staff     480 Oct 31 10:14 .
drwxr-xr-x@ 11 susanmontalvo  staff     352 Oct 31 08:31 ..
-rw-r--r--@  1 susanmontalvo  staff    6148 Oct 31 09:15 .DS_Store
drwxr-xr-x@  3 susanmontalvo  staff      96 Oct 31 08:31 .claude
drwxr-xr-x@  9 susanmontalvo  staff     288 Oct 31 09:08 .git
-rw-r--r--@  1 susanmontalvo  staff     187 Oct 31 09:08 .gitignore
-rw-r--r--@  1 susanmontalvo  staff       5 Oct 31 08:31 .python-version
drwxr-xr-x@  9 susanmontalvo  staff     288 Oct 31 08:32 .venv
drwxr-xr-x@  7 susanmontalvo  staff     224 Oct 31 08:58 datos
drwxr-xr-x@  2 susanmontalvo  staff      64 Oct 31 10:14 figuras
drwxr-xr-x@  2 susanmontalvo  staff      64 Oct 31 10:14 mapas
drwxr-xr-x@  4 susanmontalvo  staff     128 Oct 31 10:14 notas
-rw-r--r--@  1 susanmontalvo  staff     296 Oct 31 08:32 pyproject.toml
drwxr-xr-x@  3 susanmontalvo  staff      96 Oct 31 10:14 salidas
-rw-r--r--@  1 susanmontalvo  staff  204085 Oct 31 08:32 uv.lock
.claude:
skills

.claude/skills:
graficando-enaho
limpiando-enaho
mapeando-enaho

.claude/skills/graficando-enaho:
SKILL.md
scripts

.claude/skills/graficando-enaho/scripts:
graficar.py

.claude/skills/limpiando-enaho:
SKILL.md
reference.md
scripts

.claude/skills/limpiando-enaho/scripts:
limpiar.py

.claude/skills/mapeando-enaho:
SKILL.md
scripts

.claude/skills/mapeando-enaho/scripts:
mapear.py

salidas:
validacion.txt
[project]
name = "skills-enaho"
version = "0.1.0"
description = "Tres skills de Claude Code que limpian, grafican y mapean la ENAHO 2024"
requires-python = ">=3.12"
dependencies = [
    "geopandas>=1.2.0",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
    "pyproj<3.8",
]
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/.claude/skills/limpiando-enaho/SKILL.md"
}
```

<details><summary>Resultado</summary>

```
1	---
2	name: limpiando-enaho
3	description: Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO del INEI y arma una base de personas con pobreza y factor de expansión. Úsala cuando pidan limpiar, unir o analizar la ENAHO, o calcular pobreza por región, departamento, área, sexo o edad.
4	argument-hint: [año]
5	allowed-tools: Bash(uv run *)
6	---
7	
8	# Limpiar la ENAHO
9	
10	1. Si faltan los zip en datos/, pide al usuario bajarlos del INEI desde el navegador (código 966 = 2024):
11	   proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip y 966-Modulo02.zip
12	2. Corre exactamente, desde la raíz del repo: `uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio $0`
13	   Si no se pasó año, usa `--anio 2024`. No escribas otro script de limpieza ni cambies filtros, llaves o factores.
14	3. Lee salidas/validacion.txt. Si dice VALIDACIÓN FALLIDA o la pobreza difiere del INEI en más de 0.1 puntos, detente y muestra el archivo.
15	4. Responde con salidas/personas_<año>.parquet. Toda cifra va ponderada con facpob07; pobre es `pobreza <= 2`, nunca un promedio del código.
16	5. Antes de usar una variable que no está en la base, lee [reference.md](reference.md).
17	
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/.claude/skills/limpiando-enaho/scripts/limpiar.py"
}
```

<details><summary>Resultado</summary>

```
1	"""Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO y arma una base de personas.
2	
3	Uso: uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
4	"""
5	
6	import argparse
7	import sys
8	import unicodedata
9	import zipfile
10	from pathlib import Path
11	
12	import pandas as pd
13	
14	LLAVES = ["conglome", "vivienda", "hogar"]
15	LLAVES_PERSONA = LLAVES + ["codperso"]
16	CODIGO_INEI = {2024: 966}  # código de la ENAHO en el portal de microdatos
17	POBREZA_INEI = {2024: 27.6}  # pobreza monetaria oficial, en %
18	
19	RAIZ = Path.cwd()
20	DATOS = RAIZ / "datos"
21	SALIDAS = RAIZ / "salidas"
22	
23	
24	def normalizar(nombre: str) -> str:
25	    """Pasa a minúsculas y quita tildes: «aÑo» se vuelve «anio»."""
26	    nombre = nombre.lower().replace("ñ", "ni")
27	    return unicodedata.normalize("NFKD", nombre).encode("ascii", "ignore").decode()
28	
29	
30	def leer(codigo: int, modulo: str, archivo: str) -> pd.DataFrame:
31	    """1 · Leer: extrae el .dta del zip si hace falta y lo lee con códigos, no etiquetas."""
32	    carpeta = DATOS / f"{codigo}-Modulo{modulo}"
33	    ruta = carpeta / archivo
34	    if not ruta.exists():
35	        zip_ = DATOS / f"{codigo}-Modulo{modulo}.zip"
36	        if not zip_.exists():
37	            sys.exit(f"Falta {zip_}. Bájalo de proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/{zip_.name}")
38	        with zipfile.ZipFile(zip_) as z:
39	            z.extract(f"{carpeta.name}/{archivo}", DATOS)
40	    df = pd.read_stata(ruta, convert_categoricals=False)
41	    # 2 · Normalizar nombres
42	    df.columns = [normalizar(c) for c in df.columns]
43	    for c in LLAVES_PERSONA + ["ubigeo"]:
44	        if c in df.columns:
45	            df[c] = df[c].astype("string")
46	    return df
47	
48	
49	def ponderada(serie: pd.Series, peso: pd.Series) -> float:
50	    return 100 * (serie * peso).sum() / peso.sum()
51	
52	
53	def main() -> None:
54	    parser = argparse.ArgumentParser()
55	    parser.add_argument("--anio", type=int, default=2024)
56	    anio = parser.parse_args().anio
57	    if anio not in CODIGO_INEI:
58	        sys.exit(f"Año {anio} sin código INEI conocido. Agrégalo en CODIGO_INEI.")
59	    codigo = CODIGO_INEI[anio]
60	
61	    sumaria = leer(codigo, "34", f"sumaria-{anio}.dta")
62	    miembros = leer(codigo, "02", f"enaho01-{anio}-200.dta")
63	
64	    # 3 · Filtrar residentes habituales (definición del INEI)
65	    residente = ((miembros.p204 == 1) & (miembros.p205 == 2)) | ((miembros.p204 == 2) & (miembros.p206 == 1))
66	    personas = miembros.loc[residente, LLAVES_PERSONA + ["p203", "p207", "p208a", "facpob07"]]
67	
68	    # 4 · Unir cada persona con su hogar
69	    columnas_hogar = LLAVES + ["ubigeo", "estrato", "dominio", "pobreza", "mieperho", "factor07"]
70	    base = personas.merge(sumaria[columnas_hogar], on=LLAVES, how="left", validate="m:1")
71	
72	    # 5 · Construir variables
73	    base["departamento"] = base.ubigeo.str[:2]
74	    base["urbano"] = base.estrato <= 5
75	    base["pobre"] = base.pobreza <= 2
76	    base["pobre_extremo"] = base.pobreza == 1
77	    base["anio"] = anio
78	
79	    # 6 · Validar
80	    pob_hogares = ponderada(sumaria.pobreza <= 2, sumaria.factor07 * sumaria.mieperho)
81	    ext_hogares = ponderada(sumaria.pobreza == 1, sumaria.factor07 * sumaria.mieperho)
82	    pob_personas = ponderada(base.pobre, base.facpob07)
83	    oficial = POBREZA_INEI.get(anio)
84	    chequeos = {
85	        "llaves de hogar únicas en la sumaria": not sumaria.duplicated(LLAVES).any(),
86	        "llaves de persona únicas": not personas.duplicated(LLAVES_PERSONA).any(),
87	        "la unión no perdió ni duplicó filas": len(base) == len(personas),
88	        "toda persona tiene hogar en la sumaria": base.pobreza.notna().all(),
89	        "ubigeo con 6 dígitos": base.ubigeo.str.len().eq(6).all(),
90	    }
91	    if oficial is not None:
92	        chequeos[f"pobreza difiere del INEI ({oficial} %) en menos de 0.1 puntos"] = abs(pob_hogares - oficial) < 0.1
93
… [salida recortada: 1,181 caracteres más]
```

</details>

**Herramienta `Bash`** — List data, notes and outputs

```bash
ls -laR datos notas salidas && cat salidas/validacion.txt
```

<details><summary>Resultado</summary>

```
datos:
total 43760
drwxr-xr-x@  7 susanmontalvo  staff       224 Oct 31 08:58 .
drwxr-xr-x@ 15 susanmontalvo  staff       480 Oct 31 10:14 ..
drwxr-xr-x@  3 susanmontalvo  staff        96 Oct 31 08:58 966-Modulo02
-rw-r--r--@  1 susanmontalvo  staff   5793097 Oct 31 08:56 966-Modulo02.zip
drwxr-xr-x@  3 susanmontalvo  staff        96 Oct 31 08:58 966-Modulo34
-rw-r--r--@  1 susanmontalvo  staff  15935617 Oct 31 08:55 966-Modulo34.zip
-rw-r--r--@  1 susanmontalvo  staff    139681 Oct 31 08:36 peru_departamental_simple.geojson

datos/966-Modulo02:
total 19960
drwxr-xr-x@ 3 susanmontalvo  staff        96 Oct 31 08:58 .
drwxr-xr-x@ 7 susanmontalvo  staff       224 Oct 31 08:58 ..
-rw-r--r--@ 1 susanmontalvo  staff  10217755 May  7  2025 enaho01-2024-200.dta

datos/966-Modulo34:
total 41448
drwxr-xr-x@ 3 susanmontalvo  staff        96 Oct 31 08:58 .
drwxr-xr-x@ 7 susanmontalvo  staff       224 Oct 31 08:58 ..
-rw-r--r--@ 1 susanmontalvo  staff  21219121 May  8  2025 sumaria-2024.dta

notas:
total 16
drwxr-xr-x@  4 susanmontalvo  staff   128 Oct 31 10:14 .
drwxr-xr-x@ 15 susanmontalvo  staff   480 Oct 31 10:14 ..
-rw-r--r--@  1 susanmontalvo  staff  6473 Oct 31 09:07 chat-2026-10-31.md
drwxr-xr-x@  4 susanmontalvo  staff   128 Oct 31 10:14 evaluacion

notas/evaluacion:
total 80
drwxr-xr-x@ 4 susanmontalvo  staff    128 Oct 31 10:14 .
drwxr-xr-x@ 4 susanmontalvo  staff    128 Oct 31 10:14 ..
-rw-r--r--@ 1 susanmontalvo  staff      0 Oct 31 10:14 1-con.err
-rw-r--r--@ 1 susanmontalvo  staff  37402 Oct 31 10:14 1-con.jsonl

salidas:
total 8
drwxr-xr-x@  3 susanmontalvo  staff   96 Oct 31 10:14 .
drwxr-xr-x@ 15 susanmontalvo  staff  480 Oct 31 10:14 ..
-rw-r--r--@  1 susanmontalvo  staff  549 Oct 31 09:39 validacion.txt
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

## 🤖 Claude · 2026-10-31 10:14:19

Sigo los pasos de la skill: corro el script de limpieza tal cual.

**Herramienta `Bash`** — Run ENAHO cleaning script for 2024

```bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
```

<details><summary>Resultado</summary>

```
This command requires approval
```

</details>

## 🤖 Claude · 2026-10-31 10:14:25

No pude calcular la cifra: la herramienta no aprobó el comando del script de limpieza, así que no tengo el número de Cusco.

Cómo está el proyecto:
- Ya están descomprimidos los módulos 34 y 02 de 2024 en `datos/`.
- `salidas/validacion.txt` dice VALIDACIÓN OK en una corrida anterior. La pobreza nacional salió en 27,58 %, frente al 27,6 % oficial del INEI.
- Lo que falta es `salidas/personas_2024.parquet`, que es la base de personas de donde sale el dato de Cusco.

La skill `limpiando-enaho` pide generar esa base con su propio script y no con otro. Para seguir, apruebe este comando cuando aparezca el aviso, o córralo usted desde la raíz del repo:

```
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
```

Con la base lista calculo la pobreza y la pobreza extrema de Cusco (código de departamento `08`), ponderadas con `facpob07` y contando como pobre a quien tiene `pobreza <= 2`.


---

## Sesión 2f2c4e6c

- **Sesión:** `2f2c4e6c` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:14:28 · **Fin:** 2026-10-31 10:14:47 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:14:29

Grafica la pobreza urbana y rural

**Herramienta `Skill`**

```json
{
 "skill": "graficando-enaho",
 "args": "area"
}
```

<details><summary>Resultado</summary>

```
Execute skill: graficando-enaho
```

</details>

**Herramienta `Bash`** — List skills and project files

```bash
ls -R .claude | head -50 && ls salidas figuras 2>/dev/null; cat pyproject.toml
```

<details><summary>Resultado</summary>

```
skills

.claude/skills:
graficando-enaho
limpiando-enaho
mapeando-enaho

.claude/skills/graficando-enaho:
SKILL.md
scripts

.claude/skills/graficando-enaho/scripts:
graficar.py

.claude/skills/limpiando-enaho:
SKILL.md
reference.md
scripts

.claude/skills/limpiando-enaho/scripts:
limpiar.py

.claude/skills/mapeando-enaho:
SKILL.md
scripts

.claude/skills/mapeando-enaho/scripts:
mapear.py
figuras:

salidas:
validacion.txt
[project]
name = "skills-enaho"
version = "0.1.0"
description = "Tres skills de Claude Code que limpian, grafican y mapean la ENAHO 2024"
requires-python = ">=3.12"
dependencies = [
    "geopandas>=1.2.0",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
    "pyproj<3.8",
]
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/.claude/skills/graficando-enaho/SKILL.md"
}
```

<details><summary>Resultado</summary>

```
1	---
2	name: graficando-enaho
3	description: Grafica la pobreza de la ENAHO del INEI en barras, por área (urbano y rural), departamento, sexo o grupo de edad, y guarda un PNG en figuras/. Úsala cuando pidan un gráfico, una figura o una comparación visual de la pobreza o la pobreza extrema en el Perú.
4	argument-hint: [area|departamento|sexo|edad]
5	allowed-tools: Bash(uv run *)
6	---
7	
8	# Graficar la ENAHO
9	
10	1. Si no existe salidas/personas_2024.parquet, usa primero la skill limpiando-enaho.
11	2. Corre exactamente, desde la raíz del repo:
12	   `uv run ${CLAUDE_SKILL_DIR}/scripts/graficar.py --por $0 --anio 2024`
13	   Para pobreza extrema agrega `--indicador pobre_extremo`. No escribas otro script de gráficos.
14	3. Reglas que el script ya cumple y que no se cambian: ponderar con facpob07; barras desde cero
15	   y ordenadas; un solo color con el valor escrito en cada barra; título con qué y cuándo;
16	   nota «Fuente: INEI, ENAHO 2024»; PNG a 200 dpi.
17	4. Responde con las cifras que imprime el script y la ruta del PNG en figuras/.
18	5. Las cifras salen de la base de personas: urbano 24.7 % y rural 39.4 %. La sumaria da 24.8 % y 39.3 %.
19	
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/.claude/skills/graficando-enaho/scripts/graficar.py"
}
```

<details><summary>Resultado</summary>

```
1	"""Grafica la pobreza de la ENAHO por grupo, desde la base de personas de limpiando-enaho.
2	
3	Uso: uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area --anio 2024
4	"""
5	
6	import argparse
7	import sys
8	from pathlib import Path
9	
10	import matplotlib
11	
12	matplotlib.use("Agg")
13	import matplotlib.pyplot as plt
14	import pandas as pd
15	
16	RAIZ = Path.cwd()
17	SALIDAS = RAIZ / "salidas"
18	FIGURAS = RAIZ / "figuras"
19	
20	COLOR = "#2a78d6"  # un solo color para todas las barras
21	TINTA = "#0b0b0b"
22	TINTA_SECUNDARIA = "#52514e"
23	
24	DEPARTAMENTOS = {
25	    "01": "Amazonas", "02": "Áncash", "03": "Apurímac", "04": "Arequipa", "05": "Ayacucho",
26	    "06": "Cajamarca", "07": "Callao", "08": "Cusco", "09": "Huancavelica", "10": "Huánuco",
27	    "11": "Ica", "12": "Junín", "13": "La Libertad", "14": "Lambayeque", "15": "Lima",
28	    "16": "Loreto", "17": "Madre de Dios", "18": "Moquegua", "19": "Pasco", "20": "Piura",
29	    "21": "Puno", "22": "San Martín", "23": "Tacna", "24": "Tumbes", "25": "Ucayali",
30	}
31	EDADES = [0, 18, 30, 45, 60, 200]
32	GRUPOS_EDAD = ["0–17", "18–29", "30–44", "45–59", "60 y más"]
33	
34	INDICADORES = {"pobre": "Pobreza monetaria", "pobre_extremo": "Pobreza extrema"}
35	NOMBRE_GRUPO = {"area": "área", "departamento": "departamento", "sexo": "sexo", "edad": "grupo de edad"}
36	
37	
38	def agrupar(base: pd.DataFrame, por: str) -> pd.Series:
39	    """Devuelve la etiqueta de grupo de cada persona."""
40	    if por == "area":
41	        return base.urbano.map({True: "Urbano", False: "Rural"})
42	    if por == "departamento":
43	        return base.departamento.map(DEPARTAMENTOS)
44	    if por == "sexo":
45	        return base.p207.map({1: "Hombre", 2: "Mujer"})
46	    return pd.cut(base.p208a, EDADES, right=False, labels=GRUPOS_EDAD).astype("string")
47	
48	
49	def ponderar(base: pd.DataFrame, grupo: pd.Series, indicador: str) -> pd.Series:
50	    """% de personas con el indicador, ponderado con facpob07."""
51	    peso = base.facpob07
52	    con = (base[indicador] * peso).groupby(grupo).sum()
53	    return (100 * con / peso.groupby(grupo).sum()).sort_values()
54	
55	
56	def graficar(valores: pd.Series, titulo: str, anio: int, ruta: Path) -> None:
57	    alto = 1.2 + 0.32 * len(valores)
58	    fig, ax = plt.subplots(figsize=(7, max(alto, 2.6)))
59	    barras = ax.barh(valores.index, valores.values, color=COLOR, height=0.7)
60	    ax.bar_label(barras, labels=[f"{v:.1f} %" for v in valores], padding=4, color=TINTA, fontsize=9)
61	
62	    ax.set_xlim(0, valores.max() * 1.15)  # barras desde cero, con aire para el valor
63	    ax.margins(y=0.02)
64	    ax.set_xticks([])
65	    ax.tick_params(axis="y", length=0, labelcolor=TINTA, labelsize=10)
66	    for lado in ["top", "right", "bottom"]:
67	        ax.spines[lado].set_visible(False)
68	    ax.spines["left"].set_color(TINTA_SECUNDARIA)
69	
70	    fig.suptitle(titulo, x=0.02, ha="left", fontsize=12, fontweight="bold", color=TINTA)
71	    ax.set_title("% de personas", loc="left", fontsize=9, color=TINTA_SECUNDARIA)
72	    fig.text(0.02, 0.01, f"Fuente: INEI, ENAHO {anio}", fontsize=8, color=TINTA_SECUNDARIA)
73	    fig.tight_layout(rect=(0, 0.04, 1, 1))
74	    fig.savefig(ruta, dpi=200, facecolor="white")
75	    plt.close(fig)
76	
77	
78	def main() -> None:
79	    parser = argparse.ArgumentParser()
80	    parser.add_argument("--por", choices=list(NOMBRE_GRUPO), required=True)
81	    parser.add_argument("--indicador", choices=list(INDICADORES), default="pobre")
82	    parser.add_argument("--anio", type=int, default=2024)
83	    args = parser.parse_args()
84	
85	    archivo = SALIDAS / f"personas_{args.anio}.parquet"
86	    if not archivo.exists():
87	        sys.exit(f"Falta {archivo}. Usa primero la skill limpiando-enaho.")
88	    base = pd.read_parquet(archivo)
89	
90	    grupo = agrupar(base, args.por)
91	    if grupo.isna().any():
92	        sys.exit(f"{grupo.isna().sum()} personas sin grupo de {args.por}; revisa la base.
… [salida recortada: 648 caracteres más]
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/salidas/validacion.txt"
}
```

<details><summary>Resultado</summary>

```
1	ENAHO 2024 · validación
2	Hogares en la sumaria: 33,691
3	Filas en el módulo 200: 117,721
4	Residentes habituales en la base: 108,664
5	Pobreza (sumaria, factor07 × mieperho): 27.58 %
6	Pobreza extrema (sumaria): 5.50 %
7	Pobreza (personas, facpob07): 27.53 %
8	Pobreza oficial INEI: 27.6 %
9	
10	[OK] llaves de hogar únicas en la sumaria
11	[OK] llaves de persona únicas
12	[OK] la unión no perdió ni duplicó filas
13	[OK] toda persona tiene hogar en la sumaria
14	[OK] ubigeo con 6 dígitos
15	[OK] pobreza difiere del INEI (27.6 %) en menos de 0.1 puntos
16	
17	VALIDACIÓN OK
18	
```

</details>

## 🤖 Claude · 2026-10-31 10:14:37

The base de personas (`salidas/personas_2024.parquet`) no existe todavía, así que primero toca la limpieza.

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/.claude/skills/limpiando-enaho/SKILL.md"
}
```

<details><summary>Resultado</summary>

```
1	---
2	name: limpiando-enaho
3	description: Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO del INEI y arma una base de personas con pobreza y factor de expansión. Úsala cuando pidan limpiar, unir o analizar la ENAHO, o calcular pobreza por región, departamento, área, sexo o edad.
4	argument-hint: [año]
5	allowed-tools: Bash(uv run *)
6	---
7	
8	# Limpiar la ENAHO
9	
10	1. Si faltan los zip en datos/, pide al usuario bajarlos del INEI desde el navegador (código 966 = 2024):
11	   proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip y 966-Modulo02.zip
12	2. Corre exactamente, desde la raíz del repo: `uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio $0`
13	   Si no se pasó año, usa `--anio 2024`. No escribas otro script de limpieza ni cambies filtros, llaves o factores.
14	3. Lee salidas/validacion.txt. Si dice VALIDACIÓN FALLIDA o la pobreza difiere del INEI en más de 0.1 puntos, detente y muestra el archivo.
15	4. Responde con salidas/personas_<año>.parquet. Toda cifra va ponderada con facpob07; pobre es `pobreza <= 2`, nunca un promedio del código.
16	5. Antes de usar una variable que no está en la base, lee [reference.md](reference.md).
17	
```

</details>

**Herramienta `Bash`** — Check for ENAHO zip files

```bash
ls -la datos 2>&1; cat .gitignore
```

<details><summary>Resultado</summary>

```
total 43760
drwxr-xr-x@  7 susanmontalvo  staff       224 Oct 31 08:58 .
drwxr-xr-x@ 15 susanmontalvo  staff       480 Oct 31 10:14 ..
drwxr-xr-x@  3 susanmontalvo  staff        96 Oct 31 08:58 966-Modulo02
-rw-r--r--@  1 susanmontalvo  staff   5793097 Oct 31 08:56 966-Modulo02.zip
drwxr-xr-x@  3 susanmontalvo  staff        96 Oct 31 08:58 966-Modulo34
-rw-r--r--@  1 susanmontalvo  staff  15935617 Oct 31 08:55 966-Modulo34.zip
-rw-r--r--@  1 susanmontalvo  staff    139681 Oct 31 08:36 peru_departamental_simple.geojson
## Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv

# Microdatos del INEI: no se suben
datos/
.DS_Store
salidas/*.parquet
notas/
```

</details>

**Herramienta `Bash`** — Run ENAHO cleaning script for 2024

```bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 && cat salidas/validacion.txt
```

<details><summary>Resultado</summary>

```
This Bash command contains multiple operations. The following part requires approval: uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
```

</details>

**Herramienta `Bash`** — Run ENAHO cleaning script for 2024

```bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
```

<details><summary>Resultado</summary>

```
This command requires approval
```

</details>

## 🤖 Claude · 2026-10-31 10:14:47

No pude generar el gráfico: el comando para limpiar los datos necesita tu aprobación y no se ejecutó.

El gráfico sale de `salidas/personas_2024.parquet`, y ese archivo todavía no existe. Para crearlo hay que correr primero la limpieza (skill `limpiando-enaho`). Los zip de los módulos 34 y 02 ya están en `datos/`. El comando, desde la raíz del repo, es:

```
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
```

Después correría `uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area --anio 2024`, que guarda el PNG en `figuras/pobreza_area_2024.png`.

Si lo apruebas, sigo. Según la skill, las cifras deberían salir en torno a **urbano 24.7 %** y **rural 39.4 %** (ponderadas con facpob07). No las confirmo hasta correr el script.


---

## Sesión d0eee21d

- **Sesión:** `d0eee21d` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:14:50 · **Fin:** 2026-10-31 10:15:09 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:14:51

Haz un mapa de la pobreza por departamento con la ENAHO 2024

**Herramienta `Skill`**

```json
{
 "skill": "mapeando-enaho",
 "args": "ENAHO 2024, pobreza por departamento"
}
```

<details><summary>Resultado</summary>

```
Execute skill: mapeando-enaho
```

</details>

**Herramienta `Bash`** — Inspect project and skill files

```bash
ls -la && find .claude -type f | head -50 && ls salidas | head && cat pyproject.toml
```

<details><summary>Resultado</summary>

```
total 440
drwxr-xr-x@ 15 susanmontalvo  staff     480 Oct 31 10:14 .
drwxr-xr-x@ 11 susanmontalvo  staff     352 Oct 31 08:31 ..
-rw-r--r--@  1 susanmontalvo  staff    6148 Oct 31 09:15 .DS_Store
drwxr-xr-x@  3 susanmontalvo  staff      96 Oct 31 08:31 .claude
drwxr-xr-x@  9 susanmontalvo  staff     288 Oct 31 09:08 .git
-rw-r--r--@  1 susanmontalvo  staff     187 Oct 31 09:08 .gitignore
-rw-r--r--@  1 susanmontalvo  staff       5 Oct 31 08:31 .python-version
drwxr-xr-x@  9 susanmontalvo  staff     288 Oct 31 08:32 .venv
drwxr-xr-x@  7 susanmontalvo  staff     224 Oct 31 08:58 datos
drwxr-xr-x@  2 susanmontalvo  staff      64 Oct 31 10:14 figuras
drwxr-xr-x@  2 susanmontalvo  staff      64 Oct 31 10:14 mapas
drwxr-xr-x@  4 susanmontalvo  staff     128 Oct 31 10:14 notas
-rw-r--r--@  1 susanmontalvo  staff     296 Oct 31 08:32 pyproject.toml
drwxr-xr-x@  3 susanmontalvo  staff      96 Oct 31 10:14 salidas
-rw-r--r--@  1 susanmontalvo  staff  204085 Oct 31 08:32 uv.lock
.claude/skills/mapeando-enaho/SKILL.md
.claude/skills/graficando-enaho/SKILL.md
.claude/skills/limpiando-enaho/reference.md
.claude/skills/limpiando-enaho/SKILL.md
.claude/skills/mapeando-enaho/scripts/mapear.py
.claude/skills/graficando-enaho/scripts/graficar.py
.claude/skills/limpiando-enaho/scripts/limpiar.py
validacion.txt
[project]
name = "skills-enaho"
version = "0.1.0"
description = "Tres skills de Claude Code que limpian, grafican y mapean la ENAHO 2024"
requires-python = ">=3.12"
dependencies = [
    "geopandas>=1.2.0",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
    "pyproj<3.8",
]
```

</details>

**Herramienta `Bash`** — Read skill instructions, scripts, and data layout

```bash
cat .claude/skills/mapeando-enaho/SKILL.md .claude/skills/mapeando-enaho/scripts/mapear.py .claude/skills/limpiando-enaho/SKILL.md; echo ----; find datos notas salidas -maxdepth 2 | head -40; cat salidas/validacion.txt
```

<details><summary>Resultado</summary>

```
---
name: mapeando-enaho
description: Dibuja un mapa coroplético de la pobreza de la ENAHO del INEI por departamento del Perú y lo guarda en mapas/pobreza_departamento.png. Úsala cuando pidan un mapa, la distribución geográfica o la pobreza de los 25 departamentos.
argument-hint: [año]
allowed-tools: Bash(uv run *)
---

## Mapear la ENAHO

1. Si no existe salidas/personas_2024.parquet, usa primero la skill limpiando-enaho.
2. Si falta datos/peru_departamental_simple.geojson, bájalo de
   raw.githubusercontent.com/juaneladio/peru-geojson/master/peru_departamental_simple.geojson
3. Corre exactamente, desde la raíz del repo: `uv run ${CLAUDE_SKILL_DIR}/scripts/mapear.py --anio $0`
   Si no se pasó año, usa `--anio 2024`. No escribas otro script de mapas.
4. Si algún chequeo sale FALLA, detente y muestra la salida. Reglas que el script ya cumple:
   unir `ubigeo[:2]` con FIRST_IDDP, nunca por nombre; 25 departamentos con dato; escala de un
   solo tono desde 0, sin arcoíris; leyenda «% de personas»; Lima (15) y Callao (07) separados.
5. Responde con las cifras que imprime el script y la ruta del mapa. Se calculan como la sumaria
   (factor07 × mieperho): Cajamarca 45.0 %, Ica 6.0 %.
"""Mapea la pobreza de la ENAHO por departamento, desde la base de personas de limpiando-enaho.

Uso: uv run .claude/skills/mapeando-enaho/scripts/mapear.py --anio 2024
"""

import argparse
import sys
from pathlib import Path

import geopandas as gpd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

LLAVES = ["conglome", "vivienda", "hogar"]

RAIZ = Path.cwd()
DATOS = RAIZ / "datos"
SALIDAS = RAIZ / "salidas"
MAPAS = RAIZ / "mapas"
GEOJSON = DATOS / "peru_departamental_simple.geojson"
URL_GEOJSON = "https://raw.githubusercontent.com/juaneladio/peru-geojson/master/peru_departamental_simple.geojson"

ESCALA = "Blues"  # un solo tono, de claro (0 %) a oscuro
TINTA = "#0b0b0b"
TINTA_SECUNDARIA = "#52514e"

# Calculadas con la sumaria (factor07 × mieperho); el mapa debe dar lo mismo.
REFERENCIA = {
    2024: {"06": 45.0, "16": 43.0, "21": 39.9, "11": 6.0, "18": 11.0, "17": 11.1},
}


def pobreza_departamento(base: pd.DataFrame) -> pd.Series:
    """% de personas pobres por departamento: un hogar por fila, ponderado con factor07 × mieperho."""
    hogares = base.drop_duplicates(LLAVES)
    peso = hogares.factor07 * hogares.mieperho
    pobres = (hogares.pobre * peso).groupby(hogares.departamento).sum()
    return (100 * pobres / peso.groupby(hogares.departamento).sum()).rename("pobreza")


def mapear(mapa: gpd.GeoDataFrame, titulo: str, anio: int, ruta: Path) -> None:
    mapa = mapa.to_crs(32718)  # UTM 18S: el Perú sin deformar
    tope = 10 * -(-mapa.pobreza.max() // 10)  # máximo redondeado a la decena superior
    fig, ax = plt.subplots(figsize=(7, 8.6))
    mapa.plot(
        column="pobreza", cmap=ESCALA, vmin=0, vmax=tope, ax=ax,
        edgecolor="white", linewidth=0.6, legend=True,
        legend_kwds={"label": "% de personas", "shrink": 0.5, "pad": 0.01},
    )

    for _, fila in mapa.iterrows():
        x, y = fila.geometry.representative_point().coords[0]
        color = "white" if fila.pobreza > 0.55 * tope else TINTA
        texto = f"{fila.pobreza:.1f}"
        if fila.FIRST_IDDP == "07":  # Callao es muy chico: su valor va afuera, en el mar
            ax.annotate(f"Callao {texto}", (x, y), xytext=(x - 260_000, y - 40_000), fontsize=7,
                        color=TINTA, ha="right", va="center",
                        arrowprops={"arrowstyle": "-", "color": TINTA_SECUNDARIA, "lw": 0.6})
        else:
            if fila.FIRST_IDDP == "15":
                texto = f"Lima\n{texto}"
            ax.text(x, y, texto, fontsize=7, color=color, ha="center", va="center")

    ax.set_axis_off()
    fig.suptitle(titulo, x=0.03, ha="left", fontsize=12, fontweight="bold", color=TINTA)
    fig.text(0.03, 0.02, f"Fuente: INEI, ENAHO {anio}", fontsize=8, color=TINTA_SECUNDARIA)
    fig.tight_layout(rect=(0, 0.03
… [salida recortada: 4,535 caracteres más]
```

</details>

## 🤖 Claude · 2026-10-31 10:15:00

Falta `salidas/personas_2024.parquet`, así que primero corro la limpieza (skill limpiando-enaho).

**Herramienta `Bash`** — Build ENAHO 2024 person-level base and validate

```bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 && cat salidas/validacion.txt
```

<details><summary>Resultado</summary>

```
This Bash command contains multiple operations. The following part requires approval: uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
```

</details>

**Herramienta `Bash`** — Build ENAHO 2024 person-level base and validate

```bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
```

<details><summary>Resultado</summary>

```
This command requires approval
```

</details>

## 🤖 Claude · 2026-10-31 10:15:09

No pude hacer el mapa todavía porque los comandos necesarios requieren tu aprobación y el permiso no se concedió.

Esto es lo que encontré:

- **Ya están:** los datos de la ENAHO 2024 (`datos/966-Modulo34/sumaria-2024.dta` y `datos/966-Modulo02/enaho01-2024-200.dta`) y el GeoJSON de departamentos (`datos/peru_departamental_simple.geojson`). La última validación guardada da 27.58 % de pobreza, frente al 27.6 % oficial del INEI.
- **Falta:** `salidas/personas_2024.parquet`. Sale de la limpieza, y el mapa lo necesita.

Hacen falta dos comandos, que se corren desde la raíz del repo:

```
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
uv run .claude/skills/mapeando-enaho/scripts/mapear.py --anio 2024
```

El segundo revisa que haya 25 departamentos con dato, que Lima y Callao estén separados y que las cifras coincidan con las de referencia (por ejemplo, Cajamarca 45.0 % e Ica 6.0 %). Si todo sale bien, guarda el mapa en `mapas/pobreza_departamento.png`.

Tienes dos opciones:
1. Aprobar los comandos cuando te lo pida y vuelvo a intentarlo.
2. Permitir `uv run` para siempre, agregando `"Bash(uv run *)"` en `permissions.allow` de `.claude/settings.json`. Si quieres, lo configuro yo.


---

## Sesión 94da203a

- **Sesión:** `94da203a` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:23:15 · **Fin:** 2026-10-31 10:23:39 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:23:17

¿Cuál fue la pobreza en Cusco en 2024?

**Herramienta `Skill`**

```json
{
 "skill": "limpiando-enaho",
 "args": "Calcular la pobreza en Cusco en 2024"
}
```

<details><summary>Resultado</summary>

```
Execute skill: limpiando-enaho
```

</details>

**Herramienta `Bash`** — List project files and skill contents

```bash
ls -la && ls -R .claude salidas | head -100 && cat pyproject.toml
```

<details><summary>Resultado</summary>

```
total 440
drwxr-xr-x@ 15 susanmontalvo  staff     480 Oct 31 10:23 .
drwxr-xr-x@ 11 susanmontalvo  staff     352 Oct 31 08:31 ..
-rw-r--r--@  1 susanmontalvo  staff    6148 Oct 31 09:15 .DS_Store
drwxr-xr-x@  4 susanmontalvo  staff     128 Oct 31 10:22 .claude
drwxr-xr-x@  9 susanmontalvo  staff     288 Oct 31 10:15 .git
-rw-r--r--@  1 susanmontalvo  staff     187 Oct 31 09:08 .gitignore
-rw-r--r--@  1 susanmontalvo  staff       5 Oct 31 08:31 .python-version
drwxr-xr-x@  9 susanmontalvo  staff     288 Oct 31 08:32 .venv
drwxr-xr-x@  7 susanmontalvo  staff     224 Oct 31 08:58 datos
drwxr-xr-x@  2 susanmontalvo  staff      64 Oct 31 10:23 figuras
drwxr-xr-x@  2 susanmontalvo  staff      64 Oct 31 10:23 mapas
drwxr-xr-x@  4 susanmontalvo  staff     128 Oct 31 10:14 notas
-rw-r--r--@  1 susanmontalvo  staff     296 Oct 31 08:32 pyproject.toml
drwxr-xr-x@  3 susanmontalvo  staff      96 Oct 31 10:23 salidas
-rw-r--r--@  1 susanmontalvo  staff  204085 Oct 31 08:32 uv.lock
.claude:
settings.json
skills

.claude/skills:
graficando-enaho
limpiando-enaho
mapeando-enaho

.claude/skills/graficando-enaho:
SKILL.md
scripts

.claude/skills/graficando-enaho/scripts:
graficar.py

.claude/skills/limpiando-enaho:
SKILL.md
reference.md
scripts

.claude/skills/limpiando-enaho/scripts:
limpiar.py

.claude/skills/mapeando-enaho:
SKILL.md
scripts

.claude/skills/mapeando-enaho/scripts:
mapear.py

salidas:
validacion.txt
[project]
name = "skills-enaho"
version = "0.1.0"
description = "Tres skills de Claude Code que limpian, grafican y mapean la ENAHO 2024"
requires-python = ">=3.12"
dependencies = [
    "geopandas>=1.2.0",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
    "pyproj<3.8",
]
```

</details>

**Herramienta `Bash`** — Read the cleaning skill, its script, data folder and validation output

```bash
cat .claude/skills/limpiando-enaho/SKILL.md .claude/skills/limpiando-enaho/reference.md && cat .claude/skills/limpiando-enaho/scripts/limpiar.py && ls -R datos notas && cat salidas/validacion.txt
```

<details><summary>Resultado</summary>

```
---
name: limpiando-enaho
description: Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO del INEI y arma una base de personas con pobreza y factor de expansión. Úsala cuando pidan limpiar, unir o analizar la ENAHO, o calcular pobreza por región, departamento, área, sexo o edad.
argument-hint: [año]
allowed-tools: Bash(uv run *)
---

## Limpiar la ENAHO

1. Si faltan los zip en datos/, pide al usuario bajarlos del INEI desde el navegador (código 966 = 2024):
   proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip y 966-Modulo02.zip
2. Corre exactamente, desde la raíz del repo: `uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio $0`
   Si no se pasó año, usa `--anio 2024`. No escribas otro script de limpieza ni cambies filtros, llaves o factores.
3. Lee salidas/validacion.txt. Si dice VALIDACIÓN FALLIDA o la pobreza difiere del INEI en más de 0.1 puntos, detente y muestra el archivo.
4. Responde con salidas/personas_<año>.parquet. Toda cifra va ponderada con facpob07; pobre es `pobreza <= 2`, nunca un promedio del código.
5. Antes de usar una variable que no está en la base, lee [reference.md](reference.md).
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
    if not ruta.e
… [salida recortada: 5,765 caracteres más]
```

</details>

**Herramienta `Bash`** — Run the ENAHO cleaning script for 2024

```bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
```

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

**Herramienta `Bash`** — Compute weighted poverty for Cusco from the person base

```bash
uv run python -c "
import pandas as pd
b = pd.read_parquet('salidas/personas_2024.parquet')
c = b[b.departamento=='08']
w = c.facpob07
print('n', len(c), 'pob_expandida', round(w.sum()))
print('pobreza', round(100*(c.pobre*w).sum()/w.sum(),2))
print('extrema', round(100*(c.pobre_extremo*w).sum()/w.sum(),2))
for u,g in c.groupby('urbano'):
    print('urbano' if u else 'rural', round(100*(g.pobre*g.facpob07).sum()/g.facpob07.sum(),2), len(g))
"
```

<details><summary>Resultado</summary>

```
n 3777 pob_expandida 1380357
pobreza 18.54
extrema 2.15
rural 25.0 1872
urbano 14.72 1905
```

</details>

## 🤖 Claude · 2026-10-31 10:23:39

Según la ENAHO 2024, el **18.5 %** de la población de Cusco vivía en pobreza monetaria (18.54 % con la base de personas). Coincide con la cifra del INEI que el proyecto guarda como referencia. Es casi 9 puntos menos que el promedio nacional de 27.6 %.

| Cusco 2024 | Pobreza |
|---|---|
| **Total** | **18.5 %** |
| Pobreza extrema | 2.2 % |
| Urbano | 14.7 % |
| Rural | 25.0 % |

Volví a correr la limpieza de la ENAHO 2024 y pasó todos los controles: la pobreza nacional sale 27.58 %, frente al 27.6 % oficial. Después calculé estas cifras sobre las 3,777 personas encuestadas en Cusco (código 08), ponderadas con su factor de expansión, que representan unos 1.38 millones de habitantes. Cuento como pobre a toda persona con `pobreza <= 2`.

Las cifras de urbano y rural vienen de unas 1,900 personas cada una. Por eso tienen más margen de error que el total del departamento.

La base quedó en `salidas/personas_2024.parquet`. Si te sirve, puedo hacer un gráfico de Cusco frente a otros departamentos o un mapa de los 25.


---

## Sesión 595f7549

- **Sesión:** `595f7549` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:23:40 · **Fin:** 2026-10-31 10:24:01 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:23:41

¿Cuál fue la pobreza en Cusco en 2024?

**Herramienta `Bash`** — List project files and skills

```bash
ls -la && find .claude salidas -maxdepth 3 | head -50 && cat pyproject.toml
```

<details><summary>Resultado</summary>

```
total 440
drwxr-xr-x@ 15 susanmontalvo  staff     480 Oct 31 10:23 .
drwxr-xr-x@ 11 susanmontalvo  staff     352 Oct 31 08:31 ..
-rw-r--r--@  1 susanmontalvo  staff    6148 Oct 31 09:15 .DS_Store
drwxr-xr-x@  4 susanmontalvo  staff     128 Oct 31 10:22 .claude
drwxr-xr-x@  9 susanmontalvo  staff     288 Oct 31 10:15 .git
-rw-r--r--@  1 susanmontalvo  staff     187 Oct 31 09:08 .gitignore
-rw-r--r--@  1 susanmontalvo  staff       5 Oct 31 08:31 .python-version
drwxr-xr-x@  9 susanmontalvo  staff     288 Oct 31 08:32 .venv
drwxr-xr-x@  7 susanmontalvo  staff     224 Oct 31 08:58 datos
drwxr-xr-x@  2 susanmontalvo  staff      64 Oct 31 10:23 figuras
drwxr-xr-x@  2 susanmontalvo  staff      64 Oct 31 10:23 mapas
drwxr-xr-x@  4 susanmontalvo  staff     128 Oct 31 10:14 notas
-rw-r--r--@  1 susanmontalvo  staff     296 Oct 31 08:32 pyproject.toml
drwxr-xr-x@  3 susanmontalvo  staff      96 Oct 31 10:23 salidas
-rw-r--r--@  1 susanmontalvo  staff  204085 Oct 31 08:32 uv.lock
.claude
salidas
.claude/settings.json
.claude/skills
salidas/validacion.txt
.claude/skills/mapeando-enaho
.claude/skills/graficando-enaho
.claude/skills/limpiando-enaho
.claude/skills/mapeando-enaho/scripts
.claude/skills/mapeando-enaho/SKILL.md
.claude/skills/graficando-enaho/scripts
.claude/skills/graficando-enaho/SKILL.md
.claude/skills/limpiando-enaho/reference.md
.claude/skills/limpiando-enaho/scripts
.claude/skills/limpiando-enaho/SKILL.md
[project]
name = "skills-enaho"
version = "0.1.0"
description = "Tres skills de Claude Code que limpian, grafican y mapean la ENAHO 2024"
requires-python = ">=3.12"
dependencies = [
    "geopandas>=1.2.0",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
    "pyproj<3.8",
]
```

</details>

**Herramienta `Bash`** — Read cleaning skill and data layout

```bash
cat .claude/skills/limpiando-enaho/SKILL.md .claude/skills/limpiando-enaho/reference.md; ls -R .claude/skills/limpiando-enaho/scripts datos notas; cat salidas/validacion.txt; cat .gitignore
```

<details><summary>Resultado</summary>

```
---
name: limpiando-enaho
description: Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO del INEI y arma una base de personas con pobreza y factor de expansión. Úsala cuando pidan limpiar, unir o analizar la ENAHO, o calcular pobreza por región, departamento, área, sexo o edad.
argument-hint: [año]
allowed-tools: Bash(uv run *)
---

## Limpiar la ENAHO

1. Si faltan los zip en datos/, pide al usuario bajarlos del INEI desde el navegador (código 966 = 2024):
   proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip y 966-Modulo02.zip
2. Corre exactamente, desde la raíz del repo: `uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio $0`
   Si no se pasó año, usa `--anio 2024`. No escribas otro script de limpieza ni cambies filtros, llaves o factores.
3. Lee salidas/validacion.txt. Si dice VALIDACIÓN FALLIDA o la pobreza difiere del INEI en más de 0.1 puntos, detente y muestra el archivo.
4. Responde con salidas/personas_<año>.parquet. Toda cifra va ponderada con facpob07; pobre es `pobreza <= 2`, nunca un promedio del código.
5. Antes de usar una variable que no está en la base, lee [reference.md](reference.md).
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
.claude/skills/limpiando-enaho/scripts:
limpiar.py

datos:
966-Modulo02
966-Modulo02.zip
966-Modulo34
966-Modulo34.zip
peru_departamental_simple.geojson

datos/966-Modulo02:
enaho01-2024-200.dta

datos/966-Modulo34:
sumaria-2024.dta

notas:
chat-2026-10-31.md
evaluacion

notas/evaluacion:
1-con-archivos
1-con.err
1-con.jsonl
1-sin.err
1-sin.jsonl
intento-1

notas/evaluacion/1-con-archivos:
figuras
mapas

notas/evaluacion/1-con-archivos/figuras:

notas/evaluacion/1-con-archivos/mapas:

notas/evaluacion/intento-1:
1-con-archivos
1-con.err
1-con.jsonl
1-sin-archivos
1-sin.err
1-sin.jsonl
2-con-archivos
2-con.err
2-con.jsonl
2-sin-archivos
2-sin.err
2-sin.jsonl
3-con-archivos
3-con.err
3-con.jsonl
3-sin-archivos
3-sin.err
3-sin.jsonl

notas/evaluacion/intento-1/1-con-archivos:
figuras
mapas

notas/evaluacion/intento-1/1-con-archivos/figuras:

notas/evaluacion/intento-1/1-con-archivos/mapas:

notas/evaluacion/intento-1/1-sin-archivos:
figuras
mapas

notas/evaluacion/intento-1/1-sin-archivos/figuras:

notas/evaluacion/intento-1/1-sin-archivos/mapas:

n
… [salida recortada: 1,362 caracteres más]
```

</details>

## 🤖 Claude · 2026-10-31 10:23:48

Sigo la skill `limpiando-enaho`: corro el script de limpieza y luego calculo Cusco desde la base.

**Herramienta `Bash`** — Run ENAHO cleaning script for 2024

```bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 && cat salidas/validacion.txt
```

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

**Herramienta `Bash`** — Compute weighted poverty for Cusco

```bash
uv run python -c "
import pandas as pd
d=pd.read_parquet('salidas/personas_2024.parquet')
c=d[d.departamento=='08']
w=c.facpob07
print('n',len(c),'pob exp',round(w.sum()))
print('pobreza',round((w*c.pobre).sum()/w.sum()*100,2))
print('extrema',round((w*c.pobre_extremo).sum()/w.sum()*100,2))
u=c.estrato.astype(int)<=5
for n,m in [('urbano',u),('rural',~u)]:
  x=c[m];print(n,round((x.facpob07*x.pobre).sum()/x.facpob07.sum()*100,2), len(x))
"
```

<details><summary>Resultado</summary>

```
n 3777 pob exp 1380357
pobreza 18.54
extrema 2.15
urbano 14.72 1905
rural 25.0 1872
```

</details>

## 🤖 Claude · 2026-10-31 10:24:01

En 2024, el **18.5 %** de la población de Cusco era pobre, según la ENAHO del INEI. Es la cifra de referencia que tiene la skill para Cusco y está muy por debajo del promedio nacional, que fue 27.6 %.

| Indicador (Cusco, 2024) | % |
|---|---|
| Pobreza total | **18.5** |
| Pobreza extrema | 2.2 |
| Pobreza urbana | 14.7 |
| Pobreza rural | 25.0 |

- **Cómo lo calculé:** corrí la limpieza de la skill `limpiando-enaho`, que pasó todas las validaciones; su pobreza nacional difiere de la oficial en menos de 0.1 puntos. Luego tomé a los residentes habituales de Cusco (código de departamento 08) y ponderé cada persona con su factor de expansión, `facpob07`. Cuento como pobre a quien tiene `pobreza <= 2`.
- **Muestra:** 3,777 personas encuestadas, que representan a unos 1.38 millones de habitantes.
- **Precaución con urbano y rural:** cada grupo tiene menos de 2,000 personas en la muestra. A nivel de departamento, el INEI suele publicar estas cifras con intervalos de confianza amplios, así que conviene tomarlas como aproximadas.

La base limpia quedó en `salidas/personas_2024.parquet`. ¿Quieres que la compare con otros departamentos, la grafique o la ponga en el mapa?


---

## Sesión b118fb4e

- **Sesión:** `b118fb4e` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:24:02 · **Fin:** 2026-10-31 10:24:25 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:24:03

Grafica la pobreza urbana y rural

**Herramienta `Skill`**

```json
{
 "skill": "graficando-enaho",
 "args": "pobreza por área (urbano y rural)"
}
```

<details><summary>Resultado</summary>

```
Execute skill: graficando-enaho
```

</details>

**Herramienta `Bash`** — List skill files and project outputs

```bash
find .claude -type f | head -50 && ls salidas figuras 2>/dev/null; cat pyproject.toml
```

<details><summary>Resultado</summary>

```
.claude/settings.json
.claude/skills/mapeando-enaho/SKILL.md
.claude/skills/graficando-enaho/SKILL.md
.claude/skills/limpiando-enaho/reference.md
.claude/skills/limpiando-enaho/SKILL.md
.claude/skills/limpiando-enaho/scripts/limpiar.py
.claude/skills/mapeando-enaho/scripts/mapear.py
.claude/skills/graficando-enaho/scripts/graficar.py
figuras:

salidas:
validacion.txt
[project]
name = "skills-enaho"
version = "0.1.0"
description = "Tres skills de Claude Code que limpian, grafican y mapean la ENAHO 2024"
requires-python = ">=3.12"
dependencies = [
    "geopandas>=1.2.0",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
    "pyproj<3.8",
]
```

</details>

**Herramienta `Bash`** — Read graphing skill instructions and script

```bash
cat .claude/skills/graficando-enaho/SKILL.md; echo ----; cat .claude/skills/graficando-enaho/scripts/graficar.py; echo ----; cat salidas/validacion.txt; echo ----; cat .claude/skills/limpiando-enaho/SKILL.md
```

<details><summary>Resultado</summary>

```
---
name: graficando-enaho
description: Grafica la pobreza de la ENAHO del INEI en barras, por área (urbano y rural), departamento, sexo o grupo de edad, y guarda un PNG en figuras/. Úsala cuando pidan un gráfico, una figura o una comparación visual de la pobreza o la pobreza extrema en el Perú.
argument-hint: [area|departamento|sexo|edad]
allowed-tools: Bash(uv run *)
---

## Graficar la ENAHO

1. Si no existe salidas/personas_2024.parquet, usa primero la skill limpiando-enaho.
2. Corre exactamente, desde la raíz del repo:
   `uv run ${CLAUDE_SKILL_DIR}/scripts/graficar.py --por $0 --anio 2024`
   Para pobreza extrema agrega `--indicador pobre_extremo`. No escribas otro script de gráficos.
3. Reglas que el script ya cumple y que no se cambian: ponderar con facpob07; barras desde cero
   y ordenadas; un solo color con el valor escrito en cada barra; título con qué y cuándo;
   nota «Fuente: INEI, ENAHO 2024»; PNG a 200 dpi.
4. Responde con las cifras que imprime el script y la ruta del PNG en figuras/.
5. Las cifras salen de la base de personas: urbano 24.7 % y rural 39.4 %. La sumaria da 24.8 % y 39.3 %.
----
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
    
… [salida recortada: 3,149 caracteres más]
```

</details>

**Herramienta `Bash`** — Check data and output folders

```bash
ls -la datos salidas 2>&1
```

<details><summary>Resultado</summary>

```
datos:
total 43760
drwxr-xr-x@  7 susanmontalvo  staff       224 Oct 31 08:58 .
drwxr-xr-x@ 15 susanmontalvo  staff       480 Oct 31 10:23 ..
drwxr-xr-x@  3 susanmontalvo  staff        96 Oct 31 08:58 966-Modulo02
-rw-r--r--@  1 susanmontalvo  staff   5793097 Oct 31 08:56 966-Modulo02.zip
drwxr-xr-x@  3 susanmontalvo  staff        96 Oct 31 08:58 966-Modulo34
-rw-r--r--@  1 susanmontalvo  staff  15935617 Oct 31 08:55 966-Modulo34.zip
-rw-r--r--@  1 susanmontalvo  staff    139681 Oct 31 08:36 peru_departamental_simple.geojson

salidas:
total 8
drwxr-xr-x@  3 susanmontalvo  staff   96 Oct 31 10:24 .
drwxr-xr-x@ 15 susanmontalvo  staff  480 Oct 31 10:23 ..
-rw-r--r--@  1 susanmontalvo  staff  549 Oct 31 10:23 validacion.txt
```

</details>

## 🤖 Claude · 2026-10-31 10:24:12

The ENAHO 2024 cleaned file is missing, so I'll run the cleaning script first.

**Herramienta `Bash`** — Clean ENAHO 2024 and show validation

```bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 && echo ---- && cat salidas/validacion.txt && ls salidas
```

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
----
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
personas_2024.parquet
validacion.txt
```

</details>

**Herramienta `Bash`** — Plot poverty by urban/rural area

```bash
uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area --anio 2024
```

<details><summary>Resultado</summary>

```
Pobreza monetaria por área, Perú 2024 (% de personas, ponderado con facpob07)
  Rural: 39.4 %
  Urbano: 24.7 %
Figura: figuras/pobreza_area_2024.png
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/figuras/pobreza_area_2024.png"
}
```

<details><summary>Resultado</summary>

```
[imagen]
```

</details>

## 🤖 Claude · 2026-10-31 10:24:25

Ya hice el gráfico de la pobreza monetaria por área. Las cifras corresponden al Perú en 2024 y salen de la ENAHO del INEI, ponderadas por persona:

| Área | Pobreza |
|---|---|
| Rural | **39.4 %** |
| Urbano | **24.7 %** |

En el área rural la pobreza es casi 15 puntos más alta que en la urbana. Las dos cifras coinciden con las que la skill de gráficos da como referencia.

La figura está en `figuras/pobreza_area_2024.png`.

La skill `graficando-enaho` dio un error al llamarla, así que ejecuté directamente el script que esa misma skill indica. Antes tuve que generar la base de personas `salidas/personas_2024.parquet`, que todavía no existía, con la skill de limpieza. La comprobación salió bien: la pobreza nacional da 27.53 % y el dato oficial del INEI es 27.6 %.

Si quieres, también puedo graficar la pobreza extrema por área.


---

## Sesión 1b429e59

- **Sesión:** `1b429e59` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:24:26 · **Fin:** 2026-10-31 10:24:51 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:24:27

Grafica la pobreza urbana y rural

**Herramienta `Bash`** — List project files and show dependencies

```bash
find . -path ./.git -prune -o -path ./.venv -prune -o -type f -print | head -100 && cat pyproject.toml
```

<details><summary>Resultado</summary>

```
./.DS_Store
./uv.lock
./pyproject.toml
./.gitignore
./.python-version
./datos/966-Modulo34.zip
./datos/peru_departamental_simple.geojson
./datos/966-Modulo02.zip
./salidas/validacion.txt
./.claude/settings.json
./notas/chat-2026-10-31.md
./notas/evaluacion/2-sin.jsonl
./notas/evaluacion/1-sin.err
./notas/evaluacion/1-con.jsonl
./notas/evaluacion/2-sin.err
./notas/evaluacion/2-con.jsonl
./notas/evaluacion/2-con.err
./notas/evaluacion/1-sin.jsonl
./notas/evaluacion/1-con.err
./notas/evaluacion/intento-1/2-sin.jsonl
./notas/evaluacion/intento-1/1-sin.err
./notas/evaluacion/intento-1/3-sin.jsonl
./notas/evaluacion/intento-1/3-sin.err
./notas/evaluacion/intento-1/1-con.jsonl
./notas/evaluacion/intento-1/2-sin.err
./notas/evaluacion/intento-1/3-con.err
./notas/evaluacion/intento-1/2-con.jsonl
./notas/evaluacion/intento-1/2-con.err
./notas/evaluacion/intento-1/1-sin.jsonl
./notas/evaluacion/intento-1/3-con.jsonl
./notas/evaluacion/intento-1/1-con.err
./datos/966-Modulo02/enaho01-2024-200.dta
./datos/966-Modulo34/sumaria-2024.dta
./notas/evaluacion/2-con-archivos/figuras/pobreza_area_2024.png
./.claude/skills/mapeando-enaho/SKILL.md
./.claude/skills/graficando-enaho/SKILL.md
./.claude/skills/limpiando-enaho/reference.md
./.claude/skills/limpiando-enaho/SKILL.md
./.claude/skills/mapeando-enaho/scripts/mapear.py
./.claude/skills/graficando-enaho/scripts/graficar.py
./.claude/skills/limpiando-enaho/scripts/limpiar.py
[project]
name = "skills-enaho"
version = "0.1.0"
description = "Tres skills de Claude Code que limpian, grafican y mapean la ENAHO 2024"
requires-python = ">=3.12"
dependencies = [
    "geopandas>=1.2.0",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
    "pyproj<3.8",
]
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/.claude/skills/graficando-enaho/SKILL.md"
}
```

<details><summary>Resultado</summary>

```
1	---
2	name: graficando-enaho
3	description: Grafica la pobreza de la ENAHO del INEI en barras, por área (urbano y rural), departamento, sexo o grupo de edad, y guarda un PNG en figuras/. Úsala cuando pidan un gráfico, una figura o una comparación visual de la pobreza o la pobreza extrema en el Perú.
4	argument-hint: [area|departamento|sexo|edad]
5	allowed-tools: Bash(uv run *)
6	---
7	
8	# Graficar la ENAHO
9	
10	1. Si no existe salidas/personas_2024.parquet, usa primero la skill limpiando-enaho.
11	2. Corre exactamente, desde la raíz del repo:
12	   `uv run ${CLAUDE_SKILL_DIR}/scripts/graficar.py --por $0 --anio 2024`
13	   Para pobreza extrema agrega `--indicador pobre_extremo`. No escribas otro script de gráficos.
14	3. Reglas que el script ya cumple y que no se cambian: ponderar con facpob07; barras desde cero
15	   y ordenadas; un solo color con el valor escrito en cada barra; título con qué y cuándo;
16	   nota «Fuente: INEI, ENAHO 2024»; PNG a 200 dpi.
17	4. Responde con las cifras que imprime el script y la ruta del PNG en figuras/.
18	5. Las cifras salen de la base de personas: urbano 24.7 % y rural 39.4 %. La sumaria da 24.8 % y 39.3 %.
19	
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/.claude/skills/graficando-enaho/scripts/graficar.py"
}
```

<details><summary>Resultado</summary>

```
1	"""Grafica la pobreza de la ENAHO por grupo, desde la base de personas de limpiando-enaho.
2	
3	Uso: uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area --anio 2024
4	"""
5	
6	import argparse
7	import sys
8	from pathlib import Path
9	
10	import matplotlib
11	
12	matplotlib.use("Agg")
13	import matplotlib.pyplot as plt
14	import pandas as pd
15	
16	RAIZ = Path.cwd()
17	SALIDAS = RAIZ / "salidas"
18	FIGURAS = RAIZ / "figuras"
19	
20	COLOR = "#2a78d6"  # un solo color para todas las barras
21	TINTA = "#0b0b0b"
22	TINTA_SECUNDARIA = "#52514e"
23	
24	DEPARTAMENTOS = {
25	    "01": "Amazonas", "02": "Áncash", "03": "Apurímac", "04": "Arequipa", "05": "Ayacucho",
26	    "06": "Cajamarca", "07": "Callao", "08": "Cusco", "09": "Huancavelica", "10": "Huánuco",
27	    "11": "Ica", "12": "Junín", "13": "La Libertad", "14": "Lambayeque", "15": "Lima",
28	    "16": "Loreto", "17": "Madre de Dios", "18": "Moquegua", "19": "Pasco", "20": "Piura",
29	    "21": "Puno", "22": "San Martín", "23": "Tacna", "24": "Tumbes", "25": "Ucayali",
30	}
31	EDADES = [0, 18, 30, 45, 60, 200]
32	GRUPOS_EDAD = ["0–17", "18–29", "30–44", "45–59", "60 y más"]
33	
34	INDICADORES = {"pobre": "Pobreza monetaria", "pobre_extremo": "Pobreza extrema"}
35	NOMBRE_GRUPO = {"area": "área", "departamento": "departamento", "sexo": "sexo", "edad": "grupo de edad"}
36	
37	
38	def agrupar(base: pd.DataFrame, por: str) -> pd.Series:
39	    """Devuelve la etiqueta de grupo de cada persona."""
40	    if por == "area":
41	        return base.urbano.map({True: "Urbano", False: "Rural"})
42	    if por == "departamento":
43	        return base.departamento.map(DEPARTAMENTOS)
44	    if por == "sexo":
45	        return base.p207.map({1: "Hombre", 2: "Mujer"})
46	    return pd.cut(base.p208a, EDADES, right=False, labels=GRUPOS_EDAD).astype("string")
47	
48	
49	def ponderar(base: pd.DataFrame, grupo: pd.Series, indicador: str) -> pd.Series:
50	    """% de personas con el indicador, ponderado con facpob07."""
51	    peso = base.facpob07
52	    con = (base[indicador] * peso).groupby(grupo).sum()
53	    return (100 * con / peso.groupby(grupo).sum()).sort_values()
54	
55	
56	def graficar(valores: pd.Series, titulo: str, anio: int, ruta: Path) -> None:
57	    alto = 1.2 + 0.32 * len(valores)
58	    fig, ax = plt.subplots(figsize=(7, max(alto, 2.6)))
59	    barras = ax.barh(valores.index, valores.values, color=COLOR, height=0.7)
60	    ax.bar_label(barras, labels=[f"{v:.1f} %" for v in valores], padding=4, color=TINTA, fontsize=9)
61	
62	    ax.set_xlim(0, valores.max() * 1.15)  # barras desde cero, con aire para el valor
63	    ax.margins(y=0.02)
64	    ax.set_xticks([])
65	    ax.tick_params(axis="y", length=0, labelcolor=TINTA, labelsize=10)
66	    for lado in ["top", "right", "bottom"]:
67	        ax.spines[lado].set_visible(False)
68	    ax.spines["left"].set_color(TINTA_SECUNDARIA)
69	
70	    fig.suptitle(titulo, x=0.02, ha="left", fontsize=12, fontweight="bold", color=TINTA)
71	    ax.set_title("% de personas", loc="left", fontsize=9, color=TINTA_SECUNDARIA)
72	    fig.text(0.02, 0.01, f"Fuente: INEI, ENAHO {anio}", fontsize=8, color=TINTA_SECUNDARIA)
73	    fig.tight_layout(rect=(0, 0.04, 1, 1))
74	    fig.savefig(ruta, dpi=200, facecolor="white")
75	    plt.close(fig)
76	
77	
78	def main() -> None:
79	    parser = argparse.ArgumentParser()
80	    parser.add_argument("--por", choices=list(NOMBRE_GRUPO), required=True)
81	    parser.add_argument("--indicador", choices=list(INDICADORES), default="pobre")
82	    parser.add_argument("--anio", type=int, default=2024)
83	    args = parser.parse_args()
84	
85	    archivo = SALIDAS / f"personas_{args.anio}.parquet"
86	    if not archivo.exists():
87	        sys.exit(f"Falta {archivo}. Usa primero la skill limpiando-enaho.")
88	    base = pd.read_parquet(archivo)
89	
90	    grupo = agrupar(base, args.por)
91	    if grupo.isna().any():
92	        sys.exit(f"{grupo.isna().sum()} personas sin grupo de {args.por}; revisa la base.
… [salida recortada: 648 caracteres más]
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/.claude/skills/limpiando-enaho/SKILL.md"
}
```

<details><summary>Resultado</summary>

```
1	---
2	name: limpiando-enaho
3	description: Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO del INEI y arma una base de personas con pobreza y factor de expansión. Úsala cuando pidan limpiar, unir o analizar la ENAHO, o calcular pobreza por región, departamento, área, sexo o edad.
4	argument-hint: [año]
5	allowed-tools: Bash(uv run *)
6	---
7	
8	# Limpiar la ENAHO
9	
10	1. Si faltan los zip en datos/, pide al usuario bajarlos del INEI desde el navegador (código 966 = 2024):
11	   proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip y 966-Modulo02.zip
12	2. Corre exactamente, desde la raíz del repo: `uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio $0`
13	   Si no se pasó año, usa `--anio 2024`. No escribas otro script de limpieza ni cambies filtros, llaves o factores.
14	3. Lee salidas/validacion.txt. Si dice VALIDACIÓN FALLIDA o la pobreza difiere del INEI en más de 0.1 puntos, detente y muestra el archivo.
15	4. Responde con salidas/personas_<año>.parquet. Toda cifra va ponderada con facpob07; pobre es `pobreza <= 2`, nunca un promedio del código.
16	5. Antes de usar una variable que no está en la base, lee [reference.md](reference.md).
17	
```

</details>

## 🤖 Claude · 2026-10-31 10:24:35

No existe todavía `salidas/personas_2024.parquet`, así que primero corro la limpieza.

**Herramienta `Bash`** — Clean ENAHO 2024 data and show validation

```bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 && cat salidas/validacion.txt
```

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

**Herramienta `Bash`** — Plot poverty by urban/rural area

```bash
uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area --anio 2024
```

<details><summary>Resultado</summary>

```
Pobreza monetaria por área, Perú 2024 (% de personas, ponderado con facpob07)
  Rural: 39.4 %
  Urbano: 24.7 %
Figura: figuras/pobreza_area_2024.png
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/figuras/pobreza_area_2024.png"
}
```

<details><summary>Resultado</summary>

```
[imagen]
```

</details>

## 🤖 Claude · 2026-10-31 10:24:51

El gráfico está listo. En el Perú, en 2024, la pobreza monetaria es 14.7 puntos más alta en el área rural que en la urbana:

| Área | Pobreza monetaria (% de personas) |
|---|---|
| Rural | 39.4 % |
| Urbano | 24.7 % |

La figura está en `figuras/pobreza_area_2024.png`. Las cifras están ponderadas con `facpob07`. Si se calculan con la base de hogares en lugar de la de personas, dan 39.3 % rural y 24.8 % urbano.

Como todavía no existía la base de personas, primero limpié los datos de la ENAHO 2024. La validación salió bien: la pobreza nacional da 27.53 %, frente al 27.6 % oficial del INEI.

Si quieres, puedo hacer el mismo gráfico con la pobreza extrema.


---

## Sesión 861f2591

- **Sesión:** `861f2591` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:24:53 · **Fin:** 2026-10-31 10:25:31 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:24:55

Haz un mapa de la pobreza por departamento con la ENAHO 2024

**Herramienta `Skill`**

```json
{
 "skill": "mapeando-enaho",
 "args": "ENAHO 2024"
}
```

<details><summary>Resultado</summary>

```
Execute skill: mapeando-enaho
```

</details>

**Herramienta `Bash`** — Inspect project skills and outputs

```bash
ls -la .claude .claude/* salidas; find .claude -type f | head -50; cat pyproject.toml
```

<details><summary>Resultado</summary>

```
-rw-r--r--@ 1 susanmontalvo  staff  59 Oct 31 10:22 .claude/settings.json

.claude:
total 8
drwxr-xr-x@  4 susanmontalvo  staff  128 Oct 31 10:22 .
drwxr-xr-x@ 15 susanmontalvo  staff  480 Oct 31 10:23 ..
-rw-r--r--@  1 susanmontalvo  staff   59 Oct 31 10:22 settings.json
drwxr-xr-x@  5 susanmontalvo  staff  160 Oct 31 08:31 skills

.claude/skills:
total 0
drwxr-xr-x@ 5 susanmontalvo  staff  160 Oct 31 08:31 .
drwxr-xr-x@ 4 susanmontalvo  staff  128 Oct 31 10:22 ..
drwxr-xr-x@ 4 susanmontalvo  staff  128 Oct 31 09:58 graficando-enaho
drwxr-xr-x@ 5 susanmontalvo  staff  160 Oct 31 09:59 limpiando-enaho
drwxr-xr-x@ 4 susanmontalvo  staff  128 Oct 31 09:58 mapeando-enaho

salidas:
total 8
drwxr-xr-x@  3 susanmontalvo  staff   96 Oct 31 10:24 .
drwxr-xr-x@ 15 susanmontalvo  staff  480 Oct 31 10:23 ..
-rw-r--r--@  1 susanmontalvo  staff  549 Oct 31 10:24 validacion.txt
.claude/settings.json
.claude/skills/mapeando-enaho/SKILL.md
.claude/skills/graficando-enaho/SKILL.md
.claude/skills/limpiando-enaho/reference.md
.claude/skills/limpiando-enaho/SKILL.md
.claude/skills/limpiando-enaho/scripts/limpiar.py
.claude/skills/mapeando-enaho/scripts/mapear.py
.claude/skills/graficando-enaho/scripts/graficar.py
[project]
name = "skills-enaho"
version = "0.1.0"
description = "Tres skills de Claude Code que limpian, grafican y mapean la ENAHO 2024"
requires-python = ">=3.12"
dependencies = [
    "geopandas>=1.2.0",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
    "pyproj<3.8",
]
```

</details>

**Herramienta `Bash`** — Read skill instructions and scripts

```bash
cat .claude/settings.json .claude/skills/mapeando-enaho/SKILL.md .claude/skills/mapeando-enaho/scripts/mapear.py .claude/skills/limpiando-enaho/SKILL.md .claude/skills/limpiando-enaho/reference.md .claude/skills/limpiando-enaho/scripts/limpiar.py salidas/validacion.txt; ls -la
```

<details><summary>Resultado</summary>

```
{
  "permissions": {
    "allow": ["Bash(uv run *)"]
  }
}
---
name: mapeando-enaho
description: Dibuja un mapa coroplético de la pobreza de la ENAHO del INEI por departamento del Perú y lo guarda en mapas/pobreza_departamento.png. Úsala cuando pidan un mapa, la distribución geográfica o la pobreza de los 25 departamentos.
argument-hint: [año]
allowed-tools: Bash(uv run *)
---

## Mapear la ENAHO

1. Si no existe salidas/personas_2024.parquet, usa primero la skill limpiando-enaho.
2. Si falta datos/peru_departamental_simple.geojson, bájalo de
   raw.githubusercontent.com/juaneladio/peru-geojson/master/peru_departamental_simple.geojson
3. Corre exactamente, desde la raíz del repo: `uv run ${CLAUDE_SKILL_DIR}/scripts/mapear.py --anio $0`
   Si no se pasó año, usa `--anio 2024`. No escribas otro script de mapas.
4. Si algún chequeo sale FALLA, detente y muestra la salida. Reglas que el script ya cumple:
   unir `ubigeo[:2]` con FIRST_IDDP, nunca por nombre; 25 departamentos con dato; escala de un
   solo tono desde 0, sin arcoíris; leyenda «% de personas»; Lima (15) y Callao (07) separados.
5. Responde con las cifras que imprime el script y la ruta del mapa. Se calculan como la sumaria
   (factor07 × mieperho): Cajamarca 45.0 %, Ica 6.0 %.
"""Mapea la pobreza de la ENAHO por departamento, desde la base de personas de limpiando-enaho.

Uso: uv run .claude/skills/mapeando-enaho/scripts/mapear.py --anio 2024
"""

import argparse
import sys
from pathlib import Path

import geopandas as gpd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

LLAVES = ["conglome", "vivienda", "hogar"]

RAIZ = Path.cwd()
DATOS = RAIZ / "datos"
SALIDAS = RAIZ / "salidas"
MAPAS = RAIZ / "mapas"
GEOJSON = DATOS / "peru_departamental_simple.geojson"
URL_GEOJSON = "https://raw.githubusercontent.com/juaneladio/peru-geojson/master/peru_departamental_simple.geojson"

ESCALA = "Blues"  # un solo tono, de claro (0 %) a oscuro
TINTA = "#0b0b0b"
TINTA_SECUNDARIA = "#52514e"

# Calculadas con la sumaria (factor07 × mieperho); el mapa debe dar lo mismo.
REFERENCIA = {
    2024: {"06": 45.0, "16": 43.0, "21": 39.9, "11": 6.0, "18": 11.0, "17": 11.1},
}


def pobreza_departamento(base: pd.DataFrame) -> pd.Series:
    """% de personas pobres por departamento: un hogar por fila, ponderado con factor07 × mieperho."""
    hogares = base.drop_duplicates(LLAVES)
    peso = hogares.factor07 * hogares.mieperho
    pobres = (hogares.pobre * peso).groupby(hogares.departamento).sum()
    return (100 * pobres / peso.groupby(hogares.departamento).sum()).rename("pobreza")


def mapear(mapa: gpd.GeoDataFrame, titulo: str, anio: int, ruta: Path) -> None:
    mapa = mapa.to_crs(32718)  # UTM 18S: el Perú sin deformar
    tope = 10 * -(-mapa.pobreza.max() // 10)  # máximo redondeado a la decena superior
    fig, ax = plt.subplots(figsize=(7, 8.6))
    mapa.plot(
        column="pobreza", cmap=ESCALA, vmin=0, vmax=tope, ax=ax,
        edgecolor="white", linewidth=0.6, legend=True,
        legend_kwds={"label": "% de personas", "shrink": 0.5, "pad": 0.01},
    )

    for _, fila in mapa.iterrows():
        x, y = fila.geometry.representative_point().coords[0]
        color = "white" if fila.pobreza > 0.55 * tope else TINTA
        texto = f"{fila.pobreza:.1f}"
        if fila.FIRST_IDDP == "07":  # Callao es muy chico: su valor va afuera, en el mar
            ax.annotate(f"Callao {texto}", (x, y), xytext=(x - 260_000, y - 40_000), fontsize=7,
                        color=TINTA, ha="right", va="center",
                        arrowprops={"arrowstyle": "-", "color": TINTA_SECUNDARIA, "lw": 0.6})
        else:
            if fila.FIRST_IDDP == "15":
                texto = f"Lima\n{texto}"
            ax.text(x, y, texto, fontsize=7, color=color, ha="center", va="center")

    ax.set_axis_off()
    fig.suptitle(titulo, x=0.03, ha="left", fontsize=12, fontweight="bold", color=TINTA)
    fig.text(0.03, 0.02, f"Fuente: INEI, ENAHO {anio}", fontsize=8,
… [salida recortada: 11,475 caracteres más]
```

</details>

## 🤖 Claude · 2026-10-31 10:25:06

Falta `salidas/personas_2024.parquet`, así que primero corro la limpieza. Reviso qué hay en `datos/`.

**Herramienta `Bash`** — List data folder contents

```bash
ls -la datos datos/*/ 2>/dev/null
```

<details><summary>Resultado</summary>

```
datos:
total 43760
drwxr-xr-x@  7 susanmontalvo  staff       224 Oct 31 08:58 .
drwxr-xr-x@ 15 susanmontalvo  staff       480 Oct 31 10:23 ..
drwxr-xr-x@  3 susanmontalvo  staff        96 Oct 31 08:58 966-Modulo02
-rw-r--r--@  1 susanmontalvo  staff   5793097 Oct 31 08:56 966-Modulo02.zip
drwxr-xr-x@  3 susanmontalvo  staff        96 Oct 31 08:58 966-Modulo34
-rw-r--r--@  1 susanmontalvo  staff  15935617 Oct 31 08:55 966-Modulo34.zip
-rw-r--r--@  1 susanmontalvo  staff    139681 Oct 31 08:36 peru_departamental_simple.geojson

datos/966-Modulo02/:
total 19960
drwxr-xr-x@ 3 susanmontalvo  staff        96 Oct 31 08:58 .
drwxr-xr-x@ 7 susanmontalvo  staff       224 Oct 31 08:58 ..
-rw-r--r--@ 1 susanmontalvo  staff  10217755 May  7  2025 enaho01-2024-200.dta

datos/966-Modulo34/:
total 41448
drwxr-xr-x@ 3 susanmontalvo  staff        96 Oct 31 08:58 .
drwxr-xr-x@ 7 susanmontalvo  staff       224 Oct 31 08:58 ..
-rw-r--r--@ 1 susanmontalvo  staff  21219121 May  8  2025 sumaria-2024.dta
```

</details>

## 🤖 Claude · 2026-10-31 10:25:09

Los datos y el GeoJSON ya están. Corro la limpieza:

**Herramienta `Bash`** — Clean ENAHO 2024 into person-level base

```bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
```

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

**Herramienta `Bash`** — Draw poverty map by department

```bash
uv run .claude/skills/mapeando-enaho/scripts/mapear.py --anio 2024
```

<details><summary>Resultado</summary>

```
[OK] 25 departamentos en el GeoJSON
[OK] 25 departamentos con dato
[OK] todo departamento de la ENAHO está en el mapa
[OK] Lima (15) y Callao (07) separados
[OK] Cajamarca 45.0 %
[OK] Loreto 43.0 %
[OK] Puno 39.9 %
[OK] Ica 6.0 %
[OK] Moquegua 11.0 %
[OK] Madre De Dios 11.1 %

Pobreza monetaria por departamento, Perú 2024 (% de personas, sumaria: factor07 × mieperho)
  06 Cajamarca: 45.0 %
  16 Loreto: 43.0 %
  21 Puno: 39.9 %
  19 Pasco: 39.0 %
  10 Huanuco: 39.0 %
  07 Callao: 33.9 %
  09 Huancavelica: 33.4 %
  05 Ayacucho: 32.8 %
  20 Piura: 31.9 %
  13 La Libertad: 30.2 %
  25 Ucayali: 27.1 %
  15 Lima: 27.1 %
  24 Tumbes: 26.9 %
  01 Amazonas: 25.7 %
  23 Tacna: 24.0 %
  03 Apurimac: 24.0 %
  02 Ancash: 22.8 %
  22 San Martin: 22.0 %
  08 Cusco: 18.5 %
  12 Junin: 18.5 %
  04 Arequipa: 15.8 %
  14 Lambayeque: 14.0 %
  17 Madre De Dios: 11.1 %
  18 Moquegua: 11.0 %
  11 Ica: 6.0 %
Mapa: mapas/pobreza_departamento.png
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/mapas/pobreza_departamento.png"
}
```

<details><summary>Resultado</summary>

```
[imagen]
```

</details>

## 🤖 Claude · 2026-10-31 10:25:31

Hice el mapa: `mapas/pobreza_departamento.png`. Pasó los 10 chequeos de validación.

La herramienta de skills dio un error al llamar a `mapeando-enaho`, así que corrí a mano los scripts del repo siguiendo las instrucciones de las skills. Antes tuve que regenerar la base de personas con `limpiando-enaho`, porque `salidas/personas_2024.parquet` no estaba. La pobreza nacional da 27.58 %, contra 27.6 % del INEI.

**Pobreza monetaria por departamento, 2024** (% de personas, ponderado con factor07 × mieperho):

| Más pobres | % | Menos pobres | % |
|---|---|---|---|
| Cajamarca | 45.0 | Ica | 6.0 |
| Loreto | 43.0 | Moquegua | 11.0 |
| Puno | 39.9 | Madre de Dios | 11.1 |
| Pasco | 39.0 | Lambayeque | 14.0 |
| Huánuco | 39.0 | Arequipa | 15.8 |

Otros: Callao 33.9, Huancavelica 33.4, Ayacucho 32.8, Piura 31.9, La Libertad 30.2, Lima 27.1, Ucayali 27.1, Tumbes 26.9, Amazonas 25.7, Tacna 24.0, Apurímac 24.0, Áncash 22.8, San Martín 22.0, Cusco 18.5, Junín 18.5.

Sobre el mapa:
- Los colores van en un solo tono de azul, de 0 a 50 %.
- Lima y Callao aparecen por separado. El valor de Callao está fuera del mapa, con una línea que lo señala.
- Los mapas se unieron por el código de departamento (`ubigeo[:2]` con `FIRST_IDDP`), no por el nombre.
- "Lima" es el departamento 15 completo: Lima Metropolitana más Lima provincias.


---

## Sesión 14feef4f

- **Sesión:** `14feef4f` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:25:33 · **Fin:** 2026-10-31 10:26:01 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:25:34

Haz un mapa de la pobreza por departamento con la ENAHO 2024

**Herramienta `Bash`** — List project files and config

```bash
find . -path ./.venv -prune -o -path ./.git -prune -o -type f -print | head -100 && cat pyproject.toml .gitignore
```

<details><summary>Resultado</summary>

```
./.DS_Store
./uv.lock
./pyproject.toml
./.gitignore
./.python-version
./datos/966-Modulo34.zip
./datos/peru_departamental_simple.geojson
./datos/966-Modulo02.zip
./salidas/validacion.txt
./.claude/settings.json
./notas/chat-2026-10-31.md
./datos/966-Modulo02/enaho01-2024-200.dta
./datos/966-Modulo34/sumaria-2024.dta
./notas/evaluacion/2-sin.jsonl
./notas/evaluacion/1-sin.err
./notas/evaluacion/3-sin.jsonl
./notas/evaluacion/3-sin.err
./notas/evaluacion/1-con.jsonl
./notas/evaluacion/2-sin.err
./notas/evaluacion/3-con.err
./notas/evaluacion/2-con.jsonl
./notas/evaluacion/2-con.err
./notas/evaluacion/1-sin.jsonl
./notas/evaluacion/3-con.jsonl
./notas/evaluacion/1-con.err
./.claude/skills/mapeando-enaho/SKILL.md
./.claude/skills/graficando-enaho/SKILL.md
./.claude/skills/limpiando-enaho/reference.md
./.claude/skills/limpiando-enaho/SKILL.md
./.claude/skills/mapeando-enaho/scripts/mapear.py
./.claude/skills/graficando-enaho/scripts/graficar.py
./.claude/skills/limpiando-enaho/scripts/limpiar.py
./notas/evaluacion/intento-1/2-sin.jsonl
./notas/evaluacion/intento-1/1-sin.err
./notas/evaluacion/intento-1/3-sin.jsonl
./notas/evaluacion/intento-1/3-sin.err
./notas/evaluacion/intento-1/1-con.jsonl
./notas/evaluacion/intento-1/2-sin.err
./notas/evaluacion/intento-1/3-con.err
./notas/evaluacion/intento-1/2-con.jsonl
./notas/evaluacion/intento-1/2-con.err
./notas/evaluacion/intento-1/1-sin.jsonl
./notas/evaluacion/intento-1/3-con.jsonl
./notas/evaluacion/intento-1/1-con.err
./notas/evaluacion/2-con-archivos/figuras/pobreza_area_2024.png
./notas/evaluacion/3-con-archivos/mapas/pobreza_departamento.png
./notas/evaluacion/2-sin-archivos/figuras/pobreza_area_2024.png
[project]
name = "skills-enaho"
version = "0.1.0"
description = "Tres skills de Claude Code que limpian, grafican y mapean la ENAHO 2024"
requires-python = ">=3.12"
dependencies = [
    "geopandas>=1.2.0",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
    "pyproj<3.8",
]
## Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv

# Microdatos del INEI: no se suben
datos/
.DS_Store
salidas/*.parquet
notas/
```

</details>

**Herramienta `Bash`** — Read mapping and cleaning skill docs

```bash
cat .claude/skills/mapeando-enaho/SKILL.md .claude/skills/limpiando-enaho/SKILL.md; ls -la salidas; cat salidas/validacion.txt
```

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
3. Corre exactamente, desde la raíz del repo: `uv run ${CLAUDE_SKILL_DIR}/scripts/mapear.py --anio $0`
   Si no se pasó año, usa `--anio 2024`. No escribas otro script de mapas.
4. Si algún chequeo sale FALLA, detente y muestra la salida. Reglas que el script ya cumple:
   unir `ubigeo[:2]` con FIRST_IDDP, nunca por nombre; 25 departamentos con dato; escala de un
   solo tono desde 0, sin arcoíris; leyenda «% de personas»; Lima (15) y Callao (07) separados.
5. Responde con las cifras que imprime el script y la ruta del mapa. Se calculan como la sumaria
   (factor07 × mieperho): Cajamarca 45.0 %, Ica 6.0 %.
---
name: limpiando-enaho
description: Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO del INEI y arma una base de personas con pobreza y factor de expansión. Úsala cuando pidan limpiar, unir o analizar la ENAHO, o calcular pobreza por región, departamento, área, sexo o edad.
argument-hint: [año]
allowed-tools: Bash(uv run *)
---

# Limpiar la ENAHO

1. Si faltan los zip en datos/, pide al usuario bajarlos del INEI desde el navegador (código 966 = 2024):
   proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip y 966-Modulo02.zip
2. Corre exactamente, desde la raíz del repo: `uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio $0`
   Si no se pasó año, usa `--anio 2024`. No escribas otro script de limpieza ni cambies filtros, llaves o factores.
3. Lee salidas/validacion.txt. Si dice VALIDACIÓN FALLIDA o la pobreza difiere del INEI en más de 0.1 puntos, detente y muestra el archivo.
4. Responde con salidas/personas_<año>.parquet. Toda cifra va ponderada con facpob07; pobre es `pobreza <= 2`, nunca un promedio del código.
5. Antes de usar una variable que no está en la base, lee [reference.md](reference.md).
total 8
drwxr-xr-x@  3 susanmontalvo  staff   96 Oct 31 10:25 .
drwxr-xr-x@ 15 susanmontalvo  staff  480 Oct 31 10:23 ..
-rw-r--r--@  1 susanmontalvo  staff  549 Oct 31 10:25 validacion.txt
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

## 🤖 Claude · 2026-10-31 10:25:41

Falta `salidas/personas_2024.parquet`, así que primero corro la limpieza.

**Herramienta `Bash`** — Run ENAHO cleaning script for 2024

```bash
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 && cat salidas/validacion.txt
```

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

## 🤖 Claude · 2026-10-31 10:25:47

Validación OK (27.58 % vs. 27.6 % del INEI). Ahora el mapa:

**Herramienta `Bash`** — Run ENAHO poverty map script for 2024

```bash
uv run .claude/skills/mapeando-enaho/scripts/mapear.py --anio 2024
```

<details><summary>Resultado</summary>

```
[OK] 25 departamentos en el GeoJSON
[OK] 25 departamentos con dato
[OK] todo departamento de la ENAHO está en el mapa
[OK] Lima (15) y Callao (07) separados
[OK] Cajamarca 45.0 %
[OK] Loreto 43.0 %
[OK] Puno 39.9 %
[OK] Ica 6.0 %
[OK] Moquegua 11.0 %
[OK] Madre De Dios 11.1 %

Pobreza monetaria por departamento, Perú 2024 (% de personas, sumaria: factor07 × mieperho)
  06 Cajamarca: 45.0 %
  16 Loreto: 43.0 %
  21 Puno: 39.9 %
  19 Pasco: 39.0 %
  10 Huanuco: 39.0 %
  07 Callao: 33.9 %
  09 Huancavelica: 33.4 %
  05 Ayacucho: 32.8 %
  20 Piura: 31.9 %
  13 La Libertad: 30.2 %
  25 Ucayali: 27.1 %
  15 Lima: 27.1 %
  24 Tumbes: 26.9 %
  01 Amazonas: 25.7 %
  23 Tacna: 24.0 %
  03 Apurimac: 24.0 %
  02 Ancash: 22.8 %
  22 San Martin: 22.0 %
  08 Cusco: 18.5 %
  12 Junin: 18.5 %
  04 Arequipa: 15.8 %
  14 Lambayeque: 14.0 %
  17 Madre De Dios: 11.1 %
  18 Moquegua: 11.0 %
  11 Ica: 6.0 %
Mapa: mapas/pobreza_departamento.png
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/mapas/pobreza_departamento.png"
}
```

<details><summary>Resultado</summary>

```
[imagen]
```

</details>

## 🤖 Claude · 2026-10-31 10:26:01

Hice el mapa: está en `mapas/pobreza_departamento.png`. Los 25 departamentos tienen dato y todos los chequeos del script salieron OK.

Primero tuve que regenerar la base de personas (`salidas/personas_2024.parquet`), porque no estaba en la carpeta. La validación salió bien: la pobreza nacional da **27.58 %**, frente al **27.6 %** que publica el INEI.

**Pobreza monetaria por departamento, 2024** (% de personas; cada hogar pesa por su factor de expansión `factor07` multiplicado por su número de miembros `mieperho`):

| Más pobres | % | Menos pobres | % |
|---|---|---|---|
| Cajamarca | 45.0 | Ica | 6.0 |
| Loreto | 43.0 | Moquegua | 11.0 |
| Puno | 39.9 | Madre de Dios | 11.1 |
| Pasco | 39.0 | Lambayeque | 14.0 |
| Huánuco | 39.0 | Arequipa | 15.8 |

Los demás departamentos:
- **Entre 30 % y 34 %:** Callao 33.9, Huancavelica 33.4, Ayacucho 32.8, Piura 31.9, La Libertad 30.2.
- **Entre 22 % y 28 %:** Ucayali 27.1, Lima 27.1, Tumbes 26.9, Amazonas 25.7, Tacna 24.0, Apurímac 24.0, Áncash 22.8, San Martín 22.0.
- **18.5 %:** Cusco y Junín.

El mapa usa una escala de azules que empieza en 0 %. Lima y Callao van por separado, y Callao lleva una etiqueta aparte porque su área es muy pequeña. En Huánuco, la cifra (39.0) queda un poco tapada por la línea del borde; si quieres, la muevo.


---

## Sesión a947b0a5

- **Sesión:** `a947b0a5` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:44:10 · **Fin:** 2026-10-31 10:44:32 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:44:11

¿Cuál fue la pobreza en Cusco en 2024?

**Herramienta `Skill`**

```json
{
 "skill": "limpiando-enaho",
 "args": "Calcular la pobreza en el departamento de Cusco en 2024"
}
```

<details><summary>Resultado</summary>

```
Launching skill: limpiando-enaho
```

</details>

**Herramienta `Bash`** — List data and output folders

```bash
ls datos/ salidas/ 2>&1
```

<details><summary>Resultado</summary>

```
datos/:
966-Modulo02
966-Modulo02.zip
966-Modulo34
966-Modulo34.zip
peru_departamental_simple.geojson

salidas/:
validacion.txt
```

</details>

**Herramienta `Bash`** — Run ENAHO cleaning script for 2024 and show validation

```bash
uv run ~/Documents/GitHub/skills-enaho/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 && cat salidas/validacion.txt
```

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

**Herramienta `Bash`** — Compute weighted poverty for Cusco 2024

```bash
uv run python -c "
import pandas as pd
df=pd.read_parquet('salidas/personas_2024.parquet')
print(df.columns.tolist()); print(df.head(3))
c=df[df.ubigeo.astype(str).str[:2]=='08']
w=c.facpob07
print('n',len(c),'pob',w.sum())
print('pobreza',(w*(c.pobreza<=2)).sum()/w.sum()*100)
print('extrema',(w*(c.pobreza==1)).sum()/w.sum()*100)
"
```

<details><summary>Resultado</summary>

```
['conglome', 'vivienda', 'hogar', 'codperso', 'p203', 'p207', 'p208a', 'facpob07', 'ubigeo', 'estrato', 'dominio', 'pobreza', 'mieperho', 'factor07', 'departamento', 'urbano', 'pobre', 'pobre_extremo', 'anio']
  conglome vivienda hogar codperso  ...  urbano  pobre  pobre_extremo  anio
0   010651      013    11       01  ...    True  False          False  2024
1   010651      013    11       02  ...    True  False          False  2024
2   010651      013    11       03  ...    True  False          False  2024

[3 rows x 19 columns]
n 3777 pob 1.3803571e+06
pobreza 18.539291
extrema 2.1484504
```

</details>

## 🤖 Claude · 2026-10-31 10:44:32

En 2024, el **18.5 %** de la población de Cusco era pobre, según la ENAHO del INEI.

| Indicador (Cusco, 2024) | Valor |
|---|---|
| Pobreza total | **18.5 %** |
| Pobreza extrema | 2.1 % |
| Población representada | ~1.38 millones |
| Personas en la muestra | 3,777 |

Cusco queda unos 9 puntos por debajo del promedio nacional, que fue 27.6 %.

**Cómo lo calculé:**
- Usé los módulos 34 y 02 de la ENAHO 2024 y me quedé con los residentes habituales.
- Ponderé con `facpob07`. Conté como pobre a quien tiene `pobreza <= 2` y como pobre extremo a quien tiene `pobreza == 1`. Cusco son los ubigeos que empiezan con `08`.
- La validación pasó: la pobreza nacional que reproduje (27.5–27.6 %) coincide con la cifra oficial del INEI (27.6 %).

**Una precaución:** a nivel de un solo departamento la muestra es pequeña (3,777 personas), así que el margen de error es de varios puntos. Si vas a citar la cifra, conviene compararla con la que publica el INEI, que suele darla por grupos de departamentos o con intervalos de confianza.

La base limpia está en `salidas/personas_2024.parquet`. Si te sirve, puedo calcularla separando zona urbana y rural, o compararla con otros departamentos en un gráfico o un mapa.


---

## Sesión 9dcfccef

- **Sesión:** `9dcfccef` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:44:34 · **Fin:** 2026-10-31 10:45:01 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:44:35

Grafica la pobreza urbana y rural

**Herramienta `Skill`**

```json
{
 "skill": "graficando-enaho",
 "args": "por área (urbano y rural)"
}
```

<details><summary>Resultado</summary>

```
Launching skill: graficando-enaho
```

</details>

**Herramienta `Bash`** — Check cleaned data and script options

```bash
ls salidas/ && grep -n "add_argument\|choices" .claude/skills/graficando-enaho/scripts/graficar.py
```

<details><summary>Resultado</summary>

```
validacion.txt
80:    parser.add_argument("--por", choices=list(NOMBRE_GRUPO), required=True)
81:    parser.add_argument("--indicador", choices=list(INDICADORES), default="pobre")
82:    parser.add_argument("--anio", type=int, default=2024)
```

</details>

**Herramienta `Bash`** — Show grouping options in script

```bash
grep -n -A8 "^NOMBRE_GRUPO" .claude/skills/graficando-enaho/scripts/graficar.py
```

<details><summary>Resultado</summary>

```
35:NOMBRE_GRUPO = {"area": "área", "departamento": "departamento", "sexo": "sexo", "edad": "grupo de edad"}
36-
37-
38-def agrupar(base: pd.DataFrame, por: str) -> pd.Series:
39-    """Devuelve la etiqueta de grupo de cada persona."""
40-    if por == "area":
41-        return base.urbano.map({True: "Urbano", False: "Rural"})
42-    if por == "departamento":
43-        return base.departamento.map(DEPARTAMENTOS)
```

</details>

**Herramienta `Skill`**

```json
{
 "skill": "limpiando-enaho"
}
```

<details><summary>Resultado</summary>

```
Launching skill: limpiando-enaho
```

</details>

**Herramienta `Bash`** — Check for ENAHO zip files

```bash
ls datos/ 2>&1
```

<details><summary>Resultado</summary>

```
966-Modulo02
966-Modulo02.zip
966-Modulo34
966-Modulo34.zip
peru_departamental_simple.geojson
```

</details>

**Herramienta `Bash`** — Clean ENAHO 2024 and show validation

```bash
uv run ~/Documents/GitHub/skills-enaho/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 && cat salidas/validacion.txt
```

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

## 🤖 Claude · 2026-10-31 10:44:50

Ya está lista la base limpia de 2024 y pasó la validación. Ahora hago el gráfico por área.

**Herramienta `Bash`** — Plot poverty by urban/rural area

```bash
uv run ~/Documents/GitHub/skills-enaho/.claude/skills/graficando-enaho/scripts/graficar.py --por area --anio 2024
```

<details><summary>Resultado</summary>

```
Pobreza monetaria por área, Perú 2024 (% de personas, ponderado con facpob07)
  Rural: 39.4 %
  Urbano: 24.7 %
Figura: figuras/pobreza_area_2024.png
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/figuras/pobreza_area_2024.png"
}
```

<details><summary>Resultado</summary>

```
[imagen]
```

</details>

## 🤖 Claude · 2026-10-31 10:45:01

Hice el gráfico de la pobreza monetaria por área para 2024, con los datos ponderados por persona (factor `facpob07`):

| Área | Pobreza |
|---|---|
| Rural | **39.4 %** |
| Urbano | **24.7 %** |

En 2024, la pobreza rural fue casi 15 puntos más alta que la urbana.

Antes de graficar tuve que limpiar la base, porque todavía no existía la base de personas de 2024. El chequeo salió bien: la pobreza nacional me dio 27.53 %, frente al 27.6 % oficial del INEI.

Si se calcula con la sumaria (los datos por hogar) en vez de por persona, las cifras cambian un poco: urbano 24.8 % y rural 39.3 %.

Las instrucciones del gráfico traen el comando escrito como `--por por`, y ese valor no es válido. Usé `--por area`. Conviene corregirlo en el archivo de instrucciones.

Si quieres, hago la misma figura para la pobreza extrema.

Archivo:
- figuras/pobreza_area_2024.png


---

## Sesión d3122a25

- **Sesión:** `d3122a25` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:45:02 · **Fin:** 2026-10-31 10:45:32 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:45:03

Haz un mapa de la pobreza por departamento con la ENAHO 2024

**Herramienta `Skill`**

```json
{
 "skill": "mapeando-enaho",
 "args": "ENAHO 2024"
}
```

<details><summary>Resultado</summary>

```
Launching skill: mapeando-enaho
```

</details>

**Herramienta `Bash`** — Check for cleaned data, geojson, and script

```bash
ls salidas datos 2>&1; ls .claude/skills/mapeando-enaho/scripts
```

<details><summary>Resultado</summary>

```
datos:
966-Modulo02
966-Modulo02.zip
966-Modulo34
966-Modulo34.zip
peru_departamental_simple.geojson

salidas:
validacion.txt
mapear.py
```

</details>

## 🤖 Claude · 2026-10-31 10:45:10

Falta `salidas/personas_2024.parquet`, así que primero limpio la ENAHO.

**Herramienta `Skill`**

```json
{
 "skill": "limpiando-enaho",
 "args": "2024"
}
```

<details><summary>Resultado</summary>

```
Launching skill: limpiando-enaho
```

</details>

**Herramienta `Bash`** — Run ENAHO cleaning script and show validation

```bash
uv run ~/Documents/GitHub/skills-enaho/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 2>&1 | tail -40; echo "---"; cat salidas/validacion.txt
```

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
---
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

## 🤖 Claude · 2026-10-31 10:45:17

Validación OK. Ahora el mapa:

**Herramienta `Bash`** — Run the poverty map script for 2024

```bash
uv run ~/Documents/GitHub/skills-enaho/.claude/skills/mapeando-enaho/scripts/mapear.py --anio 2024 2>&1 | tail -60
```

<details><summary>Resultado</summary>

```
[OK] 25 departamentos en el GeoJSON
[OK] 25 departamentos con dato
[OK] todo departamento de la ENAHO está en el mapa
[OK] Lima (15) y Callao (07) separados
[OK] Cajamarca 45.0 %
[OK] Loreto 43.0 %
[OK] Puno 39.9 %
[OK] Ica 6.0 %
[OK] Moquegua 11.0 %
[OK] Madre De Dios 11.1 %

Pobreza monetaria por departamento, Perú 2024 (% de personas, sumaria: factor07 × mieperho)
  06 Cajamarca: 45.0 %
  16 Loreto: 43.0 %
  21 Puno: 39.9 %
  19 Pasco: 39.0 %
  10 Huanuco: 39.0 %
  07 Callao: 33.9 %
  09 Huancavelica: 33.4 %
  05 Ayacucho: 32.8 %
  20 Piura: 31.9 %
  13 La Libertad: 30.2 %
  25 Ucayali: 27.1 %
  15 Lima: 27.1 %
  24 Tumbes: 26.9 %
  01 Amazonas: 25.7 %
  23 Tacna: 24.0 %
  03 Apurimac: 24.0 %
  02 Ancash: 22.8 %
  22 San Martin: 22.0 %
  08 Cusco: 18.5 %
  12 Junin: 18.5 %
  04 Arequipa: 15.8 %
  14 Lambayeque: 14.0 %
  17 Madre De Dios: 11.1 %
  18 Moquegua: 11.0 %
  11 Ica: 6.0 %
Mapa: mapas/pobreza_departamento.png
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/mapas/pobreza_departamento.png"
}
```

<details><summary>Resultado</summary>

```
[imagen]
```

</details>

## 🤖 Claude · 2026-10-31 10:45:32

Hice el mapa de la pobreza monetaria por departamento con la ENAHO 2024. Está en `mapas/pobreza_departamento.png`.

Antes del mapa tuve que limpiar los datos: `salidas/personas_2024.parquet` todavía no existía y lo armé con `limpiando-enaho`. La pobreza nacional sale **27.58 %**, contra 27.6 % del INEI, así que la diferencia queda dentro de la tolerancia de 0,1 puntos. La pobreza extrema es 5.50 %. Pasaron todos los chequeos, tanto de la limpieza como del mapa.

**Pobreza por departamento, 2024** (% de personas, calculado con la sumaria: factor07 × mieperho)

| Departamento | % | Departamento | % |
|---|---|---|---|
| Cajamarca | **45.0** | Amazonas | 25.7 |
| Loreto | 43.0 | Tacna | 24.0 |
| Puno | 39.9 | Apurímac | 24.0 |
| Pasco | 39.0 | Áncash | 22.8 |
| Huánuco | 39.0 | San Martín | 22.0 |
| Callao | 33.9 | Cusco | 18.5 |
| Huancavelica | 33.4 | Junín | 18.5 |
| Ayacucho | 32.8 | Arequipa | 15.8 |
| Piura | 31.9 | Lambayeque | 14.0 |
| La Libertad | 30.2 | Madre de Dios | 11.1 |
| Ucayali | 27.1 | Moquegua | 11.0 |
| Lima | 27.1 | Ica | **6.0** |
| Tumbes | 26.9 | | |

- **Mayor pobreza:** Cajamarca, Loreto y Puno, que van de 40 % a 45 %, seguidos de Pasco y Huánuco con 39 %.
- **Menor pobreza:** Ica tiene 6 %. Le siguen Moquegua y Madre de Dios, con alrededor de 11 %.
- **Lima y Callao:** van por separado. Callao (33.9 %) tiene más pobreza que Lima (27.1 %).

El mapa usa un solo tono de azul, con la escala empezando en 0 y la leyenda «% de personas». Los departamentos se unen al mapa por código de ubigeo, no por nombre. Un detalle visual menor: la etiqueta «39.0» de Huánuco se superpone un poco con un borde.


---

## Sesión ca2a9033

- **Sesión:** `ca2a9033` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:55:20 · **Fin:** 2026-10-31 10:55:39 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:55:21

¿Cuál fue la pobreza en Cusco en 2024?

**Herramienta `Skill`**

```json
{
 "skill": "limpiando-enaho",
 "args": "Calcular pobreza en Cusco en 2024"
}
```

<details><summary>Resultado</summary>

```
Launching skill: limpiando-enaho
```

</details>

**Herramienta `Bash`** — List data and output folders

```bash
ls datos/ salidas/ 2>&1
```

<details><summary>Resultado</summary>

```
datos/:
966-Modulo02
966-Modulo02.zip
966-Modulo34
966-Modulo34.zip
peru_departamental_simple.geojson

salidas/:
validacion.txt
```

</details>

**Herramienta `Bash`** — Run ENAHO cleaning script for 2024 and show validation

```bash
uv run ~/Documents/GitHub/skills-enaho/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 2>&1 | tail -30; echo ---; cat salidas/validacion.txt
```

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
---
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

**Herramienta `Bash`** — Compute weighted poverty for Cusco 2024

```bash
uv run python -c "
import pandas as pd
d=pd.read_parquet('salidas/personas_2024.parquet')
print(d.columns.tolist())
c=d[d.ubigeo.astype(str).str[:2]=='08']
w=c.facpob07
print('n',len(c),'pob',w.sum())
print('pobreza', ((c.pobreza<=2)*w).sum()/w.sum()*100)
print('extrema', ((c.pobreza==1)*w).sum()/w.sum()*100)
"
```

<details><summary>Resultado</summary>

```
['conglome', 'vivienda', 'hogar', 'codperso', 'p203', 'p207', 'p208a', 'facpob07', 'ubigeo', 'estrato', 'dominio', 'pobreza', 'mieperho', 'factor07', 'departamento', 'urbano', 'pobre', 'pobre_extremo', 'anio']
n 3777 pob 1.3803571e+06
pobreza 18.539291
extrema 2.1484504
```

</details>

## 🤖 Claude · 2026-10-31 10:55:39

En 2024, el **18.5 %** de la población de Cusco era pobre, unas 256 mil de sus 1.38 millones de habitantes. La pobreza extrema fue de **2.1 %**.

Cusco quedó casi 9 puntos por debajo del promedio nacional de 2024, que fue de 27.5 % (el INEI publica 27.6 %).

**Cómo lo calculé:**
- Usé los módulos 34 y 02 de la ENAHO 2024. La limpieza pasó todos los controles y la pobreza nacional sale a 0.07 puntos de la cifra del INEI.
- Para Cusco tomé las personas con ubigeo que empieza en 08. Son 3,777 residentes habituales en la muestra.
- Cuento como pobre a quien tiene `pobreza <= 2`, y como pobre extremo a quien tiene `pobreza == 1`. Todas las cifras están ponderadas con `facpob07`.

**Precaución:** la muestra de Cusco es chica y la cifra tiene un margen de error de varios puntos. No calculé el intervalo de confianza. Antes de citarla, compárala con el dato departamental que publica el INEI.

La base limpia está en `salidas/personas_2024.parquet`. Si quieres, puedo separar Cusco en urbano y rural o hacer un gráfico comparándolo con otros departamentos.


---

## Sesión 542f7e5c

- **Sesión:** `542f7e5c` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:55:41 · **Fin:** 2026-10-31 10:56:05 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:55:41

Grafica la pobreza urbana y rural

**Herramienta `Skill`**

```json
{
 "skill": "graficando-enaho",
 "args": "pobreza por área (urbano y rural)"
}
```

<details><summary>Resultado</summary>

```
Launching skill: graficando-enaho
```

</details>

**Herramienta `Bash`** — Check cleaned data and run poverty-by-area chart script

```bash
ls salidas/ && uv run ~/Documents/GitHub/skills-enaho/.claude/skills/graficando-enaho/scripts/graficar.py --por area --anio 2024
```

<details><summary>Resultado</summary>

```
Exit code 1
validacion.txt
Falta ~/Documents/GitHub/skills-enaho/salidas/personas_2024.parquet. Usa primero la skill limpiando-enaho.
```

</details>

**Herramienta `Skill`**

```json
{
 "skill": "limpiando-enaho",
 "args": "2024"
}
```

<details><summary>Resultado</summary>

```
Launching skill: limpiando-enaho
```

</details>

**Herramienta `Bash`** — Check for ENAHO zip files

```bash
ls datos/ 2>&1
```

<details><summary>Resultado</summary>

```
966-Modulo02
966-Modulo02.zip
966-Modulo34
966-Modulo34.zip
peru_departamental_simple.geojson
```

</details>

**Herramienta `Bash`** — Clean ENAHO 2024 and show validation

```bash
uv run ~/Documents/GitHub/skills-enaho/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 && cat salidas/validacion.txt
```

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

## 🤖 Claude · 2026-10-31 10:55:56

Validé la base 2024 (27.5 % de pobreza, coincide con el INEI). Ahora genero el gráfico por área.

**Herramienta `Bash`** — Generate poverty-by-area bar chart

```bash
uv run ~/Documents/GitHub/skills-enaho/.claude/skills/graficando-enaho/scripts/graficar.py --por area --anio 2024
```

<details><summary>Resultado</summary>

```
Pobreza monetaria por área, Perú 2024 (% de personas, ponderado con facpob07)
  Rural: 39.4 %
  Urbano: 24.7 %
Figura: figuras/pobreza_area_2024.png
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/figuras/pobreza_area_2024.png"
}
```

<details><summary>Resultado</summary>

```
[imagen]
```

</details>

## 🤖 Claude · 2026-10-31 10:56:05

Hice el gráfico de la pobreza monetaria por área en el Perú en 2024:

| Área | Pobreza (% de personas) |
|---|---|
| Rural | 39,4 % |
| Urbano | 24,7 % |

En la zona rural la pobreza es casi 15 puntos más alta que en la urbana.

El gráfico está en `figuras/pobreza_area_2024.png`. Las barras parten de cero y la fuente indicada es INEI, ENAHO 2024.

Para hacerlo primero tuve que armar la base de personas, porque todavía no existía. La pobreza nacional que da esa base es 27,5 %, muy cerca del 27,6 % oficial del INEI.

Las cifras salen de la base de personas, ponderadas con `facpob07`. Si se calculan desde la sumaria (el resumen por hogar) cambian en una décima: 24,8 % urbano y 39,3 % rural.

Si quieres, también puedo graficar la pobreza extrema por área.


---

## Sesión 43b9153f

- **Sesión:** `43b9153f` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/skills-enaho`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-31 10:56:06 · **Fin:** 2026-10-31 10:56:31 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-31 10:56:07

Haz un mapa de la pobreza por departamento con la ENAHO 2024

**Herramienta `Skill`**

```json
{
 "skill": "mapeando-enaho",
 "args": "ENAHO 2024"
}
```

<details><summary>Resultado</summary>

```
Launching skill: mapeando-enaho
```

</details>

**Herramienta `Bash`** — Check for required input files

```bash
ls salidas datos 2>&1; ls .claude/skills/mapeando-enaho/scripts
```

<details><summary>Resultado</summary>

```
datos:
966-Modulo02
966-Modulo02.zip
966-Modulo34
966-Modulo34.zip
peru_departamental_simple.geojson

salidas:
validacion.txt
mapear.py
```

</details>

## 🤖 Claude · 2026-10-31 10:56:13

Falta `salidas/personas_2024.parquet`, así que primero corro la limpieza.

**Herramienta `Skill`**

```json
{
 "skill": "limpiando-enaho",
 "args": "2024"
}
```

<details><summary>Resultado</summary>

```
Launching skill: limpiando-enaho
```

</details>

**Herramienta `Bash`** — Run ENAHO cleaning script and show validation

```bash
uv run ~/Documents/GitHub/skills-enaho/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 && cat salidas/validacion.txt
```

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

## 🤖 Claude · 2026-10-31 10:56:19

Validación OK. Ahora el mapa.

**Herramienta `Bash`** — Run poverty map script for 2024

```bash
uv run ~/Documents/GitHub/skills-enaho/.claude/skills/mapeando-enaho/scripts/mapear.py --anio 2024
```

<details><summary>Resultado</summary>

```
[OK] 25 departamentos en el GeoJSON
[OK] 25 departamentos con dato
[OK] todo departamento de la ENAHO está en el mapa
[OK] Lima (15) y Callao (07) separados
[OK] Cajamarca 45.0 %
[OK] Loreto 43.0 %
[OK] Puno 39.9 %
[OK] Ica 6.0 %
[OK] Moquegua 11.0 %
[OK] Madre De Dios 11.1 %

Pobreza monetaria por departamento, Perú 2024 (% de personas, sumaria: factor07 × mieperho)
  06 Cajamarca: 45.0 %
  16 Loreto: 43.0 %
  21 Puno: 39.9 %
  19 Pasco: 39.0 %
  10 Huanuco: 39.0 %
  07 Callao: 33.9 %
  09 Huancavelica: 33.4 %
  05 Ayacucho: 32.8 %
  20 Piura: 31.9 %
  13 La Libertad: 30.2 %
  25 Ucayali: 27.1 %
  15 Lima: 27.1 %
  24 Tumbes: 26.9 %
  01 Amazonas: 25.7 %
  23 Tacna: 24.0 %
  03 Apurimac: 24.0 %
  02 Ancash: 22.8 %
  22 San Martin: 22.0 %
  08 Cusco: 18.5 %
  12 Junin: 18.5 %
  04 Arequipa: 15.8 %
  14 Lambayeque: 14.0 %
  17 Madre De Dios: 11.1 %
  18 Moquegua: 11.0 %
  11 Ica: 6.0 %
Mapa: mapas/pobreza_departamento.png
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~/Documents/GitHub/skills-enaho/mapas/pobreza_departamento.png"
}
```

<details><summary>Resultado</summary>

```
[imagen]
```

</details>

## 🤖 Claude · 2026-10-31 10:56:31

Hice el mapa de la pobreza por departamento con la ENAHO 2024. Está en `mapas/pobreza_departamento.png`.

Primero preparé la base de personas, que todavía no existía. La pobreza nacional me sale 27.58 %, contra 27.6 % del INEI, y pasó todas las validaciones. El mapa también pasó todos sus chequeos: tiene los 25 departamentos con dato y Lima y Callao están separados.

**Pobreza monetaria 2024 (% de personas)**

| Más pobres | % | Menos pobres | % |
|---|---|---|---|
| Cajamarca | 45.0 | Ica | 6.0 |
| Loreto | 43.0 | Moquegua | 11.0 |
| Puno | 39.9 | Madre de Dios | 11.1 |
| Pasco | 39.0 | Lambayeque | 14.0 |
| Huánuco | 39.0 | Arequipa | 15.8 |

El resto, de mayor a menor:
- Callao 33.9
- Huancavelica 33.4
- Ayacucho 32.8
- Piura 31.9
- La Libertad 30.2
- Ucayali 27.1
- Lima 27.1
- Tumbes 26.9
- Amazonas 25.7
- Tacna 24.0
- Apurímac 24.0
- Áncash 22.8
- San Martín 22.0
- Cusco 18.5
- Junín 18.5

- **Cómo se calcula:** las cifras usan la sumaria, ponderada por factor07 × mieperho.
- **Lima:** el 27.1 % es el departamento entero, sin separar Lima Metropolitana de Lima Provincias.
- **Callao:** es muy pequeño en el mapa, así que su cifra va en una etiqueta con flecha.
- **Colores:** la escala va de 0 a 50 % en un solo tono de azul.

