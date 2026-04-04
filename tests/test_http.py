import pytest
from aioresponses import aioresponses
from synchra.http import HTTPClient, SynchraAuth, SynchraError

@pytest.mark.asyncio
async def test_auth_headers(auth):
    headers = await auth.get_auth_header()
    assert headers["Authorization"] == "Bearer test-token"

@pytest.mark.asyncio
async def test_http_get_success(http_client, mock_aioresponse):
    mock_aioresponse.get("https://api.synchra.net/api/2/test", status=200, payload={"key": "value"})
    
    response = await http_client.get("/test")
    assert response == {"key": "value"}

@pytest.mark.asyncio
async def test_http_error_handling(http_client, mock_aioresponse):
    mock_aioresponse.get("https://api.synchra.net/api/2/test", status=400, payload={"type": "bad_request", "message": "invalid parameters", "code": 400, "errors": []})
    
    with pytest.raises(SynchraError) as excinfo:
        await http_client.get("/test")
    
    assert "bad_request" in str(excinfo.value)
    assert excinfo.value.status == 400

@pytest.mark.asyncio
async def test_http_204_no_content(http_client, mock_aioresponse):
    mock_aioresponse.delete("https://api.synchra.net/api/2/test", status=204)
    
    response = await http_client.delete("/test")
    assert response is None
