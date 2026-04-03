from enum import Enum
from typing import Literal
from pydantic import RootModel

class TikTokActivityType(Enum):
    tiktok_gift = 'tiktok_gift'
    tiktok_follow = 'tiktok_follow'
    tiktok_share = 'tiktok_share'
    tiktok_like = 'tiktok_like'

class TikTokActivityName(Enum):
    tiktok_gift = 'tiktok_gift'
    tiktok_follow = 'tiktok_follow'
    tiktok_share = 'tiktok_share'
    tiktok_like = 'tiktok_like'

class TikTokActivitySubType(RootModel[Literal['tiktok_gift']]):
    root: Literal['tiktok_gift']
