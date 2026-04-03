from typing import List, Optional, Any
from uuid import UUID

from .base import APIGroup
from ..models.resources import (
    Channel, 
    ChannelProvider, 
    Activity,
    PageCursorChannel,
    PageCursorActivity,
    ChannelUserAccessLevel,
    ChannelUserAccessLevelWithUser,
    ChannelUserInvite,
    AccessLevel
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
        return await self._get_list("/channels", Channel, params=params)

    async def create(self, display_name: str, show_on_landing_page: bool = True) -> Channel:
        """Create a new channel."""
        data = {
            "display_name": display_name,
            "show_on_landing_page": show_on_landing_page
        }
        return await self._http.post("/channels", json=data, response_model=Channel)

    async def get(self, channel_id: UUID) -> Channel:
        """Get details for a specific channel."""
        return await self._http.get(f"/channels/{channel_id}", response_model=Channel)

    async def delete(self, channel_id: UUID) -> None:
        """Delete a channel."""
        await self._http.delete(f"/channels/{channel_id}")

    async def list_providers(self, channel_id: UUID) -> List[ChannelProvider]:
        """
        List all platform providers (Twitch, YouTube, Kick, etc.) currently linked to this channel.
        
        Args:
            channel_id: The UUID of the Synchra channel.
        """
        return await self._get_list(f"/channels/{channel_id}/providers", ChannelProvider)

    async def list_activities(self, channel_id: UUID, limit: int = 100, offset: int = 0) -> List[Activity]:
        """
        List past activities/events (subs, tips, follows) associated with this channel.
        
        Args:
            channel_id: The UUID of the Synchra channel.
            limit: Maximum activities to return.
            offset: Number of items to skip.
        """
        params = {"limit": limit, "offset": offset}
        return await self._get_list(f"/channels/{channel_id}/activities", Activity, params=params)

    async def list_user_access(self, channel_id: UUID, cursor: Optional[str] = None) -> List[ChannelUserAccessLevelWithUser]:
        """
        List all users who currently have permissions for this channel.
        
        Args:
            channel_id: The UUID of the Synchra channel.
            cursor: Optional pagination cursor for large lists.
        """
        params = {"cursor": cursor} if cursor else {}
        return await self._get_list(f"/channels/{channel_id}/users-access", ChannelUserAccessLevelWithUser, params=params)

    async def update_user_access(self, channel_id: UUID, access_id: UUID, access_level: AccessLevel) -> ChannelUserAccessLevel:
        """
        Update the permission level of a specific user on a channel.
        
        Args:
            channel_id: The UUID of the Synchra channel.
            access_id: The UUID of the access record to modify.
            access_level: The new AccessLevel (MOD, EDITOR, ADMIN, etc.).
        """
        data = {"access_level": access_level}
        return await self._http.put(f"/channels/{channel_id}/users-access/{access_id}", json=data, response_model=ChannelUserAccessLevel)

    async def list_invites(self, channel_id: UUID, cursor: Optional[str] = None) -> List[ChannelUserInvite]:
        """
        Retrieve all active, pending user invite links for this channel.
        
        Args:
            channel_id: The UUID of the Synchra channel.
            cursor: Optional pagination cursor for large lists.
        """
        params = {"cursor": cursor} if cursor else {}
        return await self._get_list(f"/channels/{channel_id}/user-invites", ChannelUserInvite, params=params)

    async def create_invite(self, channel_id: UUID, access_level: AccessLevel = AccessLevel.USER) -> ChannelUserInvite:
        """
        Generate a new invite link with specific permissions.
        
        Args:
            channel_id: The UUID of the Synchra channel.
            access_level: The default AccessLevel for whoever joins via this link.
        """
        data = {"access_level": access_level}
        return await self._http.post(f"/channels/{channel_id}/user-invites", json=data, response_model=ChannelUserInvite)

    async def delete_invite(self, channel_id: UUID, invite_id: UUID) -> None:
        """
        Revoke an existing invite link, preventing further use.
        
        Args:
            channel_id: The UUID of the Synchra channel.
            invite_id: The UUID of the invite link to revoke.
        """
        await self._http.delete(f"/channels/{channel_id}/user-invites/{invite_id}")
