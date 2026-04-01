# swagger_client.UserApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_api2_user_delete**](UserApi.md#delete_user_api2_user_delete) | **DELETE** /api/2/user | Delete User
[**delete_user_provider_route_api2_user_providers_user_provider_id_delete**](UserApi.md#delete_user_provider_route_api2_user_providers_user_provider_id_delete) | **DELETE** /api/2/user/providers/{user_provider_id} | Delete User Provider Route
[**get_user_provider_route_api2_user_providers_user_provider_id_get**](UserApi.md#get_user_provider_route_api2_user_providers_user_provider_id_get) | **GET** /api/2/user/providers/{user_provider_id} | Get User Provider Route
[**get_user_providers_route_api2_user_providers_get**](UserApi.md#get_user_providers_route_api2_user_providers_get) | **GET** /api/2/user/providers | Get User Providers Route
[**update_user_settings_api2_user_settings_put**](UserApi.md#update_user_settings_api2_user_settings_put) | **PUT** /api/2/user/settings | Update User Settings
[**user_info_api2_user_get**](UserApi.md#user_info_api2_user_get) | **GET** /api/2/user | User Info
[**user_settings_api2_user_settings_get**](UserApi.md#user_settings_api2_user_settings_get) | **GET** /api/2/user/settings | User Settings


# **delete_user_api2_user_delete**
> delete_user_api2_user_delete(username)

Delete User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
username = NULL # object | 

try:
    # Delete User
    api_instance.delete_user_api2_user_delete(username)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_api2_user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_provider_route_api2_user_providers_user_provider_id_delete**
> delete_user_provider_route_api2_user_providers_user_provider_id_delete(user_provider_id)

Delete User Provider Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_provider_id = NULL # object | 

try:
    # Delete User Provider Route
    api_instance.delete_user_provider_route_api2_user_providers_user_provider_id_delete(user_provider_id)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_provider_route_api2_user_providers_user_provider_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_provider_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_provider_route_api2_user_providers_user_provider_id_get**
> get_user_provider_route_api2_user_providers_user_provider_id_get(user_provider_id)

Get User Provider Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_provider_id = NULL # object | 

try:
    # Get User Provider Route
    api_instance.get_user_provider_route_api2_user_providers_user_provider_id_get(user_provider_id)
except ApiException as e:
    print("Exception when calling UserApi->get_user_provider_route_api2_user_providers_user_provider_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_provider_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_providers_route_api2_user_providers_get**
> get_user_providers_route_api2_user_providers_get()

Get User Providers Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()

try:
    # Get User Providers Route
    api_instance.get_user_providers_route_api2_user_providers_get()
except ApiException as e:
    print("Exception when calling UserApi->get_user_providers_route_api2_user_providers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_settings_api2_user_settings_put**
> update_user_settings_api2_user_settings_put()

Update User Settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()

try:
    # Update User Settings
    api_instance.update_user_settings_api2_user_settings_put()
except ApiException as e:
    print("Exception when calling UserApi->update_user_settings_api2_user_settings_put: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_info_api2_user_get**
> user_info_api2_user_get()

User Info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()

try:
    # User Info
    api_instance.user_info_api2_user_get()
except ApiException as e:
    print("Exception when calling UserApi->user_info_api2_user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_api2_user_settings_get**
> user_settings_api2_user_settings_get()

User Settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()

try:
    # User Settings
    api_instance.user_settings_api2_user_settings_get()
except ApiException as e:
    print("Exception when calling UserApi->user_settings_api2_user_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

