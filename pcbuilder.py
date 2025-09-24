import pandas as pd
from mcp.server import FastMCP
import os

mcp = FastMCP("pc_builder")

# Cargar datasets
cpus = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/cpu.csv")
gpus = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/video-card.csv")
motherboards = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/motherboard.csv")
rams = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/memory.csv")
cases = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/case.csv")
hardDrives = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/internal-hard-drive.csv")
keyboards = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/keyboard.csv")
mice = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/mouse.csv")
psus = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/power-supply.csv")
monitors = pd.read_csv("/home/dandelion/Documentos/Redes/Proyectos/PChecker/DB/csv/monitor.csv")

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
    
    # Crear una columna temporal con capacidad total en GB
    def total_capacity(modules_str):
        try:
            num_modules, size_per_module = map(int, modules_str.split(","))
            return num_modules * size_per_module
        except:
            return 0  # si hay algún error, ignorar
     
    rams["total_capacity"] = rams["modules"].apply(total_capacity)
    
    # Filtrar por precio y capacidad
    results = rams[(rams["price"] <= max_price) & (rams["total_capacity"] >= min_capacity)]
    
    return results.to_dict(orient="records")[:10]


@mcp.tool()
async def search_case(max_price: float = 9999, form_factor: str = None):
    """Search cases by price and form factor"""
    df = cases[cases["price"] <= max_price]
    if form_factor:
        df = df[df["type"].str.contains(form_factor, na=False)]
    return df.to_dict(orient="records")[:10]

@mcp.tool()
async def search_psu(max_price: float = 9999, min_wattage: int = 400) -> list[dict]:
    """Search power supplies by price and wattage"""
    results = psus[
        (psus["price"] <= max_price) &
        (psus["wattage"] >= min_wattage)
    ]
    return results.to_dict(orient="records")[:10]

@mcp.tool()
async def search_storage(max_price: float = 9999, min_capacity: int = 256) -> list[dict]:
    """Search hard drives/SSDs by price and capacity (GB)"""
    results = hardDrives[
        (hardDrives["price"] <= max_price) &
        (hardDrives["capacity"] >= min_capacity)
    ]
    return results.to_dict(orient="records")[:10]

@mcp.tool()
async def search_keyboard(max_price: float = 9999, tks: bool = False) -> list[dict]:
    """Search keyboards by price and if is TKS (ten key less) or not"""
    df = keyboards[keyboards["price"] <= max_price]
    if tks:
        df = df[df["tenkeyless"] == True]
    return df.to_dict(orient="records")[:10]

@mcp.tool()
async def search_mouse(max_price: float = 9999, connection_type: str = None) -> list[dict]:
    """Search mice by price and connection type"""
    df = mice[mice["price"] <= max_price]
    if connection_type:
        df = df[df["connection_type"].str.contains(connection_type, na=False)]
    return df.to_dict(orient="records")[:10]

@mcp.tool()
async def search_monitor(max_price: float = 9999, min_size: float = 15, resolution: str = None) -> list[dict]:
    """Search monitor by price, size and resolution"""
    results = monitors[
        (monitors["price"] <= max_price) &
        (monitors["screen_size"] >= min_size)
    ]
    if resolution:
        results = results[results["resolution"].str.contains(resolution, na=False)]
    return results.to_dict(orient="records")[:10]

@mcp.tool()
async def list_dir(path: str = ".") -> list[str]:
    """List all files in a directory"""
    try:
        return os.listdir(path)
    except Exception as e:
        return [f"Error: {e}"]

@mcp.tool()
async def read_file(path: str) -> str:
    """Read the content of a file"""
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
async def write_file(path: str, content: str) -> str:
    """Write content to a file"""
    try:
        with open(path, "w") as f:
            f.write(content)
        return "File written successfully"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
