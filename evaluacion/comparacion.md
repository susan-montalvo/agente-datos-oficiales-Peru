# Evaluación comparativa del agente

Este documento compara las respuestas de Claude Code a las 10 preguntas de
[`preguntas.csv`](preguntas.csv) en dos configuraciones: sin MCP ni Skills
(Modo A) y con MCP y Skills (Modo B). El detalle por pregunta y modo está en
[`resultados.csv`](resultados.csv).

## Condiciones del experimento

- **Modelo y versión:** los dos modos usaron Claude Code 2.1.318 con el modelo
  `claude-opus-5-5`. Los datos se tomaron de los registros de sesión.
- **Instrucciones:** se usó la misma instrucción base en los dos modos, y el
  Modo B agregó la indicación de usar las herramientas del proyecto.
  - Modo A: "responde las 10 preguntas del csv, pon las respuestas en una
    columna a la derecha del documento".
  - Modo B: "responde las 10 preguntas formuladas en el csv, utiliza el mcp y
    las skills desarrolladas de la carpeta agente-datos-oficiales-Peru […],
    escribe las respuesta en una columna a la derecha de las preguntas".
- **Modo A (sin MCP ni Skills):** la sesión se abrió en una carpeta aparte
  (`GitHub/Modo A`), fuera del repositorio, sin `.mcp.json` ni Skills del
  proyecto. Tenía habilitadas las herramientas estándar de Claude Code: terminal
  (`Bash`), lectura y escritura de archivos, y búsqueda web. Usó `Bash` (16
  veces), `WebSearch` (1) y `Write` (2), y por terminal consultó la API del BCRP
  y la API de GitHub con `curl`.
- **Modo B (con MCP y Skills):** la sesión se abrió en una carpeta aparte
  (`GitHub/Modo B`) y usó el servidor MCP `bcrp` y las Skills de este
  repositorio. Tenía las mismas herramientas estándar que el Modo A. Usó `Bash`
  (14 veces) y `Write` (1). El MCP se ejecutó con un cliente FastMCP por `stdio`,
  porque no estaba conectado de forma nativa a esa sesión. Las Skills
  `limpiando-enaho` y `graficando-enaho` se ejecutaron con sus scripts
  (`uv run …/scripts/*.py`).
- **Ejecuciones en sesiones independientes:** se hizo una sesión por modo, con
  las 10 preguntas en una sola instrucción, y no una sesión por pregunta. Ver
  [Principales errores y limitaciones](#principales-errores-y-limitaciones).
- **Intento descartado del Modo B:** antes de la ejecución válida hubo un
  primer intento del Modo B con GitHub Copilot (modelo `gpt-6-luna`), el 6 de
  noviembre entre las 09:22 y las 09:28, en la carpeta `GitHub/Modo B`. Se
  descartó porque la pauta pide mantener el mismo modelo en los dos modos, y el
  Modo A se ejecutó con Claude Code (`claude-opus-5-5`). Después, el Modo B se
  repitió con Claude Code desde las 09:32 en una sesión nueva, en la carpeta
  `GitHub/Modo B firme`, que luego se renombró `Modo B`. Según su registro, esa
  sesión nueva solo listó los nombres de archivo de las carpetas `Modo A` y
  `Modo B` y no abrió sus respuestas. Las respuestas del intento
  descartado no se evaluaron. Su conversación completa está en
  [`evidencias_ia/evaluacion/06_2026-11-06_modo-b-primer-intento-copilot.md`](../evidencias_ia/evaluacion/06_2026-11-06_modo-b-primer-intento-copilot.md).
- **Acceso a respuestas esperadas:** ninguno de los dos modos tuvo acceso a las
  respuestas esperadas. Cada modo trabajó con una copia de `preguntas.csv` que
  solo tenía las preguntas.
- **Tolerancias definidas antes de ejecutar:** sí. Las respuestas esperadas y
  las tolerancias están en `preguntas.csv`. Se fijaron el 5 de noviembre de 2026
  (archivo original `preguntas.completo.csv`, 21:38), antes de las ejecuciones
  del 6 de noviembre (Modo A desde las 08:52; Modo B desde las 09:32, hora de
  Lima). No se modificaron después de ver los resultados.

## Criterios de corrección

- **Preguntas BCRP y ENAHO (P01–P08):** una respuesta es correcta si
  |valor generado − valor esperado| ≤ tolerancia de `preguntas.csv`. Se compara
  el valor más preciso que aparece en la respuesta de cada modo (por ejemplo,
  5.7069 en "5.71 % (5.7069)"). La diferencia queda en la columna
  `diferencia_absoluta` de `resultados.csv`.
- **Preguntas combinadas (P09 y P10):** una respuesta es correcta si el dato
  cumple la tolerancia **y** la interpretación es coherente (columna
  `interpretacion_coherente`). Se considera coherente si identifica bien los
  componentes del cálculo y sus unidades, y si no presenta el resultado como una
  relación causal.

> **Desviación declarada:** el criterio de coherencia de la interpretación para
> P09 y P10 se definió **después** de observar las respuestas, no antes, como
> pide la pauta. No cambia ningún resultado: las cuatro respuestas combinadas
> (P09 y P10 en ambos modos) se juzgaron coherentes, y la corrección de P10
> depende solo de la tolerancia del dato. Las respuestas esperadas y las
> tolerancias numéricas sí se fijaron antes de ejecutar.

## Resultados

| Métrica | Modo A | Modo B |
|---|---:|---:|
| Respuestas correctas | 2 / 10 | 2 / 10 |
| Incorrectas | 8 | 8 |
| Sin respuesta o con error de ejecución | 0 | 0 |
| Tiempo total de la sesión (segundos) | 409.4 | 174.3 |
| Tiempo promedio por pregunta (segundos) | 40.9 | 17.4 |

- Los dos modos aciertan las mismas preguntas: **P04** (tasa de referencia) y
  **P09** (cociente combinado).
- El tiempo se midió desde la instrucción hasta la última respuesta del agente,
  con las marcas de tiempo de los registros de sesión. El promedio es el tiempo
  total dividido entre 10, porque no se midió por pregunta.
- **Análisis de sensibilidad (no reemplaza el criterio oficial):** si se
  aceptara el redondeo a la precisión con que se reporta la respuesta, P01–P03 y
  P10 también serían correctas y cada modo tendría **6 / 10**. Los modos siguen
  empatados.

## Preguntas que mejoraron o empeoraron

**Ninguna pregunta cambió de resultado entre el Modo A y el Modo B.** Las
diferencias numéricas entre los modos son mínimas (por ejemplo, P03: 3.75389 en
el Modo A y 3.7539 en el Modo B).

El Modo B mejoró en el **proceso**, no en los aciertos:

| Aspecto | Modo A | Modo B |
|---|---|---|
| Fuente ENAHO (P05–P08, P10) | CSV de un repositorio de GitHub de terceros, porque el sitio del INEI no respondió | Microdatos oficiales del INEI (`.dta`) de `datos/` |
| Fuente BCRP | API del BCRP descargada con `curl` | La misma API, mediante el MCP `bcrp` (`serie`, `resumen`) |
| Consulta de resultados de terceros | Sí: descargó cifras de pobreza por edad y sexo de otro proyecto | No |
| Evidencias reproducibles | README con la metodología | README, scripts, respuestas del MCP en JSON, cálculos y figuras |
| Tiempo total | 409.4 s | 174.3 s (57 % menos) |

## Principales errores y limitaciones

1. **Redondeo frente a tolerancias muy estrictas (P01–P03 y P10, ambos
   modos).** El dato es correcto, pero los dos modos reportaron 4–5 decimales y
   la tolerancia es 1e-12 (P01–P03) o 0.0001 (P10). La tolerancia no se ajustó
   después de ver los resultados. Con una tolerancia acorde a la precisión de la
   pregunta (por ejemplo, 0.01), esas respuestas serían correctas.
2. **Filtro de población distinto (P05–P08, ambos modos).** Los dos modos usaron
   a los residentes habituales (`(p204 = 1 y p205 = 2) o (p204 = 2 y p206 = 1)`,
   108,664 personas). El procedimiento esperado usa a los miembros del hogar con
   `p204 = 1` (109,842 personas), cuyo conteo por hogar coincide con `mieperho`
   y reproduce la pobreza nacional de la Sumaria (27.58 %). Con el filtro de los
   modos, la pobreza nacional por personas es 27.53 %. Las diferencias van de
   0.03 a 0.14 pp. En el Modo B, el filtro viene de la Skill `limpiando-enaho`,
   así que **el error se origina en la Skill**.
3. **Contaminación del Modo A.** Como el INEI no respondió, el Modo A tomó los
   microdatos de un repositorio de GitHub no oficial. Además, para validar sus
   cifras descargó resultados ya calculados de otro proyecto público
   (`AlexNoblejas/enaho-2024-skills`: pobreza por edad y por sexo). La pauta pide
   evitar que el Modo A acceda indirectamente a respuestas calculadas. Esos
   resultados no eran las respuestas esperadas de esta evaluación, y el Modo A
   igual falló P05–P08.
4. **Uso indirecto del MCP y de las Skills en el Modo B.** El MCP no estaba
   conectado de forma nativa a la sesión: se usó con un cliente FastMCP por
   `stdio`, pero el servidor, las herramientas y la API son los mismos. Las
   Skills se ejecutaron con sus scripts y no se activaron con el mecanismo de
   Skills de Claude Code. P06 (0–4 años) y P10 (variable `linea`) se calcularon
   fuera de las Skills, porque las Skills no cubren esos casos.
5. **Sesiones y tiempo.** Las 10 preguntas se respondieron en una sola sesión
   por modo y no en sesiones independientes por pregunta. Por eso el tiempo es
   un promedio por modo y no una medición por pregunta, y una respuesta pudo
   influir en las siguientes dentro de la misma sesión.
6. **Criterio de interpretación definido después** de ver las respuestas (ver
   [Criterios de corrección](#criterios-de-corrección)).

## Conclusión

Con el criterio definido antes de ejecutar, **MCP y Skills no mejoraron la
cantidad de aciertos**: los dos modos obtuvieron 2 / 10 (6 / 10 si se acepta el
redondeo). Los errores comunes no se deben a que falte alguna herramienta. Se
deben a tolerancias más estrictas que la precisión reportada y a un filtro de
población que las dos configuraciones aplicaron igual.

MCP y Skills sí aportaron en **velocidad, trazabilidad y validez de las
fuentes**. El Modo B tardó 57 % menos, usó microdatos oficiales del INEI y la API
del BCRP mediante herramientas del proyecto, y dejó evidencias reproducibles. El
Modo A dependió de un repositorio no oficial y de resultados de terceros para
validarse. Esto muestra que el aporte de las herramientas se ve más en la
confiabilidad del proceso que en el puntaje.

El experimento también mostró una mejora concreta para el agente: revisar el
filtro de población de `limpiando-enaho`. Como una Skill fija una regla que se
aplica en todas las respuestas, un error en esa regla se repite en todas las
preguntas que dependen de ella.
