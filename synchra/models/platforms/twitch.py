from enum import Enum
from pydantic import Field
from ..base import SynchraBaseModel
from ..fragments import Emote, Mention

class TwitchActivityType(Enum):
    sub = 'sub'
    resub = 'resub'
    sub_gift = 'sub_gift'
    community_sub_gift = 'community_sub_gift'
    raid = 'raid'
    charity_donation = 'charity_donation'
    bits = 'bits'
    follow = 'follow'
    points = 'points'
    twitch_shoutout = 'twitch_shoutout'
    twitch_watch_streak = 'twitch_watch_streak'

class TwitchActivityName(Enum):
    sub = 'sub'
    resub = 'resub'
    sub_gift = 'sub_gift'
    community_sub_gift = 'community_sub_gift'
    raid = 'raid'
    charity_donation = 'charity_donation'
    bits = 'bits'
    follow = 'follow'
    points = 'points'
    twitch_shoutout = 'twitch_shoutout'
    twitch_watch_streak = 'twitch_watch_streak'

class TwitchCheerFragmentType(Enum):
    text = 'text'
    cheermote = 'cheermote'
    emote = 'emote'
    mention = 'mention'

class Cheermote(SynchraBaseModel):
    prefix: str = Field(..., title='Prefix')
    bits: int = Field(..., title='Bits')
    tier: int = Field(..., title='Tier')

class TwitchMessagePartType(Enum):
    text = 'text'
    cheermote = 'cheermote'
    emote = 'emote'
    mention = 'mention'

class Fragment(SynchraBaseModel):
    type: TwitchCheerFragmentType | str = Field(..., title='Type')
    text: str = Field(..., title='Text')
    cheermote: Cheermote | None = None
    emote: Emote | None = None
    mention: Mention | None = None

class TwitchActivitySubType(Enum):
    sub = 'sub'
    resub = 'resub'
    sub_gift = 'sub_gift'
    community_sub_gift = 'community_sub_gift'
    gift_paid_upgrade = 'gift_paid_upgrade'
    prime_paid_upgrade = 'prime_paid_upgrade'
    pay_it_forward = 'pay_it_forward'
    raid = 'raid'
    unraid = 'unraid'
    announcement = 'announcement'
    bits_badge_tier = 'bits_badge_tier'
    charity_donation = 'charity_donation'
    shared_chat_sub = 'shared_chat_sub'
    shared_chat_resub = 'shared_chat_resub'
    shared_chat_sub_gift = 'shared_chat_sub_gift'
    shared_chat_community_sub_gift = 'shared_chat_community_sub_gift'
    shared_chat_gift_paid_upgrade = 'shared_chat_gift_paid_upgrade'
    shared_chat_prime_paid_upgrade = 'shared_chat_prime_paid_upgrade'
    shared_chat_pay_it_forward = 'shared_chat_pay_it_forward'
    shared_chat_raid = 'shared_chat_raid'
    shared_chat_announcement = 'shared_chat_announcement'
    cheer = 'cheer'
    twitch_shoutout = 'twitch_shoutout'

class TwitchModActionSubType(Enum):
    ban = 'ban'
    timeout = 'timeout'
    unban = 'unban'
    untimeout = 'untimeout'
    clear = 'clear'
    emoteonly = 'emoteonly'
    emoteonlyoff = 'emoteonlyoff'
    followers = 'followers'
    followersoff = 'followersoff'
    uniquechat = 'uniquechat'
    uniquechatoff = 'uniquechatoff'
    slow = 'slow'
    slowoff = 'slowoff'
    subscribers = 'subscribers'
    subscribersoff = 'subscribersoff'
    unraid = 'unraid'
    delete = 'delete'
    vip = 'vip'
    unvip = 'unvip'
    raid = 'raid'
    add_blocked_term = 'add_blocked_term'
    add_permitted_term = 'add_permitted_term'
    remove_blocked_term = 'remove_blocked_term'
    remove_permitted_term = 'remove_permitted_term'
    mod = 'mod'
    unmod = 'unmod'
    approve_unban_request = 'approve_unban_request'
    deny_unban_request = 'deny_unban_request'
    warn = 'warn'
    shield_mode_activated = 'shield_mode_activated'
    shield_mode_deactivated = 'shield_mode_deactivated'

class TwitchMessageSubType(Enum):
    text = 'text'
    custom_reward_redemption = 'custom_reward_redemption'
    channel_points_highlighted = 'channel_points_highlighted'
    channel_points_sub_only = 'channel_points_sub_only'
    user_intro = 'user_intro'
    power_ups_message_effect = 'power_ups_message_effect'
    power_ups_gigantified_emote = 'power_ups_gigantified_emote'
    first_message = 'first_message'
    returning_chatter = 'returning_chatter'

class Cheer(SynchraBaseModel):
    bits: int = Field(..., title='Bits')

class MessageType(Enum):
    text = 'text'
    custom_reward_redemption = 'custom_reward_redemption'
    channel_points_highlighted = 'channel_points_highlighted'
    channel_points_sub_only = 'channel_points_sub_only'
    user_intro = 'user_intro'
    power_ups_message_effect = 'power_ups_message_effect'
    power_ups_gigantified_emote = 'power_ups_gigantified_emote'
    first_message = 'first_message'
    returning_chatter = 'returning_chatter'

class TwitchBanRequest(SynchraBaseModel):
    provider_viewer_id: str = Field(..., title='Provider Viewer Id')
    duration_seconds: int | None = Field(None, title='Duration Seconds')
    reason: str | None = Field(None, title='Reason')

class TwitchEmulateChatMessageRequest(SynchraBaseModel):
    fragments: list[Fragment] = Field(..., title='Fragments')
    cheer: Cheer | None = None
    message_type: MessageType | None = Field('text', title='Message Type')
    source_provider_channel_id: str | None = Field(None, title='Source Provider Channel Id')
    source_provider_channel_name: str | None = Field(None, title='Source Provider Channel Name')

class TwitchAddVIPRequest(SynchraBaseModel):
    provider_viewer_id: str = Field(..., title='Provider Viewer Id')

class TwitchRaidRequest(SynchraBaseModel):
    to_provider_channel_id: str = Field(..., title='To Provider Channel Id')

class TwitchShoutoutRequest(SynchraBaseModel):
    to_provider_channel_id: str = Field(..., title='To Provider Channel Id')
