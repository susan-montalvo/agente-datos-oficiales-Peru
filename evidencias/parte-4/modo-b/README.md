# Modo B: respuestas a las 10 preguntas con MCP y Skills

**Autoría:** este procedimiento lo ejecutó y documentó **Claude Code** (asistente de IA de
Anthropic, modelo Claude Opus 5.5, `claude-opus-5-5`) el 6 de noviembre de 2026, a pedido de
Susan Montalvo. Claude Code consultó el servidor MCP, ejecutó las Skills, hizo los cálculos,
escribió las respuestas en `preguntas.csv` y redactó este README. Las respuestas no se revisaron
a mano antes de guardarse.

Se usaron las herramientas del proyecto
[`agente-datos-oficiales-Peru`](../agente-datos-oficiales-Peru/):

- **MCP `bcrp`** (`mcp/server.py`): series oficiales del BCRP (P01–P04, P09 y P10).
- **Skills `limpiando-enaho` y `graficando-enaho`** (`.claude/skills/`): microdatos ENAHO 2024
  del INEI (P05–P08 y P10).

Para que esta ejecución fuera independiente, no se consultaron las respuestas de la carpeta
`Modo A` ni las de una ejecución anterior del Modo B.

## Resultados

| ID | Respuesta | Fuente y herramienta |
|---|---|---|
| P01 | **5.71 %** (5.7069 %) | BCRP PN01728AM, mayo 2024 · MCP `serie` |
| P02 | **1.97 %** (1.9663 %) | BCRP PN01273PM, dic. 2024 · MCP `serie` |
| P03 | **S/ 3.754 por US$** (3.7539) | BCRP PN01210PM, ene.–dic. 2024 · MCP `resumen` |
| P04 | **−1.50 pp** (de 6.50 % a 5.00 %) | BCRP PD04722MM, ene. y dic. 2024 · MCP `serie` |
| P05 | **36.5 %** (36.47 %) | ENAHO 2024 · Skills `limpiando-enaho` y `graficando-enaho --por edad` |
| P06 | **10.0 %** (9.96 %) | ENAHO 2024 · base de `limpiando-enaho`, cálculo para 0–4 años |
| P07 | **27.7 %** (27.68 %) | ENAHO 2024 · Skill `graficando-enaho --por sexo` |
| P08 | **14.5 pp** (36.47 − 22.02 = 14.45) | ENAHO 2024 · Skill `graficando-enaho --por edad` |
| P09 | **−0.40** (−1.4 / 3.4825 = −0.402) | Enunciado + BCRP PN01728AM · MCP `resumen` |
| P10 | **US$ 121.04** (S/ 454.39 / 3.7539) | ENAHO 2024, Módulo 34 (`linea`) + BCRP PN01210PM · MCP |

Las respuestas completas, con su fuente, están en la columna `respuesta` de
[`preguntas.csv`](preguntas.csv).

## Procedimiento

### 1. Series del BCRP mediante el MCP (P01–P04, P09, P10)

El servidor `bcrp` está configurado en el `.mcp.json` del repositorio del agente, pero no estaba
conectado a esta sesión de Claude Code, que se abrió en otra carpeta. Para usarlo, Claude Code
lo inició con un cliente FastMCP por `stdio`, como en la verificación de la Parte 1 del agente
([`evidencias/scripts/consultar_mcp.py`](evidencias/scripts/consultar_mcp.py)). El cliente
enumeró las herramientas (`buscar_series`, `serie`, `resumen` y `comparar_series`) e hizo estas
llamadas:

| Herramienta | Código | Periodo | Uso |
|---|---|---|---|
| `serie` | PN01728AM | 2024-01 a 2024-12 | P01 (mayo) y P09 (12 meses) |
| `serie` | PN01273PM | 2024-12 | P02 |
| `resumen` | PN01210PM | 2024-01 a 2024-12 | P03 y P10 (`promedio` de 12 meses) |
| `serie` | PD04722MM | 2024-01 a 2024-12 | P04 (diciembre − enero) |
| `resumen` | PN01728AM | 2024-01 a 2024-12 | P09 (`promedio` de 12 meses) |

Las respuestas completas del MCP, con los enlaces de la API oficial del BCRP, están en
[`evidencias/mcp_respuestas.json`](evidencias/mcp_respuestas.json). Cada serie tuvo las 12
observaciones de 2024.

### 2. Microdatos ENAHO 2024 mediante las Skills (P05–P08, P10)

Las Skills se ejecutaron en una carpeta temporal de trabajo enlazada a `datos/` del agente. Así
no se sobrescribieron `salidas/` ni `figuras/` del repositorio original.

1. **`limpiando-enaho`**: `limpiar.py --anio 2024` unió el Módulo 02 (miembros) con el
   Módulo 34 (sumaria) y conservó 108,664 residentes habituales. Terminó con **VALIDACIÓN OK**:
   la pobreza es 27.58 % con la sumaria y 27.53 % con la base de personas; la cifra oficial del
   INEI es 27.6 %
   ([`evidencias/validacion.txt`](evidencias/validacion.txt)).
2. **`graficando-enaho`**: se ejecutó por edad, por sexo y por edad con pobreza extrema.
   Resultados: 0–17 años, 36.5 %; 60 años a más, 22.0 %; mujeres, 27.7 %; hombres, 27.4 %.
   Las figuras están en [`evidencias/figuras/`](evidencias/figuras/).
3. **Cálculos fuera de los grupos de la Skill**
   ([`evidencias/scripts/calcular.py`](evidencias/scripts/calcular.py)). Se siguieron las mismas
   reglas: ponderar con `facpob07`, considerar pobre a quien tiene `pobreza <= 2` y pobre extremo
   a quien tiene `pobreza == 1`.
   - **P06:** la Skill agrupa 0–17 años, no 0–4. Se filtró `p208a` entre 0 y 4 años
     (6,746 casos en la muestra) en la base de personas de `limpiando-enaho`.
   - **P10:** la variable `linea` (línea de pobreza mensual per cápita) no está en la base de la
     Skill. Se leyó de `sumaria-2024.dta` y se promedió con el factor de personas
     `factor07 × mieperho`: **S/ 454.39**, que coincide con la línea oficial del INEI de 2024
     (S/ 454). Ese valor se dividió entre el tipo de cambio promedio del MCP.
4. **P05, P07 y P08** se recalcularon con dos decimales en el mismo script. Coinciden con lo que
   imprimió la Skill. Para descartar errores de redondeo, los cálculos se hicieron en `float64`.

### 3. Cálculos combinados

- **P09:** (27.6 − 29.0) / promedio(PBI interanual de ene. a dic. 2024)
  = −1.4 / 3.4825 = **−0.402**. Las cifras de pobreza 29.0 % y 27.6 % vienen del enunciado. La
  de 2024 coincide con la que calcularon las Skills.
- **P10:** S/ 454.39 / 3.7539 = **US$ 121.04** por persona al mes.

Todos los valores intermedios están en [`evidencias/calculos.json`](evidencias/calculos.json).

## Decisiones y limitaciones

- **P06 y P10** usan la base y las reglas de las Skills, pero sus cálculos se hicieron fuera de
  los scripts de las Skills porque los scripts no cubren esos casos. La `reference.md` de la
  Skill recomienda agregar variables nuevas en `limpiar.py`. No se modificó el repositorio del
  agente: `linea` se leyó directamente de la sumaria.
- **P10:** la línea promedio se ponderó por personas (`factor07 × mieperho`), que es el criterio
  con el que el INEI publica la línea nacional. Otros criterios dan otros valores: S/ 452.04
  ponderando por hogares (US$ 120.42) y S/ 414.71 con el promedio simple sin ponderar
  (US$ 110.48).
- **P04:** se informa la diferencia entre diciembre y enero. Como la tasa de enero de 2024 ya era
  6.50 %, la reducción dentro de 2024 medida así es de 1.50 pp.
- El MCP se usó con un cliente FastMCP por `stdio`, no con las herramientas MCP nativas de la
  sesión de Claude Code. El servidor, las herramientas y la API consultada son los mismos.

## Reproducir

Desde `agente-datos-oficiales-Peru/`, con los ZIP de la ENAHO 2024 en `datos/`:

```bash
# 1) MCP del BCRP
uv run python "../Modo B/evidencias/scripts/consultar_mcp.py" "$PWD" /ruta/mcp_respuestas.json

# 2) Skills ENAHO (ejecutar desde una carpeta de trabajo que tenga datos/ o un enlace a datos/)
uv run --project <repo> <repo>/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
uv run --project <repo> <repo>/.claude/skills/graficando-enaho/scripts/graficar.py --por edad --anio 2024
uv run --project <repo> <repo>/.claude/skills/graficando-enaho/scripts/graficar.py --por sexo --anio 2024
uv run --project <repo> <repo>/.claude/skills/graficando-enaho/scripts/graficar.py --por edad --indicador pobre_extremo --anio 2024

# 3) Cálculos finales
uv run --project <repo> python -I "../Modo B/evidencias/scripts/calcular.py" <carpeta_trabajo> /ruta/mcp_respuestas.json <repo>/datos
```
