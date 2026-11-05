# Parte 3: plan de análisis

## Pregunta de investigación

¿Cómo evolucionó la actividad económica del Perú durante 2024 y cómo se
distribuyó territorialmente la pobreza monetaria entre sus departamentos en
ese mismo año?

## 1. Evolución de la actividad económica

- Consultar en el MCP BCRP la serie mensual `PN01728AM`, variación porcentual
  interanual del Producto Bruto Interno (PBI), para enero-diciembre de 2024.
- Presentar los 12 valores en un gráfico de línea: meses en el eje horizontal
  y variación interanual porcentual en el eje vertical.
- Describir el mínimo, el máximo, el valor de diciembre y el recorrido durante
  el año. El promedio simple de las tasas mensuales puede incluirse solo como
  resumen descriptivo; no debe denominarse crecimiento anual del PBI.
- Citar la serie y el período consultado:
  [BCRP, PN01728AM, 2024](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01728AM/json/2024-1/2024-12).

## 2. Distribución territorial de la pobreza monetaria

- Usar la ENAHO 2024 procesada a partir de los módulos 02 y 34 mediante
  `limpiando-enaho`.
- Obtener la pobreza por departamento con `mapeando-enaho`, ponderando la
  sumaria por `factor07 × mieperho`.
- Presentar el mapa coroplético y un ranking departamental. Unir los
  indicadores con las geometrías mediante códigos territoriales (`ubigeo[:2]`
  y `FIRST_IDDP`), nunca solo por nombres, y mantener Lima y Callao separados.
- Verificar las 25 unidades y comparar los resultados con
  [la referencia departamental ENAHO 2024](referencias/pobreza_departamento_2024.csv).

## 3. Integración e interpretación

Presentar ambos componentes como perspectivas complementarias de 2024: una
serie temporal nacional de actividad económica y una distribución territorial
de pobreza. Describir sus patrones sin afirmar que el crecimiento del PBI
causó las diferencias departamentales de pobreza; este análisis descriptivo no
identifica causalidad.

## 4. Entregables

1. Gráfico de la variación interanual mensual del PBI en 2024, con título,
   período, unidad y fuente BCRP.
2. Mapa y tabla ordenada de pobreza monetaria departamental ENAHO 2024, con
   unidad, fuente y resultado de las validaciones.
3. Texto breve que integre los hallazgos y explicite su alcance descriptivo.
