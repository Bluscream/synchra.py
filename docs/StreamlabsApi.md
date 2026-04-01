# swagger_client.StreamlabsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_channel_streamlabs_connect_url_route_api2_channels_channel_id_streamlabs_connect_url_get**](StreamlabsApi.md#get_channel_streamlabs_connect_url_route_api2_channels_channel_id_streamlabs_connect_url_get) | **GET** /api/2/channels/{channel_id}/streamlabs/connect-url | Get Channel Streamlabs Connect Url Route
[**streamlabs_auth_route_api2_streamlabs_auth_get**](StreamlabsApi.md#streamlabs_auth_route_api2_streamlabs_auth_get) | **GET** /api/2/streamlabs/auth | Streamlabs Auth Route


# **get_channel_streamlabs_connect_url_route_api2_channels_channel_id_streamlabs_connect_url_get**
> get_channel_streamlabs_connect_url_route_api2_channels_channel_id_streamlabs_connect_url_get(channel_id, redirect_to=redirect_to)

Get Channel Streamlabs Connect Url Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamlabsApi()
channel_id = NULL # object | 
redirect_to = NULL # object |  (optional)

try:
    # Get Channel Streamlabs Connect Url Route
    api_instance.get_channel_streamlabs_connect_url_route_api2_channels_channel_id_streamlabs_connect_url_get(channel_id, redirect_to=redirect_to)
except ApiException as e:
    print("Exception when calling StreamlabsApi->get_channel_streamlabs_connect_url_route_api2_channels_channel_id_streamlabs_connect_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **redirect_to** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **streamlabs_auth_route_api2_streamlabs_auth_get**
> streamlabs_auth_route_api2_streamlabs_auth_get(code, state, scope=scope)

Streamlabs Auth Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamlabsApi()
code = NULL # object | 
state = NULL # object | 
scope = NULL # object |  (optional)

try:
    # Streamlabs Auth Route
    api_instance.streamlabs_auth_route_api2_streamlabs_auth_get(code, state, scope=scope)
except ApiException as e:
    print("Exception when calling StreamlabsApi->streamlabs_auth_route_api2_streamlabs_auth_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | [**object**](.md)|  | 
 **state** | [**object**](.md)|  | 
 **scope** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

