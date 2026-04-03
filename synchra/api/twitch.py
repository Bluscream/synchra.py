from typing import List, Optional, Any
from uuid import UUID

from .base import APIGroup
from ..models.resources import (
    BodyEmulateChannelChatMessageApi2TwitchEventsubEmulateChannelChatMessagePost as EmulateChatData,
    BodyBanUserApi2ChannelsChannelIdTwitchChannelProviderIdBanPost as BanUserBody
)

class TwitchAPI(APIGroup):
    """API for Twitch-specific features in Synchra."""

    async def emulate_chat_message(self, data: EmulateChatData, channel_id: UUID) -> None:
        """Emulate a Twitch channel chat message for testing."""
        await self._http.post(
            "/twitch/eventsub/emulate-channel-chat-message",
            json=data.model_dump(exclude_none=True),
            params={"channel_id": str(channel_id)}
        )

    async def ban_user(self, channel_id: UUID, channel_provider_id: UUID, provider_viewer_id: str, duration: Optional[int] = None, reason: Optional[str] = None):
        """Ban a user from a Twitch channel."""
        data = BanUserBody(
            provider_viewer_id=provider_viewer_id,
            duration_seconds=duration,
            reason=reason
        )
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

    async def raid(self, channel_id: UUID, channel_provider_id: UUID, to_provider_channel_id: str):
        """Start a raid on another Twitch channel."""
        await self._http.post(
            f"/channels/{channel_id}/twitch/{channel_provider_id}/raid",
            json={"to_provider_channel_id": to_provider_channel_id}
        )

    async def shoutout(self, channel_id: UUID, channel_provider_id: UUID, to_provider_channel_id: str):
        """Send a shoutout to another Twitch channel."""
        await self._http.post(
            f"/channels/{channel_id}/twitch/{channel_provider_id}/shoutout",
            json={"to_provider_channel_id": to_provider_channel_id}
        )
