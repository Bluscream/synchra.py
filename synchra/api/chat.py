import asyncio
from typing import Optional, List, Any, Dict
from uuid import UUID
from .base import APIGroup
from ..models.resources import ChannelProvider

class ChatAPI(APIGroup):
    """API for sending chat messages to platforms via Synchra."""

    async def send_message(self, channel_provider_id: str, message: str, user_provider_id: str) -> None:
        """
        Send a chat message to a specific provider channel.
        
        Args:
            channel_provider_id: The ID of the provider channel to send to.
            message: The text content of the message.
            user_provider_id: The ID of the user provider (sender) to use.
        """
        data = {
            "channel_provider_id": str(channel_provider_id),
            "user_provider_id": str(user_provider_id),
            "message": message
        }
        await self._http.post("/api/2/chat/messages", json=data)

    async def send_message_all(
        self, 
        channel_id: UUID, 
        message: str, 
        user_provider_id: str,
        providers: Optional[List[ChannelProvider]] = None
    ) -> Dict[str, Any]:
        """
        Broadcast a message to all sendable providers linked to a channel.
        
        Args:
            channel_id: The Synchra channel UUID.
            message: The message to broadcast.
            user_provider_id: The sender's user provider ID.
            providers: Optional pre-fetched list of channel providers.
            
        Returns:
            Dict containing success and failure counts/exceptions.
        """
        if providers is None:
            providers = await self._get_list(f"/api/2/channels/{channel_id}/providers", ChannelProvider)
            
        # Broadcast to all platforms except those that don't support chat sending (e.g. TikTok)
        platform_send_blacklist = {'tiktok'}
        targets = [
            p for p in providers 
            if getattr(p.provider, 'value', str(p.provider)).lower() not in platform_send_blacklist
        ]
        
        if not targets:
            return {"success": 0, "failed": 0, "errors": []}
            
        tasks = [self.send_message(p.id, message, user_provider_id) for p in targets]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        success_count = 0
        errors = []
        for i, res in enumerate(results):
            if isinstance(res, Exception):
                errors.append({"platform": targets[i].provider, "error": str(res)})
            else:
                success_count += 1
                
        return {
            "success": success_count,
            "failed": len(targets) - success_count,
            "errors": errors
        }
