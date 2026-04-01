# swagger_client.CommandsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_command_api2_channels_channel_id_commands_post**](CommandsApi.md#create_command_api2_channels_channel_id_commands_post) | **POST** /api/2/channels/{channel_id}/commands | Create Command
[**delete_command_api2_channels_channel_id_commands_command_id_delete**](CommandsApi.md#delete_command_api2_channels_channel_id_commands_command_id_delete) | **DELETE** /api/2/channels/{channel_id}/commands/{command_id} | Delete Command
[**get_command_api2_channels_channel_id_commands_command_id_get**](CommandsApi.md#get_command_api2_channels_channel_id_commands_command_id_get) | **GET** /api/2/channels/{channel_id}/commands/{command_id} | Get Command
[**get_commands_api2_channels_channel_id_commands_get**](CommandsApi.md#get_commands_api2_channels_channel_id_commands_get) | **GET** /api/2/channels/{channel_id}/commands | Get Commands
[**update_command_api2_channels_channel_id_commands_command_id_put**](CommandsApi.md#update_command_api2_channels_channel_id_commands_command_id_put) | **PUT** /api/2/channels/{channel_id}/commands/{command_id} | Update Command


# **create_command_api2_channels_channel_id_commands_post**
> create_command_api2_channels_channel_id_commands_post(channel_id)

Create Command

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommandsApi()
channel_id = NULL # object | 

try:
    # Create Command
    api_instance.create_command_api2_channels_channel_id_commands_post(channel_id)
except ApiException as e:
    print("Exception when calling CommandsApi->create_command_api2_channels_channel_id_commands_post: %s\n" % e)
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

# **delete_command_api2_channels_channel_id_commands_command_id_delete**
> delete_command_api2_channels_channel_id_commands_command_id_delete(channel_id, command_id)

Delete Command

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommandsApi()
channel_id = NULL # object | 
command_id = NULL # object | 

try:
    # Delete Command
    api_instance.delete_command_api2_channels_channel_id_commands_command_id_delete(channel_id, command_id)
except ApiException as e:
    print("Exception when calling CommandsApi->delete_command_api2_channels_channel_id_commands_command_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **command_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_command_api2_channels_channel_id_commands_command_id_get**
> get_command_api2_channels_channel_id_commands_command_id_get(channel_id, command_id)

Get Command

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommandsApi()
channel_id = NULL # object | 
command_id = NULL # object | 

try:
    # Get Command
    api_instance.get_command_api2_channels_channel_id_commands_command_id_get(channel_id, command_id)
except ApiException as e:
    print("Exception when calling CommandsApi->get_command_api2_channels_channel_id_commands_command_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **command_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commands_api2_channels_channel_id_commands_get**
> get_commands_api2_channels_channel_id_commands_get(channel_id, cursor=cursor, per_page=per_page)

Get Commands

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommandsApi()
channel_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Commands
    api_instance.get_commands_api2_channels_channel_id_commands_get(channel_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling CommandsApi->get_commands_api2_channels_channel_id_commands_get: %s\n" % e)
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

# **update_command_api2_channels_channel_id_commands_command_id_put**
> update_command_api2_channels_channel_id_commands_command_id_put(channel_id, command_id)

Update Command

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommandsApi()
channel_id = NULL # object | 
command_id = NULL # object | 

try:
    # Update Command
    api_instance.update_command_api2_channels_channel_id_commands_command_id_put(channel_id, command_id)
except ApiException as e:
    print("Exception when calling CommandsApi->update_command_api2_channels_channel_id_commands_command_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **command_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

