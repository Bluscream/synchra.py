from ..http import HTTPClient

class APIGroup:
    """Base class for all Synchra API groups."""
    def __init__(self, http: HTTPClient):
        self._http = http
