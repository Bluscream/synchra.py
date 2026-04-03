from typing import List, Optional, Any
from uuid import UUID

from ..base import APIGroup

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

    async def unban_user(self, channel_id: UUID, provider_id: UUID, provider_viewer_id: str):
        """Unban a user from a Kick channel."""
        await self._http.delete(
            f"/channels/{channel_id}/kick/{provider_id}/ban",
            params={"provider_viewer_id": provider_viewer_id}
        )
