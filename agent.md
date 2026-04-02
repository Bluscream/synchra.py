# Synchra SDK - Agent Context

This document provides a technical overview of the Synchra Python SDK for future AI agents and developers.

## Project Architecture

The SDK is built with an async-first approach using `aiohttp` and `pydantic` v2.

### Core Components
- **`SynchraClient`**: The main entry point. Orchestrates API groups and the WebSocket client.
- **`HTTPClient`**: Low-level wrapper around `aiohttp.ClientSession`. Handles:
    - Automatic JSON serialization/deserialization.
    - Model validation using `pydantic.TypeAdapter`.
    - Error mapping to `SynchraError`.
- **`SynchraAuth`**: Manages OAuth2 tokens and direct access token injection.
- **`SynchraWSClient`**: WebSocket client for real-time events.
    - Uses a subscription-based model.
    - Dispatcher uses `@on("event_type")` decorators.
    - Includes exponential backoff reconnection logic.

### API Groups
API endpoints are grouped logically in `synchra/api/`:
- `ChannelsAPI`: Core channel and provider management.
- `TwitchAPI`, `YouTubeAPI`, `KickAPI`: Provider-specific moderation and emulation tools.

## Data Models
All models are generated from the OpenAPI spec and located in `synchra/models/resources.py`.
- **Validation**: Incoming API responses are strictly validated.
- **Types**: Use `UUID` for IDs and `datetime` for timestamps where applicable.

## Testing
- Framework: `pytest` + `pytest-asyncio`.
- Mocking: `aioresponses`.
- Location: `tests/`.

## Style Guidelines
1. **Async Only**: All network-related methods must be `async`.
2. **Type Hints**: Mandatory for all public methods.
3. **Pydantic v2**: Use `model_validate` or `TypeAdapter` for data mapping.
4. **Logging**: Use the `synchra` parent logger.
