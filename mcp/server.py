"""MCP server for official Banco Central de Reserva del Peru time series."""

from __future__ import annotations

import re
import time
import unicodedata
from functools import lru_cache
from pathlib import Path
from typing import Any

import httpx
import pandas as pd
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError

CATALOG_URL = "https://estadisticas.bcrp.gob.pe/estadisticas/series/metadata"
API_URL = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"
CATALOG_PATH = Path(__file__).parent / "data" / "catalogo_bcrp.csv"
READ_ONLY = {"readOnlyHint": True, "openWorldHint": True}

mcp = FastMCP(
    "bcrp",
    instructions=(
        "Consulta series oficiales del BCRP. Busca primero el codigo con "
        "buscar_series, usa serie para observaciones y resumen para estadisticas. "
        "Cita siempre el codigo, el periodo y el enlace oficial; no estimes cifras."
    ),
)

_COLUMN_NAMES = {
    "Código de serie": "codigo",
    "Categoría de serie": "categoria",
    "Grupo de serie": "grupo",
    "Nombre de serie": "nombre",
    "Frecuencia": "frecuencia",
    "Fecha de actualización": "actualizada",
    "Fecha de inicio": "inicio",
}


def _sin_tildes(texto: str) -> str:
    normalizado = unicodedata.normalize("NFD", texto.casefold())
    return "".join(caracter for caracter in normalizado if unicodedata.category(caracter) != "Mn")


@lru_cache(maxsize=1)
def _catalogo() -> pd.DataFrame:
    """Load the official series catalog, downloading and caching it on first use."""
    try:
        if not CATALOG_PATH.exists():
            CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
            respuesta = httpx.get(CATALOG_URL, timeout=120)
            respuesta.raise_for_status()
            CATALOG_PATH.write_bytes(respuesta.content)
        catalogo = pd.read_csv(CATALOG_PATH, sep=";", encoding="latin-1", dtype=str).fillna("")
    except (httpx.HTTPError, OSError, pd.errors.ParserError, UnicodeError) as exc:
        raise ToolError(f"No se pudo cargar el catalogo oficial del BCRP: {exc}") from exc

    columnas_faltantes = set(_COLUMN_NAMES).difference(catalogo.columns)
    if columnas_faltantes:
        raise ToolError(
            "El catalogo del BCRP no contiene las columnas esperadas: "
            + ", ".join(sorted(columnas_faltantes))
        )

    catalogo = catalogo.rename(columns=_COLUMN_NAMES)
    catalogo["texto_busqueda"] = (
        catalogo["categoria"] + " " + catalogo["grupo"] + " " + catalogo["nombre"]
    ).map(_sin_tildes)
    return catalogo


def _ficha(codigo: str) -> dict[str, str]:
    filas = _catalogo()
    coincidencias = filas.loc[filas["codigo"] == codigo]
    if coincidencias.empty:
        raise ToolError(f"No existe el codigo de serie {codigo!r}. Buscalo con buscar_series.")

    fila = coincidencias.iloc[0]
    return {
        "codigo": fila["codigo"],
        "nombre": f"{fila['grupo']} - {fila['nombre']}",
        "categoria": fila["categoria"],
        "frecuencia": fila["frecuencia"],
        "inicio": fila["inicio"],
        "actualizada": fila["actualizada"],
    }


@mcp.tool(annotations=READ_ONLY)
def buscar_series(texto: str, frecuencia: str | None = None, limite: int = 10) -> list[dict[str, str]]:
    """Busca series BCRP por palabras clave, categoria, grupo o frecuencia.

    Todas las palabras de texto deben aparecer en los metadatos de la serie.
    Ejemplos: "ipc 12 meses", "tipo de cambio venta" o "reservas internacionales".
    """
    if not texto.strip():
        raise ToolError("El texto de busqueda no puede estar vacio.")
    if not 1 <= limite <= 50:
        raise ToolError("El limite debe ser un entero entre 1 y 50.")

    catalogo = _catalogo()
    coincidencias = pd.Series(True, index=catalogo.index)
    for palabra in _sin_tildes(texto).split():
        coincidencias &= catalogo["texto_busqueda"].str.contains(re.escape(palabra), na=False)
    if frecuencia:
        coincidencias &= catalogo["frecuencia"].str.casefold() == frecuencia.casefold()

    encontrados = catalogo.loc[coincidencias].copy()
    encontrados["obsoleta"] = encontrados["actualizada"] < "2025"
    encontrados["largo"] = (encontrados["grupo"] + encontrados["nombre"]).str.len()
    encontrados = encontrados.sort_values(["obsoleta", "largo"])
    return [_ficha(codigo) for codigo in encontrados["codigo"].head(limite)]


def _fecha_api(fecha: str, frecuencia: str) -> str:
    frecuencia = frecuencia.casefold()
    if "diari" in frecuencia:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fecha):
            raise ToolError(f"Fecha diaria invalida: {fecha!r}. Usa YYYY-MM-DD.")
        try:
            return pd.Timestamp(fecha).strftime("%Y-%m-%d")
        except (TypeError, ValueError):
            raise ToolError(f"Fecha diaria invalida: {fecha!r}. Usa YYYY-MM-DD.") from None

    mensual = re.fullmatch(r"(\d{4})-(\d{1,2})", fecha)
    if mensual and "mensual" in frecuencia:
        mes = int(mensual.group(2))
        if 1 <= mes <= 12:
            return f"{mensual.group(1)}-{mes}"
        raise ToolError(f"Mes invalido en {fecha!r}.")

    trimestral = re.fullmatch(r"(\d{4})-T([1-4])", fecha, re.IGNORECASE)
    if trimestral and "trimestral" in frecuencia:
        return f"{trimestral.group(1)}-{trimestral.group(2)}"

    if re.fullmatch(r"\d{4}", fecha) and "anual" in frecuencia:
        return fecha

    raise ToolError(
        f"Fecha {fecha!r} incompatible con la frecuencia {frecuencia!r}. "
        "Usa YYYY-MM (mensual), YYYY-T1 (trimestral), "
        "YYYY-MM-DD (diaria) o YYYY (anual)."
    )


def _clave_fecha_api(fecha: str, frecuencia: str) -> tuple[int, ...]:
    frecuencia = frecuencia.casefold()
    if "diari" in frecuencia:
        return tuple(int(parte) for parte in fecha.split("-"))
    if "mensual" in frecuencia or "trimestral" in frecuencia:
        anio, periodo = fecha.split("-")
        return int(anio), int(periodo)
    return (int(fecha),)


def _periodo_api(nombre: str, frecuencia: str) -> str:
    frecuencia = frecuencia.casefold()
    meses = {
        "ene": "01",
        "jan": "01",
        "feb": "02",
        "mar": "03",
        "abr": "04",
        "apr": "04",
        "may": "05",
        "jun": "06",
        "jul": "07",
        "ago": "08",
        "aug": "08",
        "set": "09",
        "sep": "09",
        "oct": "10",
        "nov": "11",
        "dic": "12",
        "dec": "12",
    }
    if "diari" in frecuencia:
        coincidencia = re.fullmatch(r"(\d{2})\.([A-Za-zÁÉÍÓÚáéíóú]{3})\.(\d{2})", nombre)
        if coincidencia:
            dia, mes, anio = coincidencia.groups()
            mes_numero = meses.get(_sin_tildes(mes)[:3])
            if mes_numero:
                prefijo = "20" if int(anio) < 69 else "19"
                return f"{prefijo}{anio}-{mes_numero}-{dia}"

    if "mensual" in frecuencia:
        coincidencia = re.fullmatch(r"([A-Za-zÁÉÍÓÚáéíóú]{3})\.(\d{4})", nombre)
        if coincidencia:
            mes, anio = coincidencia.groups()
            mes_numero = meses.get(_sin_tildes(mes)[:3])
            if mes_numero:
                return f"{anio}-{mes_numero}"

    if "trimestral" in frecuencia:
        coincidencia = re.fullmatch(r"T([1-4])\.(\d{2})", nombre)
        if coincidencia:
            trimestre, anio = coincidencia.groups()
            prefijo = "20" if int(anio) < 69 else "19"
            return f"{prefijo}{anio}-T{trimestre}"

    if "anual" in frecuencia and re.fullmatch(r"\d{4}", nombre):
        return nombre
    raise ToolError(f"El BCRP devolvio un periodo no reconocido: {nombre!r}.")


@lru_cache(maxsize=256)
def _descargar(codigo: str, desde: str, hasta: str, frecuencia: str) -> tuple[dict[str, Any], ...]:
    url = f"{API_URL}/{codigo}/json/{desde}/{hasta}"
    for intento in range(3):
        try:
            respuesta = httpx.get(url, timeout=60)
            respuesta.raise_for_status()
            payload = respuesta.json()
        except httpx.HTTPStatusError as exc:
            status = exc.response.status_code
            if (status == 429 or status >= 500) and intento < 2:
                time.sleep(2 * (intento + 1))
                continue
            raise ToolError(f"El BCRP respondio HTTP {status} al consultar {codigo}.") from exc
        except httpx.RequestError as exc:
            if intento < 2:
                time.sleep(2 * (intento + 1))
                continue
            raise ToolError(f"No se pudo consultar la API del BCRP: {exc}") from exc
        except ValueError as exc:
            if intento < 2:
                time.sleep(2 * (intento + 1))
                continue
            raise ToolError("El BCRP no devolvio JSON valido despues de tres intentos.") from exc

        periodos = payload.get("periods")
        if not isinstance(periodos, list):
            raise ToolError(f"La respuesta del BCRP no contiene periodos para {codigo}.")

        datos: list[dict[str, Any]] = []
        for periodo in periodos:
            valores = periodo.get("values", [])
            valor = valores[0] if valores else None
            if valor is None or str(valor).strip().casefold() in {"", "n.d.", "n.d", "nd"}:
                continue
            try:
                numero = float(str(valor).replace(",", "."))
            except ValueError as exc:
                raise ToolError(
                    f"El BCRP devolvio un valor no numerico para "
                    f"{periodo.get('name')!r}: {valor!r}."
                ) from exc
            datos.append({"periodo": _periodo_api(periodo["name"], frecuencia), "valor": numero})
        return tuple(datos)

    raise ToolError(f"No se pudieron descargar los datos de la serie {codigo}.")


@mcp.tool(annotations=READ_ONLY)
def serie(codigo: str, desde: str, hasta: str) -> dict[str, Any]:
    """Consulta observaciones BCRP en un intervalo inclusivo y devuelve la fuente reproducible.

    Usa YYYY-MM para series mensuales, YYYY-T1 para trimestrales, YYYY-MM-DD para
    diarias y YYYY para anuales.
    """
    ficha = _ficha(codigo)
    inicio = _fecha_api(desde, ficha["frecuencia"])
    fin = _fecha_api(hasta, ficha["frecuencia"])
    if _clave_fecha_api(inicio, ficha["frecuencia"]) > _clave_fecha_api(
        fin, ficha["frecuencia"]
    ):
        raise ToolError(f"El inicio {desde!r} debe ser anterior o igual al final {hasta!r}.")

    datos = _descargar(codigo, inicio, fin, ficha["frecuencia"])
    return {
        "codigo": ficha["codigo"],
        "nombre": ficha["nombre"],
        "frecuencia": ficha["frecuencia"],
        "datos": list(datos),
        "fuente": f"{API_URL}/{codigo}/json/{inicio}/{fin}",
    }


@mcp.tool(annotations=READ_ONLY)
def resumen(codigo: str, desde: str, hasta: str) -> dict[str, Any]:
    """Calcula extremos, cambio, variacion porcentual y promedio de una serie BCRP."""
    resultado = serie(codigo, desde, hasta)
    datos = resultado["datos"]
    if not datos:
        raise ToolError(f"No hay observaciones para {codigo} entre {desde} y {hasta}.")

    primero, ultimo = datos[0], datos[-1]
    cambio = ultimo["valor"] - primero["valor"]
    variacion = cambio / primero["valor"] * 100 if primero["valor"] else None
    return {
        "codigo": codigo,
        "nombre": resultado["nombre"],
        "frecuencia": resultado["frecuencia"],
        "periodo": {"desde": primero["periodo"], "hasta": ultimo["periodo"]},
        "primero": primero,
        "ultimo": ultimo,
        "cambio": cambio,
        "variacion_pct": variacion,
        "promedio": sum(punto["valor"] for punto in datos) / len(datos),
        "maximo": max(datos, key=lambda punto: punto["valor"]),
        "minimo": min(datos, key=lambda punto: punto["valor"]),
        "fuente": resultado["fuente"],
    }


@mcp.tool(annotations=READ_ONLY)
def comparar_series(codigo_a: str, codigo_b: str, desde: str, hasta: str) -> dict[str, Any]:
    """Alinea dos series BCRP por periodo y calcula su correlacion en observaciones coincidentes.

    Ambas series deben tener la misma frecuencia. La correlacion describe asociacion y
    no implica causalidad.
    """
    serie_a = serie(codigo_a, desde, hasta)
    serie_b = serie(codigo_b, desde, hasta)
    if serie_a["frecuencia"].casefold() != serie_b["frecuencia"].casefold():
        raise ToolError("Para comparar series, ambas deben tener la misma frecuencia.")

    valores_b = {punto["periodo"]: punto["valor"] for punto in serie_b["datos"]}
    pares = [
        {
            "periodo": punto["periodo"],
            "valor_a": punto["valor"],
            "valor_b": valores_b[punto["periodo"]],
        }
        for punto in serie_a["datos"]
        if punto["periodo"] in valores_b
    ]
    if len(pares) < 2:
        raise ToolError("Se necesitan al menos dos periodos coincidentes para comparar las series.")

    correlacion = pd.Series([punto["valor_a"] for punto in pares]).corr(
        pd.Series([punto["valor_b"] for punto in pares])
    )
    return {
        "codigo_a": codigo_a,
        "codigo_b": codigo_b,
        "periodos_coincidentes": len(pares),
        "correlacion": float(correlacion) if pd.notna(correlacion) else None,
        "datos": pares,
        "fuentes": [serie_a["fuente"], serie_b["fuente"]],
        "nota": "La correlacion describe asociacion; no demuestra causalidad.",
    }


@mcp.resource("bcrp://serie/{codigo}")
def recurso_ficha_serie(codigo: str) -> dict[str, str]:
    """Devuelve metadatos oficiales de una serie identificada por su codigo."""
    return _ficha(codigo)


@mcp.prompt
def informe(tema: str) -> str:
    """Prepara un informe breve con indicadores BCRP y referencias verificables."""
    return (
        f"Prepara un informe breve sobre {tema}. Busca las series BCRP relevantes y "
        "verifica las cifras con serie o resumen. Para cada cifra incluye codigo, "
        "periodo, unidad y enlace oficial. No estimes valores ni infieras causalidad "
        "de una correlacion."
    )


if __name__ == "__main__":
    mcp.run()
