import pandas as pd
from mcp.server import FastMCP

mcp = FastMCP("pc_builder")

# Cargar datasets
cpus = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/cpu.csv")
gpus = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/video-card.csv")
motherboards = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/motherboard.csv")
rams = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/memory.csv")

@mcp.tool()
async def search_cpu(max_price: float = 9999, min_cores: int = 1) -> list[dict]:
    """Search CPUs filtered by price and cores."""
    results = cpus[
        (cpus["price"] <= max_price) & 
        (cpus["core_count"] >= min_cores)
    ]
    return results.to_dict(orient="records")[:10]  # devolver hasta 10

@mcp.tool()
async def search_gpu(max_price: float = 9999, min_memory: int = 4) -> list[dict]:
    """Search GPUs filtered by price and VRAM."""
    results = gpus[
        (gpus["price"] <= max_price) & 
        (gpus["memory"] >= min_memory)
    ]
    return results.to_dict(orient="records")[:10]

@mcp.tool()
async def search_motherboard(socket: str = None, max_price: float = 9999) -> list[dict]:
    """Search motherboards by socket and price."""
    df = motherboards[motherboards["price"] <= max_price]
    if socket:
        df = df[df["socket"].str.contains(socket, na=False)]
    return df.to_dict(orient="records")[:10]

@mcp.tool()
async def search_ram(max_price: float = 9999, min_capacity: int = 8) -> list[dict]:
    """Search RAM kits filtered by price and capacity."""
    results = rams[
        (rams["price"] <= max_price) & 
        (rams["capacity"] >= min_capacity)
    ]
    return results.to_dict(orient="records")[:10]

if __name__ == "__main__":
    mcp.run(transport="stdio")
