# swagger_client.ChannelGiveawayApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_giveaway_api2_channels_channel_id_giveaways_post**](ChannelGiveawayApi.md#create_giveaway_api2_channels_channel_id_giveaways_post) | **POST** /api/2/channels/{channel_id}/giveaways | Create Giveaway
[**delete_giveaway_api2_channels_channel_id_giveaways_giveaway_id_delete**](ChannelGiveawayApi.md#delete_giveaway_api2_channels_channel_id_giveaways_giveaway_id_delete) | **DELETE** /api/2/channels/{channel_id}/giveaways/{giveaway_id} | Delete Giveaway
[**get_giveaway_api2_channels_channel_id_giveaways_giveaway_id_get**](ChannelGiveawayApi.md#get_giveaway_api2_channels_channel_id_giveaways_giveaway_id_get) | **GET** /api/2/channels/{channel_id}/giveaways/{giveaway_id} | Get Giveaway
[**get_giveaway_entries_api2_channels_channel_id_giveaways_giveaway_id_entries_get**](ChannelGiveawayApi.md#get_giveaway_entries_api2_channels_channel_id_giveaways_giveaway_id_entries_get) | **GET** /api/2/channels/{channel_id}/giveaways/{giveaway_id}/entries | Get Giveaway Entries
[**get_giveaways_api2_channels_channel_id_giveaways_get**](ChannelGiveawayApi.md#get_giveaways_api2_channels_channel_id_giveaways_get) | **GET** /api/2/channels/{channel_id}/giveaways | Get Giveaways
[**pick_giveaway_winner_api2_channels_channel_id_giveaways_giveaway_id_pick_winner_post**](ChannelGiveawayApi.md#pick_giveaway_winner_api2_channels_channel_id_giveaways_giveaway_id_pick_winner_post) | **POST** /api/2/channels/{channel_id}/giveaways/{giveaway_id}/pick-winner | Pick Giveaway Winner
[**update_giveaway_api2_channels_channel_id_giveaways_giveaway_id_put**](ChannelGiveawayApi.md#update_giveaway_api2_channels_channel_id_giveaways_giveaway_id_put) | **PUT** /api/2/channels/{channel_id}/giveaways/{giveaway_id} | Update Giveaway


# **create_giveaway_api2_channels_channel_id_giveaways_post**
> create_giveaway_api2_channels_channel_id_giveaways_post(channel_id)

Create Giveaway

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelGiveawayApi()
channel_id = NULL # object | 

try:
    # Create Giveaway
    api_instance.create_giveaway_api2_channels_channel_id_giveaways_post(channel_id)
except ApiException as e:
    print("Exception when calling ChannelGiveawayApi->create_giveaway_api2_channels_channel_id_giveaways_post: %s\n" % e)
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

# **delete_giveaway_api2_channels_channel_id_giveaways_giveaway_id_delete**
> delete_giveaway_api2_channels_channel_id_giveaways_giveaway_id_delete(channel_id, giveaway_id)

Delete Giveaway

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelGiveawayApi()
channel_id = NULL # object | 
giveaway_id = NULL # object | 

try:
    # Delete Giveaway
    api_instance.delete_giveaway_api2_channels_channel_id_giveaways_giveaway_id_delete(channel_id, giveaway_id)
except ApiException as e:
    print("Exception when calling ChannelGiveawayApi->delete_giveaway_api2_channels_channel_id_giveaways_giveaway_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **giveaway_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_giveaway_api2_channels_channel_id_giveaways_giveaway_id_get**
> get_giveaway_api2_channels_channel_id_giveaways_giveaway_id_get(channel_id, giveaway_id)

Get Giveaway

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelGiveawayApi()
channel_id = NULL # object | 
giveaway_id = NULL # object | 

try:
    # Get Giveaway
    api_instance.get_giveaway_api2_channels_channel_id_giveaways_giveaway_id_get(channel_id, giveaway_id)
except ApiException as e:
    print("Exception when calling ChannelGiveawayApi->get_giveaway_api2_channels_channel_id_giveaways_giveaway_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **giveaway_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_giveaway_entries_api2_channels_channel_id_giveaways_giveaway_id_entries_get**
> get_giveaway_entries_api2_channels_channel_id_giveaways_giveaway_id_entries_get(channel_id, giveaway_id, cursor=cursor, per_page=per_page)

Get Giveaway Entries

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelGiveawayApi()
channel_id = NULL # object | 
giveaway_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Giveaway Entries
    api_instance.get_giveaway_entries_api2_channels_channel_id_giveaways_giveaway_id_entries_get(channel_id, giveaway_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelGiveawayApi->get_giveaway_entries_api2_channels_channel_id_giveaways_giveaway_id_entries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **giveaway_id** | [**object**](.md)|  | 
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

# **get_giveaways_api2_channels_channel_id_giveaways_get**
> get_giveaways_api2_channels_channel_id_giveaways_get(channel_id, cursor=cursor, per_page=per_page)

Get Giveaways

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelGiveawayApi()
channel_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Giveaways
    api_instance.get_giveaways_api2_channels_channel_id_giveaways_get(channel_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelGiveawayApi->get_giveaways_api2_channels_channel_id_giveaways_get: %s\n" % e)
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

# **pick_giveaway_winner_api2_channels_channel_id_giveaways_giveaway_id_pick_winner_post**
> pick_giveaway_winner_api2_channels_channel_id_giveaways_giveaway_id_pick_winner_post(channel_id, giveaway_id)

Pick Giveaway Winner

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelGiveawayApi()
channel_id = NULL # object | 
giveaway_id = NULL # object | 

try:
    # Pick Giveaway Winner
    api_instance.pick_giveaway_winner_api2_channels_channel_id_giveaways_giveaway_id_pick_winner_post(channel_id, giveaway_id)
except ApiException as e:
    print("Exception when calling ChannelGiveawayApi->pick_giveaway_winner_api2_channels_channel_id_giveaways_giveaway_id_pick_winner_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **giveaway_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_giveaway_api2_channels_channel_id_giveaways_giveaway_id_put**
> update_giveaway_api2_channels_channel_id_giveaways_giveaway_id_put(channel_id, giveaway_id)

Update Giveaway

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelGiveawayApi()
channel_id = NULL # object | 
giveaway_id = NULL # object | 

try:
    # Update Giveaway
    api_instance.update_giveaway_api2_channels_channel_id_giveaways_giveaway_id_put(channel_id, giveaway_id)
except ApiException as e:
    print("Exception when calling ChannelGiveawayApi->update_giveaway_api2_channels_channel_id_giveaways_giveaway_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **giveaway_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

