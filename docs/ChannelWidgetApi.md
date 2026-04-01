# swagger_client.ChannelWidgetApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_widget_api2_channels_channel_id_widgets_post**](ChannelWidgetApi.md#create_widget_api2_channels_channel_id_widgets_post) | **POST** /api/2/channels/{channel_id}/widgets | Create Widget
[**delete_widget_api2_channels_channel_id_widgets_widget_id_delete**](ChannelWidgetApi.md#delete_widget_api2_channels_channel_id_widgets_widget_id_delete) | **DELETE** /api/2/channels/{channel_id}/widgets/{widget_id} | Delete Widget
[**get_widget_api2_widgets_widget_id_get**](ChannelWidgetApi.md#get_widget_api2_widgets_widget_id_get) | **GET** /api/2/widgets/{widget_id} | Get Widget
[**get_widgets_api2_channels_channel_id_widgets_get**](ChannelWidgetApi.md#get_widgets_api2_channels_channel_id_widgets_get) | **GET** /api/2/channels/{channel_id}/widgets | Get Widgets
[**update_widget_api2_channels_channel_id_widgets_widget_id_put**](ChannelWidgetApi.md#update_widget_api2_channels_channel_id_widgets_widget_id_put) | **PUT** /api/2/channels/{channel_id}/widgets/{widget_id} | Update Widget


# **create_widget_api2_channels_channel_id_widgets_post**
> create_widget_api2_channels_channel_id_widgets_post(channel_id)

Create Widget

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelWidgetApi()
channel_id = NULL # object | 

try:
    # Create Widget
    api_instance.create_widget_api2_channels_channel_id_widgets_post(channel_id)
except ApiException as e:
    print("Exception when calling ChannelWidgetApi->create_widget_api2_channels_channel_id_widgets_post: %s\n" % e)
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

# **delete_widget_api2_channels_channel_id_widgets_widget_id_delete**
> delete_widget_api2_channels_channel_id_widgets_widget_id_delete(channel_id, widget_id)

Delete Widget

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelWidgetApi()
channel_id = NULL # object | 
widget_id = NULL # object | 

try:
    # Delete Widget
    api_instance.delete_widget_api2_channels_channel_id_widgets_widget_id_delete(channel_id, widget_id)
except ApiException as e:
    print("Exception when calling ChannelWidgetApi->delete_widget_api2_channels_channel_id_widgets_widget_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **widget_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_api2_widgets_widget_id_get**
> get_widget_api2_widgets_widget_id_get(widget_id)

Get Widget

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelWidgetApi()
widget_id = NULL # object | 

try:
    # Get Widget
    api_instance.get_widget_api2_widgets_widget_id_get(widget_id)
except ApiException as e:
    print("Exception when calling ChannelWidgetApi->get_widget_api2_widgets_widget_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widgets_api2_channels_channel_id_widgets_get**
> get_widgets_api2_channels_channel_id_widgets_get(channel_id, cursor=cursor, per_page=per_page)

Get Widgets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelWidgetApi()
channel_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Widgets
    api_instance.get_widgets_api2_channels_channel_id_widgets_get(channel_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelWidgetApi->get_widgets_api2_channels_channel_id_widgets_get: %s\n" % e)
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

# **update_widget_api2_channels_channel_id_widgets_widget_id_put**
> update_widget_api2_channels_channel_id_widgets_widget_id_put(channel_id, widget_id)

Update Widget

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelWidgetApi()
channel_id = NULL # object | 
widget_id = NULL # object | 

try:
    # Update Widget
    api_instance.update_widget_api2_channels_channel_id_widgets_widget_id_put(channel_id, widget_id)
except ApiException as e:
    print("Exception when calling ChannelWidgetApi->update_widget_api2_channels_channel_id_widgets_widget_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **widget_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

