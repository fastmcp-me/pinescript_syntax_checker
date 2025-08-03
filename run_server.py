#!/usr/bin/env python3
"""
Standalone script to run the PineScript Syntax Checker MCP Server
This script automatically detects the environment and runs the server appropriately.
"""

import sys
import os
import importlib.util

def find_package():
    """Find the pinescript_syntax_checker package."""
    # First, try to import as installed package
    try:
        import pinescript_syntax_checker
        return pinescript_syntax_checker
    except ImportError:
        pass
    
    # If not installed, try to find in current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    package_dir = os.path.join(current_dir, "pinescript_syntax_checker")
    
    if os.path.exists(package_dir):
        # Add current directory to path for development
        sys.path.insert(0, current_dir)
        try:
            import pinescript_syntax_checker
            return pinescript_syntax_checker
        except ImportError:
            pass
    
    raise ImportError("Could not find pinescript_syntax_checker package")

def main():
    """Main entry point."""
    try:
        # Find and import the package
        package = find_package()
        from pinescript_syntax_checker.server import main as server_main
        
        # Run the server
        server_main()
    except ImportError as e:
        print(f"Error: {e}")
        print("Please ensure the package is installed or in the current directory.")
        sys.exit(1)
    except Exception as e:
        print(f"Error running server: {e}")
        sys.exit(1)

# Make app available globally for MCP
try:
    package = find_package()
    from pinescript_syntax_checker.server import app
except ImportError:
    # If package not found, create a dummy app for MCP detection
    from mcp.server.fastmcp import FastMCP
    app = FastMCP('pinescript-syntax-checker')

if __name__ == "__main__":
    main() 