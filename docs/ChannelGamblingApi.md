# swagger_client.ChannelGamblingApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_roulette_settings_api2_channels_channel_id_roulette_settings_get**](ChannelGamblingApi.md#get_roulette_settings_api2_channels_channel_id_roulette_settings_get) | **GET** /api/2/channels/{channel_id}/roulette-settings | Get Roulette Settings
[**get_slots_settings_api2_channels_channel_id_slots_settings_get**](ChannelGamblingApi.md#get_slots_settings_api2_channels_channel_id_slots_settings_get) | **GET** /api/2/channels/{channel_id}/slots-settings | Get Slots Settings
[**update_roulette_settings_api2_channels_channel_id_roulette_settings_put**](ChannelGamblingApi.md#update_roulette_settings_api2_channels_channel_id_roulette_settings_put) | **PUT** /api/2/channels/{channel_id}/roulette-settings | Update Roulette Settings
[**update_slots_settings_api2_channels_channel_id_slots_settings_put**](ChannelGamblingApi.md#update_slots_settings_api2_channels_channel_id_slots_settings_put) | **PUT** /api/2/channels/{channel_id}/slots-settings | Update Slots Settings


# **get_roulette_settings_api2_channels_channel_id_roulette_settings_get**
> get_roulette_settings_api2_channels_channel_id_roulette_settings_get(channel_id)

Get Roulette Settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelGamblingApi()
channel_id = NULL # object | 

try:
    # Get Roulette Settings
    api_instance.get_roulette_settings_api2_channels_channel_id_roulette_settings_get(channel_id)
except ApiException as e:
    print("Exception when calling ChannelGamblingApi->get_roulette_settings_api2_channels_channel_id_roulette_settings_get: %s\n" % e)
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

# **get_slots_settings_api2_channels_channel_id_slots_settings_get**
> get_slots_settings_api2_channels_channel_id_slots_settings_get(channel_id)

Get Slots Settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelGamblingApi()
channel_id = NULL # object | 

try:
    # Get Slots Settings
    api_instance.get_slots_settings_api2_channels_channel_id_slots_settings_get(channel_id)
except ApiException as e:
    print("Exception when calling ChannelGamblingApi->get_slots_settings_api2_channels_channel_id_slots_settings_get: %s\n" % e)
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

# **update_roulette_settings_api2_channels_channel_id_roulette_settings_put**
> update_roulette_settings_api2_channels_channel_id_roulette_settings_put(channel_id)

Update Roulette Settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelGamblingApi()
channel_id = NULL # object | 

try:
    # Update Roulette Settings
    api_instance.update_roulette_settings_api2_channels_channel_id_roulette_settings_put(channel_id)
except ApiException as e:
    print("Exception when calling ChannelGamblingApi->update_roulette_settings_api2_channels_channel_id_roulette_settings_put: %s\n" % e)
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

# **update_slots_settings_api2_channels_channel_id_slots_settings_put**
> update_slots_settings_api2_channels_channel_id_slots_settings_put(channel_id)

Update Slots Settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelGamblingApi()
channel_id = NULL # object | 

try:
    # Update Slots Settings
    api_instance.update_slots_settings_api2_channels_channel_id_slots_settings_put(channel_id)
except ApiException as e:
    print("Exception when calling ChannelGamblingApi->update_slots_settings_api2_channels_channel_id_slots_settings_put: %s\n" % e)
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

