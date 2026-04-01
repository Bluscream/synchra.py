# swagger_client.BotProvidersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_bot_provider_api2_system_bot_providers_provider_delete**](BotProvidersApi.md#delete_system_bot_provider_api2_system_bot_providers_provider_delete) | **DELETE** /api/2/system-bot-providers/{provider} | Delete System Bot Provider
[**get_system_bot_provider_api2_system_bot_providers_provider_get**](BotProvidersApi.md#get_system_bot_provider_api2_system_bot_providers_provider_get) | **GET** /api/2/system-bot-providers/{provider} | Get System Bot Provider
[**get_system_bot_providers_api2_system_bot_providers_get**](BotProvidersApi.md#get_system_bot_providers_api2_system_bot_providers_get) | **GET** /api/2/system-bot-providers | Get System Bot Providers


# **delete_system_bot_provider_api2_system_bot_providers_provider_delete**
> delete_system_bot_provider_api2_system_bot_providers_provider_delete(provider)

Delete System Bot Provider

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotProvidersApi()
provider = NULL # object | 

try:
    # Delete System Bot Provider
    api_instance.delete_system_bot_provider_api2_system_bot_providers_provider_delete(provider)
except ApiException as e:
    print("Exception when calling BotProvidersApi->delete_system_bot_provider_api2_system_bot_providers_provider_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_bot_provider_api2_system_bot_providers_provider_get**
> get_system_bot_provider_api2_system_bot_providers_provider_get(provider)

Get System Bot Provider

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotProvidersApi()
provider = NULL # object | 

try:
    # Get System Bot Provider
    api_instance.get_system_bot_provider_api2_system_bot_providers_provider_get(provider)
except ApiException as e:
    print("Exception when calling BotProvidersApi->get_system_bot_provider_api2_system_bot_providers_provider_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_bot_providers_api2_system_bot_providers_get**
> get_system_bot_providers_api2_system_bot_providers_get(cursor=cursor, per_page=per_page)

Get System Bot Providers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BotProvidersApi()
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get System Bot Providers
    api_instance.get_system_bot_providers_api2_system_bot_providers_get(cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling BotProvidersApi->get_system_bot_providers_api2_system_bot_providers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

