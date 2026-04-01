# swagger_client.ChannelProviderApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_channel_provider_api2_channels_channel_id_providers_channel_provider_id_delete**](ChannelProviderApi.md#delete_channel_provider_api2_channels_channel_id_providers_channel_provider_id_delete) | **DELETE** /api/2/channels/{channel_id}/providers/{channel_provider_id} | Delete Channel Provider
[**disconnect_channel_provider_bot_api2_channels_channel_id_providers_channel_provider_id_bot_delete**](ChannelProviderApi.md#disconnect_channel_provider_bot_api2_channels_channel_id_providers_channel_provider_id_bot_delete) | **DELETE** /api/2/channels/{channel_id}/providers/{channel_provider_id}/bot | Disconnect Channel Provider Bot
[**get_channel_provider_route_api2_channels_channel_id_providers_channel_provider_id_get**](ChannelProviderApi.md#get_channel_provider_route_api2_channels_channel_id_providers_channel_provider_id_get) | **GET** /api/2/channels/{channel_id}/providers/{channel_provider_id} | Get Channel Provider Route
[**get_channel_providers_api2_channels_channel_id_providers_get**](ChannelProviderApi.md#get_channel_providers_api2_channels_channel_id_providers_get) | **GET** /api/2/channels/{channel_id}/providers | Get Channel Providers
[**get_stream_categories_api2_stream_categories_get**](ChannelProviderApi.md#get_stream_categories_api2_stream_categories_get) | **GET** /api/2/stream-categories | Get Stream Categories
[**start_commercial_api2_channels_channel_id_providers_channel_provider_id_run_commercial_post**](ChannelProviderApi.md#start_commercial_api2_channels_channel_id_providers_channel_provider_id_run_commercial_post) | **POST** /api/2/channels/{channel_id}/providers/{channel_provider_id}/run-commercial | Start Commercial
[**update_channel_provider_api2_channels_channel_id_providers_channel_provider_id_stream_put**](ChannelProviderApi.md#update_channel_provider_api2_channels_channel_id_providers_channel_provider_id_stream_put) | **PUT** /api/2/channels/{channel_id}/providers/{channel_provider_id}/stream | Update Channel Provider


# **delete_channel_provider_api2_channels_channel_id_providers_channel_provider_id_delete**
> delete_channel_provider_api2_channels_channel_id_providers_channel_provider_id_delete(channel_id, channel_provider_id)

Delete Channel Provider

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelProviderApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Delete Channel Provider
    api_instance.delete_channel_provider_api2_channels_channel_id_providers_channel_provider_id_delete(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling ChannelProviderApi->delete_channel_provider_api2_channels_channel_id_providers_channel_provider_id_delete: %s\n" % e)
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

# **disconnect_channel_provider_bot_api2_channels_channel_id_providers_channel_provider_id_bot_delete**
> disconnect_channel_provider_bot_api2_channels_channel_id_providers_channel_provider_id_bot_delete(channel_id, channel_provider_id)

Disconnect Channel Provider Bot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelProviderApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Disconnect Channel Provider Bot
    api_instance.disconnect_channel_provider_bot_api2_channels_channel_id_providers_channel_provider_id_bot_delete(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling ChannelProviderApi->disconnect_channel_provider_bot_api2_channels_channel_id_providers_channel_provider_id_bot_delete: %s\n" % e)
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

# **get_channel_provider_route_api2_channels_channel_id_providers_channel_provider_id_get**
> get_channel_provider_route_api2_channels_channel_id_providers_channel_provider_id_get(channel_id, channel_provider_id)

Get Channel Provider Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelProviderApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Get Channel Provider Route
    api_instance.get_channel_provider_route_api2_channels_channel_id_providers_channel_provider_id_get(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling ChannelProviderApi->get_channel_provider_route_api2_channels_channel_id_providers_channel_provider_id_get: %s\n" % e)
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

# **get_channel_providers_api2_channels_channel_id_providers_get**
> get_channel_providers_api2_channels_channel_id_providers_get(channel_id)

Get Channel Providers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelProviderApi()
channel_id = NULL # object | 

try:
    # Get Channel Providers
    api_instance.get_channel_providers_api2_channels_channel_id_providers_get(channel_id)
except ApiException as e:
    print("Exception when calling ChannelProviderApi->get_channel_providers_api2_channels_channel_id_providers_get: %s\n" % e)
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

# **get_stream_categories_api2_stream_categories_get**
> get_stream_categories_api2_stream_categories_get(provider, query, cursor=cursor, per_page=per_page)

Get Stream Categories

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelProviderApi()
provider = NULL # object | 
query = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Stream Categories
    api_instance.get_stream_categories_api2_stream_categories_get(provider, query, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelProviderApi->get_stream_categories_api2_stream_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**object**](.md)|  | 
 **query** | [**object**](.md)|  | 
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

# **start_commercial_api2_channels_channel_id_providers_channel_provider_id_run_commercial_post**
> start_commercial_api2_channels_channel_id_providers_channel_provider_id_run_commercial_post(channel_id, channel_provider_id)

Start Commercial

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelProviderApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Start Commercial
    api_instance.start_commercial_api2_channels_channel_id_providers_channel_provider_id_run_commercial_post(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling ChannelProviderApi->start_commercial_api2_channels_channel_id_providers_channel_provider_id_run_commercial_post: %s\n" % e)
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

# **update_channel_provider_api2_channels_channel_id_providers_channel_provider_id_stream_put**
> update_channel_provider_api2_channels_channel_id_providers_channel_provider_id_stream_put(channel_id, channel_provider_id)

Update Channel Provider

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelProviderApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Update Channel Provider
    api_instance.update_channel_provider_api2_channels_channel_id_providers_channel_provider_id_stream_put(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling ChannelProviderApi->update_channel_provider_api2_channels_channel_id_providers_channel_provider_id_stream_put: %s\n" % e)
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

