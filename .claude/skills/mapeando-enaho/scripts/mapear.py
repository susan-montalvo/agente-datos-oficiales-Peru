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
REFERENCIA_CSV = RAIZ / "referencias" / "pobreza_departamento_2024.csv"
URL_GEOJSON = "https://raw.githubusercontent.com/juaneladio/peru-geojson/master/peru_departamental_simple.geojson"

ESCALA = "Blues"  # un solo tono, de claro (0 %) a oscuro
TINTA = "#0b0b0b"
TINTA_SECUNDARIA = "#52514e"

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
    fig.tight_layout(rect=(0, 0.03, 1, 0.97))
    fig.savefig(ruta, dpi=200, facecolor="white", bbox_inches="tight", pad_inches=0.2)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--anio", type=int, default=2024)
    anio = parser.parse_args().anio

    archivo = SALIDAS / f"personas_{anio}.parquet"
    if not archivo.exists():
        sys.exit(f"Falta {archivo}. Usa primero la skill limpiando-enaho.")
    if not GEOJSON.exists():
        sys.exit(f"Falta {GEOJSON}. Bájalo de {URL_GEOJSON}")

    pobreza = pobreza_departamento(pd.read_parquet(archivo))
    pobreza.index = pobreza.index.astype(str).str.zfill(2)
    departamentos = gpd.read_file(GEOJSON)
    departamentos["FIRST_IDDP"] = departamentos["FIRST_IDDP"].astype(str).str.zfill(2)

    referencia = None
    if anio == 2024:
        if not REFERENCIA_CSV.exists():
            sys.exit(f"Falta el archivo de referencia: {REFERENCIA_CSV}")
        referencia = pd.read_csv(REFERENCIA_CSV, dtype={"ccdd": str})
        referencia["ccdd"] = referencia["ccdd"].str.zfill(2)

    chequeos = {
        "25 códigos territoriales únicos en la ENAHO": len(pobreza.index) == 25 and pobreza.index.is_unique,
        "25 códigos territoriales únicos en el GeoJSON": (
            len(departamentos) == 25 and departamentos["FIRST_IDDP"].is_unique
        ),
    }
    if referencia is not None:
        chequeos["25 códigos territoriales únicos en la referencia"] = (
            len(referencia) == 25 and referencia["ccdd"].is_unique
        )

    for nombre, ok in chequeos.items():
        print(f"[{'OK' if ok else 'FALLA'}] {nombre}")
    if not all(chequeos.values()):
        sys.exit("No se puede comparar: hay códigos territoriales duplicados o faltantes.")

    # Unir por código, nunca por nombre: ubigeo[:2] (departamento) con FIRST_IDDP
    mapa = departamentos.merge(pobreza, left_on="FIRST_IDDP", right_index=True, how="left", validate="1:1")
    codigos_mapa = set(mapa["FIRST_IDDP"])
    chequeos = {
        "25 departamentos en el GeoJSON": len(departamentos) == 25,
        "25 departamentos con dato": mapa.pobreza.notna().sum() == 25,
        "todos los códigos de la ENAHO están en el mapa": set(pobreza.index) == codigos_mapa,
        "Lima (15) y Callao (07) separados": {"15", "07"} <= set(mapa.dropna(subset="pobreza").FIRST_IDDP),
    }
    diferencias_referencia = []
    if referencia is not None:
        codigos_referencia = set(referencia["ccdd"])
        chequeos["todos los códigos de la referencia están en el mapa"] = (
            codigos_referencia == codigos_mapa
        )
        por_codigo = mapa.set_index("FIRST_IDDP")
        for _, fila_referencia in referencia.set_index("ccdd").iterrows():
            codigo = fila_referencia.name
            esperado = float(fila_referencia["pobreza_pct"])
            if codigo in por_codigo.index:
                fila_mapa = por_codigo.loc[codigo]
                nombre = fila_referencia["departamento"].title()
                calculado = float(fila_mapa["pobreza"])
                coincide = round(calculado, 1) == round(esperado, 1)
            else:
                nombre = fila_referencia["departamento"].title()
                calculado = None
                coincide = False
            chequeos[f"Referencia {nombre} ({codigo}): {esperado:.1f} %"] = coincide
            if not coincide:
                valor_calculado = f"{calculado:.1f} %" if calculado is not None else "sin dato"
                diferencias_referencia.append(
                    f"{codigo} {nombre}: ENAHO {valor_calculado}; referencia {esperado:.1f} %"
                )
    for nombre, ok in chequeos.items():
        print(f"[{'OK' if ok else 'FALLA'}] {nombre}")
    if not all(chequeos.values()):
        if diferencias_referencia:
            print("\nDiferencias con el archivo de referencia:")
            for diferencia in diferencias_referencia:
                print(f"  - {diferencia}")
        sys.exit("No se dibuja el mapa: hay chequeos que fallan.")

    titulo = f"Pobreza monetaria por departamento, Perú {anio}"
    MAPAS.mkdir(exist_ok=True)
    ruta = MAPAS / "pobreza_departamento.png"
    mapear(mapa, titulo, anio, ruta)

    print(f"\n{titulo} (% de personas, sumaria: factor07 × mieperho)")
    for _, fila in mapa.sort_values("pobreza", ascending=False).iterrows():
        print(f"  {fila.FIRST_IDDP} {fila.NOMBDEP.title()}: {fila.pobreza:.1f} %")
    print(f"Mapa: {ruta.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
