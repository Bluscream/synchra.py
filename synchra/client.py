import logging
from typing import Optional
from uuid import UUID

from .http import SynchraAuth, HTTPClient
from .ws import SynchraWSClient
from .api.channels import ChannelsAPI
from .api.twitch import TwitchAPI
from .api.youtube import YouTubeAPI
from .api.kick import KickAPI

logger = logging.getLogger("synchra")

class SynchraClient:
    """The main client for the Synchra API."""
    def __init__(
        self,
        access_token: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        refresh_token: Optional[str] = None,
        base_url: str = "https://api.synchra.net",
        ws_url: str = "wss://api.synchra.net/api/2/ws"
    ):
        self.auth = SynchraAuth(
            access_token=access_token,
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token
        )
        self.http = HTTPClient(self.auth, base_url=base_url)
        self.ws = SynchraWSClient(self.auth, base_url=ws_url)
        
        # API Groups
        self.channels = ChannelsAPI(self.http)
        self.twitch = TwitchAPI(self.http)
        self.youtube = YouTubeAPI(self.http)
        self.kick = KickAPI(self.http)

    async def connect(self):
        """Connect the WebSocket client."""
        await self.ws.connect()

    async def close(self):
        """Close both HTTP and WebSocket connections."""
        await self.http.close()
        await self.ws.close()
