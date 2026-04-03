from typing import List, Optional, Any
from uuid import UUID

from .base import APIGroup
from ..models.platforms.twitch import (
    TwitchEmulateChatMessageRequest,
    TwitchBanRequest,
    TwitchRaidRequest,
    TwitchShoutoutRequest,
    TwitchAddVIPRequest
)

class TwitchAPI(APIGroup):
    """API for Twitch-specific features in Synchra."""

    async def emulate_chat_message(self, data: TwitchEmulateChatMessageRequest, channel_id: UUID) -> None:
        """Emulate a Twitch channel chat message for testing."""
        await self._http.post(
            "/twitch/eventsub/emulate-channel-chat-message",
            json=data.model_dump(exclude_none=True),
            params={"channel_id": str(channel_id)}
        )

    async def ban_user(self, channel_id: UUID, channel_provider_id: UUID, data: TwitchBanRequest):
        """Ban a user from a Twitch channel."""
        await self._http.post(
            f"/channels/{channel_id}/twitch/{channel_provider_id}/ban",
            json=data.model_dump(exclude_none=True)
        )

    async def unban_user(self, channel_id: UUID, channel_provider_id: UUID, provider_viewer_id: str):
        """Unban a user from a Twitch channel."""
        await self._http.delete(
            f"/channels/{channel_id}/twitch/{channel_provider_id}/ban",
            params={"provider_viewer_id": provider_viewer_id}
        )

    async def raid(self, channel_id: UUID, channel_provider_id: UUID, data: TwitchRaidRequest):
        """Start a raid on another Twitch channel."""
        await self._http.post(
            f"/channels/{channel_id}/twitch/{channel_provider_id}/raid",
            json=data.model_dump(exclude_none=True)
        )

    async def shoutout(self, channel_id: UUID, channel_provider_id: UUID, data: TwitchShoutoutRequest):
        """Send a shoutout to another Twitch channel."""
        await self._http.post(
            f"/channels/{channel_id}/twitch/{channel_provider_id}/shoutout",
            json=data.model_dump(exclude_none=True)
        )

    async def add_vip(self, channel_id: UUID, channel_provider_id: UUID, data: TwitchAddVIPRequest):
        """Add a VIP user to a Twitch channel."""
        await self._http.post(
            f"/channels/{channel_id}/twitch/{channel_provider_id}/vips",
            json=data.model_dump(exclude_none=True)
        )

    async def remove_vip(self, channel_id: UUID, channel_provider_id: UUID, provider_viewer_id: str):
        """Remove a VIP user from a Twitch channel."""
        await self._http.delete(
            f"/channels/{channel_id}/twitch/{channel_provider_id}/vips",
            params={"provider_viewer_id": provider_viewer_id}
        )
