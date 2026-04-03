import logging
from typing import Type, TypeVar, List, Any, Optional
from pydantic import BaseModel
from ..http import HTTPClient

logger = logging.getLogger("synchra.api")

T = TypeVar("T", bound=BaseModel)

class APIGroup:
    """Base class for all Synchra API groups with pagination support."""
    def __init__(self, http: HTTPClient):
        self._http = http

    async def _get_list(
        self, 
        path: str, 
        model: Type[T], 
        params: Optional[dict] = None,
        **kwargs
    ) -> List[T]:
        """
        Helper to handle Synchra's PageCursor pagination format or plain lists.
        Returns the list of records validated against the provided model.
        """
        data = await self._http.get(path, params=params, **kwargs)
        
        # 1. Handle Synchra's PageCursor format { "records": [...], "cursor": "..." }
        if isinstance(data, dict) and "records" in data:
            records = data.get("records", [])
            return [model.model_validate(r) for r in records]
            
        # 2. Handle plain lists [...]
        if isinstance(data, list):
            return [model.model_validate(r) for r in data]
            
        # 3. Handle single objects or unexpected formats
        try:
            return [model.model_validate(data)]
        except Exception as e:
            logger.error(f"Failed to validate response as {model}: {e}")
            return []
