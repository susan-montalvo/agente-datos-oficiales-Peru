# Antecedente: lectura del recurso bcrp://serie del MCP

- **Sesión:** `3301fed6` · Claude Code
- **Carpeta de trabajo:** `~/Documents/GitHub/Diplomado-Su-2026/mcp-bcrp`
- **Modelo:** claude-opus-5-5
- **Inicio:** 2026-10-28 20:59:41 · **Fin:** 2026-10-28 21:12:56 (hora de Lima)

> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; las salidas de herramientas de más de 4,000 caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.

## 🧑 Usuaria · 2026-10-28 20:59:41

`/mcp`

## 🧑 Usuaria · 2026-10-28 21:02:54

`/mcp`

## 🧑 Usuaria · 2026-10-28 21:06:57

@bcrp:bcrp://serie/PN01273PM

**Herramienta `ToolSearch`**

```json
{
 "query": "select:ReadMcpResourceTool,mcp__bcrp__resumen",
 "max_results": 2
}
```

<details><summary>Resultado</summary>

```
[imagen]
[imagen]
```

</details>

**Herramienta `ReadMcpResourceTool`**

```json
{
 "server": "bcrp",
 "uri": "bcrp://serie/PN01273PM"
}
```

<details><summary>Resultado</summary>

```
{"contents":[{"uri":"bcrp://serie/PN01273PM","mimeType":"text/plain","text":"{\"codigo\": \"PN01273PM\", \"nombre\": \"\\u00cdndice de precios Lima Metropolitana (var% 12 meses) - IPC\", \"categoria\": \"Inflaci\\u00f3n\", \"frecuencia\": \"Mensual\", \"inicio\": \"Ene-1950\", \"actualizada\": \"2026-10-08\"}"}]}
```

</details>

**Herramienta `mcp__bcrp__resumen`**

```json
{
 "codigo": "PN01273PM",
 "desde": "2025-09",
 "hasta": "2026-09"
}
```

<details><summary>Resultado</summary>

```
{"codigo":"PN01273PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC","frecuencia":"Mensual","periodo":{"desde":"2025-09","hasta":"2026-09"},"primero":{"periodo":"2025-09","valor":1.35839342135424},"ultimo":{"periodo":"2026-09","valor":4.54865469481509},"cambio":3.19026127346085,"variacion_pct":234.8554714200797,"promedio":2.945148596768775,"maximo":{"periodo":"2026-09","valor":4.54865469481509},"minimo":{"periodo":"2025-10","valor":1.35177475650182},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01273PM/json/2025-9/2026-9"}
```

</details>

## 🤖 Claude · 2026-10-28 21:07:13

La serie **PN01273PM** es la **inflación interanual de Lima Metropolitana**: la variación % del IPC frente al mismo mes del año anterior. Es una serie mensual del BCRP que empieza en enero de 1950 y se actualizó por última vez el 8 de octubre de 2026.

El recurso solo trae la descripción de la serie, así que pedí al BCRP el resumen de los últimos 12 meses (septiembre 2025 a septiembre 2026):

| Indicador | Periodo | Valor |
|---|---|---|
| Inicio | Sep-2025 | 1,36 % |
| Último dato | Sep-2026 | **4,55 %** |
| Mínimo | Oct-2025 | 1,35 % |
| Máximo | Sep-2026 | 4,55 % |
| Promedio del periodo | — | 2,95 % |
| Cambio | — | **+3,19 puntos porcentuales** |

**Cómo leerlo:**
- En un año, la inflación interanual subió de cerca de 1,4 % a 4,5 %. El dato de septiembre de 2026 es el más alto del periodo.
- El BCRP busca mantener la inflación entre 1 % y 3 %. El 4,55 % de septiembre de 2026 está por encima del techo de ese rango.
- La herramienta también da una "variación" de 234,9 %, pero no sirve aquí. Como la serie ya está en porcentajes, lo correcto es decir que **subió 3,19 puntos porcentuales**.

Fuente: BCRP, serie PN01273PM, de Sep-2025 a Sep-2026 ([API](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01273PM/json/2025-9/2026-9)).

Si quieres, puedo hacer un gráfico de la serie, comparar este periodo con otros (por ejemplo, el pico de 2022) o compararla con otra serie del BCRP.

## 🧑 Usuaria · 2026-10-28 21:09:08

`/mcp__bcrp__informe`

**Herramienta `ToolSearch`**

```json
{
 "query": "select:mcp__bcrp__buscar_series,mcp__bcrp__serie,mcp__bcrp__comparar_series",
 "max_results": 3
}
```

<details><summary>Resultado</summary>

```
[imagen]
[imagen]
[imagen]
```

</details>

**Herramienta `mcp__bcrp__buscar_series`**

```json
{
 "texto": "ipc 12 meses",
 "frecuencia": "Mensual",
 "limite": 15
}
```

**Herramienta `mcp__bcrp__buscar_series`**

```json
{
 "texto": "subyacente",
 "frecuencia": "Mensual",
 "limite": 10
}
```

**Herramienta `mcp__bcrp__buscar_series`**

```json
{
 "texto": "tasa de referencia",
 "limite": 5
}
```

**Herramienta `mcp__bcrp__buscar_series`**

```json
{
 "texto": "expectativas inflación",
 "limite": 5
}
```

<details><summary>Resultado</summary>

```
{"result":[{"codigo":"PD12912AM","nombre":"Expectativas macroeconómicas - Expectativa de Inflación a 12 meses","categoria":"Expectativas Macroeconómicas","frecuencia":"Mensual","inicio":"Ene-2002","actualizada":"2026-10-02"}]}
```

</details>

<details><summary>Resultado</summary>

```
{"result":[{"codigo":"PD12301MD","nombre":"Tasas de interés - Tasa de Referencia de la Política Monetaria","categoria":"Tasas de interés","frecuencia":"Diaria","inicio":"2003-09-05","actualizada":"2026-10-23"},{"codigo":"PD04722MM","nombre":"Tasas de interés del Banco Central de Reserva - Tasa de Referencia de la Política Monetaria","categoria":"Tasas de interés","frecuencia":"Mensual","inicio":"Ene-2004","actualizada":"2026-10-15"},{"codigo":"PN07809NM","nombre":"Tasas de interés activas y pasivas promedio de las empresas bancarias en MN (términos efectivos anuales) - Activas - Preferencial Corporativa a 90 días","categoria":"Tasas de interés","frecuencia":"Mensual","inicio":"Ene-2011","actualizada":"2026-10-23"},{"codigo":"PN07829NM","nombre":"Tasas de interés activas y pasivas promedio de las empresas bancarias en ME (términos efectivos anuales) - Activas - Preferencial Corporativa a 90 días","categoria":"Tasas de interés","frecuencia":"Mensual","inicio":"Ene-2011","actualizada":"2026-10-23"}]}
```

</details>

<details><summary>Resultado</summary>

```
{"result":[{"codigo":"PN01273PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1950","actualizada":"2026-10-08"},{"codigo":"PN09821PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC Importado","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1992","actualizada":"2026-10-08"},{"codigo":"PN01279PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC Subyacente","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"},{"codigo":"PN01281PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC Transables","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"},{"codigo":"PN01283PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC No Transables","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"},{"codigo":"PN09820PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC No Subyacente","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1992","actualizada":"2026-10-08"},{"codigo":"PN09830PM","nombre":"Inflación de socios comerciales - IPC Externo Multilateral (var% 12 meses)","categoria":"Tipo de cambio real","frecuencia":"Mensual","inicio":"Ene-1996","actualizada":"2026-10-08"},{"codigo":"PN09819PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC Alimentos y Energía","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1992","actualizada":"2026-10-08"},{"codigo":"PN09822PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC Alimentos y Bebidas","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"},{"codigo":"PN01277PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC Sin Alimentos y Energía","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"},{"codigo":"PN09823PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC sin Alimentos y Bebidas","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"},{"codigo":"PN09824PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC Subyacente Sin Alimentos y Bebidas","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"},{"codigo":"PN01285PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC No Transables Sin Alimentos y Bebidas","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"},{"codigo":"PN40410PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC rubros vinculados a tipo de cambio, IPM y cotizaciones","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-2001","actualizada":"2026-10-12"},{"codigo":"PN40411PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC rubros no vinculados a tipo de cambio, IPM y cotizaciones","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-2001","actualizada":"2026-10-12"}]}
```

</details>

<details><summary>Resultado</summary>

```
{"result":[{"codigo":"PN01278PM","nombre":"Índice de precios Lima Metropolitana (var% mensual) - IPC Subyacente","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"},{"codigo":"PN01279PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC Subyacente","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"},{"codigo":"PN09817PM","nombre":"Índice de precios Lima Metropolitana (var% mensual) - IPC No Subyacente","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1991","actualizada":"2026-10-08"},{"codigo":"PN09820PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC No Subyacente","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1992","actualizada":"2026-10-08"},{"codigo":"PN38708PM","nombre":"Índice de precios Lima Metropolitana (índice Dic.2021 = 100) - IPC Subyacente","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1992","actualizada":"2026-10-08"},{"codigo":"PN39522PM","nombre":"Índice de precios Lima Metropolitana (índice Dic.2021 = 100) - IPC No Subyacente","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1991","actualizada":"2026-10-08"},{"codigo":"PN01315PM","nombre":"Índice de precios Lima Metropolitana (var% mensual) - IPC Subyacente Sin Alimentos y Bebidas","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"},{"codigo":"PN09824PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC Subyacente Sin Alimentos y Bebidas","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"},{"codigo":"PN39447PM","nombre":"Índice de precios Lima Metropolitana (índice Dic.2021 = 100) - IPC Subyacente Sin Alimentos y Bebidas","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1992","actualizada":"2026-10-08"},{"codigo":"PN01296PM","nombre":"Índice de precios al consumidor Lima Metropolitana: clasificación sectorial (variación porcentual) - Inflación Subyacente - Bienes","categoria":"Inflación","frecuencia":"Mensual","inicio":"Ene-1993","actualizada":"2026-10-08"}]}
```

</details>

**Herramienta `mcp__bcrp__serie`**

```json
{
 "codigo": "PN01273PM",
 "desde": "2025-09",
 "hasta": "2026-09"
}
```

**Herramienta `mcp__bcrp__resumen`**

```json
{
 "codigo": "PN01279PM",
 "desde": "2025-09",
 "hasta": "2026-09"
}
```

**Herramienta `mcp__bcrp__resumen`**

```json
{
 "codigo": "PN09819PM",
 "desde": "2025-09",
 "hasta": "2026-09"
}
```

**Herramienta `mcp__bcrp__resumen`**

```json
{
 "codigo": "PD12912AM",
 "desde": "2025-09",
 "hasta": "2026-09"
}
```

**Herramienta `mcp__bcrp__resumen`**

```json
{
 "codigo": "PD04722MM",
 "desde": "2025-09",
 "hasta": "2026-09"
}
```

<details><summary>Resultado</summary>

```
{"codigo":"PN01273PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC","frecuencia":"Mensual","datos":[{"periodo":"2025-09","valor":1.35839342135424},{"periodo":"2025-10","valor":1.35177475650182},{"periodo":"2025-11","valor":1.36861256988846},{"periodo":"2025-12","valor":1.50879973918667},{"periodo":"2026-01","valor":1.70091694832201},{"periodo":"2026-02","valor":2.21416625767848},{"periodo":"2026-03","valor":3.80454581291585},{"periodo":"2026-04","valor":4.01414363472928},{"periodo":"2026-05","valor":3.90505240621645},{"periodo":"2026-06","valor":4.00890965651766},{"periodo":"2026-07","valor":4.06515256208199},{"periodo":"2026-08","valor":4.43780929778608},{"periodo":"2026-09","valor":4.54865469481509}],"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01273PM/json/2025-9/2026-9"}
```

</details>

<details><summary>Resultado</summary>

```
{"codigo":"PN01279PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC Subyacente","frecuencia":"Mensual","periodo":{"desde":"2025-09","hasta":"2026-09"},"primero":{"periodo":"2025-09","valor":2.08799365989528},"ultimo":{"periodo":"2026-09","valor":2.84823369707569},"cambio":0.7602400371804099,"variacion_pct":36.41007402381377,"promedio":2.354754666111215,"maximo":{"periodo":"2026-09","valor":2.84823369707569},"minimo":{"periodo":"2025-09","valor":2.08799365989528},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01279PM/json/2025-9/2026-9"}
```

</details>

<details><summary>Resultado</summary>

```
{"codigo":"PD12912AM","nombre":"Expectativas macroeconómicas - Expectativa de Inflación a 12 meses","frecuencia":"Mensual","periodo":{"desde":"2025-09","hasta":"2026-09"},"primero":{"periodo":"2025-09","valor":2.1625},"ultimo":{"periodo":"2026-09","valor":3.0875},"cambio":0.9249999999999998,"variacion_pct":42.77456647398843,"promedio":2.538653846153847,"maximo":{"periodo":"2026-09","valor":3.0875},"minimo":{"periodo":"2026-01","valor":2.025},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD12912AM/json/2025-9/2026-9"}
```

</details>

<details><summary>Resultado</summary>

```
{"codigo":"PN09819PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC Alimentos y Energía","frecuencia":"Mensual","periodo":{"desde":"2025-09","hasta":"2026-09"},"primero":{"periodo":"2025-09","valor":0.831379875935237},"ultimo":{"periodo":"2026-09","valor":4.5900959530384},"cambio":3.758716077103163,"variacion_pct":452.10573239758816,"promedio":2.617235629169578,"maximo":{"periodo":"2026-09","valor":4.5900959530384},"minimo":{"periodo":"2025-09","valor":0.831379875935237},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN09819PM/json/2025-9/2026-9"}
```

</details>

<details><summary>Resultado</summary>

```
{"codigo":"PD04722MM","nombre":"Tasas de interés del Banco Central de Reserva - Tasa de Referencia de la Política Monetaria","frecuencia":"Mensual","periodo":{"desde":"2025-09","hasta":"2026-09"},"primero":{"periodo":"2025-09","valor":4.25},"ultimo":{"periodo":"2026-09","valor":4.25},"cambio":0,"variacion_pct":0,"promedio":4.25,"maximo":{"periodo":"2025-09","valor":4.25},"minimo":{"periodo":"2025-09","valor":4.25},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04722MM/json/2025-9/2026-9"}
```

</details>

**Herramienta `mcp__bcrp__resumen`**

```json
{
 "codigo": "PN01273PM",
 "desde": "2021-01",
 "hasta": "2026-09"
}
```

**Herramienta `mcp__bcrp__serie`**

```json
{
 "codigo": "PD12301MD",
 "desde": "2026-10-01",
 "hasta": "2026-10-23"
}
```

<details><summary>Resultado</summary>

```
{"codigo":"PN01273PM","nombre":"Índice de precios Lima Metropolitana (var% 12 meses) - IPC","frecuencia":"Mensual","periodo":{"desde":"2021-01","hasta":"2026-09"},"primero":{"periodo":"2021-01","valor":2.67554538350913},"ultimo":{"periodo":"2026-09","valor":4.54865469481509},"cambio":1.87310931130596,"variacion_pct":70.00850454083013,"promedio":4.301080593093512,"maximo":{"periodo":"2022-06","valor":8.81263294388897},"minimo":{"periodo":"2025-08","valor":1.10633077531991},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01273PM/json/2021-1/2026-9"}
```

</details>

<details><summary>Resultado</summary>

```
{"codigo":"PD12301MD","nombre":"Tasas de interés - Tasa de Referencia de la Política Monetaria","frecuencia":"Diaria","datos":[{"periodo":"2026-10-01","valor":4.25},{"periodo":"2026-10-02","valor":4.25},{"periodo":"2026-10-05","valor":4.25},{"periodo":"2026-10-06","valor":4.25},{"periodo":"2026-10-07","valor":4.25},{"periodo":"2026-10-09","valor":4.25},{"periodo":"2026-10-12","valor":4.25},{"periodo":"2026-10-13","valor":4.25},{"periodo":"2026-10-14","valor":4.25},{"periodo":"2026-10-15","valor":4.25},{"periodo":"2026-10-16","valor":4.25},{"periodo":"2026-10-19","valor":4.25},{"periodo":"2026-10-20","valor":4.25},{"periodo":"2026-10-21","valor":4.25},{"periodo":"2026-10-22","valor":4.25},{"periodo":"2026-10-23","valor":4.25}],"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD12301MD/json/2026-10-01/2026-10-23"}
```

</details>

## 🤖 Claude · 2026-10-28 21:09:53

# Informe breve: inflación en el Perú (sep-2025 a sep-2026)

**Fuente:** BCRP, consultado el 28-oct-2026. Todas las cifras son de **Lima Metropolitana**, que es el IPC de referencia del BCRP, y no del país completo.

## 1. Resumen
- La inflación a 12 meses subió de **1,36 %** en septiembre de 2025 a **4,55 %** en septiembre de 2026, un aumento de **3,19 puntos porcentuales**. Septiembre de 2026 es el dato más alto del periodo.
- La subida fue mucho mayor en **alimentos y energía** (+3,76 pp) que en la **inflación subyacente** (+0,76 pp).
- Las **expectativas de inflación** a 12 meses pasaron de 2,16 % a 3,09 %.
- La **tasa de referencia** se mantuvo en **4,25 %** durante todo el periodo.

## 2. Inflación total (IPC)
Serie `PN01273PM`, var. % 12 meses, mensual:

| Mes | Valor | Mes | Valor |
|---|---|---|---|
| Sep-25 | 1,36 % | Mar-26 | 3,80 % |
| Oct-25 | 1,35 % (mínimo del periodo) | Abr-26 | 4,01 % |
| Nov-25 | 1,37 % | May-26 | 3,91 % |
| Dic-25 | 1,51 % | Jun-26 | 4,01 % |
| Ene-26 | 1,70 % | Jul-26 | 4,07 % |
| Feb-26 | 2,21 % | Ago-26 | 4,44 % |
|  |  | Sep-26 | **4,55 %** (máximo del periodo) |

- **Cuándo cambió:** el salto más visible está entre febrero (2,21 %) y marzo de 2026 (3,80 %). Desde marzo, la serie lleva **siete meses seguidos por encima de 3 %**.
- **Contexto desde enero de 2021:** el máximo fue **8,81 % en junio de 2022** y el mínimo **1,11 % en agosto de 2025**. El dato actual está lejos del pico de 2022, pero es cuatro veces el mínimo de hace un año.
- **Rango meta:** el BCRP busca una inflación entre 1 % y 3 %. Este rango no viene de las series consultadas, sino del marco de metas de inflación del BCRP.

## 3. Componentes
Todas son var. % 12 meses, mensuales:

| Serie | Código | Sep-25 | Sep-26 | Cambio |
|---|---|---|---|---|
| IPC Subyacente | `PN01279PM` | 2,09 % | 2,85 % | +0,76 pp |
| IPC Alimentos y Energía | `PN09819PM` | 0,83 % | 4,59 % | +3,76 pp |

- La inflación subyacente quita los precios más volátiles. Subió poco y en septiembre de 2026 seguía por debajo de 3 %.
- Alimentos y energía subió mucho más y hoy está en un nivel parecido al IPC total.
- Esto describe cómo se movió cada grupo de precios. No dice qué provocó la subida.

## 4. Expectativas y política monetaria
- **Expectativa de inflación a 12 meses** (`PD12912AM`, %, mensual): pasó de 2,16 % en septiembre de 2025 a **3,09 %** en septiembre de 2026. Su mínimo fue 2,03 % en enero de 2026, y el dato de septiembre de 2026 es el máximo del periodo.
- **Tasa de referencia** (`PD04722MM`, % anual, mensual): **4,25 %** todos los meses de septiembre de 2025 a septiembre de 2026. La serie diaria (`PD12301MD`) también marca 4,25 % hasta el 23 de octubre de 2026.

## 5. Advertencias
- **Sin causalidad:** que la inflación y las expectativas suban a la vez, o que la tasa no cambie, no permite concluir que una variable causó a otra. Las series solo muestran movimientos al mismo tiempo.
- **Puntos porcentuales:** las series ya están en %, así que los cambios se expresan en pp. La "variación %" que entrega la herramienta (por ejemplo, 234,9 %) no tiene sentido económico aquí.
- **Cobertura:** las series son de Lima Metropolitana, no del país completo.
- **Fecha de los datos:** las series de IPC se actualizaron el 08-oct-2026. El último dato disponible es septiembre de 2026.

## Fuentes (API oficial BCRP)
- `PN01273PM`, IPC var. % 12m, sep-25 a sep-26: https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01273PM/json/2025-9/2026-9
- `PN01273PM`, IPC var. % 12m, ene-21 a sep-26: https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01273PM/json/2021-1/2026-9
- `PN01279PM`, IPC Subyacente var. % 12m: https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01279PM/json/2025-9/2026-9
- `PN09819PM`, IPC Alimentos y Energía var. % 12m: https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN09819PM/json/2025-9/2026-9
- `PD12912AM`, Expectativa de inflación a 12 meses: https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD12912AM/json/2025-9/2026-9
- `PD04722MM`, Tasa de referencia (mensual): https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04722MM/json/2025-9/2026-9
- `PD12301MD`, Tasa de referencia (diaria), 01 a 23-oct-2026: https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD12301MD/json/2026-10-01/2026-10-23

Si lo necesitas para entregar, puedo pasarlo a un documento compartible o agregarle un gráfico del IPC y sus componentes.
