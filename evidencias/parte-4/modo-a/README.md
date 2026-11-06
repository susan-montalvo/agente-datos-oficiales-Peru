# Respuestas a `preguntas.csv`

> **Autoría:** este trabajo lo hizo **Claude** (modelo Claude Opus 5.5 de Anthropic, en Claude Code) el 6 de noviembre de 2026, a pedido de la usuaria. Claude buscó y descargó los datos, escribió el script de cálculo, obtuvo las cifras y redactó este README. Las respuestas están en la columna `respuesta` de [preguntas.csv](preguntas.csv).

## Resultados

| ID | Pregunta (resumen) | Respuesta |
|---|---|---|
| P01 | Var. interanual del PBI, mayo 2024 (PN01728AM) | 5.71 % |
| P02 | Inflación 12 meses Lima Metropolitana, dic. 2024 (PN01273PM) | 1.97 % |
| P03 | Tipo de cambio bancario promedio 2024 (PN01210PM) | S/ 3.754 por US$ |
| P04 | Cambio de la tasa de referencia, ene.–dic. 2024 (PD04722MM) | −1.50 pp |
| P05 | Pobreza monetaria, 0–17 años (ENAHO 2024) | 36.5 % |
| P06 | Pobreza extrema, 0–4 años (ENAHO 2024) | 10.0 % |
| P07 | Pobreza monetaria, mujeres (ENAHO 2024) | 27.7 % |
| P08 | Brecha de pobreza 0–17 años frente a 60+ años | 14.5 pp |
| P09 | (Var. de pobreza en pp) ÷ (promedio de var. mensuales del PBI 2024) | −0.40 |
| P10 | Línea de pobreza promedio 2024 en dólares | US$ 121.04 |

## 1. Búsqueda y obtención de datos

### BCRP (P01–P04, P09, P10)

Claude descargó las cuatro series de la API oficial de estadísticas del BCRP, de diciembre de 2023 a diciembre de 2024:

```
https://estadisticas.bcrp.gob.pe/estadisticas/series/api/{SERIE}/json/2023-12/2024-12
```

Las series son `PN01728AM` (PBI, var. % interanual), `PN01273PM` (IPC Lima Metropolitana, var. % 12 meses), `PN01210PM` (tipo de cambio bancario promedio) y `PD04722MM` (tasa de referencia).

### ENAHO 2024 (P05–P08, P10)

1. **Primer intento, la fuente oficial del INEI.** Claude intentó descargar los módulos 02 y 34 desde `proyectos.inei.gob.pe/iinei/srienaho/descarga/...`. El servidor no respondió: la conexión expiró tanto por HTTPS como por HTTP, y tampoco cargó `www.inei.gob.pe`.
2. **Búsqueda de una alternativa.** Claude buscó en la web y en la API de GitHub (`enaho 2024`) repositorios públicos que tuvieran los microdatos originales. Encontró los dos archivos necesarios en el repositorio **MsanchezBI/segmentacion-consumidores-enaho-2024**:
   - `Enaho01-2024-200.csv`: Módulo 02, características de los miembros del hogar (117 721 registros de personas).
   - `Sumaria-2024.csv`: Módulo 34, sumaria con las variables de pobreza (33 691 hogares).
3. **Validación de los archivos.** Como estos archivos no vienen directamente del INEI, Claude los contrastó de dos maneras:
   - Con ellos, la pobreza monetaria nacional da **27.58 %**, que coincide con el **27.6 %** que el INEI publicó para 2024.
   - Las cifras por sexo y edad coinciden exactamente con las de otro proyecto público independiente (AlexNoblejas/enaho-2024-skills): mujeres 27.676 % y personas de 60 años a más 22.020 %.

## 2. Metodología de cálculo

El cálculo se hizo con un script de Python que solo usa la librería estándar (`csv`, `json`).

### Preguntas BCRP

- **P01:** el valor de `PN01728AM` en mayo de 2024 (5.7069).
- **P02:** el valor de `PN01273PM` en diciembre de 2024 (1.9663).
- **P03:** el promedio simple de los 12 valores mensuales de `PN01210PM` en 2024 (3.75389).
- **P04:** diciembre 2024 menos enero 2024 de `PD04722MM`, es decir 5.00 − 6.50 = **−1.50 pp**.

### Preguntas ENAHO

1. **Unión de módulos.** Cada persona del Módulo 02 se unió con su hogar en la Sumaria usando la llave `CONGLOME + VIVIENDA + HOGAR`.
2. **Población de referencia.** Solo se contaron los residentes habituales, con el filtro estándar del INEI:
   `(P204 = 1 y P205 = 2)` o `(P204 = 2 y P206 = 1)`.
3. **Ponderador.** Se usó `FACTOR07`, el factor de expansión del hogar, aplicado a cada persona.
4. **Clasificación de pobreza.** Se usó la variable `POBREZA` de la Sumaria:
   - 1 = pobre extremo
   - 2 = pobre no extremo
   - 3 = no pobre

   Una persona es *pobre* si `POBREZA ∈ {1, 2}` y *pobre extrema* si `POBREZA = 1`.
5. **Grupos.** La edad se tomó de `P208A` y el sexo de `P207` (2 = mujer).
6. **Fórmula.** Para cada grupo se calculó el porcentaje ponderado:

```
% = 100 × Σ(FACTOR07 × indicador) / Σ(FACTOR07)
```

Resultados:

- **P05:** 0–17 años pobres = 36.471 %.
- **P06:** 0–4 años en pobreza extrema = 9.962 %.
- **P07:** mujeres pobres = 27.676 %.
- **P08:** 36.471 % − 22.020 % (60 años a más) = **14.451 pp**.

### Preguntas combinadas

- **P09:**
  - Variación de la pobreza: 27.6 − 29.0 = −1.4 pp.
  - Promedio simple de las 12 variaciones mensuales del PBI de 2024 (`PN01728AM`): 3.4825 %.
  - Cociente: −1.4 / 3.4825 = **−0.402**.
- **P10:**
  - Línea de pobreza promedio 2024: promedio de `LINEA` en la Sumaria, ponderado por población (`FACTOR07 × MIEPERHO`), igual a S/ 454.39 por persona al mes.
  - Conversión a dólares: 454.39 / 3.75389 = **US$ 121.04**.

## 3. Advertencias

- **Origen de los microdatos.** Los archivos ENAHO vienen de un repositorio de GitHub y no de la web del INEI, que no estaba disponible al momento del cálculo. La validación contra el 27.6 % oficial y contra otro proyecto independiente da confianza en ellos, pero conviene recalcular con los archivos oficiales cuando se pueda.
- **P08 está en el límite del redondeo.** La cifra exacta es 14.451 pp. Si además se excluye a trabajadores del hogar y pensionistas (`P203 ∈ {8, 9}`), da 14.443 pp, que se redondea a 14.4. Claude dejó 14.5 porque usa el filtro estándar del INEI y coincide con la referencia independiente.
- **Total a nivel persona.** Calculada persona por persona con el Módulo 02, la pobreza total da 27.53 %. Calculada a nivel hogar con la Sumaria (`FACTOR07 × MIEPERHO`), da 27.58 %. La pequeña diferencia viene de discrepancias entre el conteo de residentes y `MIEPERHO` en algunos hogares, y no cambia ninguna respuesta redondeada salvo el caso de P08 descrito arriba.
- **Copia del original.** Antes de modificar `preguntas.csv`, Claude guardó una copia de la versión original, sin la columna de respuestas, en el directorio temporal de la sesión.
