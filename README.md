# PChecker

Project aimed at assisting users in building a PC from any starting point, taking into account parameters such as price, budget, capacity, compatibility, and more.

## Installation Scripts

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

Windows
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

## Execution
```bash
# Weather MCP Server
uv run client.py ../weather.py

# PChecker
uv run client.py ../pcbuilder.py
```

From this point on, the program will request queries through the terminal, which will be processed by the Claude 4 model to analyze the dataset obtained from pc-part-dataset
.
This dataset contains around 67,000 records with information about multiple computer components.
