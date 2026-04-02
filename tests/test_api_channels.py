import pytest
from uuid import uuid4
from synchra.api.channels import ChannelsAPI
from synchra.models.resources import Channel

@pytest.mark.asyncio
async def test_list_channels(http_client, mock_aioresponse):
    channel_id = str(uuid4())
    mock_data = {
        "records": [{
            "id": channel_id,
            "display_name": "Test Channel",
            "created_at": "2026-04-02T10:50:00Z",
            "subscription": None,
            "features": ["channel_viewer_extra_stats"]
        }],
        "cursor": None,
        "total": 1
    }
    
    # Correct endpoint mapping
    mock_aioresponse.get("https://api.synchra.net/api/2/channels", status=200, payload=mock_data)
    
    api = ChannelsAPI(http_client)
    channels = await api.list()
    
    assert len(channels) == 1
    # Note: Records might be a generated class like Record7 which matches Channel's structure
    assert channels[0].display_name == "Test Channel"

@pytest.mark.asyncio
async def test_create_channel(http_client, mock_aioresponse):
    channel_id = str(uuid4())
    mock_data = {
        "id": channel_id,
        "display_name": "New Channel",
        "created_at": "2026-04-02T10:55:00Z",
        "subscription": None,
        "features": []
    }
    
    mock_aioresponse.post("https://api.synchra.net/api/2/channels", status=201, payload=mock_data)
    
    api = ChannelsAPI(http_client)
    channel = await api.create(display_name="New Channel")
    
    assert channel.id == UUID(channel_id)
    assert channel.display_name == "New Channel"

from uuid import UUID
