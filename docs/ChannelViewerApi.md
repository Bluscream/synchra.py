# swagger_client.ChannelViewerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**viewer_info_api2_channels_channel_id_viewers_provider_provider_viewer_id_get**](ChannelViewerApi.md#viewer_info_api2_channels_channel_id_viewers_provider_provider_viewer_id_get) | **GET** /api/2/channels/{channel_id}/viewers/{provider}/{provider_viewer_id} | Viewer Info
[**viewer_search_api2_viewer_search_get**](ChannelViewerApi.md#viewer_search_api2_viewer_search_get) | **GET** /api/2/viewer-search | Viewer Search
[**viewer_watched_streams_api2_channels_channel_id_viewers_provider_provider_viewer_id_streams_get**](ChannelViewerApi.md#viewer_watched_streams_api2_channels_channel_id_viewers_provider_provider_viewer_id_streams_get) | **GET** /api/2/channels/{channel_id}/viewers/{provider}/{provider_viewer_id}/streams | Viewer Watched Streams


# **viewer_info_api2_channels_channel_id_viewers_provider_provider_viewer_id_get**
> viewer_info_api2_channels_channel_id_viewers_provider_provider_viewer_id_get(channel_id, provider, provider_viewer_id)

Viewer Info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelViewerApi()
channel_id = NULL # object | 
provider = NULL # object | 
provider_viewer_id = NULL # object | 

try:
    # Viewer Info
    api_instance.viewer_info_api2_channels_channel_id_viewers_provider_provider_viewer_id_get(channel_id, provider, provider_viewer_id)
except ApiException as e:
    print("Exception when calling ChannelViewerApi->viewer_info_api2_channels_channel_id_viewers_provider_provider_viewer_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **provider** | [**object**](.md)|  | 
 **provider_viewer_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **viewer_search_api2_viewer_search_get**
> viewer_search_api2_viewer_search_get(query, exact=exact, provider=provider)

Viewer Search

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelViewerApi()
query = NULL # object | 
exact = NULL # object |  (optional)
provider = NULL # object |  (optional)

try:
    # Viewer Search
    api_instance.viewer_search_api2_viewer_search_get(query, exact=exact, provider=provider)
except ApiException as e:
    print("Exception when calling ChannelViewerApi->viewer_search_api2_viewer_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**object**](.md)|  | 
 **exact** | [**object**](.md)|  | [optional] 
 **provider** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **viewer_watched_streams_api2_channels_channel_id_viewers_provider_provider_viewer_id_streams_get**
> viewer_watched_streams_api2_channels_channel_id_viewers_provider_provider_viewer_id_streams_get(channel_id, provider, provider_viewer_id, cursor=cursor, per_page=per_page)

Viewer Watched Streams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelViewerApi()
channel_id = NULL # object | 
provider = NULL # object | 
provider_viewer_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Viewer Watched Streams
    api_instance.viewer_watched_streams_api2_channels_channel_id_viewers_provider_provider_viewer_id_streams_get(channel_id, provider, provider_viewer_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelViewerApi->viewer_watched_streams_api2_channels_channel_id_viewers_provider_provider_viewer_id_streams_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **provider** | [**object**](.md)|  | 
 **provider_viewer_id** | [**object**](.md)|  | 
 **cursor** | [**object**](.md)|  | [optional] 
 **per_page** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

