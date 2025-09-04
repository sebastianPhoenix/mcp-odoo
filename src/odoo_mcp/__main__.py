"""
Command line entry point for the Odoo MCP Server
"""
import sys
import asyncio
import traceback
import os

from .server import mcp


def main() -> int:
    """
    Run the MCP server
    """
    try:
        print("=== ODOO MCP SERVER STARTING ===", file=sys.stderr)
        print(f"Python version: {sys.version}", file=sys.stderr)
        print("Environment variables:", file=sys.stderr)
        for key, value in os.environ.items():
            if key.startswith("ODOO_"):
                if key == "ODOO_PASSWORD":
                    print(f"  {key}: ***hidden***", file=sys.stderr)
                else:
                    print(f"  {key}: {value}", file=sys.stderr)
        
        # Check if server instance has the run_stdio method
        methods = [method for method in dir(mcp) if not method.startswith('_')]
        print(f"Available methods on mcp object: {methods}", file=sys.stderr)
        
        print("Starting MCP server with run() method...", file=sys.stderr)
        sys.stderr.flush()  # Ensure log information is written immediately
        
        # Use the run() method directly
        mcp.run()
        
        # If execution reaches here, the server exited normally
        print("MCP server stopped normally", file=sys.stderr)
        return 0
    except KeyboardInterrupt:
        print("MCP server stopped by user", file=sys.stderr)
        return 0
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)
        print("Exception details:", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        print("\nServer object information:", file=sys.stderr)
        print(f"MCP object type: {type(mcp)}", file=sys.stderr)
        print(f"MCP object dir: {dir(mcp)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
