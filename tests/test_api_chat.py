import pytest
from uuid import uuid4, UUID
from unittest.mock import AsyncMock, patch
from synchra.api.chat import ChatAPI
from synchra.models import ChannelProvider, Provider


def _make_provider(provider_name: str, **overrides) -> ChannelProvider:
    """Helper to create a mock ChannelProvider with sensible defaults."""
    defaults = {
        "id": uuid4(),
        "channel_id": uuid4(),
        "provider": Provider(provider_name),
        "provider_channel_id": "ch-123",
        "provider_channel_name": "test_channel",
        "provider_channel_display_name": "Test ChannelRecord",
        "scope": "chat:write",
        "stream_title": None,
        "stream_category": None,
        "stream_tags": [],
        "live_stream_id": None,
        "stream_live": False,
        "channel_provider_stream_id": None,
        "state": None,
        "bot_provider": None,
        "scope_needed": False,
    }
    defaults.update(overrides)
    return ChannelProvider.model_validate(defaults)


@pytest.mark.asyncio
async def test_send_message(http_client, mock_aioresponse):
    """Test sending a single chat message to a provider."""
    mock_aioresponse.post(
        "https://api.synchra.net/api/2/chat/messages",
        status=200,
        payload={"ok": True},
    )

    api = ChatAPI(http_client)
    await api.send_message(
        channel_provider_id="provider-123",
        message="Hello world",
        user_provider_id="user-456",
    )

    # Verify the request was made (no exception = success)


@pytest.mark.asyncio
async def test_send_message_all_broadcasts_to_non_tiktok(http_client, mock_aioresponse):
    """Test that send_message_all skips TikTok and sends to other platforms."""
    # Mock the chat message endpoint for each call
    mock_aioresponse.post(
        "https://api.synchra.net/api/2/chat/messages",
        status=200,
        payload={"ok": True},
        repeat=True,
    )

    twitch_provider = _make_provider("twitch")
    youtube_provider = _make_provider("youtube")
    tiktok_provider = _make_provider("tiktok")

    api = ChatAPI(http_client)
    result = await api.send_message_all(
        channel_id=uuid4(),
        message="Hello everyone!",
        user_provider_id="user-456",
        providers=[twitch_provider, youtube_provider, tiktok_provider],
    )

    assert result.success == 2
    assert result.failed == 0
    assert result.errors == []


@pytest.mark.asyncio
async def test_send_message_all_tiktok_only_channel(http_client, mock_aioresponse):
    """Test that a TikTok-only channel returns zero successes."""
    api = ChatAPI(http_client)
    result = await api.send_message_all(
        channel_id=uuid4(),
        message="Hello!",
        user_provider_id="user-456",
        providers=[_make_provider("tiktok")],
    )

    assert result.success == 0
    assert result.failed == 0
    assert result.errors == []


@pytest.mark.asyncio
async def test_send_message_all_partial_failure(http_client, mock_aioresponse):
    """Test that partial failures are reported correctly."""
    # First call succeeds, second fails
    mock_aioresponse.post(
        "https://api.synchra.net/api/2/chat/messages",
        status=200,
        payload={"ok": True},
    )
    mock_aioresponse.post(
        "https://api.synchra.net/api/2/chat/messages",
        status=500,
        payload={"type": "internal_error", "message": "Server error", "code": 500, "errors": []},
    )

    twitch_provider = _make_provider("twitch")
    kick_provider = _make_provider("kick")

    api = ChatAPI(http_client)
    result = await api.send_message_all(
        channel_id=uuid4(),
        message="Test",
        user_provider_id="user-456",
        providers=[twitch_provider, kick_provider],
    )

    assert result.success == 1
    assert result.failed == 1
    assert len(result.errors) == 1
    assert isinstance(result.errors[0].platform, str)
