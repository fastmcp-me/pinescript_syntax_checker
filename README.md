# PineScript Syntax Checker MCP Server

A Model Context Protocol (MCP) server for checking PineScript syntax using TradingView's API.

## Features

- Check PineScript syntax using TradingView's official API
- MCP-compatible server with httpx for async HTTP requests
- Detailed error reporting with line and column information

## Quick Start

### Option 1: Using uvx (Recommended)

```bash
# Run directly (will install automatically if needed)
uvx pinescript-syntax-checker
```

### Option 2: Using uv (Development)

```bash
# Clone and run
git clone https://github.com/erevus-cn/pinescript-syntax-checker.git
cd pinescript-syntax-checker
uv sync
uv run python -m pinescript_syntax_checker.server
```

### Option 3: Using pip

```bash
# Install from PyPI
pip install pinescript-syntax-checker

# Run directly
pinescript-syntax-checker

# Or as module
python -m pinescript_syntax_checker.server
```

## MCP Integration

### Configure in Cursor

To use this MCP server in Cursor:

1. **Open Cursor Settings**:
   - Press `Cmd+,` (macOS) or `Ctrl+,` (Windows/Linux)
   - Go to "Extensions" → "MCP"

2. **Add Server Configuration**:

   **Method 1 - Using uvx (Recommended):**
   ```json
   {
     "mcpServers": {
       "pinescript-syntax-checker": {
         "command": "uvx",
         "args": ["pinescript-syntax-checker"]
       }
     }
   }
   ```

   **Method 2 - Using installed package:**
   ```json
   {
     "mcpServers": {
       "pinescript-syntax-checker": {
         "command": "python",
         "args": ["-m", "pinescript_syntax_checker.server"]
       }
     }
   }
   ```

3. **Restart Cursor** to load the MCP server

### Verify Installation

To verify the MCP server is working correctly:

1. **In Cursor:** After configuration, try asking:
   ```
   Can you check this PineScript code for syntax errors?
   
   //@version=5
   indicator("Test", overlay=true)
   plot(close)
   ```

## API

### check_syntax

Checks PineScript syntax using TradingView's API.

**Parameters:**
- `pine_code` (str): The PineScript code to check

## Example

**Input:**
```pinescript
//@version=5
strategy("Test")
plot(close)
```

**Output:**
```json
{
  "success": true,
  "result": {
    "variables": [],
    "functions": [],
    "types": [],
    "enums": [],
    "scopes": []
  }
}
```

## License

MIT License
