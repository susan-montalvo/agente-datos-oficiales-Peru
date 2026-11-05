import pytest
from fastmcp.exceptions import ToolError

import server


def test_comparar_series_alinea_periodos_y_calcula_correlacion(monkeypatch):
    series = {
        "A": {
            "frecuencia": "Mensual",
            "datos": [
                {"periodo": "2025-01", "valor": 1.0},
                {"periodo": "2025-02", "valor": 2.0},
                {"periodo": "2025-03", "valor": 3.0},
                {"periodo": "2025-04", "valor": 4.0},
            ],
            "fuente": "https://bcrp.example/A",
        },
        "B": {
            "frecuencia": "Mensual",
            "datos": [
                {"periodo": "2025-02", "valor": 20.0},
                {"periodo": "2025-03", "valor": 30.0},
                {"periodo": "2025-04", "valor": 25.0},
                {"periodo": "2025-05", "valor": 40.0},
            ],
            "fuente": "https://bcrp.example/B",
        },
    }
    monkeypatch.setattr(server, "serie", lambda codigo, desde, hasta: series[codigo])

    resultado = server.comparar_series("A", "B", "2025-01", "2025-05")

    assert [dato["periodo"] for dato in resultado["datos"]] == [
        "2025-02",
        "2025-03",
        "2025-04",
    ]
    assert resultado["correlacion"] == pytest.approx(0.5)


def test_comparar_series_rechaza_frecuencias_distintas(monkeypatch):
    series = {
        "A": {
            "frecuencia": "Mensual",
            "datos": [{"periodo": "2025-01", "valor": 1.0}],
            "fuente": "https://bcrp.example/A",
        },
        "B": {
            "frecuencia": "Diaria",
            "datos": [{"periodo": "2025-01-01", "valor": 2.0}],
            "fuente": "https://bcrp.example/B",
        },
    }
    monkeypatch.setattr(server, "serie", lambda codigo, desde, hasta: series[codigo])

    with pytest.raises(ToolError, match="misma frecuencia"):
        server.comparar_series("A", "B", "2025-01", "2025-02")