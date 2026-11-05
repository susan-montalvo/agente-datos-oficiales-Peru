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
        f"Filas en el módulo 200: {len(miembros):,}",
        f"Residentes habituales en la base: {len(base):,}",
        f"Pobreza (sumaria, factor07 × mieperho): {pob_hogares:.2f} %",
        f"Pobreza extrema (sumaria): {ext_hogares:.2f} %",
        f"Pobreza (personas, facpob07): {pob_personas:.2f} %",
        f"Pobreza oficial INEI: {oficial} %" if oficial is not None else "Pobreza oficial INEI: sin dato",
        "",
    ]
    lineas += [f"[{'OK' if ok else 'FALLA'}] {nombre}" for nombre, ok in chequeos.items()]
    estado = "VALIDACIÓN OK" if all(chequeos.values()) else "VALIDACIÓN FALLIDA"
    lineas += ["", estado]
    texto = "\n".join(lineas)
    (SALIDAS / "validacion.txt").write_text(texto + "\n", encoding="utf-8")
    print(texto)
    if not all(chequeos.values()):
        sys.exit(1)


if __name__ == "__main__":
    main()
