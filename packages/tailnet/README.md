# Tailnet - Composable Tailscale Authentication

A reusable package for adding Tailscale-based authentication and access control to any server.

## Features

- 🔒 **Composable Design**: Works with FastAPI, TCP servers, and any Python application
- 🌐 **Auto-Detection**: Automatically detects Tailscale network configuration
- 🚦 **Access Control**: Configurable IP allowlists and Tailscale-only mode
- 🔧 **Easy Integration**: Drop-in middleware and decorators

## Installation

```bash
# For FastAPI integration
pip install -e "packages/tailnet[fastapi]"

# For development
pip install -e "packages/tailnet[dev]"
```

## Usage

### FastAPI

```python
from fastapi import FastAPI
from tailnet import TailnetConfig, TailnetMiddleware

config = TailnetConfig(
    enabled=True,
    enforce_tailscale=True,
    allowed_ips=["100.64.0.0/10"]  # Tailscale IPs
)

app = FastAPI()
app.add_middleware(TailnetMiddleware, config=config)
```

### TCP Server

```python
from tailnet import TailnetConfig, validate_connection

config = TailnetConfig(enabled=True, enforce_tailscale=True)

async def handle_client(reader, writer):
    client_addr = writer.get_extra_info('peername')[0]
    
    if not validate_connection(client_addr, config):
        writer.close()
        await writer.wait_closed()
        return
    
    # Handle authenticated client
    ...
```

### Generic Use

```python
from tailnet import TailnetConfig, is_tailscale_ip

config = TailnetConfig.from_env()

if config.enabled and not is_tailscale_ip(client_ip, config):
    raise PermissionError("Access denied")
```

## Configuration

Set via environment variables:

```bash
TAILSCALE_ENABLED=true
TAILSCALE_ENFORCE=true
TAILSCALE_ALLOWED_IPS=100.64.0.0/10,fd7a:115c:a1e0::/48
TAILSCALE_NETWORK=100.64.0.0/10
```

Or programmatically:

```python
config = TailnetConfig(
    enabled=True,
    enforce_tailscale=True,
    allowed_ips=["100.64.0.0/10"],
    tailscale_network="100.64.0.0/10"
)
```
