from mcp.server import FastMCP
import git

mcp = FastMCP("git_tools")

@mcp.tool()
async def clone_repo(repo_url: str, path: str) -> str:
    """Clone a git repository"""
    try:
        git.Repo.clone_from(repo_url, path)
        return f"Repository cloned to {path}"
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
async def list_branches(repo_path: str) -> list[str]:
    """List all branches in a repo"""
    try:
        repo = git.Repo(repo_path)
        return [b.name for b in repo.branches]
    except Exception as e:
        return [f"Error: {e}"]

@mcp.tool()
async def git_commit(repo_path: str, message: str) -> str:
    """Commit changes in a repo"""
    try:
        repo = git.Repo(repo_path)
        repo.git.add(A=True)
        repo.index.commit(message)
        return "Changes committed successfully"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
