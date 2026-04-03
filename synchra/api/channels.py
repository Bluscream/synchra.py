from typing import List, Optional, Any
from uuid import UUID

from .base import APIGroup
from ..models.resources import (
    Channel, 
    ChannelProvider, 
    Activity,
    PageCursorChannel,
    PageCursorActivity
)

class ChannelsAPI(APIGroup):
    """API for managing Synchra channels and providers."""

    async def list(
        self, 
        name: Optional[str] = None, 
        channel_id: Optional[UUID] = None, 
        provider: Optional[str] = None, 
        provider_channel_name: Optional[str] = None,
        cursor: Optional[str] = None,
        per_page: int = 25
    ) -> List[Channel]:
        """List and filter channels accessible to the user."""
        params = {
            "name": name,
            "channel_id": channel_id,
            "provider": provider,
            "provider_channel_name": provider_channel_name,
            "cursor": cursor,
            "per_page": per_page
        }
        # Filter out None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self._get_list("/api/2/channels", Channel, params=params)

    async def create(self, display_name: str, show_on_landing_page: bool = True) -> Channel:
        """Create a new channel."""
        data = {
            "display_name": display_name,
            "show_on_landing_page": show_on_landing_page
        }
        return await self._http.post("/api/2/channels", json=data, response_model=Channel)

    async def get(self, channel_id: UUID) -> Channel:
        """Get details for a specific channel."""
        return await self._http.get(f"/api/2/channels/{channel_id}", response_model=Channel)

    async def delete(self, channel_id: UUID) -> None:
        """Delete a channel."""
        await self._http.delete(f"/api/2/channels/{channel_id}")

    async def list_providers(self, channel_id: UUID) -> List[ChannelProvider]:
        """List providers linked to a channel."""
        return await self._get_list(f"/api/2/channels/{channel_id}/providers", ChannelProvider)

    async def list_activities(self, channel_id: UUID, limit: int = 100, offset: int = 0) -> List[Activity]:
        """List activities for a channel."""
        params = {"limit": limit, "offset": offset}
        return await self._get_list(f"/api/2/channels/{channel_id}/activities", Activity, params=params)
