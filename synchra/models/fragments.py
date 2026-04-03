from __future__ import annotations
from enum import Enum
from typing import Any
from uuid import UUID
from pydantic import Field, AwareDatetime
from .base import SynchraBaseModel
from .common import CountCurrency

class MessagePartType(Enum):
    text = 'text'
    emote = 'emote'
    mention = 'mention'
    gift = 'gift'
    date = 'date'
    link = 'link'

class GiftedViewer(SynchraBaseModel):
    user_id: str = Field(..., title='User Id')
    username: str = Field(..., title='Username')
    display_name: str = Field(..., title='Display Name')

class Urls(SynchraBaseModel):
    url_1x: str = Field(..., alias='1x', title='1x')
    url_2x: str = Field(..., alias='2x', title='2x')
    url_4x: str = Field(..., alias='4x', title='4x')

class Gift(SynchraBaseModel):
    id: str = Field(..., title='Id')
    name: str = Field(..., title='Name')
    type: str = Field(..., title='Type')
    count: int = Field(..., title='Count')
    count_decimal_place: int | None = Field(0, title='Count Decimal Place')
    count_currency: CountCurrency | None = Field(None, title='Count Currency')
    animated: bool | None = Field(False, title='Animated')
    image_url: str | None = Field(None, title='Image Url')

class Emote(SynchraBaseModel):
    id: str = Field(..., title='Id')
    name: str = Field(..., title='Name')
    animated: bool = Field(..., title='Animated')
    emote_provider: str = Field(..., title='Emote Provider')
    urls: Urls | None = None

class Mention(SynchraBaseModel):
    user_id: str = Field(..., title='User Id')
    username: str = Field(..., title='Username')
    display_name: str = Field(..., title='Display Name')

class MessagePart(SynchraBaseModel):
    type: MessagePartType = Field(..., title='Type')
    text: str = Field(..., title='Text')
    gift: Gift | None = None
    emote: Emote | None = None
    mention: Mention | None = None
    date: AwareDatetime | None = Field(None, title='Date')
    url: str | None = Field(None, title='Url')

class ChatMessageBadge(SynchraBaseModel):
    id: str = Field(..., title='Id')
    type: str = Field(..., title='Type')
    name: str = Field(..., title='Name')

class NoticeMessagePart(SynchraBaseModel):
    type: MessagePartType = Field(..., title='Type')
    text: str = Field(..., title='Text')
    gift: Gift | None = None
    emote: Emote | None = None
    mention: Mention | None = None
    date: AwareDatetime | None = Field(None, title='Date')
    url: str | None = Field(None, title='Url')

class TaskParent(SynchraBaseModel):
    provider_message_id: str = Field(..., title='Provider Message Id')
    message: str = Field(..., title='Message')
    provider_viewer_id: str = Field(..., title='Provider Viewer Id')
    viewer_name: str = Field(..., title='Viewer Name')
    viewer_display_name: str = Field(..., title='Viewer Display Name')

class Log(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    task_id: UUID = Field(..., title='Task Id')
    created_at: AwareDatetime = Field(..., title='Created At')
    level: str = Field(..., title='Level')
    message: str = Field(..., title='Message')
    extra: dict[str, Any] | None = Field(None, title='Extra')

class PollChoice(SynchraBaseModel):
    id: str = Field(..., title='Id')
    title: str = Field(..., title='Title')
    votes: int | None = Field(0, title='Votes')

class ImageUrls(SynchraBaseModel):
    sm: str = Field(..., title='Sm')
    md: str = Field(..., title='Md')
    lg: str = Field(..., title='Lg')
