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
