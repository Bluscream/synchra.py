from typing import List, Dict, Any
from .base import APIGroup

class UserAPI(APIGroup):
    """API for managing the authenticated Synchra user account."""

    async def get_info(self) -> Dict[str, Any]:
        """Fetch basic profile info for the current user (ID, username, email)."""
        return await self._http.get("/api/2/user")

    async def list_providers(self) -> List[Dict[str, Any]]:
        """Fetch all linked platform providers for the current user."""
        return await self._http.get("/api/2/user/providers")
