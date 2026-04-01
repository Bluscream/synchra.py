# swagger_client.TikTokApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_tiktok_username_route_api2_channels_channel_id_register_provider_tiktok_post**](TikTokApi.md#register_tiktok_username_route_api2_channels_channel_id_register_provider_tiktok_post) | **POST** /api/2/channels/{channel_id}/register-provider/tiktok | Register Tiktok Username Route


# **register_tiktok_username_route_api2_channels_channel_id_register_provider_tiktok_post**
> register_tiktok_username_route_api2_channels_channel_id_register_provider_tiktok_post(channel_id)

Register Tiktok Username Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TikTokApi()
channel_id = NULL # object | 

try:
    # Register Tiktok Username Route
    api_instance.register_tiktok_username_route_api2_channels_channel_id_register_provider_tiktok_post(channel_id)
except ApiException as e:
    print("Exception when calling TikTokApi->register_tiktok_username_route_api2_channels_channel_id_register_provider_tiktok_post: %s\n" % e)
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

