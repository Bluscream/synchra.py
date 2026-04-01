# swagger_client.ChannelStreamApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**force_end_channel_provider_stream_api2_channels_channel_id_provider_streams_channel_provider_stream_id_force_end_post**](ChannelStreamApi.md#force_end_channel_provider_stream_api2_channels_channel_id_provider_streams_channel_provider_stream_id_force_end_post) | **POST** /api/2/channels/{channel_id}/provider-streams/{channel_provider_stream_id}/force-end | Force End Channel Provider Stream
[**get_channel_streams_api2_channels_channel_id_streams_get**](ChannelStreamApi.md#get_channel_streams_api2_channels_channel_id_streams_get) | **GET** /api/2/channels/{channel_id}/streams | Get Channel Streams
[**get_channel_streams_period_api2_channels_channel_id_streams_period_get**](ChannelStreamApi.md#get_channel_streams_period_api2_channels_channel_id_streams_period_get) | **GET** /api/2/channels/{channel_id}/streams-period | Get Channel Streams Period
[**get_channel_streams_stats_api2_channels_channel_id_streams_stats_get**](ChannelStreamApi.md#get_channel_streams_stats_api2_channels_channel_id_streams_stats_get) | **GET** /api/2/channels/{channel_id}/streams-stats | Get Channel Streams Stats


# **force_end_channel_provider_stream_api2_channels_channel_id_provider_streams_channel_provider_stream_id_force_end_post**
> force_end_channel_provider_stream_api2_channels_channel_id_provider_streams_channel_provider_stream_id_force_end_post(channel_id, channel_provider_stream_id)

Force End Channel Provider Stream

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelStreamApi()
channel_id = NULL # object | 
channel_provider_stream_id = NULL # object | 

try:
    # Force End Channel Provider Stream
    api_instance.force_end_channel_provider_stream_api2_channels_channel_id_provider_streams_channel_provider_stream_id_force_end_post(channel_id, channel_provider_stream_id)
except ApiException as e:
    print("Exception when calling ChannelStreamApi->force_end_channel_provider_stream_api2_channels_channel_id_provider_streams_channel_provider_stream_id_force_end_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_provider_stream_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_streams_api2_channels_channel_id_streams_get**
> get_channel_streams_api2_channels_channel_id_streams_get(channel_id, cursor=cursor, per_page=per_page)

Get Channel Streams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelStreamApi()
channel_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Channel Streams
    api_instance.get_channel_streams_api2_channels_channel_id_streams_get(channel_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelStreamApi->get_channel_streams_api2_channels_channel_id_streams_get: %s\n" % e)
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

# **get_channel_streams_period_api2_channels_channel_id_streams_period_get**
> get_channel_streams_period_api2_channels_channel_id_streams_period_get(channel_id, from_date, to_date=to_date)

Get Channel Streams Period

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelStreamApi()
channel_id = NULL # object | 
from_date = NULL # object | 
to_date = NULL # object |  (optional)

try:
    # Get Channel Streams Period
    api_instance.get_channel_streams_period_api2_channels_channel_id_streams_period_get(channel_id, from_date, to_date=to_date)
except ApiException as e:
    print("Exception when calling ChannelStreamApi->get_channel_streams_period_api2_channels_channel_id_streams_period_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **from_date** | [**object**](.md)|  | 
 **to_date** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_streams_stats_api2_channels_channel_id_streams_stats_get**
> get_channel_streams_stats_api2_channels_channel_id_streams_stats_get(channel_id, from_date, to_date=to_date, group_by=group_by)

Get Channel Streams Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelStreamApi()
channel_id = NULL # object | 
from_date = NULL # object | 
to_date = NULL # object |  (optional)
group_by = NULL # object |  (optional)

try:
    # Get Channel Streams Stats
    api_instance.get_channel_streams_stats_api2_channels_channel_id_streams_stats_get(channel_id, from_date, to_date=to_date, group_by=group_by)
except ApiException as e:
    print("Exception when calling ChannelStreamApi->get_channel_streams_stats_api2_channels_channel_id_streams_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **from_date** | [**object**](.md)|  | 
 **to_date** | [**object**](.md)|  | [optional] 
 **group_by** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

