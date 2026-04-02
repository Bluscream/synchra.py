import pytest
import json
from uuid import uuid4
from synchra.ws import SynchraWSClient

@pytest.mark.asyncio
async def test_ws_event_handler(auth):
    client = SynchraWSClient(auth)
    received_data = []

    @client.on("activity")
    async def handle_activity(event):
        received_data.append(event)

    # Simulate receiving a message
    mock_payload = {
        "type": "activity",
        "action": "new",
        "data": {"id": str(uuid4())}
    }
    await client._handle_message(json.dumps(mock_payload))
    
    assert len(received_data) == 1
    assert received_data[0]["type"] == "activity"

@pytest.mark.asyncio
async def test_ws_subscribe_payload(auth):
    client = SynchraWSClient(auth)
    channel_id = uuid4()
    
    await client.subscribe("chat_message", channel_id, nonce="test-nonce")
    
    assert len(client._subscriptions) == 1
    sub = client._subscriptions[0]
    assert sub["command"] == "subscribe"
    assert sub["type"] == "chat_message"
    assert sub["data"]["channel_id"] == str(channel_id)
    assert sub["nonce"] == "test-nonce"

@pytest.mark.asyncio
async def test_ws_unsubscribe_payload(auth):
    client = SynchraWSClient(auth)
    channel_id = uuid4()
    
    await client.subscribe("chat_message", channel_id)
    await client.unsubscribe("chat_message", channel_id)
    
    assert len(client._subscriptions) == 0
