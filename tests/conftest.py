import pytest
import aiohttp
from aioresponses import aioresponses
from synchra import SynchraClient, SynchraAuth
from synchra.http import HTTPClient

@pytest.fixture
def mock_aioresponse():
    with aioresponses() as m:
        yield m

@pytest.fixture
def auth():
    return SynchraAuth(access_token="test-token")

@pytest.fixture
async def http_client(auth):
    client = HTTPClient(auth)
    yield client
    await client.close()

@pytest.fixture
def synchra_client():
    return SynchraClient(access_token="test-token")
