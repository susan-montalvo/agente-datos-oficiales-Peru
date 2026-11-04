"""Pruebas adicionales de la herramienta propia comparar_series."""

import pytest
from fastmcp.exceptions import ToolError

import server


def _serie(codigo, frecuencia, datos):
    return {
        "codigo": codigo,
        "nombre": f"Serie {codigo}",
        "frecuencia": frecuencia,
        "datos": datos,
        "fuente": f"https://estadisticas.bcrp.gob.pe/{codigo}",
    }


def test_comparar_series_alinea_periodos_y_calcula_correlacion(monkeypatch):
    resultados = {
        "A": _serie(
            "A",
            "Mensual",
            [
                {"periodo": "2025-01", "valor": 1.0},
                {"periodo": "2025-02", "valor": 2.0},
                {"periodo": "2025-03", "valor": 3.0},
            ],
        ),
        "B": _serie(
            "B",
            "Mensual",
            [
                {"periodo": "2025-02", "valor": 20.0},
                {"periodo": "2025-03", "valor": 30.0},
                {"periodo": "2025-04", "valor": 40.0},
            ],
        ),
    }
    monkeypatch.setattr(server, "serie", lambda codigo, desde, hasta: resultados[codigo])

    resultado = server.comparar_series("A", "B", "2025-01", "2025-04")

    assert resultado["periodos_coincidentes"] == 2
    assert resultado["datos"] == [
        {"periodo": "2025-02", "valor_a": 2.0, "valor_b": 20.0},
        {"periodo": "2025-03", "valor_a": 3.0, "valor_b": 30.0},
    ]
    assert resultado["correlacion"] == pytest.approx(1.0)
    assert len(resultado["fuentes"]) == 2
    assert "no demuestra causalidad" in resultado["nota"]


def test_comparar_series_rechaza_frecuencias_distintas(monkeypatch):
    resultados = {
        "A": _serie("A", "Mensual", [{"periodo": "2025-01", "valor": 1.0}]),
        "B": _serie("B", "Diaria", [{"periodo": "2025-01-01", "valor": 2.0}]),
    }
    monkeypatch.setattr(server, "serie", lambda codigo, desde, hasta: resultados[codigo])

    with pytest.raises(ToolError, match="misma frecuencia"):
        server.comparar_series("A", "B", "2025-01", "2025-02")
