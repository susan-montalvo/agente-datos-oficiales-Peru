"""Consulta el servidor MCP bcrp (mcp/server.py) por stdio con un cliente FastMCP."""
import asyncio, json, sys
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

REPO = sys.argv[1]
SALIDA = sys.argv[2]

LLAMADAS = [
    ("serie",   {"codigo": "PN01728AM", "desde": "2024-01", "hasta": "2024-12"}),  # P01, P09
    ("serie",   {"codigo": "PN01273PM", "desde": "2024-12", "hasta": "2024-12"}),  # P02
    ("resumen", {"codigo": "PN01210PM", "desde": "2024-01", "hasta": "2024-12"}),  # P03, P10
    ("serie",   {"codigo": "PD04722MM", "desde": "2024-01", "hasta": "2024-12"}),  # P04
    ("resumen", {"codigo": "PN01728AM", "desde": "2024-01", "hasta": "2024-12"}),  # P09
]

async def main():
    transporte = StdioTransport(command="uv", args=["run", "--project", REPO, "python", f"{REPO}/mcp/server.py"], cwd=REPO)
    resultados = []
    async with Client(transporte) as cliente:
        herramientas = [h.name for h in await cliente.list_tools()]
        for nombre, args in LLAMADAS:
            r = await cliente.call_tool(nombre, args)
            datos = r.structured_content if r.structured_content is not None else json.loads(r.content[0].text)
            resultados.append({"herramienta": nombre, "argumentos": args, "respuesta": datos})
    json.dump({"herramientas_disponibles": herramientas, "llamadas": resultados}, open(SALIDA, "w"), ensure_ascii=False, indent=2)
    print(json.dumps({"herramientas_disponibles": herramientas, "llamadas": resultados}, ensure_ascii=False, indent=1))

asyncio.run(main())
