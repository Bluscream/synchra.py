# swagger_client.ChannelTimerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_channel_timer_api2_channels_channel_id_timers_post**](ChannelTimerApi.md#create_channel_timer_api2_channels_channel_id_timers_post) | **POST** /api/2/channels/{channel_id}/timers | Create Channel Timer
[**delete_channel_timer_api2_channels_channel_id_timers_timer_id_delete**](ChannelTimerApi.md#delete_channel_timer_api2_channels_channel_id_timers_timer_id_delete) | **DELETE** /api/2/channels/{channel_id}/timers/{timer_id} | Delete Channel Timer
[**get_channel_timer_api2_channels_channel_id_timers_timer_id_get**](ChannelTimerApi.md#get_channel_timer_api2_channels_channel_id_timers_timer_id_get) | **GET** /api/2/channels/{channel_id}/timers/{timer_id} | Get Channel Timer
[**get_channel_timers_api2_channels_channel_id_timers_get**](ChannelTimerApi.md#get_channel_timers_api2_channels_channel_id_timers_get) | **GET** /api/2/channels/{channel_id}/timers | Get Channel Timers
[**update_channel_timer_api2_channels_channel_id_timers_timer_id_put**](ChannelTimerApi.md#update_channel_timer_api2_channels_channel_id_timers_timer_id_put) | **PUT** /api/2/channels/{channel_id}/timers/{timer_id} | Update Channel Timer


# **create_channel_timer_api2_channels_channel_id_timers_post**
> create_channel_timer_api2_channels_channel_id_timers_post(channel_id)

Create Channel Timer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelTimerApi()
channel_id = NULL # object | 

try:
    # Create Channel Timer
    api_instance.create_channel_timer_api2_channels_channel_id_timers_post(channel_id)
except ApiException as e:
    print("Exception when calling ChannelTimerApi->create_channel_timer_api2_channels_channel_id_timers_post: %s\n" % e)
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

# **delete_channel_timer_api2_channels_channel_id_timers_timer_id_delete**
> delete_channel_timer_api2_channels_channel_id_timers_timer_id_delete(channel_id, timer_id)

Delete Channel Timer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelTimerApi()
channel_id = NULL # object | 
timer_id = NULL # object | 

try:
    # Delete Channel Timer
    api_instance.delete_channel_timer_api2_channels_channel_id_timers_timer_id_delete(channel_id, timer_id)
except ApiException as e:
    print("Exception when calling ChannelTimerApi->delete_channel_timer_api2_channels_channel_id_timers_timer_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **timer_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_timer_api2_channels_channel_id_timers_timer_id_get**
> get_channel_timer_api2_channels_channel_id_timers_timer_id_get(channel_id, timer_id)

Get Channel Timer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelTimerApi()
channel_id = NULL # object | 
timer_id = NULL # object | 

try:
    # Get Channel Timer
    api_instance.get_channel_timer_api2_channels_channel_id_timers_timer_id_get(channel_id, timer_id)
except ApiException as e:
    print("Exception when calling ChannelTimerApi->get_channel_timer_api2_channels_channel_id_timers_timer_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **timer_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_timers_api2_channels_channel_id_timers_get**
> get_channel_timers_api2_channels_channel_id_timers_get(channel_id, cursor=cursor, per_page=per_page)

Get Channel Timers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelTimerApi()
channel_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Channel Timers
    api_instance.get_channel_timers_api2_channels_channel_id_timers_get(channel_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelTimerApi->get_channel_timers_api2_channels_channel_id_timers_get: %s\n" % e)
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

# **update_channel_timer_api2_channels_channel_id_timers_timer_id_put**
> update_channel_timer_api2_channels_channel_id_timers_timer_id_put(channel_id, timer_id)

Update Channel Timer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelTimerApi()
channel_id = NULL # object | 
timer_id = NULL # object | 

try:
    # Update Channel Timer
    api_instance.update_channel_timer_api2_channels_channel_id_timers_timer_id_put(channel_id, timer_id)
except ApiException as e:
    print("Exception when calling ChannelTimerApi->update_channel_timer_api2_channels_channel_id_timers_timer_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **timer_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

