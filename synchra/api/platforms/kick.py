from typing import List, Optional, Any
from uuid import UUID

from ..base import APIGroup
from ...models.platforms.kick import KickBanRequest

class KickAPI(APIGroup):
    """API for Kick-specific features in Synchra."""

    async def ban_user(self, channel_id: UUID, provider_id: UUID, data: KickBanRequest):
        """Ban a user from a Kick channel."""
        await self._http.post(
            f"/channels/{channel_id}/kick/{provider_id}/ban",
            json=data.model_dump(exclude_none=True)
        )

    async def unban_user(self, channel_id: UUID, provider_id: UUID, provider_viewer_id: str):
        """Unban a user from a Kick channel."""
        await self._http.delete(
            f"/channels/{channel_id}/kick/{provider_id}/ban",
            params={"provider_viewer_id": provider_viewer_id}
        )
