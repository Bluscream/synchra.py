# swagger_client.YouTubeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ban_user_api2_channels_channel_id_youtube_channel_provider_id_ban_post**](YouTubeApi.md#ban_user_api2_channels_channel_id_youtube_channel_provider_id_ban_post) | **POST** /api/2/channels/{channel_id}/youtube/{channel_provider_id}/ban | Ban User
[**ban_user_api2_channels_channel_id_youtube_channel_provider_id_moderators_delete**](YouTubeApi.md#ban_user_api2_channels_channel_id_youtube_channel_provider_id_moderators_delete) | **DELETE** /api/2/channels/{channel_id}/youtube/{channel_provider_id}/moderators | Ban User
[**ban_user_api2_channels_channel_id_youtube_channel_provider_id_moderators_post**](YouTubeApi.md#ban_user_api2_channels_channel_id_youtube_channel_provider_id_moderators_post) | **POST** /api/2/channels/{channel_id}/youtube/{channel_provider_id}/moderators | Ban User
[**get_moderators_api2_channels_channel_id_youtube_channel_provider_id_moderators_get**](YouTubeApi.md#get_moderators_api2_channels_channel_id_youtube_channel_provider_id_moderators_get) | **GET** /api/2/channels/{channel_id}/youtube/{channel_provider_id}/moderators | Get Moderators
[**unban_user_api2_channels_channel_id_youtube_channel_provider_id_ban_delete**](YouTubeApi.md#unban_user_api2_channels_channel_id_youtube_channel_provider_id_ban_delete) | **DELETE** /api/2/channels/{channel_id}/youtube/{channel_provider_id}/ban | Unban User
[**youtube_create_broadcast_route_api2_channels_channel_id_providers_channel_provider_id_youtube_broadcast_post**](YouTubeApi.md#youtube_create_broadcast_route_api2_channels_channel_id_providers_channel_provider_id_youtube_broadcast_post) | **POST** /api/2/channels/{channel_id}/providers/{channel_provider_id}/youtube/broadcast | Youtube Create Broadcast Route


# **ban_user_api2_channels_channel_id_youtube_channel_provider_id_ban_post**
> ban_user_api2_channels_channel_id_youtube_channel_provider_id_ban_post(channel_id, channel_provider_id)

Ban User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Ban User
    api_instance.ban_user_api2_channels_channel_id_youtube_channel_provider_id_ban_post(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling YouTubeApi->ban_user_api2_channels_channel_id_youtube_channel_provider_id_ban_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_provider_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ban_user_api2_channels_channel_id_youtube_channel_provider_id_moderators_delete**
> ban_user_api2_channels_channel_id_youtube_channel_provider_id_moderators_delete(channel_id, channel_provider_id)

Ban User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Ban User
    api_instance.ban_user_api2_channels_channel_id_youtube_channel_provider_id_moderators_delete(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling YouTubeApi->ban_user_api2_channels_channel_id_youtube_channel_provider_id_moderators_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_provider_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ban_user_api2_channels_channel_id_youtube_channel_provider_id_moderators_post**
> ban_user_api2_channels_channel_id_youtube_channel_provider_id_moderators_post(channel_id, channel_provider_id)

Ban User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Ban User
    api_instance.ban_user_api2_channels_channel_id_youtube_channel_provider_id_moderators_post(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling YouTubeApi->ban_user_api2_channels_channel_id_youtube_channel_provider_id_moderators_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_provider_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_moderators_api2_channels_channel_id_youtube_channel_provider_id_moderators_get**
> get_moderators_api2_channels_channel_id_youtube_channel_provider_id_moderators_get(channel_id, channel_provider_id)

Get Moderators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Get Moderators
    api_instance.get_moderators_api2_channels_channel_id_youtube_channel_provider_id_moderators_get(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling YouTubeApi->get_moderators_api2_channels_channel_id_youtube_channel_provider_id_moderators_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_provider_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unban_user_api2_channels_channel_id_youtube_channel_provider_id_ban_delete**
> unban_user_api2_channels_channel_id_youtube_channel_provider_id_ban_delete(channel_id, channel_provider_id, provider_viewer_id)

Unban User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 
provider_viewer_id = NULL # object | 

try:
    # Unban User
    api_instance.unban_user_api2_channels_channel_id_youtube_channel_provider_id_ban_delete(channel_id, channel_provider_id, provider_viewer_id)
except ApiException as e:
    print("Exception when calling YouTubeApi->unban_user_api2_channels_channel_id_youtube_channel_provider_id_ban_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_provider_id** | [**object**](.md)|  | 
 **provider_viewer_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **youtube_create_broadcast_route_api2_channels_channel_id_providers_channel_provider_id_youtube_broadcast_post**
> youtube_create_broadcast_route_api2_channels_channel_id_providers_channel_provider_id_youtube_broadcast_post(channel_id, channel_provider_id)

Youtube Create Broadcast Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Youtube Create Broadcast Route
    api_instance.youtube_create_broadcast_route_api2_channels_channel_id_providers_channel_provider_id_youtube_broadcast_post(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling YouTubeApi->youtube_create_broadcast_route_api2_channels_channel_id_providers_channel_provider_id_youtube_broadcast_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_provider_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

