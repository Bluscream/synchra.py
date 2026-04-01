# swagger_client.CommandTemplatesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_command_template_api2_command_templates_post**](CommandTemplatesApi.md#create_command_template_api2_command_templates_post) | **POST** /api/2/command-templates | Create Command Template
[**delete_command_template_api2_command_templates_command_template_id_delete**](CommandTemplatesApi.md#delete_command_template_api2_command_templates_command_template_id_delete) | **DELETE** /api/2/command-templates/{command_template_id} | Delete Command Template
[**get_command_template_api2_command_templates_command_template_id_get**](CommandTemplatesApi.md#get_command_template_api2_command_templates_command_template_id_get) | **GET** /api/2/command-templates/{command_template_id} | Get Command Template
[**get_command_templates_api2_command_templates_get**](CommandTemplatesApi.md#get_command_templates_api2_command_templates_get) | **GET** /api/2/command-templates | Get Command Templates
[**update_command_template_api2_command_templates_command_template_id_put**](CommandTemplatesApi.md#update_command_template_api2_command_templates_command_template_id_put) | **PUT** /api/2/command-templates/{command_template_id} | Update Command Template


# **create_command_template_api2_command_templates_post**
> create_command_template_api2_command_templates_post()

Create Command Template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommandTemplatesApi()

try:
    # Create Command Template
    api_instance.create_command_template_api2_command_templates_post()
except ApiException as e:
    print("Exception when calling CommandTemplatesApi->create_command_template_api2_command_templates_post: %s\n" % e)
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

# **delete_command_template_api2_command_templates_command_template_id_delete**
> delete_command_template_api2_command_templates_command_template_id_delete(command_template_id)

Delete Command Template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommandTemplatesApi()
command_template_id = NULL # object | 

try:
    # Delete Command Template
    api_instance.delete_command_template_api2_command_templates_command_template_id_delete(command_template_id)
except ApiException as e:
    print("Exception when calling CommandTemplatesApi->delete_command_template_api2_command_templates_command_template_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_template_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_command_template_api2_command_templates_command_template_id_get**
> get_command_template_api2_command_templates_command_template_id_get(command_template_id)

Get Command Template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommandTemplatesApi()
command_template_id = NULL # object | 

try:
    # Get Command Template
    api_instance.get_command_template_api2_command_templates_command_template_id_get(command_template_id)
except ApiException as e:
    print("Exception when calling CommandTemplatesApi->get_command_template_api2_command_templates_command_template_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_template_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_command_templates_api2_command_templates_get**
> get_command_templates_api2_command_templates_get(cursor=cursor, per_page=per_page)

Get Command Templates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommandTemplatesApi()
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Command Templates
    api_instance.get_command_templates_api2_command_templates_get(cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling CommandTemplatesApi->get_command_templates_api2_command_templates_get: %s\n" % e)
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

# **update_command_template_api2_command_templates_command_template_id_put**
> update_command_template_api2_command_templates_command_template_id_put(command_template_id)

Update Command Template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommandTemplatesApi()
command_template_id = NULL # object | 

try:
    # Update Command Template
    api_instance.update_command_template_api2_command_templates_command_template_id_put(command_template_id)
except ApiException as e:
    print("Exception when calling CommandTemplatesApi->update_command_template_api2_command_templates_command_template_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_template_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

