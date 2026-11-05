"""Build reproducible Part 3 indicators and the BCRP activity chart.

Run from the repository root:
    uv run python scripts/parte3_analisis.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path.cwd()
PBI_CSV = ROOT / "datos" / "pbi_interanual_mensual_2024.csv"
ENAHO_PARQUET = ROOT / "salidas" / "personas_2024.parquet"
REFERENCE_CSV = ROOT / "referencias" / "pobreza_departamento_2024.csv"
MAP_PNG = ROOT / "mapas" / "pobreza_departamento.png"
OUTPUT = ROOT / "outputs" / "parte-3"

DEPARTAMENTOS = {
    "01": "Amazonas", "02": "Áncash", "03": "Apurímac", "04": "Arequipa",
    "05": "Ayacucho", "06": "Cajamarca", "07": "Callao", "08": "Cusco",
    "09": "Huancavelica", "10": "Huánuco", "11": "Ica", "12": "Junín",
    "13": "La Libertad", "14": "Lambayeque", "15": "Lima", "16": "Loreto",
    "17": "Madre de Dios", "18": "Moquegua", "19": "Pasco", "20": "Piura",
    "21": "Puno", "22": "San Martín", "23": "Tacna", "24": "Tumbes",
    "25": "Ucayali",
}
KEYS = ["conglome", "vivienda", "hogar"]


def build_pbi_chart() -> pd.DataFrame:
    pbi = pd.read_csv(PBI_CSV, parse_dates=["periodo"])
    if len(pbi) != 12 or pbi["periodo"].dt.year.nunique() != 1:
        raise ValueError("La serie BCRP debe contener los 12 meses de un solo año.")
    if pbi["periodo"].dt.month.tolist() != list(range(1, 13)):
        raise ValueError("La serie BCRP debe cubrir enero-diciembre sin saltos.")

    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.plot(pbi["periodo"], pbi["variacion_interanual_pct"], marker="o",
            linewidth=2, color="#2864a5")
    ax.axhline(0, linewidth=0.8, color="#777777")
    ax.set_xticks(pbi["periodo"])
    ax.set_xticklabels(["Ene", "Feb", "Mar", "Abr", "May", "Jun",
                        "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"])
    ax.set_ylabel("Variación interanual (%)")
    ax.set_title("Actividad económica del Perú: variación interanual del PBI, 2024")
    ax.grid(axis="y", alpha=0.25)
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.01, 0.01, "Fuente: BCRP, serie PN01728AM. Enero-diciembre de 2024.",
             fontsize=8, color="#444444")
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(OUTPUT / "pbi_interanual_mensual_2024.png", dpi=200,
                facecolor="white")
    plt.close(fig)
    return pbi


def build_poverty_ranking() -> pd.DataFrame:
    if not ENAHO_PARQUET.exists():
        raise FileNotFoundError(f"Falta {ENAHO_PARQUET}; ejecutar limpiando-enaho primero.")
    if not REFERENCE_CSV.exists():
        raise FileNotFoundError(f"Falta la referencia: {REFERENCE_CSV}")

    base = pd.read_parquet(ENAHO_PARQUET)
    hogares = base.drop_duplicates(KEYS).copy()
    hogares["departamento"] = hogares["ubigeo"].astype("string").str[:2]
    hogares["peso_hogar"] = hogares["factor07"] * hogares["mieperho"]
    hogares["pobre_ponderado"] = hogares["pobre"].astype(float) * hogares["peso_hogar"]
    grouped = hogares.groupby("departamento", sort=False)
    ranking = (100 * grouped["pobre_ponderado"].sum() /
               grouped["peso_hogar"].sum()).rename("pobreza_pct").reset_index()
    ranking["nombre_departamento"] = ranking["departamento"].map(DEPARTAMENTOS)
    if len(ranking) != 25 or ranking["departamento"].nunique() != 25:
        raise ValueError("La ENAHO debe producir 25 departamentos con códigos únicos.")

    reference = pd.read_csv(REFERENCE_CSV, dtype={"ccdd": str})
    checked = ranking.merge(
        reference, left_on="departamento", right_on="ccdd", how="outer",
        validate="1:1", indicator=True, suffixes=("_enaho", "_referencia")
    )
    if len(reference) != 25 or not checked["_merge"].eq("both").all():
        raise ValueError("La cobertura de códigos no coincide con la referencia.")
    checked["coincide"] = (
        checked["pobreza_pct_enaho"].round(1)
        == checked["pobreza_pct_referencia"].round(1)
    )
    if not checked["coincide"].all():
        failures = checked.loc[~checked["coincide"],
                               ["departamento", "pobreza_pct_enaho",
                                "pobreza_pct_referencia"]]
        raise ValueError(f"Diferencias frente a la referencia:\n{failures.to_string(index=False)}")

    ranking = ranking.sort_values("pobreza_pct", ascending=False)
    ranking[["departamento", "nombre_departamento", "pobreza_pct"]].to_csv(
        OUTPUT / "pobreza_departamental_2024.csv", index=False, float_format="%.4f"
    )
    return ranking


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pbi = build_pbi_chart()
    poverty = build_poverty_ranking()
    if not MAP_PNG.exists():
        raise FileNotFoundError(f"Falta el mapa de la Skill mapeando-enaho: {MAP_PNG}")
    map_copy = OUTPUT / "mapa_pobreza_departamental_2024.png"
    map_copy.write_bytes(MAP_PNG.read_bytes())

    rates = pbi["variacion_interanual_pct"]
    peak = pbi.loc[rates.idxmax()]
    trough = pbi.loc[rates.idxmin()]
    print("BCRP · PBI, variación interanual mensual, 2024")
    print(f"Promedio simple de las 12 tasas mensuales: {rates.mean():.2f} %")
    print(f"Máximo: {peak['periodo']:%Y-%m} ({peak['variacion_interanual_pct']:.2f} %)")
    print(f"Mínimo: {trough['periodo']:%Y-%m} ({trough['variacion_interanual_pct']:.2f} %)")
    print(f"Diciembre: {rates.iloc[-1]:.2f} %")
    print("\nENAHO · pobreza monetaria departamental 2024, %")
    for row in poverty.itertuples():
        print(f"  {row.departamento} {row.nombre_departamento}: {row.pobreza_pct:.1f} %")
    print("\n[OK] 25 departamentos con códigos únicos")
    print("[OK] cobertura completa y coincidencia con referencia a un decimal")
    print(f"\nResultados: {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
