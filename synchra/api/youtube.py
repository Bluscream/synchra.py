from typing import List, Optional
from uuid import UUID
from .base import APIGroup
from ..models.platforms.youtube import LiveBroadcastInsert, YouTubeBanRequest
from ..models.platforms.kick import KickBanRequest

class YouTubeAPI(APIGroup):
    """API for YouTube-specific features in Synchra."""

    async def create_broadcast(self, channel_id: UUID, provider_id: UUID, data: LiveBroadcastInsert) -> None:
        """Schedule a new YouTube live broadcast."""
        await self._http.post(
            f"/channels/{channel_id}/providers/{provider_id}/youtube/broadcast",
            json=data.model_dump(by_alias=True, exclude_none=True)
        )

    async def ban_user(self, channel_id: UUID, provider_id: UUID, data: YouTubeBanRequest):
        """Ban a user from a YouTube channel."""
        await self._http.post(
            f"/channels/{channel_id}/youtube/{provider_id}/ban",
            json=data.model_dump(exclude_none=True)
        )

class KickAPI(APIGroup):
    """API for Kick-specific features in Synchra."""

    async def ban_user(self, channel_id: UUID, provider_id: UUID, data: KickBanRequest):
        """Ban a user from a Kick channel."""
        await self._http.post(
            f"/channels/{channel_id}/kick/{provider_id}/ban",
            json=data.model_dump(exclude_none=True)
        )
