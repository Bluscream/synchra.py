# swagger_client.ChannelQuotesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_channel_quote_api2_channels_channel_id_quotes_post**](ChannelQuotesApi.md#create_channel_quote_api2_channels_channel_id_quotes_post) | **POST** /api/2/channels/{channel_id}/quotes | Create Channel Quote
[**delete_channel_quote_api2_channels_channel_id_quotes_quote_id_delete**](ChannelQuotesApi.md#delete_channel_quote_api2_channels_channel_id_quotes_quote_id_delete) | **DELETE** /api/2/channels/{channel_id}/quotes/{quote_id} | Delete Channel Quote
[**get_channel_quote_api2_channels_channel_id_quotes_quote_id_get**](ChannelQuotesApi.md#get_channel_quote_api2_channels_channel_id_quotes_quote_id_get) | **GET** /api/2/channels/{channel_id}/quotes/{quote_id} | Get Channel Quote
[**get_channel_quote_by_number_api2_channels_channel_id_quotes_number_number_get**](ChannelQuotesApi.md#get_channel_quote_by_number_api2_channels_channel_id_quotes_number_number_get) | **GET** /api/2/channels/{channel_id}/quotes/number/{number} | Get Channel Quote By Number
[**get_channel_quotes_api2_channels_channel_id_quotes_get**](ChannelQuotesApi.md#get_channel_quotes_api2_channels_channel_id_quotes_get) | **GET** /api/2/channels/{channel_id}/quotes | Get Channel Quotes
[**update_channel_quote_api2_channels_channel_id_quotes_quote_id_put**](ChannelQuotesApi.md#update_channel_quote_api2_channels_channel_id_quotes_quote_id_put) | **PUT** /api/2/channels/{channel_id}/quotes/{quote_id} | Update Channel Quote


# **create_channel_quote_api2_channels_channel_id_quotes_post**
> create_channel_quote_api2_channels_channel_id_quotes_post(channel_id)

Create Channel Quote

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQuotesApi()
channel_id = NULL # object | 

try:
    # Create Channel Quote
    api_instance.create_channel_quote_api2_channels_channel_id_quotes_post(channel_id)
except ApiException as e:
    print("Exception when calling ChannelQuotesApi->create_channel_quote_api2_channels_channel_id_quotes_post: %s\n" % e)
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

# **delete_channel_quote_api2_channels_channel_id_quotes_quote_id_delete**
> delete_channel_quote_api2_channels_channel_id_quotes_quote_id_delete(channel_id, quote_id)

Delete Channel Quote

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQuotesApi()
channel_id = NULL # object | 
quote_id = NULL # object | 

try:
    # Delete Channel Quote
    api_instance.delete_channel_quote_api2_channels_channel_id_quotes_quote_id_delete(channel_id, quote_id)
except ApiException as e:
    print("Exception when calling ChannelQuotesApi->delete_channel_quote_api2_channels_channel_id_quotes_quote_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **quote_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_quote_api2_channels_channel_id_quotes_quote_id_get**
> get_channel_quote_api2_channels_channel_id_quotes_quote_id_get(channel_id, quote_id)

Get Channel Quote

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQuotesApi()
channel_id = NULL # object | 
quote_id = NULL # object | 

try:
    # Get Channel Quote
    api_instance.get_channel_quote_api2_channels_channel_id_quotes_quote_id_get(channel_id, quote_id)
except ApiException as e:
    print("Exception when calling ChannelQuotesApi->get_channel_quote_api2_channels_channel_id_quotes_quote_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **quote_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_quote_by_number_api2_channels_channel_id_quotes_number_number_get**
> get_channel_quote_by_number_api2_channels_channel_id_quotes_number_number_get(channel_id, number)

Get Channel Quote By Number

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQuotesApi()
channel_id = NULL # object | 
number = NULL # object | 

try:
    # Get Channel Quote By Number
    api_instance.get_channel_quote_by_number_api2_channels_channel_id_quotes_number_number_get(channel_id, number)
except ApiException as e:
    print("Exception when calling ChannelQuotesApi->get_channel_quote_by_number_api2_channels_channel_id_quotes_number_number_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **number** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_quotes_api2_channels_channel_id_quotes_get**
> get_channel_quotes_api2_channels_channel_id_quotes_get(channel_id, cursor=cursor, per_page=per_page)

Get Channel Quotes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQuotesApi()
channel_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Channel Quotes
    api_instance.get_channel_quotes_api2_channels_channel_id_quotes_get(channel_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelQuotesApi->get_channel_quotes_api2_channels_channel_id_quotes_get: %s\n" % e)
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

# **update_channel_quote_api2_channels_channel_id_quotes_quote_id_put**
> update_channel_quote_api2_channels_channel_id_quotes_quote_id_put(channel_id, quote_id)

Update Channel Quote

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelQuotesApi()
channel_id = NULL # object | 
quote_id = NULL # object | 

try:
    # Update Channel Quote
    api_instance.update_channel_quote_api2_channels_channel_id_quotes_quote_id_put(channel_id, quote_id)
except ApiException as e:
    print("Exception when calling ChannelQuotesApi->update_channel_quote_api2_channels_channel_id_quotes_quote_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **quote_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

