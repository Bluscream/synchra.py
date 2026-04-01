# swagger_client.TwitchApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_vip_user_api2_channels_channel_id_twitch_channel_provider_id_vips_post**](TwitchApi.md#add_vip_user_api2_channels_channel_id_twitch_channel_provider_id_vips_post) | **POST** /api/2/channels/{channel_id}/twitch/{channel_provider_id}/vips | Add Vip User
[**ban_user_api2_channels_channel_id_twitch_channel_provider_id_ban_post**](TwitchApi.md#ban_user_api2_channels_channel_id_twitch_channel_provider_id_ban_post) | **POST** /api/2/channels/{channel_id}/twitch/{channel_provider_id}/ban | Ban User
[**ban_user_api2_channels_channel_id_twitch_channel_provider_id_moderators_delete**](TwitchApi.md#ban_user_api2_channels_channel_id_twitch_channel_provider_id_moderators_delete) | **DELETE** /api/2/channels/{channel_id}/twitch/{channel_provider_id}/moderators | Ban User
[**ban_user_api2_channels_channel_id_twitch_channel_provider_id_moderators_post**](TwitchApi.md#ban_user_api2_channels_channel_id_twitch_channel_provider_id_moderators_post) | **POST** /api/2/channels/{channel_id}/twitch/{channel_provider_id}/moderators | Ban User
[**delete_chat_message_api2_channels_channel_id_twitch_channel_provider_id_chat_messages_provider_message_id_delete**](TwitchApi.md#delete_chat_message_api2_channels_channel_id_twitch_channel_provider_id_chat_messages_provider_message_id_delete) | **DELETE** /api/2/channels/{channel_id}/twitch/{channel_provider_id}/chat-messages/{provider_message_id} | Delete Chat Message
[**delete_raid_api2_channels_channel_id_twitch_channel_provider_id_raid_delete**](TwitchApi.md#delete_raid_api2_channels_channel_id_twitch_channel_provider_id_raid_delete) | **DELETE** /api/2/channels/{channel_id}/twitch/{channel_provider_id}/raid | Delete Raid
[**emulate_automatic_reward_redemption_api2_twitch_eventsub_emulate_automatic_reward_redemption_post**](TwitchApi.md#emulate_automatic_reward_redemption_api2_twitch_eventsub_emulate_automatic_reward_redemption_post) | **POST** /api/2/twitch/eventsub/emulate-automatic-reward-redemption | Emulate Automatic Reward Redemption
[**emulate_channel_chat_message_api2_twitch_eventsub_emulate_channel_chat_message_post**](TwitchApi.md#emulate_channel_chat_message_api2_twitch_eventsub_emulate_channel_chat_message_post) | **POST** /api/2/twitch/eventsub/emulate-channel-chat-message | Emulate Channel Chat Message
[**emulate_cheer_api2_twitch_eventsub_emulate_cheer_post**](TwitchApi.md#emulate_cheer_api2_twitch_eventsub_emulate_cheer_post) | **POST** /api/2/twitch/eventsub/emulate-cheer | Emulate Cheer
[**emulate_custom_reward_redemption_api2_twitch_eventsub_emulate_custom_reward_redemption_post**](TwitchApi.md#emulate_custom_reward_redemption_api2_twitch_eventsub_emulate_custom_reward_redemption_post) | **POST** /api/2/twitch/eventsub/emulate-custom-reward-redemption | Emulate Custom Reward Redemption
[**emulate_subscription_api2_twitch_eventsub_emulate_subscription_post**](TwitchApi.md#emulate_subscription_api2_twitch_eventsub_emulate_subscription_post) | **POST** /api/2/twitch/eventsub/emulate-subscription | Emulate Subscription
[**get_moderators_api2_channels_channel_id_twitch_channel_provider_id_moderators_get**](TwitchApi.md#get_moderators_api2_channels_channel_id_twitch_channel_provider_id_moderators_get) | **GET** /api/2/channels/{channel_id}/twitch/{channel_provider_id}/moderators | Get Moderators
[**get_twitch_badge_image_api2_channels_channel_id_twitch_badge_image_provider_channel_id_size_id_get**](TwitchApi.md#get_twitch_badge_image_api2_channels_channel_id_twitch_badge_image_provider_channel_id_size_id_get) | **GET** /api/2/channels/{channel_id}/twitch/badge-image/{provider_channel_id}/{size}/{id} | Get Twitch Badge Image
[**get_vip_users_api2_channels_channel_id_twitch_channel_provider_id_vips_get**](TwitchApi.md#get_vip_users_api2_channels_channel_id_twitch_channel_provider_id_vips_get) | **GET** /api/2/channels/{channel_id}/twitch/{channel_provider_id}/vips | Get Vip Users
[**raid_channel_api2_channels_channel_id_twitch_channel_provider_id_raid_post**](TwitchApi.md#raid_channel_api2_channels_channel_id_twitch_channel_provider_id_raid_post) | **POST** /api/2/channels/{channel_id}/twitch/{channel_provider_id}/raid | Raid Channel
[**remove_vip_user_api2_channels_channel_id_twitch_channel_provider_id_vips_delete**](TwitchApi.md#remove_vip_user_api2_channels_channel_id_twitch_channel_provider_id_vips_delete) | **DELETE** /api/2/channels/{channel_id}/twitch/{channel_provider_id}/vips | Remove Vip User
[**shoutout_user_api2_channels_channel_id_twitch_channel_provider_id_shoutout_post**](TwitchApi.md#shoutout_user_api2_channels_channel_id_twitch_channel_provider_id_shoutout_post) | **POST** /api/2/channels/{channel_id}/twitch/{channel_provider_id}/shoutout | Shoutout User
[**unban_user_api2_channels_channel_id_twitch_channel_provider_id_ban_delete**](TwitchApi.md#unban_user_api2_channels_channel_id_twitch_channel_provider_id_ban_delete) | **DELETE** /api/2/channels/{channel_id}/twitch/{channel_provider_id}/ban | Unban User


# **add_vip_user_api2_channels_channel_id_twitch_channel_provider_id_vips_post**
> add_vip_user_api2_channels_channel_id_twitch_channel_provider_id_vips_post(channel_id, channel_provider_id)

Add Vip User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Add Vip User
    api_instance.add_vip_user_api2_channels_channel_id_twitch_channel_provider_id_vips_post(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling TwitchApi->add_vip_user_api2_channels_channel_id_twitch_channel_provider_id_vips_post: %s\n" % e)
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

# **ban_user_api2_channels_channel_id_twitch_channel_provider_id_ban_post**
> ban_user_api2_channels_channel_id_twitch_channel_provider_id_ban_post(channel_id, channel_provider_id)

Ban User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Ban User
    api_instance.ban_user_api2_channels_channel_id_twitch_channel_provider_id_ban_post(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling TwitchApi->ban_user_api2_channels_channel_id_twitch_channel_provider_id_ban_post: %s\n" % e)
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

# **ban_user_api2_channels_channel_id_twitch_channel_provider_id_moderators_delete**
> ban_user_api2_channels_channel_id_twitch_channel_provider_id_moderators_delete(channel_id, channel_provider_id)

Ban User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Ban User
    api_instance.ban_user_api2_channels_channel_id_twitch_channel_provider_id_moderators_delete(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling TwitchApi->ban_user_api2_channels_channel_id_twitch_channel_provider_id_moderators_delete: %s\n" % e)
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

# **ban_user_api2_channels_channel_id_twitch_channel_provider_id_moderators_post**
> ban_user_api2_channels_channel_id_twitch_channel_provider_id_moderators_post(channel_id, channel_provider_id)

Ban User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Ban User
    api_instance.ban_user_api2_channels_channel_id_twitch_channel_provider_id_moderators_post(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling TwitchApi->ban_user_api2_channels_channel_id_twitch_channel_provider_id_moderators_post: %s\n" % e)
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

# **delete_chat_message_api2_channels_channel_id_twitch_channel_provider_id_chat_messages_provider_message_id_delete**
> delete_chat_message_api2_channels_channel_id_twitch_channel_provider_id_chat_messages_provider_message_id_delete(provider_message_id, channel_id, channel_provider_id)

Delete Chat Message

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
provider_message_id = NULL # object | 
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Delete Chat Message
    api_instance.delete_chat_message_api2_channels_channel_id_twitch_channel_provider_id_chat_messages_provider_message_id_delete(provider_message_id, channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling TwitchApi->delete_chat_message_api2_channels_channel_id_twitch_channel_provider_id_chat_messages_provider_message_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_message_id** | [**object**](.md)|  | 
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

# **delete_raid_api2_channels_channel_id_twitch_channel_provider_id_raid_delete**
> delete_raid_api2_channels_channel_id_twitch_channel_provider_id_raid_delete(channel_id, channel_provider_id)

Delete Raid

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Delete Raid
    api_instance.delete_raid_api2_channels_channel_id_twitch_channel_provider_id_raid_delete(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling TwitchApi->delete_raid_api2_channels_channel_id_twitch_channel_provider_id_raid_delete: %s\n" % e)
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

# **emulate_automatic_reward_redemption_api2_twitch_eventsub_emulate_automatic_reward_redemption_post**
> emulate_automatic_reward_redemption_api2_twitch_eventsub_emulate_automatic_reward_redemption_post(channel_id)

Emulate Automatic Reward Redemption

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 

try:
    # Emulate Automatic Reward Redemption
    api_instance.emulate_automatic_reward_redemption_api2_twitch_eventsub_emulate_automatic_reward_redemption_post(channel_id)
except ApiException as e:
    print("Exception when calling TwitchApi->emulate_automatic_reward_redemption_api2_twitch_eventsub_emulate_automatic_reward_redemption_post: %s\n" % e)
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

# **emulate_channel_chat_message_api2_twitch_eventsub_emulate_channel_chat_message_post**
> emulate_channel_chat_message_api2_twitch_eventsub_emulate_channel_chat_message_post(channel_id)

Emulate Channel Chat Message

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 

try:
    # Emulate Channel Chat Message
    api_instance.emulate_channel_chat_message_api2_twitch_eventsub_emulate_channel_chat_message_post(channel_id)
except ApiException as e:
    print("Exception when calling TwitchApi->emulate_channel_chat_message_api2_twitch_eventsub_emulate_channel_chat_message_post: %s\n" % e)
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

# **emulate_cheer_api2_twitch_eventsub_emulate_cheer_post**
> emulate_cheer_api2_twitch_eventsub_emulate_cheer_post(channel_id)

Emulate Cheer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 

try:
    # Emulate Cheer
    api_instance.emulate_cheer_api2_twitch_eventsub_emulate_cheer_post(channel_id)
except ApiException as e:
    print("Exception when calling TwitchApi->emulate_cheer_api2_twitch_eventsub_emulate_cheer_post: %s\n" % e)
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

# **emulate_custom_reward_redemption_api2_twitch_eventsub_emulate_custom_reward_redemption_post**
> emulate_custom_reward_redemption_api2_twitch_eventsub_emulate_custom_reward_redemption_post(channel_id)

Emulate Custom Reward Redemption

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 

try:
    # Emulate Custom Reward Redemption
    api_instance.emulate_custom_reward_redemption_api2_twitch_eventsub_emulate_custom_reward_redemption_post(channel_id)
except ApiException as e:
    print("Exception when calling TwitchApi->emulate_custom_reward_redemption_api2_twitch_eventsub_emulate_custom_reward_redemption_post: %s\n" % e)
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

# **emulate_subscription_api2_twitch_eventsub_emulate_subscription_post**
> emulate_subscription_api2_twitch_eventsub_emulate_subscription_post(channel_id)

Emulate Subscription

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 

try:
    # Emulate Subscription
    api_instance.emulate_subscription_api2_twitch_eventsub_emulate_subscription_post(channel_id)
except ApiException as e:
    print("Exception when calling TwitchApi->emulate_subscription_api2_twitch_eventsub_emulate_subscription_post: %s\n" % e)
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

# **get_moderators_api2_channels_channel_id_twitch_channel_provider_id_moderators_get**
> get_moderators_api2_channels_channel_id_twitch_channel_provider_id_moderators_get(channel_id, channel_provider_id)

Get Moderators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Get Moderators
    api_instance.get_moderators_api2_channels_channel_id_twitch_channel_provider_id_moderators_get(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling TwitchApi->get_moderators_api2_channels_channel_id_twitch_channel_provider_id_moderators_get: %s\n" % e)
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

# **get_twitch_badge_image_api2_channels_channel_id_twitch_badge_image_provider_channel_id_size_id_get**
> get_twitch_badge_image_api2_channels_channel_id_twitch_badge_image_provider_channel_id_size_id_get(channel_id, provider_channel_id, id, size)

Get Twitch Badge Image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 
provider_channel_id = NULL # object | 
id = NULL # object | Format: {set_id}-{id}
size = NULL # object | 

try:
    # Get Twitch Badge Image
    api_instance.get_twitch_badge_image_api2_channels_channel_id_twitch_badge_image_provider_channel_id_size_id_get(channel_id, provider_channel_id, id, size)
except ApiException as e:
    print("Exception when calling TwitchApi->get_twitch_badge_image_api2_channels_channel_id_twitch_badge_image_provider_channel_id_size_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **provider_channel_id** | [**object**](.md)|  | 
 **id** | [**object**](.md)| Format: {set_id}-{id} | 
 **size** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vip_users_api2_channels_channel_id_twitch_channel_provider_id_vips_get**
> get_vip_users_api2_channels_channel_id_twitch_channel_provider_id_vips_get(channel_id, channel_provider_id)

Get Vip Users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Get Vip Users
    api_instance.get_vip_users_api2_channels_channel_id_twitch_channel_provider_id_vips_get(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling TwitchApi->get_vip_users_api2_channels_channel_id_twitch_channel_provider_id_vips_get: %s\n" % e)
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

# **raid_channel_api2_channels_channel_id_twitch_channel_provider_id_raid_post**
> raid_channel_api2_channels_channel_id_twitch_channel_provider_id_raid_post(channel_id, channel_provider_id)

Raid Channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Raid Channel
    api_instance.raid_channel_api2_channels_channel_id_twitch_channel_provider_id_raid_post(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling TwitchApi->raid_channel_api2_channels_channel_id_twitch_channel_provider_id_raid_post: %s\n" % e)
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

# **remove_vip_user_api2_channels_channel_id_twitch_channel_provider_id_vips_delete**
> remove_vip_user_api2_channels_channel_id_twitch_channel_provider_id_vips_delete(channel_id, channel_provider_id)

Remove Vip User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Remove Vip User
    api_instance.remove_vip_user_api2_channels_channel_id_twitch_channel_provider_id_vips_delete(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling TwitchApi->remove_vip_user_api2_channels_channel_id_twitch_channel_provider_id_vips_delete: %s\n" % e)
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

# **shoutout_user_api2_channels_channel_id_twitch_channel_provider_id_shoutout_post**
> shoutout_user_api2_channels_channel_id_twitch_channel_provider_id_shoutout_post(channel_id, channel_provider_id)

Shoutout User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 

try:
    # Shoutout User
    api_instance.shoutout_user_api2_channels_channel_id_twitch_channel_provider_id_shoutout_post(channel_id, channel_provider_id)
except ApiException as e:
    print("Exception when calling TwitchApi->shoutout_user_api2_channels_channel_id_twitch_channel_provider_id_shoutout_post: %s\n" % e)
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

# **unban_user_api2_channels_channel_id_twitch_channel_provider_id_ban_delete**
> unban_user_api2_channels_channel_id_twitch_channel_provider_id_ban_delete(channel_id, channel_provider_id, provider_viewer_id)

Unban User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitchApi()
channel_id = NULL # object | 
channel_provider_id = NULL # object | 
provider_viewer_id = NULL # object | 

try:
    # Unban User
    api_instance.unban_user_api2_channels_channel_id_twitch_channel_provider_id_ban_delete(channel_id, channel_provider_id, provider_viewer_id)
except ApiException as e:
    print("Exception when calling TwitchApi->unban_user_api2_channels_channel_id_twitch_channel_provider_id_ban_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)|  | 
 **channel_provider_id** | [**object**](.md)|  | 
 **provider_viewer_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

