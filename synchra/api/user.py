from typing import List
from .base import APIGroup
from ..models import User, UserProviderPublic

class UserAPI(APIGroup):
    """API for managing the authenticated Synchra user account."""

    async def get_info(self) -> User:
        """Fetch basic profile info for the current user (ID, username, email)."""
        data = await self._http.get("/user")
        return User.model_validate(data)

    async def list_providers(self) -> List[UserProviderPublic]:
        """Fetch all linked platform providers for the current user."""
        data = await self._http.get("/user/providers")
        return [UserProviderPublic.model_validate(p) for p in data]
