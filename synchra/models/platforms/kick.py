from enum import Enum
from pydantic import Field
from ..base import SynchraBaseModel

class KickActivityType(Enum):
    kick_sub = 'kick_sub'
    kick_resub = 'kick_resub'
    kick_gift_subs = 'kick_gift_subs'
    kick_gift_sub = 'kick_gift_sub'
    kick_follow = 'kick_follow'
    kick_kicks_gift = 'kick_kicks_gift'
    kick_reward_redemption = 'kick_reward_redemption'

class KickActivityName(Enum):
    kick_sub = 'kick_sub'
    kick_resub = 'kick_resub'
    kick_gift_subs = 'kick_gift_subs'
    kick_gift_sub = 'kick_gift_sub'
    kick_follow = 'kick_follow'
    kick_kicks_gift = 'kick_kicks_gift'
    kick_reward_redemption = 'kick_reward_redemption'

class KickActivitySubType(Enum):
    kick_sub = 'kick_sub'
    kick_resub = 'kick_resub'
    kick_gift_subs = 'kick_gift_subs'
    kick_gift_sub = 'kick_gift_sub'
    kick_kicks_gift = 'kick_kicks_gift'

class KickModActionSubType(Enum):
    kick_ban = 'kick_ban'
    kick_timeout = 'kick_timeout'

class KickMessageSubType(Enum):
    first_message = 'first_message'
    returning_chatter = 'returning_chatter'

class BodyBanUserApi2ChannelsChannelIdKickChannelProviderIdBanPost(SynchraBaseModel):
    provider_viewer_id: str = Field(..., title='Provider Viewer Id')
    duration_seconds: int | None = Field(None, title='Duration Seconds')
    reason: str | None = Field(None, title='Reason')

# Aliases for cleaner usage
KickBanUserRequest = BodyBanUserApi2ChannelsChannelIdKickChannelProviderIdBanPost
