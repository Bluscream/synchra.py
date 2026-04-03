import pytest
from uuid import uuid4
from synchra.api.channels import ChannelsAPI
from synchra.models.resources import ChannelRecord

@pytest.mark.asyncio
async def test_list_channels(http_client, mock_aioresponse):
    channel_id = str(uuid4())
    mock_data = {
        "records": [{
            "id": channel_id,
            "display_name": "Test ChannelRecord",
            "created_at": "2026-04-02T10:50:00Z",
            "subscription": None,
            "features": ["channel_viewer_extra_stats"]
        }],
        "cursor": None,
        "total": 1
    }
    
    # Correct endpoint mapping with default pagination
    mock_aioresponse.get("https://api.synchra.net/api/2/channels?per_page=25", status=200, payload=mock_data)
    
    api = ChannelsAPI(http_client)
    channels = await api.list()
    
    assert len(channels) == 1
    # Note: Records might be a generated class like Record7 which matches ChannelRecord's structure
    assert channels[0].display_name == "Test ChannelRecord"

@pytest.mark.asyncio
async def test_create_channel(http_client, mock_aioresponse):
    channel_id = str(uuid4())
    mock_data = {
        "id": channel_id,
        "display_name": "New ChannelRecord",
        "created_at": "2026-04-02T10:55:00Z",
        "subscription": None,
        "features": []
    }
    
    mock_aioresponse.post("https://api.synchra.net/api/2/channels", status=201, payload=mock_data)
    
    api = ChannelsAPI(http_client)
    channel = await api.create(display_name="New ChannelRecord")
    
    assert channel.id == UUID(channel_id)
    assert channel.display_name == "New ChannelRecord"

from uuid import UUID
