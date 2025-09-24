# PChecker

Proyecto que busca asesorar al usuario a construir una PC desde cualquier punto teniendo en cuenta parámetros como precio, presupuesto, capacidad, compatibilidad, etc.

## Scripts de instalación

### Linux

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

cd mcp_client

# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate

# Install required packages
uv add mcp anthropic python-dotenv
```

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

cd mcp_client

# Create virtual environment
uv venv

# Activate virtual environment
.venv\Scripts\activate

# Install required packages
uv add mcp anthropic python-dotenv
```

## Ejecución

```bash
# Weather MCP Server
uv run client.py ../weather.py

# PChecker
uv run client.py ../pcbuilder.py
```

A partir de este punto, el programa solicitará querys a través de la terminal que serán utilizados por el modelo Claude 4 para analizar el conjunto de datos obtenido de [pc-part-dataset](https://github.com/docyx/pc-part-dataset.git) y que contiene cerca de 67,000 registros con información sobre múltiples componentes de computadora.
