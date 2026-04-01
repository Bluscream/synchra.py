# swagger_client.SystemTasksApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_task_api2_tasks_task_id_cancel_post**](SystemTasksApi.md#cancel_task_api2_tasks_task_id_cancel_post) | **POST** /api/2/tasks/{task_id}/cancel | Cancel Task
[**get_task_api2_tasks_task_id_get**](SystemTasksApi.md#get_task_api2_tasks_task_id_get) | **GET** /api/2/tasks/{task_id} | Get Task
[**get_tasks_route_api2_tasks_get**](SystemTasksApi.md#get_tasks_route_api2_tasks_get) | **GET** /api/2/tasks | Get Tasks Route


# **cancel_task_api2_tasks_task_id_cancel_post**
> cancel_task_api2_tasks_task_id_cancel_post(task_id)

Cancel Task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemTasksApi()
task_id = NULL # object | 

try:
    # Cancel Task
    api_instance.cancel_task_api2_tasks_task_id_cancel_post(task_id)
except ApiException as e:
    print("Exception when calling SystemTasksApi->cancel_task_api2_tasks_task_id_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_api2_tasks_task_id_get**
> get_task_api2_tasks_task_id_get(task_id)

Get Task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemTasksApi()
task_id = NULL # object | 

try:
    # Get Task
    api_instance.get_task_api2_tasks_task_id_get(task_id)
except ApiException as e:
    print("Exception when calling SystemTasksApi->get_task_api2_tasks_task_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_route_api2_tasks_get**
> get_tasks_route_api2_tasks_get(status=status, work_id=work_id, task_id=task_id, path=path, cursor=cursor, per_page=per_page)

Get Tasks Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemTasksApi()
status = NULL # object |  (optional)
work_id = NULL # object |  (optional)
task_id = NULL # object |  (optional)
path = NULL # object |  (optional)
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Tasks Route
    api_instance.get_tasks_route_api2_tasks_get(status=status, work_id=work_id, task_id=task_id, path=path, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling SystemTasksApi->get_tasks_route_api2_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**object**](.md)|  | [optional] 
 **work_id** | [**object**](.md)|  | [optional] 
 **task_id** | [**object**](.md)|  | [optional] 
 **path** | [**object**](.md)|  | [optional] 
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

