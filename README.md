# Synchra Python SDK (v2.0)

A modern, async-first Python SDK for the [Synchra API](https://api.synchra.net), providing robust access to channel management, real-time events, and multi-platform moderation.

## Features

- **Async Native**: Built from the ground up for `asyncio` using `aiohttp`.
- **Full Type Safety**: Comprehensive [Pydantic v2](https://pydantic.dev) models for all API resources and WebSocket events.
- **WebSocket Client**: Real-time event subscription and dispatcher with automatic reconnection.
- **Provider Support**: Specialized API groups for **Twitch**, **YouTube**, and **Kick**.
- **OAuth2 Ready**: Support for both manual access tokens and full OAuth2 refresh flows.

## Installation

```bash
pip install synchra
```

## Quick Start

### HTTP API Client

```python
import asyncio
from synchra import SynchraClient

async def main():
    # Initialize client (with token or OAuth credentials)
    client = SynchraClient(access_token="YOUR_ACCESS_TOKEN")
    
    # List channels
    channels = await client.channels.list()
    for channel in channels:
        print(f"Channel: {channel.display_name} ({channel.id})")
        
    # Get channel providers
    providers = await client.channels.list_providers(channels[0].id)
    for p in providers:
        print(f"Provider: {p.provider} ({p.provider_channel_name})")

    await client.close()

asyncio.run(main())
```

### WebSocket Real-time Events

```python
import asyncio
from synchra import SynchraClient

async def main():
    client = SynchraClient(access_token="YOUR_ACCESS_TOKEN")
    
    # Register an event handler
    @client.ws.on("activity")
    async def on_activity(event):
        data = event['data']
        print(f"[{event['type']}] New {data['type']} from {data['viewer_display_name']}")

    # Connect and subscribe
    await client.connect()
    await client.ws.subscribe("activity", channel_id="YOUR_CHANNEL_UUID")
    
    # Keep the client running
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await client.close()

asyncio.run(main())
```

## Development & Testing

The SDK includes a full test suite using `pytest`.

```bash
# Install dev dependencies
pip install "synchra[dev]"

# Run tests
python -m pytest tests/
```

## API Groups

- **`client.channels`**: Main channel operations and provider listings.
- **`client.twitch`**: Twitch-specific features (Ban, Unban, Raid, Shoutout, Emulation).
- **`client.youtube`**: YouTube broadcasts and moderation.
- **`client.kick`**: Kick-specific moderation tools.

## Documentation

For full API documentation and endpoint details, refer to the [Synchra OpenAPI Spec](https://api.synchra.net/docs).

## License

MIT
