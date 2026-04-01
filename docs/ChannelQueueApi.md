# swagger_client.ChannelQueueApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_viewer_to_channel_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_post**](ChannelQueueApi.md#add_viewer_to_channel_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_post) | **POST** /api/2/channels/{channel_id}/queues/{channel_queue_id}/viewers | Add Viewer To Channel Queue
[**clear_viewer_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_delete**](ChannelQueueApi.md#clear_viewer_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_delete) | **DELETE** /api/2/channels/{channel_id}/queues/{channel_queue_id}/viewers | Clear Viewer Queue
[**create_queue_api2_channels_channel_id_queues_post**](ChannelQueueApi.md#create_queue_api2_channels_channel_id_queues_post) | **POST** /api/2/channels/{channel_id}/queues | Create Queue
[**delete_queue_api2_channels_channel_id_queues_channel_queue_id_delete**](ChannelQueueApi.md#delete_queue_api2_channels_channel_id_queues_channel_queue_id_delete) | **DELETE** /api/2/channels/{channel_id}/queues/{channel_queue_id} | Delete Queue
[**get_queue_api2_channels_channel_id_queues_channel_queue_id_get**](ChannelQueueApi.md#get_queue_api2_channels_channel_id_queues_channel_queue_id_get) | **GET** /api/2/channels/{channel_id}/queues/{channel_queue_id} | Get Queue
[**get_queue_viewers_api2_channels_channel_id_queues_channel_queue_id_viewers_get**](ChannelQueueApi.md#get_queue_viewers_api2_channels_channel_id_queues_channel_queue_id_viewers_get) | **GET** /api/2/channels/{channel_id}/queues/{channel_queue_id}/viewers | Get Queue Viewers
[**get_queues_api2_channels_channel_id_queues_get**](ChannelQueueApi.md#get_queues_api2_channels_channel_id_queues_get) | **GET** /api/2/channels/{channel_id}/queues | Get Queues
[**move_viewer_to_top_of_queue_api2_channels_channel_id_queues_channel_queue_id_move_to_top_put**](ChannelQueueApi.md#move_viewer_to_top_of_queue_api2_channels_channel_id_queues_channel_queue_id_move_to_top_put) | **PUT** /api/2/channels/{channel_id}/queues/{channel_queue_id}/move-to-top | Move Viewer To Top Of Queue
[**remove_viewer_from_channel_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_channel_queue_viewer_id_delete**](ChannelQueueApi.md#remove_viewer_from_channel_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_channel_queue_viewer_id_delete) | **DELETE** /api/2/channels/{channel_id}/queues/{channel_queue_id}/viewers/{channel_queue_viewer_id} | Remove Viewer From Channel Queue
[**update_queue_api2_channels_channel_id_queues_channel_queue_id_put**](ChannelQueueApi.md#update_queue_api2_channels_channel_id_queues_channel_queue_id_put) | **PUT** /api/2/channels/{channel_id}/queues/{channel_queue_id} | Update Queue


# **add_viewer_to_channel_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_post**
> add_viewer_to_channel_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_post(channel_id, channel_queue_id)

Add Viewer To Channel Queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQueueApi()
channel_id = NULL # object | 
channel_queue_id = NULL # object | 

try:
    # Add Viewer To Channel Queue
    api_instance.add_viewer_to_channel_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_post(channel_id, channel_queue_id)
except ApiException as e:
    print("Exception when calling ChannelQueueApi->add_viewer_to_channel_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_queue_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_viewer_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_delete**
> clear_viewer_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_delete(channel_id, channel_queue_id)

Clear Viewer Queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQueueApi()
channel_id = NULL # object | 
channel_queue_id = NULL # object | 

try:
    # Clear Viewer Queue
    api_instance.clear_viewer_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_delete(channel_id, channel_queue_id)
except ApiException as e:
    print("Exception when calling ChannelQueueApi->clear_viewer_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_queue_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_queue_api2_channels_channel_id_queues_post**
> create_queue_api2_channels_channel_id_queues_post(channel_id)

Create Queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQueueApi()
channel_id = NULL # object | 

try:
    # Create Queue
    api_instance.create_queue_api2_channels_channel_id_queues_post(channel_id)
except ApiException as e:
    print("Exception when calling ChannelQueueApi->create_queue_api2_channels_channel_id_queues_post: %s\n" % e)
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

# **delete_queue_api2_channels_channel_id_queues_channel_queue_id_delete**
> delete_queue_api2_channels_channel_id_queues_channel_queue_id_delete(channel_id, channel_queue_id)

Delete Queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQueueApi()
channel_id = NULL # object | 
channel_queue_id = NULL # object | 

try:
    # Delete Queue
    api_instance.delete_queue_api2_channels_channel_id_queues_channel_queue_id_delete(channel_id, channel_queue_id)
except ApiException as e:
    print("Exception when calling ChannelQueueApi->delete_queue_api2_channels_channel_id_queues_channel_queue_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_queue_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queue_api2_channels_channel_id_queues_channel_queue_id_get**
> get_queue_api2_channels_channel_id_queues_channel_queue_id_get(channel_id, channel_queue_id)

Get Queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQueueApi()
channel_id = NULL # object | 
channel_queue_id = NULL # object | 

try:
    # Get Queue
    api_instance.get_queue_api2_channels_channel_id_queues_channel_queue_id_get(channel_id, channel_queue_id)
except ApiException as e:
    print("Exception when calling ChannelQueueApi->get_queue_api2_channels_channel_id_queues_channel_queue_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_queue_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queue_viewers_api2_channels_channel_id_queues_channel_queue_id_viewers_get**
> get_queue_viewers_api2_channels_channel_id_queues_channel_queue_id_viewers_get(channel_id, channel_queue_id, provider=provider, provider_viewer_id=provider_viewer_id, cursor=cursor, per_page=per_page)

Get Queue Viewers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQueueApi()
channel_id = NULL # object | 
channel_queue_id = NULL # object | 
provider = NULL # object |  (optional)
provider_viewer_id = NULL # object |  (optional)
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Queue Viewers
    api_instance.get_queue_viewers_api2_channels_channel_id_queues_channel_queue_id_viewers_get(channel_id, channel_queue_id, provider=provider, provider_viewer_id=provider_viewer_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelQueueApi->get_queue_viewers_api2_channels_channel_id_queues_channel_queue_id_viewers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_queue_id** | [**object**](.md)|  | 
 **provider** | [**object**](.md)|  | [optional] 
 **provider_viewer_id** | [**object**](.md)|  | [optional] 
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

# **get_queues_api2_channels_channel_id_queues_get**
> get_queues_api2_channels_channel_id_queues_get(channel_id, cursor=cursor, per_page=per_page)

Get Queues

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQueueApi()
channel_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Queues
    api_instance.get_queues_api2_channels_channel_id_queues_get(channel_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelQueueApi->get_queues_api2_channels_channel_id_queues_get: %s\n" % e)
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

# **move_viewer_to_top_of_queue_api2_channels_channel_id_queues_channel_queue_id_move_to_top_put**
> move_viewer_to_top_of_queue_api2_channels_channel_id_queues_channel_queue_id_move_to_top_put(channel_id, channel_queue_id)

Move Viewer To Top Of Queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQueueApi()
channel_id = NULL # object | 
channel_queue_id = NULL # object | 

try:
    # Move Viewer To Top Of Queue
    api_instance.move_viewer_to_top_of_queue_api2_channels_channel_id_queues_channel_queue_id_move_to_top_put(channel_id, channel_queue_id)
except ApiException as e:
    print("Exception when calling ChannelQueueApi->move_viewer_to_top_of_queue_api2_channels_channel_id_queues_channel_queue_id_move_to_top_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_queue_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_viewer_from_channel_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_channel_queue_viewer_id_delete**
> remove_viewer_from_channel_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_channel_queue_viewer_id_delete(channel_id, channel_queue_id, channel_queue_viewer_id)

Remove Viewer From Channel Queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQueueApi()
channel_id = NULL # object | 
channel_queue_id = NULL # object | 
channel_queue_viewer_id = NULL # object | 

try:
    # Remove Viewer From Channel Queue
    api_instance.remove_viewer_from_channel_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_channel_queue_viewer_id_delete(channel_id, channel_queue_id, channel_queue_viewer_id)
except ApiException as e:
    print("Exception when calling ChannelQueueApi->remove_viewer_from_channel_queue_api2_channels_channel_id_queues_channel_queue_id_viewers_channel_queue_viewer_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_queue_id** | [**object**](.md)|  | 
 **channel_queue_viewer_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_queue_api2_channels_channel_id_queues_channel_queue_id_put**
> update_queue_api2_channels_channel_id_queues_channel_queue_id_put(channel_id, channel_queue_id)

Update Queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQueueApi()
channel_id = NULL # object | 
channel_queue_id = NULL # object | 

try:
    # Update Queue
    api_instance.update_queue_api2_channels_channel_id_queues_channel_queue_id_put(channel_id, channel_queue_id)
except ApiException as e:
    print("Exception when calling ChannelQueueApi->update_queue_api2_channels_channel_id_queues_channel_queue_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_queue_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

