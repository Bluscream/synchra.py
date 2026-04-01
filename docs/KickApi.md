# swagger_client.KickApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ban_user_api2_channels_channel_id_kick_channel_provider_id_ban_post**](KickApi.md#ban_user_api2_channels_channel_id_kick_channel_provider_id_ban_post) | **POST** /api/2/channels/{channel_id}/kick/{channel_provider_id}/ban | Ban User
[**get_channel_kick_connect_url_route_api2_channels_channel_id_kick_connect_url_get**](KickApi.md#get_channel_kick_connect_url_route_api2_channels_channel_id_kick_connect_url_get) | **GET** /api/2/channels/{channel_id}/kick/connect-url | Get Channel Kick Connect Url Route
[**get_kick_badge_image_api2_channels_channel_id_kick_badge_image_provider_channel_id_size_id_get**](KickApi.md#get_kick_badge_image_api2_channels_channel_id_kick_badge_image_provider_channel_id_size_id_get) | **GET** /api/2/channels/{channel_id}/kick/badge-image/{provider_channel_id}/{size}/{id} | Get Kick Badge Image
[**get_kick_connect_bot_url_route_api2_channels_channel_id_kick_connect_bot_url_get**](KickApi.md#get_kick_connect_bot_url_route_api2_channels_channel_id_kick_connect_bot_url_get) | **GET** /api/2/channels/{channel_id}/kick/connect-bot-url | Get Kick Connect Bot Url Route
[**get_kick_connect_chat_url_route_api2_kick_connect_chat_url_get**](KickApi.md#get_kick_connect_chat_url_route_api2_kick_connect_chat_url_get) | **GET** /api/2/kick/connect-chat-url | Get Kick Connect Chat Url Route
[**get_kick_sign_in_url_route_api2_kick_sign_in_url_get**](KickApi.md#get_kick_sign_in_url_route_api2_kick_sign_in_url_get) | **GET** /api/2/kick/sign-in-url | Get Kick Sign In Url Route
[**get_kick_system_provider_bot_connect_url_route_api2_kick_system_provider_bot_connect_url_get**](KickApi.md#get_kick_system_provider_bot_connect_url_route_api2_kick_system_provider_bot_connect_url_get) | **GET** /api/2/kick/system-provider-bot-connect-url | Get Kick System Provider Bot Connect Url Route
[**kick_auth_route_api2_kick_auth_get**](KickApi.md#kick_auth_route_api2_kick_auth_get) | **GET** /api/2/kick/auth | Kick Auth Route
[**unban_user_api2_channels_channel_id_kick_channel_provider_id_ban_delete**](KickApi.md#unban_user_api2_channels_channel_id_kick_channel_provider_id_ban_delete) | **DELETE** /api/2/channels/{channel_id}/kick/{channel_provider_id}/ban | Unban User


# **ban_user_api2_channels_channel_id_kick_channel_provider_id_ban_post**
> ban_user_api2_channels_channel_id_kick_channel_provider_id_ban_post(channel_id, channel_provider_id)

Ban User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KickApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Ban User
    api_instance.ban_user_api2_channels_channel_id_kick_channel_provider_id_ban_post(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling KickApi->ban_user_api2_channels_channel_id_kick_channel_provider_id_ban_post: %s\n" % e)
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

# **get_channel_kick_connect_url_route_api2_channels_channel_id_kick_connect_url_get**
> get_channel_kick_connect_url_route_api2_channels_channel_id_kick_connect_url_get(channel_id, redirect_to=redirect_to)

Get Channel Kick Connect Url Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KickApi()
channel_id = NULL # object | 
redirect_to = NULL # object |  (optional)

try:
    # Get Channel Kick Connect Url Route
    api_instance.get_channel_kick_connect_url_route_api2_channels_channel_id_kick_connect_url_get(channel_id, redirect_to=redirect_to)
except ApiException as e:
    print("Exception when calling KickApi->get_channel_kick_connect_url_route_api2_channels_channel_id_kick_connect_url_get: %s\n" % e)
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

# **get_kick_badge_image_api2_channels_channel_id_kick_badge_image_provider_channel_id_size_id_get**
> get_kick_badge_image_api2_channels_channel_id_kick_badge_image_provider_channel_id_size_id_get(channel_id, provider_channel_id, id, size)

Get Kick Badge Image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KickApi()
channel_id = NULL # object | 
provider_channel_id = NULL # object | 
id = NULL # object | 
size = NULL # object | 

try:
    # Get Kick Badge Image
    api_instance.get_kick_badge_image_api2_channels_channel_id_kick_badge_image_provider_channel_id_size_id_get(channel_id, provider_channel_id, id, size)
except ApiException as e:
    print("Exception when calling KickApi->get_kick_badge_image_api2_channels_channel_id_kick_badge_image_provider_channel_id_size_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **provider_channel_id** | [**object**](.md)|  | 
 **id** | [**object**](.md)|  | 
 **size** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kick_connect_bot_url_route_api2_channels_channel_id_kick_connect_bot_url_get**
> get_kick_connect_bot_url_route_api2_channels_channel_id_kick_connect_bot_url_get(channel_id, redirect_to=redirect_to)

Get Kick Connect Bot Url Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KickApi()
channel_id = NULL # object | 
redirect_to = NULL # object |  (optional)

try:
    # Get Kick Connect Bot Url Route
    api_instance.get_kick_connect_bot_url_route_api2_channels_channel_id_kick_connect_bot_url_get(channel_id, redirect_to=redirect_to)
except ApiException as e:
    print("Exception when calling KickApi->get_kick_connect_bot_url_route_api2_channels_channel_id_kick_connect_bot_url_get: %s\n" % e)
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

# **get_kick_connect_chat_url_route_api2_kick_connect_chat_url_get**
> get_kick_connect_chat_url_route_api2_kick_connect_chat_url_get(redirect_to=redirect_to)

Get Kick Connect Chat Url Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KickApi()
redirect_to = NULL # object |  (optional)

try:
    # Get Kick Connect Chat Url Route
    api_instance.get_kick_connect_chat_url_route_api2_kick_connect_chat_url_get(redirect_to=redirect_to)
except ApiException as e:
    print("Exception when calling KickApi->get_kick_connect_chat_url_route_api2_kick_connect_chat_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_to** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kick_sign_in_url_route_api2_kick_sign_in_url_get**
> get_kick_sign_in_url_route_api2_kick_sign_in_url_get(redirect_to=redirect_to)

Get Kick Sign In Url Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KickApi()
redirect_to = NULL # object |  (optional)

try:
    # Get Kick Sign In Url Route
    api_instance.get_kick_sign_in_url_route_api2_kick_sign_in_url_get(redirect_to=redirect_to)
except ApiException as e:
    print("Exception when calling KickApi->get_kick_sign_in_url_route_api2_kick_sign_in_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_to** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kick_system_provider_bot_connect_url_route_api2_kick_system_provider_bot_connect_url_get**
> get_kick_system_provider_bot_connect_url_route_api2_kick_system_provider_bot_connect_url_get(redirect_to=redirect_to)

Get Kick System Provider Bot Connect Url Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KickApi()
redirect_to = NULL # object |  (optional)

try:
    # Get Kick System Provider Bot Connect Url Route
    api_instance.get_kick_system_provider_bot_connect_url_route_api2_kick_system_provider_bot_connect_url_get(redirect_to=redirect_to)
except ApiException as e:
    print("Exception when calling KickApi->get_kick_system_provider_bot_connect_url_route_api2_kick_system_provider_bot_connect_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_to** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kick_auth_route_api2_kick_auth_get**
> kick_auth_route_api2_kick_auth_get(code, state, scope=scope)

Kick Auth Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KickApi()
code = NULL # object | 
state = NULL # object | 
scope = NULL # object |  (optional)

try:
    # Kick Auth Route
    api_instance.kick_auth_route_api2_kick_auth_get(code, state, scope=scope)
except ApiException as e:
    print("Exception when calling KickApi->kick_auth_route_api2_kick_auth_get: %s\n" % e)
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

# **unban_user_api2_channels_channel_id_kick_channel_provider_id_ban_delete**
> unban_user_api2_channels_channel_id_kick_channel_provider_id_ban_delete(channel_id, channel_provider_id, provider_viewer_id)

Unban User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KickApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 
provider_viewer_id = NULL # object | 

try:
    # Unban User
    api_instance.unban_user_api2_channels_channel_id_kick_channel_provider_id_ban_delete(channel_id, channel_provider_id, provider_viewer_id)
except ApiException as e:
    print("Exception when calling KickApi->unban_user_api2_channels_channel_id_kick_channel_provider_id_ban_delete: %s\n" % e)
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

