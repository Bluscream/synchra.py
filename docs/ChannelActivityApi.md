# swagger_client.ChannelActivityApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activity_types_api2_activity_types_get**](ChannelActivityApi.md#activity_types_api2_activity_types_get) | **GET** /api/2/activity-types | Activity Types
[**delete_activity_api2_channels_channel_id_activities_activity_id_delete**](ChannelActivityApi.md#delete_activity_api2_channels_channel_id_activities_activity_id_delete) | **DELETE** /api/2/channels/{channel_id}/activities/{activity_id} | Delete Activity
[**get_activities_api2_channels_channel_id_activities_get**](ChannelActivityApi.md#get_activities_api2_channels_channel_id_activities_get) | **GET** /api/2/channels/{channel_id}/activities | Get Activities
[**get_activity_api2_channels_channel_id_activities_activity_id_get**](ChannelActivityApi.md#get_activity_api2_channels_channel_id_activities_activity_id_get) | **GET** /api/2/channels/{channel_id}/activities/{activity_id} | Get Activity
[**update_activity_api2_channels_channel_id_activities_activity_id_put**](ChannelActivityApi.md#update_activity_api2_channels_channel_id_activities_activity_id_put) | **PUT** /api/2/channels/{channel_id}/activities/{activity_id} | Update Activity


# **activity_types_api2_activity_types_get**
> activity_types_api2_activity_types_get()

Activity Types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelActivityApi()

try:
    # Activity Types
    api_instance.activity_types_api2_activity_types_get()
except ApiException as e:
    print("Exception when calling ChannelActivityApi->activity_types_api2_activity_types_get: %s\n" % e)
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

# **delete_activity_api2_channels_channel_id_activities_activity_id_delete**
> delete_activity_api2_channels_channel_id_activities_activity_id_delete(channel_id, activity_id)

Delete Activity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelActivityApi()
channel_id = NULL # object | 
activity_id = NULL # object | 

try:
    # Delete Activity
    api_instance.delete_activity_api2_channels_channel_id_activities_activity_id_delete(channel_id, activity_id)
except ApiException as e:
    print("Exception when calling ChannelActivityApi->delete_activity_api2_channels_channel_id_activities_activity_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **activity_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_api2_channels_channel_id_activities_get**
> get_activities_api2_channels_channel_id_activities_get(channel_id, type=type, not_type=not_type, min_count=min_count, cursor=cursor, per_page=per_page)

Get Activities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelActivityApi()
channel_id = NULL # object | 
type = NULL # object |  (optional)
not_type = NULL # object |  (optional)
min_count = NULL # object | <type>.<min count> (optional)
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Activities
    api_instance.get_activities_api2_channels_channel_id_activities_get(channel_id, type=type, not_type=not_type, min_count=min_count, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelActivityApi->get_activities_api2_channels_channel_id_activities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **type** | [**object**](.md)|  | [optional] 
 **not_type** | [**object**](.md)|  | [optional] 
 **min_count** | [**object**](.md)| &lt;type&gt;.&lt;min count&gt; | [optional] 
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

# **get_activity_api2_channels_channel_id_activities_activity_id_get**
> get_activity_api2_channels_channel_id_activities_activity_id_get(channel_id, activity_id)

Get Activity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelActivityApi()
channel_id = NULL # object | 
activity_id = NULL # object | 

try:
    # Get Activity
    api_instance.get_activity_api2_channels_channel_id_activities_activity_id_get(channel_id, activity_id)
except ApiException as e:
    print("Exception when calling ChannelActivityApi->get_activity_api2_channels_channel_id_activities_activity_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **activity_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity_api2_channels_channel_id_activities_activity_id_put**
> update_activity_api2_channels_channel_id_activities_activity_id_put(channel_id, activity_id)

Update Activity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelActivityApi()
channel_id = NULL # object | 
activity_id = NULL # object | 

try:
    # Update Activity
    api_instance.update_activity_api2_channels_channel_id_activities_activity_id_put(channel_id, activity_id)
except ApiException as e:
    print("Exception when calling ChannelActivityApi->update_activity_api2_channels_channel_id_activities_activity_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **activity_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

