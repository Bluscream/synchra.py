# swagger_client.ChannelChatFiltersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_post**](ChannelChatFiltersApi.md#create_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_post) | **POST** /api/2/channels/{channel_id}/chat-filters/{filter_id}/banned-terms | Create Banned Term
[**create_channel_filter_api2_channels_channel_id_chat_filters_post**](ChannelChatFiltersApi.md#create_channel_filter_api2_channels_channel_id_chat_filters_post) | **POST** /api/2/channels/{channel_id}/chat-filters | Create Channel Filter
[**delete_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_delete**](ChannelChatFiltersApi.md#delete_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_delete) | **DELETE** /api/2/channels/{channel_id}/chat-filters/{filter_id}/banned-terms/{banned_term_id} | Delete Banned Term
[**delete_channel_filter_api2_channels_channel_id_chat_filters_filter_id_delete**](ChannelChatFiltersApi.md#delete_channel_filter_api2_channels_channel_id_chat_filters_filter_id_delete) | **DELETE** /api/2/channels/{channel_id}/chat-filters/{filter_id} | Delete Channel Filter
[**get_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_get**](ChannelChatFiltersApi.md#get_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_get) | **GET** /api/2/channels/{channel_id}/chat-filters/{filter_id}/banned-terms/{banned_term_id} | Get Banned Term
[**get_banned_terms_api2_channels_channel_id_chat_filters_filter_id_banned_terms_get**](ChannelChatFiltersApi.md#get_banned_terms_api2_channels_channel_id_chat_filters_filter_id_banned_terms_get) | **GET** /api/2/channels/{channel_id}/chat-filters/{filter_id}/banned-terms | Get Banned Terms
[**get_channel_filter_api2_channels_channel_id_chat_filters_filter_id_get**](ChannelChatFiltersApi.md#get_channel_filter_api2_channels_channel_id_chat_filters_filter_id_get) | **GET** /api/2/channels/{channel_id}/chat-filters/{filter_id} | Get Channel Filter
[**get_channel_filters_api2_channels_channel_id_chat_filters_get**](ChannelChatFiltersApi.md#get_channel_filters_api2_channels_channel_id_chat_filters_get) | **GET** /api/2/channels/{channel_id}/chat-filters | Get Channel Filters
[**test_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_test_post**](ChannelChatFiltersApi.md#test_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_test_post) | **POST** /api/2/channels/{channel_id}/chat-filters/{filter_id}/banned-terms/test | Test Banned Term
[**update_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_put**](ChannelChatFiltersApi.md#update_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_put) | **PUT** /api/2/channels/{channel_id}/chat-filters/{filter_id}/banned-terms/{banned_term_id} | Update Banned Term
[**update_channel_filter_api2_channels_channel_id_chat_filters_filter_id_put**](ChannelChatFiltersApi.md#update_channel_filter_api2_channels_channel_id_chat_filters_filter_id_put) | **PUT** /api/2/channels/{channel_id}/chat-filters/{filter_id} | Update Channel Filter


# **create_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_post**
> create_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_post(channel_id, filter_id)

Create Banned Term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelChatFiltersApi()
channel_id = NULL # object | 
filter_id = NULL # object | 

try:
    # Create Banned Term
    api_instance.create_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_post(channel_id, filter_id)
except ApiException as e:
    print("Exception when calling ChannelChatFiltersApi->create_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **filter_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_channel_filter_api2_channels_channel_id_chat_filters_post**
> create_channel_filter_api2_channels_channel_id_chat_filters_post(channel_id)

Create Channel Filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelChatFiltersApi()
channel_id = NULL # object | 

try:
    # Create Channel Filter
    api_instance.create_channel_filter_api2_channels_channel_id_chat_filters_post(channel_id)
except ApiException as e:
    print("Exception when calling ChannelChatFiltersApi->create_channel_filter_api2_channels_channel_id_chat_filters_post: %s\n" % e)
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

# **delete_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_delete**
> delete_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_delete(channel_id, filter_id, banned_term_id)

Delete Banned Term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelChatFiltersApi()
channel_id = NULL # object | 
filter_id = NULL # object | 
banned_term_id = NULL # object | 

try:
    # Delete Banned Term
    api_instance.delete_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_delete(channel_id, filter_id, banned_term_id)
except ApiException as e:
    print("Exception when calling ChannelChatFiltersApi->delete_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **filter_id** | [**object**](.md)|  | 
 **banned_term_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_channel_filter_api2_channels_channel_id_chat_filters_filter_id_delete**
> delete_channel_filter_api2_channels_channel_id_chat_filters_filter_id_delete(channel_id, filter_id)

Delete Channel Filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelChatFiltersApi()
channel_id = NULL # object | 
filter_id = NULL # object | 

try:
    # Delete Channel Filter
    api_instance.delete_channel_filter_api2_channels_channel_id_chat_filters_filter_id_delete(channel_id, filter_id)
except ApiException as e:
    print("Exception when calling ChannelChatFiltersApi->delete_channel_filter_api2_channels_channel_id_chat_filters_filter_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **filter_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_get**
> get_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_get(channel_id, filter_id, banned_term_id)

Get Banned Term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelChatFiltersApi()
channel_id = NULL # object | 
filter_id = NULL # object | 
banned_term_id = NULL # object | 

try:
    # Get Banned Term
    api_instance.get_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_get(channel_id, filter_id, banned_term_id)
except ApiException as e:
    print("Exception when calling ChannelChatFiltersApi->get_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **filter_id** | [**object**](.md)|  | 
 **banned_term_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_banned_terms_api2_channels_channel_id_chat_filters_filter_id_banned_terms_get**
> get_banned_terms_api2_channels_channel_id_chat_filters_filter_id_banned_terms_get(channel_id, filter_id, cursor=cursor, per_page=per_page)

Get Banned Terms

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelChatFiltersApi()
channel_id = NULL # object | 
filter_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Banned Terms
    api_instance.get_banned_terms_api2_channels_channel_id_chat_filters_filter_id_banned_terms_get(channel_id, filter_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelChatFiltersApi->get_banned_terms_api2_channels_channel_id_chat_filters_filter_id_banned_terms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **filter_id** | [**object**](.md)|  | 
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

# **get_channel_filter_api2_channels_channel_id_chat_filters_filter_id_get**
> get_channel_filter_api2_channels_channel_id_chat_filters_filter_id_get(channel_id, filter_id)

Get Channel Filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelChatFiltersApi()
channel_id = NULL # object | 
filter_id = NULL # object | 

try:
    # Get Channel Filter
    api_instance.get_channel_filter_api2_channels_channel_id_chat_filters_filter_id_get(channel_id, filter_id)
except ApiException as e:
    print("Exception when calling ChannelChatFiltersApi->get_channel_filter_api2_channels_channel_id_chat_filters_filter_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **filter_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_filters_api2_channels_channel_id_chat_filters_get**
> get_channel_filters_api2_channels_channel_id_chat_filters_get(channel_id)

Get Channel Filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelChatFiltersApi()
channel_id = NULL # object | 

try:
    # Get Channel Filters
    api_instance.get_channel_filters_api2_channels_channel_id_chat_filters_get(channel_id)
except ApiException as e:
    print("Exception when calling ChannelChatFiltersApi->get_channel_filters_api2_channels_channel_id_chat_filters_get: %s\n" % e)
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

# **test_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_test_post**
> test_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_test_post(channel_id, filter_id)

Test Banned Term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelChatFiltersApi()
channel_id = NULL # object | 
filter_id = NULL # object | 

try:
    # Test Banned Term
    api_instance.test_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_test_post(channel_id, filter_id)
except ApiException as e:
    print("Exception when calling ChannelChatFiltersApi->test_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_test_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **filter_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_put**
> update_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_put(channel_id, filter_id, banned_term_id)

Update Banned Term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelChatFiltersApi()
channel_id = NULL # object | 
filter_id = NULL # object | 
banned_term_id = NULL # object | 

try:
    # Update Banned Term
    api_instance.update_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_put(channel_id, filter_id, banned_term_id)
except ApiException as e:
    print("Exception when calling ChannelChatFiltersApi->update_banned_term_api2_channels_channel_id_chat_filters_filter_id_banned_terms_banned_term_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **filter_id** | [**object**](.md)|  | 
 **banned_term_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_channel_filter_api2_channels_channel_id_chat_filters_filter_id_put**
> update_channel_filter_api2_channels_channel_id_chat_filters_filter_id_put(channel_id, filter_id)

Update Channel Filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelChatFiltersApi()
channel_id = NULL # object | 
filter_id = NULL # object | 

try:
    # Update Channel Filter
    api_instance.update_channel_filter_api2_channels_channel_id_chat_filters_filter_id_put(channel_id, filter_id)
except ApiException as e:
    print("Exception when calling ChannelChatFiltersApi->update_channel_filter_api2_channels_channel_id_chat_filters_filter_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **filter_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

