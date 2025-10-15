from mcp.server.fastmcp import FastMCP
import logging, math, random

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("mcp")
mcp = FastMCP("Calculator")

@mcp.tool()
def calculator(python_expression: str) -> dict:
    """Use for math expressions. You may use functions from math and random."""
    try:
        safe_globals = {"__builtins__": {}, "math": math, "random": random}
        result = eval(python_expression, safe_globals, {})
        return {"success": True, "result": result}
    except Exception as e:
        log.exception("calculator failed")
        return {"success": False, "error": str(e)}

@mcp.tool()
def echo(text: str) -> dict:
    """Diagnostic tool that returns exactly what you send (use to verify wiring)."""
    return {"ok": True, "echo": text[:900]}

if __name__ == "__main__":
    mcp.run(transport="stdio")
