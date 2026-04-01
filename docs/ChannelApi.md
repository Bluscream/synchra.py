# swagger_client.ChannelApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_channel_api2_channels_post**](ChannelApi.md#create_channel_api2_channels_post) | **POST** /api/2/channels | Create Channel
[**delete_channel_api2_channels_channel_id_delete**](ChannelApi.md#delete_channel_api2_channels_channel_id_delete) | **DELETE** /api/2/channels/{channel_id} | Delete Channel
[**get_channel_api2_channels_channel_id_get**](ChannelApi.md#get_channel_api2_channels_channel_id_get) | **GET** /api/2/channels/{channel_id} | Get Channel
[**get_channels_api2_channels_get**](ChannelApi.md#get_channels_api2_channels_get) | **GET** /api/2/channels | Get Channels
[**get_channels_api2_global_channels_get**](ChannelApi.md#get_channels_api2_global_channels_get) | **GET** /api/2/global/channels | Get Channels
[**update_channel_api2_channels_channel_id_put**](ChannelApi.md#update_channel_api2_channels_channel_id_put) | **PUT** /api/2/channels/{channel_id} | Update Channel


# **create_channel_api2_channels_post**
> create_channel_api2_channels_post()

Create Channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApi()

try:
    # Create Channel
    api_instance.create_channel_api2_channels_post()
except ApiException as e:
    print("Exception when calling ChannelApi->create_channel_api2_channels_post: %s\n" % e)
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

# **delete_channel_api2_channels_channel_id_delete**
> delete_channel_api2_channels_channel_id_delete(channel_id, channel_name)

Delete Channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApi()
channel_id = NULL # object | 
channel_name = NULL # object | 

try:
    # Delete Channel
    api_instance.delete_channel_api2_channels_channel_id_delete(channel_id, channel_name)
except ApiException as e:
    print("Exception when calling ChannelApi->delete_channel_api2_channels_channel_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_name** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_api2_channels_channel_id_get**
> get_channel_api2_channels_channel_id_get(channel_id)

Get Channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApi()
channel_id = NULL # object | 

try:
    # Get Channel
    api_instance.get_channel_api2_channels_channel_id_get(channel_id)
except ApiException as e:
    print("Exception when calling ChannelApi->get_channel_api2_channels_channel_id_get: %s\n" % e)
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

# **get_channels_api2_channels_get**
> get_channels_api2_channels_get(name=name, channel_id=channel_id, provider=provider, provider_channel_name=provider_channel_name, cursor=cursor, per_page=per_page)

Get Channels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApi()
name = NULL # object |  (optional)
channel_id = NULL # object |  (optional)
provider = NULL # object |  (optional)
provider_channel_name = NULL # object |  (optional)
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Channels
    api_instance.get_channels_api2_channels_get(name=name, channel_id=channel_id, provider=provider, provider_channel_name=provider_channel_name, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelApi->get_channels_api2_channels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**object**](.md)|  | [optional] 
 **channel_id** | [**object**](.md)|  | [optional] 
 **provider** | [**object**](.md)|  | [optional] 
 **provider_channel_name** | [**object**](.md)|  | [optional] 
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

# **get_channels_api2_global_channels_get**
> get_channels_api2_global_channels_get(name=name, expand=expand, is_live=is_live, cursor=cursor, per_page=per_page)

Get Channels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApi()
name = NULL # object |  (optional)
expand = NULL # object | Values: channel_providers (optional)
is_live = NULL # object |  (optional)
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Channels
    api_instance.get_channels_api2_global_channels_get(name=name, expand=expand, is_live=is_live, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelApi->get_channels_api2_global_channels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**object**](.md)|  | [optional] 
 **expand** | [**object**](.md)| Values: channel_providers | [optional] 
 **is_live** | [**object**](.md)|  | [optional] 
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

# **update_channel_api2_channels_channel_id_put**
> update_channel_api2_channels_channel_id_put(channel_id)

Update Channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApi()
channel_id = NULL # object | 

try:
    # Update Channel
    api_instance.update_channel_api2_channels_channel_id_put(channel_id)
except ApiException as e:
    print("Exception when calling ChannelApi->update_channel_api2_channels_channel_id_put: %s\n" % e)
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

