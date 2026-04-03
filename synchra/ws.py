import asyncio
import inspect
import json
import logging
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar
from uuid import UUID

import aiohttp
from pydantic import BaseModel

from .http import SynchraAuth
from .models.resources import ActivityRecord

logger = logging.getLogger("synchra.ws")

EventHandler = Callable[[Dict[str, Any]], Any]

class SynchraWSClient:
    """Async WebSocket client for Synchra events."""
    
    def __init__(self, auth: SynchraAuth, base_url: str = "wss://api.synchra.net/api/2/ws"):
        self.auth = auth
        self.base_url = base_url
        self._session: Optional[aiohttp.ClientSession] = None
        self._ws: Optional[aiohttp.ClientWebSocketResponse] = None
        self._handlers: Dict[str, List[EventHandler]] = {}
        self._loop_task: Optional[asyncio.Task] = None
        self._subscriptions: List[Dict[str, Any]] = []
        
        # State Management
        self._running = False
        self._closed = False
        self._reconnect_delay = 1
        self._max_reconnect_delay = 300

    @property
    def is_connected(self) -> bool:
        """Whether the WebSocket is currently connected and active."""
        return self._ws is not None and not self._ws.closed

    @property
    def is_closed(self) -> bool:
        """Whether the client has been permanently closed."""
        return self._closed

    def on(self, event_type: str):
        """Decorator to register an event handler."""
        def decorator(func: EventHandler):
            if event_type not in self._handlers:
                self._handlers[event_type] = []
            self._handlers[event_type].append(func)
            return func
        return decorator

    async def connect(self):
        """Connect to the WebSocket and start the listen loop."""
        self._running = True
        self._closed = False
        self._loop_task = asyncio.create_task(self._listen_loop())

    async def _emit(self, event_type: str, *args, **kwargs):
        """Internal helper to emit an event to all registered handlers."""
        if event_type in self._handlers:
            for handler in self._handlers[event_type]:
                try:
                    if inspect.iscoroutinefunction(handler):
                        await handler(*args, **kwargs)
                    else:
                        handler(*args, **kwargs)
                except Exception as e:
                    logger.error(f"Error in {event_type} handler: {e}")

    async def _listen_loop(self):
        while self._running:
            try:
                if self._session is None or self._session.closed:
                    self._session = aiohttp.ClientSession()
                    
                headers = await self.auth.get_auth_header()
                async with self._session.ws_connect(self.base_url, headers=headers) as ws:
                    self._ws = ws
                    logger.info("Connected to Synchra WebSocket")
                    
                    # 1. Send explicit authorization command (v2 requirement)
                    auth_payload = {
                        "command": "authorization",
                        "data": {"token": self.auth.access_token}
                    }
                    await self._ws.send_json(auth_payload)
                    
                    # 2. Emit connect event
                    await self._emit("connect")
                    
                    # 3. Reset delay and resubscribe
                    self._reconnect_delay = 1
                    for sub in self._subscriptions:
                        await self._ws.send_json(sub)

                    async for msg in ws:
                        if msg.type == aiohttp.WSMsgType.TEXT:
                            await self._handle_message(msg.data)
                        elif msg.type in (aiohttp.WSMsgType.CLOSED, aiohttp.WSMsgType.ERROR):
                            break
            except Exception as e:
                logger.error(f"WebSocket error: {e}")
            
            self._ws = None
            if self._running:
                await self._emit("disconnect")
                logger.info(f"Reconnecting in {self._reconnect_delay}s...")
                await asyncio.sleep(self._reconnect_delay)
                # Exponential backoff with jitter
                self._reconnect_delay = min(self._reconnect_delay * 1.5, self._max_reconnect_delay)

    async def _handle_message(self, data: str):
        try:
            payload = json.loads(data)
            event_type = payload.get("type")
            if event_type:
                await self._emit(event_type, payload)
        except Exception as e:
            logger.error(f"Error handling WebSocket message: {e}")

    async def subscribe(self, event_type: str, channel_id: UUID, nonce: Optional[str] = None):
        """Subscribe to a specific event type for a channel."""
        payload = {
            "command": "subscribe",
            "type": event_type,
            "data": {"channel_id": str(channel_id)},
            "nonce": nonce
        }
        self._subscriptions.append(payload)
        if self._ws:
            await self._ws.send_json(payload)

    async def unsubscribe(self, event_type: str, channel_id: UUID):
        """Unsubscribe from a specific event type."""
        payload = {
            "command": "unsubscribe",
            "type": event_type,
            "data": {"channel_id": str(channel_id)}
        }
        # Remove from persistent list
        self._subscriptions = [s for s in self._subscriptions if not (s["type"] == event_type and s["data"]["channel_id"] == str(channel_id))]
        if self._ws:
            await self._ws.send_json(payload)

    async def close(self):
        """Close the WebSocket client."""
        self._running = False
        self._closed = True
        
        if self._loop_task:
            self._loop_task.cancel()
        
        if self._ws:
            await self._ws.close()
        
        if self._session:
            await self._session.close()
            self._session = None
