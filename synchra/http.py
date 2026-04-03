import asyncio
import logging
from typing import Any, Dict, Optional, Type, TypeVar, Union
from uuid import UUID

import aiohttp
from pydantic import BaseModel, ValidationError, TypeAdapter

from .models.resources import Error as SynchraErrorModel

logger = logging.getLogger("synchra.http")

T = TypeVar("T", bound=BaseModel)

class SynchraError(Exception):
    """Base exception for Synchra SDK."""
    def __init__(self, message: str, status: int = 0, data: Any = None):
        super().__init__(message)
        self.message = message
        self.status = status
        self.data = data

class SynchraAuth:
    """Handles authentication for Synchra API."""
    def __init__(
        self, 
        access_token: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        refresh_token: Optional[str] = None,
        token_url: str = "https://api.synchra.net/api/2/auth/token" # Placeholder
    ):
        self.access_token = access_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.token_url = token_url
        self._lock = asyncio.Lock()

    async def get_auth_header(self) -> Dict[str, str]:
        """Returns the Authorization header, refreshing if necessary."""
        if not self.access_token and self.refresh_token:
            async with self._lock:
                await self.refresh()
        
        if self.access_token:
            return {"Authorization": f"Bearer {self.access_token}"}
        return {}

    async def refresh(self):
        """Refreshes the access token using the refresh token."""
        if not self.refresh_token or not self.client_id or not self.client_secret:
            raise SynchraError("Missing credentials for token refresh (ID, Secret, or Refresh Token)")
        
        async with aiohttp.ClientSession() as session:
            payload = {
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
            try:
                async with session.post(self.token_url, data=payload) as resp:
                    if resp.status != 200:
                        text = await resp.text()
                        raise SynchraError(f"OAuth Refresh failed ({resp.status}): {text}", status=resp.status)
                    
                    data = await resp.json()
                    self.access_token = data.get("access_token")
                    self.refresh_token = data.get("refresh_token") or self.refresh_token
            except Exception as e:
                logger.error(f"Error during token refresh: {e}")
                raise

class HTTPClient:
    """Low-level HTTP client for Synchra API."""
    def __init__(self, auth: SynchraAuth, base_url: str = "https://api.synchra.net"):
        self.auth = auth
        self.base_url = base_url.rstrip("/")
        self._session: Optional[aiohttp.ClientSession] = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()

    async def request(
        self,
        method: str,
        path: str,
        *,
        response_model: Optional[Type[T]] = None,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Any] = None,
        **kwargs
    ) -> Union[T, Any, None]:
        session = await self._get_session()
        url = f"{self.base_url}/{path.lstrip('/')}"
        headers = await self.auth.get_auth_header()
        
        if "headers" in kwargs:
            headers.update(kwargs.pop("headers"))

        async with session.request(method, url, params=params, json=json, headers=headers, **kwargs) as resp:
            if resp.status == 204:
                return None
            
            data = await resp.json()
            
            if resp.status >= 400:
                try:
                    error_data = SynchraErrorModel.model_validate(data)
                    raise SynchraError(f"{error_data.type}: {error_data.message}", status=resp.status, data=error_data)
                except Exception:
                    raise SynchraError(f"HTTP {resp.status}: {data}", status=resp.status, data=data)

            if response_model:
                try:
                    return TypeAdapter(response_model).validate_python(data)
                except ValidationError as e:
                    logger.error(f"Validation error for {url}: {e}")
                    raise SynchraError(f"Failed to validate response: {e}", status=resp.status, data=data)
            
            return data

    async def get(self, path: str, **kwargs) -> Any:
        return await self.request("GET", path, **kwargs)

    async def post(self, path: str, **kwargs) -> Any:
        return await self.request("POST", path, **kwargs)

    async def put(self, path: str, **kwargs) -> Any:
        return await self.request("PUT", path, **kwargs)

    async def patch(self, path: str, **kwargs) -> Any:
        return await self.request("PATCH", path, **kwargs)

    async def delete(self, path: str, **kwargs) -> Any:
        return await self.request("DELETE", path, **kwargs)
