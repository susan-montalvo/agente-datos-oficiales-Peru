"""Cálculos finales P01-P10 a partir de la base de limpiando-enaho, la sumaria y las respuestas del MCP bcrp."""
import json, sys
import pandas as pd
trabajo, mcp_json, datos = sys.argv[1], sys.argv[2], sys.argv[3]
b = pd.read_parquet(f"{trabajo}/salidas/personas_2024.parquet"); b["facpob07"] = b.facpob07.astype("float64")
def pct(mask, ind="pobre"):
    s = b[mask]; return 100 * (s[ind] * s.facpob07).sum() / s.facpob07.sum()
r = {}
r["n_personas"] = len(b)
r["P05_0_17"] = pct(b.p208a.between(0, 17))
r["P06_0_4_ext"] = pct(b.p208a.between(0, 4), "pobre_extremo")
r["P06_n"] = int(b.p208a.between(0, 4).sum())
r["P07_mujer"] = pct(b.p207 == 2)
r["P07_hombre"] = pct(b.p207 == 1)
r["P08_60mas"] = pct(b.p208a >= 60)
r["P08_dif"] = r["P05_0_17"] - r["P08_60mas"]
r["edad_min_max"] = [float(b.p208a.min()), float(b.p208a.max())]
# P10: línea de pobreza (Módulo 34), solo se leen las columnas necesarias
su = pd.read_stata(f"{datos}/966-Modulo34/sumaria-2024.dta", convert_categoricals=False,
                   columns=["conglome","vivienda","hogar","linea","linpe","factor07","mieperho","pobreza"])
su = su.astype({"factor07": "float64", "linea": "float64", "mieperho": "float64"}); w = su.factor07 * su.mieperho
r["linea_pond_personas"] = float((su.linea * w).sum() / w.sum())
r["linea_pond_hogares"] = float((su.linea * su.factor07).sum() / su.factor07.sum())
r["linea_simple"] = float(su.linea.mean())
r["linea_min_max"] = [float(su.linea.min()), float(su.linea.max())]
# MCP
m = json.load(open(mcp_json))["llamadas"]
pbi = {d["periodo"]: d["valor"] for d in m[0]["respuesta"]["datos"]}
tc = m[2]["respuesta"]["promedio"]
r["pbi"] = pbi; r["pbi_n"] = len(pbi)
r["P01"] = pbi["2024-05"]
r["P02"] = m[1]["respuesta"]["datos"][0]["valor"]
r["P03"] = tc
tpm = m[3]["respuesta"]["datos"]; r["P04"] = tpm[-1]["valor"] - tpm[0]["valor"]
prom_pbi = sum(pbi.values()) / len(pbi); r["prom_pbi"] = prom_pbi
r["P09_var_pp"] = 27.6 - 29.0
r["P09"] = (27.6 - 29.0) / prom_pbi
r["P10"] = r["linea_pond_personas"] / tc
r["P10_tc_red"] = round(r["linea_pond_personas"]) / round(tc, 2)
print(json.dumps(r, indent=1, ensure_ascii=False, default=float))
json.dump(r, open(f"{trabajo}/../calculos.json", "w"), ensure_ascii=False, indent=1, default=float)
