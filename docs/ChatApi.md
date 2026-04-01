# swagger_client.ChatApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emulate_channel_chat_message_route_api2_channels_channel_id_chat_messages_emulate_post**](ChatApi.md#emulate_channel_chat_message_route_api2_channels_channel_id_chat_messages_emulate_post) | **POST** /api/2/channels/{channel_id}/chat-messages/emulate | Emulate Channel Chat Message Route
[**emulate_chat_event_progress_api2_channels_channel_id_chat_events_emulate_progress_post**](ChatApi.md#emulate_chat_event_progress_api2_channels_channel_id_chat_events_emulate_progress_post) | **POST** /api/2/channels/{channel_id}/chat-events/emulate/progress | Emulate Chat Event Progress
[**get_chat_events_api2_channels_channel_id_chat_events_get**](ChatApi.md#get_chat_events_api2_channels_channel_id_chat_events_get) | **GET** /api/2/channels/{channel_id}/chat-events | Get Chat Events
[**get_chat_messages_api2_channels_channel_id_chat_messages_get**](ChatApi.md#get_chat_messages_api2_channels_channel_id_chat_messages_get) | **GET** /api/2/channels/{channel_id}/chat-messages | Get Chat Messages
[**get_emotes_api2_chat_emotes_get**](ChatApi.md#get_emotes_api2_chat_emotes_get) | **GET** /api/2/chat/emotes | Get Emotes
[**get_random_chat_messages_for_chat_preview_api2_channels_channel_id_random_chat_messages_get**](ChatApi.md#get_random_chat_messages_for_chat_preview_api2_channels_channel_id_random_chat_messages_get) | **GET** /api/2/channels/{channel_id}/random-chat-messages | Get Random Chat Messages For Chat Preview
[**send_chat_message_api2_chat_messages_post**](ChatApi.md#send_chat_message_api2_chat_messages_post) | **POST** /api/2/chat/messages | Send Chat Message


# **emulate_channel_chat_message_route_api2_channels_channel_id_chat_messages_emulate_post**
> emulate_channel_chat_message_route_api2_channels_channel_id_chat_messages_emulate_post(channel_id)

Emulate Channel Chat Message Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChatApi()
channel_id = NULL # object | 

try:
    # Emulate Channel Chat Message Route
    api_instance.emulate_channel_chat_message_route_api2_channels_channel_id_chat_messages_emulate_post(channel_id)
except ApiException as e:
    print("Exception when calling ChatApi->emulate_channel_chat_message_route_api2_channels_channel_id_chat_messages_emulate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emulate_chat_event_progress_api2_channels_channel_id_chat_events_emulate_progress_post**
> emulate_chat_event_progress_api2_channels_channel_id_chat_events_emulate_progress_post(channel_id)

Emulate Chat Event Progress

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChatApi()
channel_id = NULL # object | 

try:
    # Emulate Chat Event Progress
    api_instance.emulate_chat_event_progress_api2_channels_channel_id_chat_events_emulate_progress_post(channel_id)
except ApiException as e:
    print("Exception when calling ChatApi->emulate_chat_event_progress_api2_channels_channel_id_chat_events_emulate_progress_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_events_api2_channels_channel_id_chat_events_get**
> get_chat_events_api2_channels_channel_id_chat_events_get(channel_id, cursor=cursor, per_page=per_page)

Get Chat Events

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChatApi()
channel_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Chat Events
    api_instance.get_chat_events_api2_channels_channel_id_chat_events_get(channel_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChatApi->get_chat_events_api2_channels_channel_id_chat_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
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

# **get_chat_messages_api2_channels_channel_id_chat_messages_get**
> get_chat_messages_api2_channels_channel_id_chat_messages_get(channel_id, provider=provider, provider_viewer_id=provider_viewer_id, type=type, lte_created_at=lte_created_at, lt_created_at=lt_created_at, cursor=cursor, per_page=per_page)

Get Chat Messages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChatApi()
channel_id = NULL # object | 
provider = NULL # object |  (optional)
provider_viewer_id = NULL # object |  (optional)
type = NULL # object |  (optional)
lte_created_at = NULL # object |  (optional)
lt_created_at = NULL # object |  (optional)
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Chat Messages
    api_instance.get_chat_messages_api2_channels_channel_id_chat_messages_get(channel_id, provider=provider, provider_viewer_id=provider_viewer_id, type=type, lte_created_at=lte_created_at, lt_created_at=lt_created_at, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChatApi->get_chat_messages_api2_channels_channel_id_chat_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **provider** | [**object**](.md)|  | [optional] 
 **provider_viewer_id** | [**object**](.md)|  | [optional] 
 **type** | [**object**](.md)|  | [optional] 
 **lte_created_at** | [**object**](.md)|  | [optional] 
 **lt_created_at** | [**object**](.md)|  | [optional] 
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

# **get_emotes_api2_chat_emotes_get**
> get_emotes_api2_chat_emotes_get(channel_provider_id)

Get Emotes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChatApi()
channel_provider_id = NULL # object | 

try:
    # Get Emotes
    api_instance.get_emotes_api2_chat_emotes_get(channel_provider_id)
except ApiException as e:
    print("Exception when calling ChatApi->get_emotes_api2_chat_emotes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_provider_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_random_chat_messages_for_chat_preview_api2_channels_channel_id_random_chat_messages_get**
> get_random_chat_messages_for_chat_preview_api2_channels_channel_id_random_chat_messages_get(channel_id)

Get Random Chat Messages For Chat Preview

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChatApi()
channel_id = NULL # object | 

try:
    # Get Random Chat Messages For Chat Preview
    api_instance.get_random_chat_messages_for_chat_preview_api2_channels_channel_id_random_chat_messages_get(channel_id)
except ApiException as e:
    print("Exception when calling ChatApi->get_random_chat_messages_for_chat_preview_api2_channels_channel_id_random_chat_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_chat_message_api2_chat_messages_post**
> send_chat_message_api2_chat_messages_post()

Send Chat Message

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChatApi()

try:
    # Send Chat Message
    api_instance.send_chat_message_api2_chat_messages_post()
except ApiException as e:
    print("Exception when calling ChatApi->send_chat_message_api2_chat_messages_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

