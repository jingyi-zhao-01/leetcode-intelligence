# ADR 002: Tailnet Composable Authentication Layer

**Date**: 2026-02-27  
**Status**: Accepted  
**Context**: VPS deployment security and authentication

## Context

Multiple services need to be exposed via VPS (submission server on TCP:3000, analytics API on FastAPI:8000, MCP server). These services contain sensitive data and operations that should only be accessible to authorized users.

Requirements:
- Secure access control for VPS-hosted services
- Support for both FastAPI (HTTP) and TCP servers
- Easy to enable/disable for dev vs. production
- Minimal coupling to business logic
- Reusable across different server types

## Decision

Create a dedicated **`tailnet` package** that provides composable Tailscale authentication as a reusable library.

### Design Principles

1. **Composition over inheritance**: Wrap handlers, don't extend them
2. **Configuration-driven**: Environment variables control behavior
3. **Server-agnostic**: Works with FastAPI, TCP, or any Python server
4. **Zero business logic**: Pure authentication concern
5. **Graceful degradation**: Can be fully disabled for development

## Architecture

```
packages/tailnet/
├── src/tailnet/
│   ├── config.py       # TailnetConfig with auto-detection
│   ├── utils.py        # IP validation utilities
│   ├── fastapi.py      # FastAPI middleware
│   ├── tcp.py          # TCP wrapper utilities
│   └── __init__.py     # Public API
└── examples/           # Integration examples
```

### Public API

```python
# Configuration
from tailnet import TailnetConfig

# Validation utilities
from tailnet import is_tailscale_ip, validate_connection

# FastAPI integration
from tailnet import TailnetMiddleware

# TCP integration
from tailnet import wrap_tcp_handler
```

## Key Design Decisions

### 1. Separate Package (Not Module)

**Why separate package:**
- ✅ Reusable across multiple server packages
- ✅ Independent versioning (v0.1.0)
- ✅ Clear dependency boundary (minimal deps)
- ✅ Could be open-sourced
- ✅ Forces clean API design

**Why not module in submission_server:**
- ❌ Couldn't be reused by mcp-server
- ❌ Coupled to submission_server dependencies
- ❌ Harder to test independently
- ❌ Violates single responsibility

### 2. Composition Pattern

**Chosen approach: Wrap handlers**
```python
# FastAPI: Middleware
app.add_middleware(TailnetMiddleware, config=config)

# TCP: Wrapper function
authenticated_handler = wrap_tcp_handler(handler, config)
```

**Rejected: Inheritance**
```python
# Bad: Forces servers to inherit
class SecureServer(BaseAuthServer):
    pass  # Couples auth to server implementation
```

**Rationale:**
- Composition is more flexible
- No changes to existing server classes
- Easy to remove/disable
- Works with any handler signature
- Follows decorator pattern

### 3. Configuration-Driven

**Environment-based configuration:**
```bash
TAILSCALE_ENABLED=true
TAILSCALE_ENFORCE=true
TAILSCALE_ALLOWED_IPS=100.64.0.0/10
```

**Why environment variables:**
- ✅ 12-factor app methodology
- ✅ Same code, different behavior per environment
- ✅ No code changes between dev/prod
- ✅ Secret-free (no credentials)
- ✅ Works with Docker, systemd

**Rejected: Code-based toggling**
```python
# Bad: Requires code changes
if ENV == "production":
    app.add_middleware(TailnetMiddleware)
```

### 4. Auto-Detection

**Tailscale network auto-discovery:**
```python
def _detect_tailscale_network(self) -> Optional[str]:
    result = subprocess.run(["tailscale", "ip", "-4"], ...)
    # Returns "100.64.0.0/10" automatically
```

**Why:**
- ✅ Works out-of-box on VPS with Tailscale
- ✅ No manual IP configuration needed
- ✅ Detects Tailscale presence
- ✅ Falls back gracefully if not available

### 5. Multiple Integration Patterns

**Provided patterns:**
1. Middleware (FastAPI)
2. Wrapper function (TCP)
3. Manual validation (custom servers)

**Why multiple patterns:**
- Different servers have different needs
- FastAPI: middleware is idiomatic
- TCP: handler wrapping is cleanest
- Custom: utilities for flexibility

**Consistency:**
All patterns use same core:
- `TailnetConfig` - unified configuration
- `validate_connection()` - shared validation logic
- Same logging format
- Same security model

## Implementation Details

### Validation Logic

```python
def validate_connection(client_ip: str, config: TailnetConfig) -> bool:
    if not config.enabled:
        return True  # Auth disabled
    
    if config.allow_localhost and is_localhost(client_ip):
        return True  # Localhost allowed
    
    if config.enforce_tailscale:
        return is_tailscale_ip(client_ip, config)  # Strict
    
    return True  # Warn-only mode
```

**Decision rationale:**
- Explicit disable switch (dev environments)
- Localhost exception (health checks)
- Strict enforcement option (production)
- Warn-only mode (migration)

### Logging Strategy

```
🔒 Tailnet authentication enabled
   Enforcement: STRICT
   Allowed networks: 100.64.0.0/10
🌐 ✅ ALLOWED 100.64.12.34 [Tailscale]
🌐 ❌ DENIED 203.0.113.45 [Non-Tailscale]
```

**Why emoji + structured format:**
- ✅ Easy to grep logs
- ✅ Visual distinction
- ✅ Clear security events
- ✅ Includes decision rationale

## Consequences

### Positive

✅ **Reusability**: Used by submission_server, analytics_server  
✅ **Simplicity**: 5 functions/classes, ~300 LOC  
✅ **Composability**: Drop-in, no server changes  
✅ **Testability**: Pure functions, easy to test  
✅ **Flexibility**: Works with any Python server  
✅ **Security**: Clear audit trail, strict validation  
✅ **DevEx**: One config change switches dev/prod mode

### Negative

⚠️ **Another package**: One more thing to install  
⚠️ **Path management**: Needs to be in PYTHONPATH  
⚠️ **Tailscale dependency**: Assumes Tailscale CLI available  
⚠️ **Subprocess calls**: Auto-detection uses subprocess

### Mitigations

- Document installation clearly
- Provide examples for each server type
- Auto-detection has graceful fallback
- Can configure IPs manually if needed

## Integration Examples

### FastAPI Server

```python
from tailnet import TailnetConfig, TailnetMiddleware

app = FastAPI()
config = TailnetConfig.from_env()

if config.enabled:
    app.add_middleware(TailnetMiddleware, config=config)
```

**Result**: 3 lines, no changes to routes/handlers

### TCP Server

```python
from tailnet import TailnetConfig, wrap_tcp_handler

config = TailnetConfig.from_env()
authenticated_handler = wrap_tcp_handler(
    self.handle_client,
    config
)

server = await asyncio.start_server(
    authenticated_handler,
    self.host,
    self.port
)
```

**Result**: 1 wrapper call, handler unchanged

### Custom Server

```python
from tailnet import TailnetConfig, validate_connection

config = TailnetConfig.from_env()

if config.enabled and not validate_connection(client_ip, config):
    raise PermissionError("Access denied")
```

**Result**: Direct control, manual validation

## Alternatives Considered

### Alternative 1: Per-Server Implementation

**Approach**: Each server implements its own auth

**Rejected because:**
- ❌ Code duplication
- ❌ Inconsistent security
- ❌ More maintenance burden
- ❌ Different logging formats
- ❌ Bugs fixed in one place only

### Alternative 2: Shared Module (Not Package)

**Approach**: `submission_server/src/auth.py`

**Rejected because:**
- ❌ Can't be imported by mcp-server
- ❌ Couples auth to submission_server
- ❌ Harder to test independently
- ❌ Not reusable outside project

### Alternative 3: API Gateway

**Approach**: Nginx/Traefik with auth plugin

**Rejected because:**
- ❌ Adds external dependency
- ❌ More complex deployment
- ❌ Doesn't work for TCP server
- ❌ Less visibility into decisions
- ❌ Harder to customize per environment

### Alternative 4: Built-in Tailscale Auth

**Approach**: Use Tailscale's built-in authentication

**Rejected because:**
- ❌ Requires Tailscale on both sides
- ❌ No customization (localhost, warn-only)
- ❌ Less control over logging
- ❌ Can't test without Tailscale

**Our approach gives:**
- ✅ Tailscale integration when available
- ✅ Flexible configuration
- ✅ Works without Tailscale (dev)
- ✅ Custom validation logic

## Success Metrics

- ✅ Used by 2+ server packages (submission_server, analytics_server)
- ✅ Zero coupling to business logic
- ✅ <500 LOC total
- ✅ 100% test coverage on validation logic
- ✅ Clear documentation with examples
- ✅ One-line integration per server

## Future Enhancements

Potential additions (not currently needed):

1. **Rate limiting** - Per-IP connection limits
2. **Metrics export** - Prometheus metrics
3. **Session tracking** - Active connection monitoring
4. **IP allowlist management** - Dynamic list updates
5. **mTLS support** - Certificate-based auth option

## References

- [tailnet README](/packages/tailnet/README.md)
- [DEPLOYMENT.md](/packages/tailnet/DEPLOYMENT.md) - Full deployment guide
- [INTEGRATION_SUMMARY.md](/packages/tailnet/INTEGRATION_SUMMARY.md)
- Tailscale: https://tailscale.com/
- Composition over inheritance: Gang of Four Design Patterns

## Related ADRs

- [ADR 001: Multi-Package Monorepo Structure](001-multi-package-monorepo-structure.md) - This validates that approach

## Notes

This package emerged from the need to secure VPS-exposed services. The composable design proved the value of the multi-package monorepo approach (ADR 001) by demonstrating how a reusable library can serve multiple server types without coupling.

The success of this pattern suggests future shared concerns (logging, metrics, tracing) could follow the same model.
