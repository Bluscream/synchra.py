# swagger_client.StreamElementsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_stream_elements_channel_provider_api2_channels_channel_id_register_provider_streamelements_post**](StreamElementsApi.md#register_stream_elements_channel_provider_api2_channels_channel_id_register_provider_streamelements_post) | **POST** /api/2/channels/{channel_id}/register-provider/streamelements | Register Streamelements Channel Provider
[**replay_stream_elements_alert_api2_channels_channel_id_providers_channel_provider_id_streamelements_alerts_replay_activity_id_post**](StreamElementsApi.md#replay_stream_elements_alert_api2_channels_channel_id_providers_channel_provider_id_streamelements_alerts_replay_activity_id_post) | **POST** /api/2/channels/{channel_id}/providers/{channel_provider_id}/streamelements/alerts-replay/{activity_id} | Replay Streamelements Alert
[**se_alerts_action_route_api2_channels_channel_id_providers_channel_provider_id_streamelements_alerts_action_put**](StreamElementsApi.md#se_alerts_action_route_api2_channels_channel_id_providers_channel_provider_id_streamelements_alerts_action_put) | **PUT** /api/2/channels/{channel_id}/providers/{channel_provider_id}/streamelements/alerts-action | Se Alerts Action Route


# **register_stream_elements_channel_provider_api2_channels_channel_id_register_provider_streamelements_post**
> register_stream_elements_channel_provider_api2_channels_channel_id_register_provider_streamelements_post(channel_id)

Register Streamelements Channel Provider

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamElementsApi()
channel_id = NULL # object | 

try:
    # Register Streamelements Channel Provider
    api_instance.register_stream_elements_channel_provider_api2_channels_channel_id_register_provider_streamelements_post(channel_id)
except ApiException as e:
    print("Exception when calling StreamElementsApi->register_stream_elements_channel_provider_api2_channels_channel_id_register_provider_streamelements_post: %s\n" % e)
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

# **replay_stream_elements_alert_api2_channels_channel_id_providers_channel_provider_id_streamelements_alerts_replay_activity_id_post**
> replay_stream_elements_alert_api2_channels_channel_id_providers_channel_provider_id_streamelements_alerts_replay_activity_id_post(channel_id, channel_provider_id, activity_id)

Replay Streamelements Alert

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamElementsApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 
activity_id = NULL # object | 

try:
    # Replay Streamelements Alert
    api_instance.replay_stream_elements_alert_api2_channels_channel_id_providers_channel_provider_id_streamelements_alerts_replay_activity_id_post(channel_id, channel_provider_id, activity_id)
except ApiException as e:
    print("Exception when calling StreamElementsApi->replay_stream_elements_alert_api2_channels_channel_id_providers_channel_provider_id_streamelements_alerts_replay_activity_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_provider_id** | [**object**](.md)|  | 
 **activity_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **se_alerts_action_route_api2_channels_channel_id_providers_channel_provider_id_streamelements_alerts_action_put**
> se_alerts_action_route_api2_channels_channel_id_providers_channel_provider_id_streamelements_alerts_action_put(channel_id, channel_provider_id)

Se Alerts Action Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamElementsApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Se Alerts Action Route
    api_instance.se_alerts_action_route_api2_channels_channel_id_providers_channel_provider_id_streamelements_alerts_action_put(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling StreamElementsApi->se_alerts_action_route_api2_channels_channel_id_providers_channel_provider_id_streamelements_alerts_action_put: %s\n" % e)
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

