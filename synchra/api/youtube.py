from typing import List, Optional, Any
from uuid import UUID

from .base import APIGroup
# Note: Specific YouTube/Kick models might be deep in resources.py
# Using Any or dict for complex nested structures if model names are not obvious

class YouTubeAPI(APIGroup):
    """API for YouTube-specific features in Synchra."""

    async def create_broadcast(self, channel_id: UUID, provider_id: UUID, snippet: dict, status: dict, content_details: Optional[dict] = None) -> Any:
        """Create a YouTube broadcast."""
        data = {
            "snippet": snippet,
            "status": status,
        }
        if content_details:
            data["contentDetails"] = content_details
            
        return await self._http.post(
            f"/channels/{channel_id}/providers/{provider_id}/youtube/broadcast",
            json=data
        )

    async def ban_user(self, channel_id: UUID, provider_id: UUID, provider_viewer_id: str, duration: Optional[int] = None):
        """Ban a user from a YouTube channel."""
        data = {"provider_viewer_id": provider_viewer_id}
        if duration:
            data["duration_seconds"] = duration
        await self._http.post(
            f"/channels/{channel_id}/youtube/{provider_id}/ban",
            json=data
        )

class KickAPI(APIGroup):
    """API for Kick-specific features in Synchra."""

    async def ban_user(self, channel_id: UUID, provider_id: UUID, provider_viewer_id: str, duration: Optional[int] = None, reason: Optional[str] = None):
        """Ban a user from a Kick channel."""
        data = {
            "provider_viewer_id": provider_viewer_id,
            "duration_seconds": duration,
            "reason": reason
        }
        await self._http.post(
            f"/channels/{channel_id}/kick/{provider_id}/ban",
            json=data
        )
