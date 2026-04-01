# swagger_client.ChannelPointSettingsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_channel_point_settings_api2_channels_channel_id_point_settings_get**](ChannelPointSettingsApi.md#get_channel_point_settings_api2_channels_channel_id_point_settings_get) | **GET** /api/2/channels/{channel_id}/point-settings | Get Channel Point Settings
[**update_channel_point_settings_api2_channels_channel_id_point_settings_put**](ChannelPointSettingsApi.md#update_channel_point_settings_api2_channels_channel_id_point_settings_put) | **PUT** /api/2/channels/{channel_id}/point-settings | Update Channel Point Settings


# **get_channel_point_settings_api2_channels_channel_id_point_settings_get**
> get_channel_point_settings_api2_channels_channel_id_point_settings_get(channel_id)

Get Channel Point Settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelPointSettingsApi()
channel_id = NULL # object | 

try:
    # Get Channel Point Settings
    api_instance.get_channel_point_settings_api2_channels_channel_id_point_settings_get(channel_id)
except ApiException as e:
    print("Exception when calling ChannelPointSettingsApi->get_channel_point_settings_api2_channels_channel_id_point_settings_get: %s\n" % e)
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

# **update_channel_point_settings_api2_channels_channel_id_point_settings_put**
> update_channel_point_settings_api2_channels_channel_id_point_settings_put(channel_id)

Update Channel Point Settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelPointSettingsApi()
channel_id = NULL # object | 

try:
    # Update Channel Point Settings
    api_instance.update_channel_point_settings_api2_channels_channel_id_point_settings_put(channel_id)
except ApiException as e:
    print("Exception when calling ChannelPointSettingsApi->update_channel_point_settings_api2_channels_channel_id_point_settings_put: %s\n" % e)
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

