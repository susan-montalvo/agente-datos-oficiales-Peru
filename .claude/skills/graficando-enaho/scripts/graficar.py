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
    ruta = FIGURAS / f"{args.indicador.replace('pobre', 'pobreza')}_{args.por}_{args.anio}.png"
    graficar(valores, titulo, args.anio, ruta)

    print(titulo + " (% de personas, ponderado con facpob07)")
    for nombre, valor in valores.sort_values(ascending=False).items():
        print(f"  {nombre}: {valor:.1f} %")
    print(f"Figura: {ruta.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
