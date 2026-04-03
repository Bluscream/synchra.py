from typing import List, Optional
from uuid import UUID
from .base import APIGroup
from ..models.platforms.youtube import LiveBroadcastInsert, YouTubeBanUserRequest
from ..models.platforms.kick import KickBanUserRequest

class YouTubeAPI(APIGroup):
    """API for YouTube-specific features in Synchra."""

    async def create_broadcast(self, channel_id: UUID, provider_id: UUID, data: LiveBroadcastInsert) -> None:
        """Schedule a new YouTube live broadcast."""
        await self._http.post(
            f"/channels/{channel_id}/providers/{provider_id}/youtube/broadcast",
            json=data.model_dump(by_alias=True, exclude_none=True)
        )

    async def ban_user(self, channel_id: UUID, provider_id: UUID, provider_viewer_id: str, duration: Optional[int] = None):
        """Ban a user from a YouTube channel."""
        data = YouTubeBanUserRequest(
            provider_viewer_id=provider_viewer_id,
            duration_seconds=duration
        )
        await self._http.post(
            f"/channels/{channel_id}/youtube/{provider_id}/ban",
            json=data.model_dump(exclude_none=True)
        )

class KickAPI(APIGroup):
    """API for Kick-specific features in Synchra."""

    async def ban_user(self, channel_id: UUID, provider_id: UUID, provider_viewer_id: str, duration: Optional[int] = None, reason: Optional[str] = None):
        """Ban a user from a Kick channel."""
        data = KickBanUserRequest(
            provider_viewer_id=provider_viewer_id,
            duration_seconds=duration,
            reason=reason
        )
        await self._http.post(
            f"/channels/{channel_id}/kick/{provider_id}/ban",
            json=data.model_dump(exclude_none=True)
        )
