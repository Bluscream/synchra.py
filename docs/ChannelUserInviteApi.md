# swagger_client.ChannelUserInviteApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_user_invite_accept_api2_channel_user_invites_channel_user_invite_id_accept_post**](ChannelUserInviteApi.md#channel_user_invite_accept_api2_channel_user_invites_channel_user_invite_id_accept_post) | **POST** /api/2/channel-user-invites/{channel_user_invite_id}/accept | Channel User Invite Accept
[**channel_user_invite_api2_channels_channel_id_user_invites_post**](ChannelUserInviteApi.md#channel_user_invite_api2_channels_channel_id_user_invites_post) | **POST** /api/2/channels/{channel_id}/user-invites | Channel User Invite
[**channel_user_invite_delete_api2_channels_channel_id_user_invites_channel_user_invite_id_delete**](ChannelUserInviteApi.md#channel_user_invite_delete_api2_channels_channel_id_user_invites_channel_user_invite_id_delete) | **DELETE** /api/2/channels/{channel_id}/user-invites/{channel_user_invite_id} | Channel User Invite Delete
[**channel_user_invite_update_api2_channels_channel_id_user_invites_channel_user_invite_id_put**](ChannelUserInviteApi.md#channel_user_invite_update_api2_channels_channel_id_user_invites_channel_user_invite_id_put) | **PUT** /api/2/channels/{channel_id}/user-invites/{channel_user_invite_id} | Channel User Invite Update
[**channel_user_invites_api2_channels_channel_id_user_invites_get**](ChannelUserInviteApi.md#channel_user_invites_api2_channels_channel_id_user_invites_get) | **GET** /api/2/channels/{channel_id}/user-invites | Channel User Invites
[**delete_channel_user_access_api2_channels_channel_id_users_access_channel_user_access_id_delete**](ChannelUserInviteApi.md#delete_channel_user_access_api2_channels_channel_id_users_access_channel_user_access_id_delete) | **DELETE** /api/2/channels/{channel_id}/users-access/{channel_user_access_id} | Delete Channel User Access
[**get_channel_access_level_route_api2_channels_channel_id_access_level_get**](ChannelUserInviteApi.md#get_channel_access_level_route_api2_channels_channel_id_access_level_get) | **GET** /api/2/channels/{channel_id}/access-level | Get Channel Access Level Route
[**get_channel_users_access_api2_channels_channel_id_users_access_get**](ChannelUserInviteApi.md#get_channel_users_access_api2_channels_channel_id_users_access_get) | **GET** /api/2/channels/{channel_id}/users-access | Get Channel Users Access
[**update_channel_user_access_level_api2_channels_channel_id_users_access_channel_user_access_id_put**](ChannelUserInviteApi.md#update_channel_user_access_level_api2_channels_channel_id_users_access_channel_user_access_id_put) | **PUT** /api/2/channels/{channel_id}/users-access/{channel_user_access_id} | Update Channel User Access Level


# **channel_user_invite_accept_api2_channel_user_invites_channel_user_invite_id_accept_post**
> channel_user_invite_accept_api2_channel_user_invites_channel_user_invite_id_accept_post(channel_user_invite_id)

Channel User Invite Accept

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelUserInviteApi()
channel_user_invite_id = NULL # object | 

try:
    # Channel User Invite Accept
    api_instance.channel_user_invite_accept_api2_channel_user_invites_channel_user_invite_id_accept_post(channel_user_invite_id)
except ApiException as e:
    print("Exception when calling ChannelUserInviteApi->channel_user_invite_accept_api2_channel_user_invites_channel_user_invite_id_accept_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_user_invite_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_user_invite_api2_channels_channel_id_user_invites_post**
> channel_user_invite_api2_channels_channel_id_user_invites_post(channel_id)

Channel User Invite

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelUserInviteApi()
channel_id = NULL # object | 

try:
    # Channel User Invite
    api_instance.channel_user_invite_api2_channels_channel_id_user_invites_post(channel_id)
except ApiException as e:
    print("Exception when calling ChannelUserInviteApi->channel_user_invite_api2_channels_channel_id_user_invites_post: %s\n" % e)
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

# **channel_user_invite_delete_api2_channels_channel_id_user_invites_channel_user_invite_id_delete**
> channel_user_invite_delete_api2_channels_channel_id_user_invites_channel_user_invite_id_delete(channel_id, channel_user_invite_id)

Channel User Invite Delete

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelUserInviteApi()
channel_id = NULL # object | 
channel_user_invite_id = NULL # object | 

try:
    # Channel User Invite Delete
    api_instance.channel_user_invite_delete_api2_channels_channel_id_user_invites_channel_user_invite_id_delete(channel_id, channel_user_invite_id)
except ApiException as e:
    print("Exception when calling ChannelUserInviteApi->channel_user_invite_delete_api2_channels_channel_id_user_invites_channel_user_invite_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_user_invite_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_user_invite_update_api2_channels_channel_id_user_invites_channel_user_invite_id_put**
> channel_user_invite_update_api2_channels_channel_id_user_invites_channel_user_invite_id_put(channel_id, channel_user_invite_id)

Channel User Invite Update

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelUserInviteApi()
channel_id = NULL # object | 
channel_user_invite_id = NULL # object | 

try:
    # Channel User Invite Update
    api_instance.channel_user_invite_update_api2_channels_channel_id_user_invites_channel_user_invite_id_put(channel_id, channel_user_invite_id)
except ApiException as e:
    print("Exception when calling ChannelUserInviteApi->channel_user_invite_update_api2_channels_channel_id_user_invites_channel_user_invite_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_user_invite_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_user_invites_api2_channels_channel_id_user_invites_get**
> channel_user_invites_api2_channels_channel_id_user_invites_get(channel_id, cursor=cursor, per_page=per_page)

Channel User Invites

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelUserInviteApi()
channel_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Channel User Invites
    api_instance.channel_user_invites_api2_channels_channel_id_user_invites_get(channel_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelUserInviteApi->channel_user_invites_api2_channels_channel_id_user_invites_get: %s\n" % e)
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

# **delete_channel_user_access_api2_channels_channel_id_users_access_channel_user_access_id_delete**
> delete_channel_user_access_api2_channels_channel_id_users_access_channel_user_access_id_delete(channel_id, channel_user_access_id)

Delete Channel User Access

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelUserInviteApi()
channel_id = NULL # object | 
channel_user_access_id = NULL # object | 

try:
    # Delete Channel User Access
    api_instance.delete_channel_user_access_api2_channels_channel_id_users_access_channel_user_access_id_delete(channel_id, channel_user_access_id)
except ApiException as e:
    print("Exception when calling ChannelUserInviteApi->delete_channel_user_access_api2_channels_channel_id_users_access_channel_user_access_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_user_access_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_access_level_route_api2_channels_channel_id_access_level_get**
> get_channel_access_level_route_api2_channels_channel_id_access_level_get(channel_id)

Get Channel Access Level Route

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelUserInviteApi()
channel_id = NULL # object | 

try:
    # Get Channel Access Level Route
    api_instance.get_channel_access_level_route_api2_channels_channel_id_access_level_get(channel_id)
except ApiException as e:
    print("Exception when calling ChannelUserInviteApi->get_channel_access_level_route_api2_channels_channel_id_access_level_get: %s\n" % e)
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

# **get_channel_users_access_api2_channels_channel_id_users_access_get**
> get_channel_users_access_api2_channels_channel_id_users_access_get(channel_id, cursor=cursor, per_page=per_page)

Get Channel Users Access

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelUserInviteApi()
channel_id = NULL # object | 
cursor = NULL # object |  (optional)
per_page = NULL # object |  (optional)

try:
    # Get Channel Users Access
    api_instance.get_channel_users_access_api2_channels_channel_id_users_access_get(channel_id, cursor=cursor, per_page=per_page)
except ApiException as e:
    print("Exception when calling ChannelUserInviteApi->get_channel_users_access_api2_channels_channel_id_users_access_get: %s\n" % e)
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

# **update_channel_user_access_level_api2_channels_channel_id_users_access_channel_user_access_id_put**
> update_channel_user_access_level_api2_channels_channel_id_users_access_channel_user_access_id_put(channel_id, channel_user_access_id)

Update Channel User Access Level

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelUserInviteApi()
channel_id = NULL # object | 
channel_user_access_id = NULL # object | 

try:
    # Update Channel User Access Level
    api_instance.update_channel_user_access_level_api2_channels_channel_id_users_access_channel_user_access_id_put(channel_id, channel_user_access_id)
except ApiException as e:
    print("Exception when calling ChannelUserInviteApi->update_channel_user_access_level_api2_channels_channel_id_users_access_channel_user_access_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_user_access_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

