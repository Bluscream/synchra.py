from __future__ import annotations
from enum import Enum
from typing import Any, Literal
from uuid import UUID
from pydantic import AwareDatetime, Field, RootModel
from .base import SynchraBaseModel
from .common import Provider, AccessLevel, AlertAction, ProviderList
from .fragments import MessagePart, GiftedViewer
from .platforms.twitch import TwitchCheerFragmentType, Cheermote, Cheer, MessageType, Fragment
from .platforms.youtube import YouTubeBroadcastStatus, ContentDetails, Snippet

# Request and Update Models
class ChannelCreate(SynchraBaseModel):
    display_name: str = Field(..., max_length=200, min_length=1, title='Display Name')
    show_on_landing_page: bool | None = Field(True, title='Show On Landing Page')

class ChannelUpdate(SynchraBaseModel):
    display_name: str | None = Field(None, max_length=200, min_length=1, title='Display Name')
    show_on_landing_page: bool | None = Field(None, title='Show On Landing Page')

class ActivityUpdate(SynchraBaseModel):
    gifted_viewers: list[GiftedViewer] | None = Field(None, title='Gifted Viewers')
    read: bool | None = Field(None, title='Read')
    count: int | None = Field(None, title='Count')

class BannedTermCreate(SynchraBaseModel):
    type: str = Field(..., title='Type') # phrase or regex
    text: str = Field(..., max_length=2000, min_length=1, title='Text')

class BannedTermUpdate(SynchraBaseModel):
    type: str | None = Field(None, title='Type')
    text: str | None = Field(None, title='Text')

class GiveawayCreate(SynchraBaseModel):
    title: str = Field(..., title='Title')
    entry_word: str = Field(..., title='Entry Word')
    providers: list[Provider | Literal['all']] = Field(..., title='Provider')

class GiveawayUpdate(SynchraBaseModel):
    title: str | None = Field(None, title='Title')
    entry_word: str | None = Field(None, title='Entry Word')
    providers: list[Provider | Literal['all']] | None = Field(None, title='Provider')
    active: bool | None = Field(None, title='Active')

class TimerCreate(SynchraBaseModel):
    name: str = Field(..., max_length=255, min_length=1, title='Name')
    messages: list[str] = Field(..., max_length=100, min_length=1, title='TimerMessageList')
    interval: int | None = Field(30, description='Minutes', ge=1, title='TimerInterval')
    enabled: bool | None = Field(True, title='Enabled')
    providers: ProviderList | None = Field(['all'], title='Provider')
    pick_mode: str | None = Field('order', title='Pick Mode')
    active_mode: str | None = Field('always', title='Active Mode')

class TimerUpdate(SynchraBaseModel):
    name: str | None = Field(None, title='Name')
    messages: list[str] | None = Field(None, title='TimerMessageList')
    interval: int | None = Field(None, title='TimerInterval')
    enabled: bool | None = Field(None, title='Enabled')
    providers: ProviderList | None = Field(None, title='Provider')
    pick_mode: str | None = Field(None, title='Pick Mode')
    active_mode: str | None = Field(None, title='Active Mode')

class QueueCreate(SynchraBaseModel):
    name: str = Field(..., max_length=255, min_length=1, title='Name')

class QueueUpdate(SynchraBaseModel):
    name: str | None = Field(None, title='Name')

class QueueViewerCreate(SynchraBaseModel):
    provider: Provider = Field(..., title='Provider')
    provider_viewer_id: str = Field(..., title='Provider Viewer Id')
    display_name: str = Field(..., title='Display Name')

# Settings Models
class ChannelPointSettingsUpdate(SynchraBaseModel):
    enabled: bool | None = Field(True, title='Enabled')
    points_name: str | None = Field('points', max_length=45, min_length=1, title='Points Name')
    points_per_min: int | None = Field(10, ge=0, le=65535, title='Points Per Min')
    points_per_min_sub_multiplier: int | None = Field(2, ge=0, le=255, title='Points Per Min Sub Multiplier')
    points_per_sub: int | None = Field(1000, ge=0, le=65535, title='Points Per Sub')
    points_per_cheer: int | None = Field(2, ge=0, le=65535, title='Points Per Cheer')
    ignore_users: list[str] | None = Field([], title='Ignore Users')

class RouletteSettingsUpdate(SynchraBaseModel):
    win_chance: int | None = Field(45, ge=0, le=100, title='Win Chance')
    win_message: str | None = Field(None, title='Win Message')
    lose_message: str | None = Field(None, title='Lose Message')
    allin_win_message: str | None = Field(None, title='Allin Win Message')
    allin_lose_message: str | None = Field(None, title='Allin Lose Message')
    min_bet: int | None = Field(5, ge=0, title='Min Bet')
    max_bet: int | None = Field(0, ge=0, title='Max Bet')

class SlotsSettingsUpdate(SynchraBaseModel):
    emotes: list[str] | None = Field(None, title='Emotes')
    emote_pool_size: int | None = Field(3, ge=1, le=255, title='Emote Pool Size')
    payout_percent: int | None = Field(95, ge=0, le=100, title='Payout Percent')
    min_bet: int | None = Field(5, ge=1, title='Min Bet')
    max_bet: int | None = Field(0, ge=0, title='Max Bet')
    win_message: str | None = Field(None, title='Win Message')
    lose_message: str | None = Field(None, title='Lose Message')


class UserSendMessageCreate(SynchraBaseModel):
    user_provider_id: UUID = Field(..., title='User Provider Id')
    channel_provider_id: UUID = Field(..., title='ChannelRecord Provider Id')
    message: str = Field(..., title='Message')
    reply_provider_message_id: str | None = Field(None, title='Reply Provider Message Id')

class ChatMessageCreate(SynchraBaseModel):
    id: UUID | None = Field(None, title='Id')
    type: str = Field(..., title='Type')
    sub_type: str | None = Field(None, title='Sub Type')
    created_at: AwareDatetime | None = Field(None, title='Created At')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    provider: Provider = Field(..., title='Provider')
    provider_channel_id: str = Field(..., title='Provider ChannelRecord Id')
    provider_message_id: str = Field(..., title='Provider Message Id')
    provider_viewer_id: str = Field(..., title='Provider Viewer Id')
    viewer_name: str = Field(..., title='Viewer Name')
    viewer_display_name: str = Field(..., title='Viewer Display Name')
    viewer_color: str | None = Field(None, title='Viewer Color')
    message_parts: list[MessagePart] | None = Field(None, title='Message Parts')

class ChatWidgetCreate(SynchraBaseModel):
    name: str = Field(..., max_length=255, min_length=1, title='Name')
    type: Literal['chat_widget'] = Field('chat_widget', title='Type')
    settings: dict[str, Any] | None = Field(None, title='ChatWidgetSettings')

class ChatWidgetUpdate(SynchraBaseModel):
    name: str | None = Field(None, title='Name')
    settings: dict[str, Any] | None = Field(None, title='ChatWidgetSettings')

class CommandCreate(SynchraBaseModel):
    cmds: list[str] | None = Field(default_factory=list, title='Cmds')
    patterns: list[str] | None = Field(default_factory=list, title='Patterns')
    response: str = Field(..., title='Response')
    group_name: str | None = Field('', title='Group Name')
    active_mode: str | None = Field('always', title='Active Mode')
    enabled: bool | None = Field(True, title='Enabled')
    access_level: AccessLevel | None = Field(AccessLevel.GUEST, title='AccessLevel')
    providers: list[Literal['all'] | Provider] | None = Field(['all'], title='Provider')

class CommandUpdate(SynchraBaseModel):
    cmds: list[str] | None = Field(None, title='Cmds')
    patterns: list[str] | None = Field(None, title='Patterns')
    response: str | None = Field(None, title='Response')
    group_name: str | None = Field(None, title='Group Name')
    active_mode: str | None = Field(None, title='Active Mode')
    enabled: bool | None = Field(None, title='Enabled')
    access_level: AccessLevel | None = None
    providers: list[Literal['all'] | Provider] | None = Field(None, title='Provider')

class CommandTemplateCreate(SynchraBaseModel):
    title: str = Field(..., title='Title')
    description: str | None = Field(None, title='Description')
    commands: list[dict[str, Any]] = Field(..., title='Commands')

class CommandTemplateUpdate(SynchraBaseModel):
    title: str | None = Field(None, title='Title')
    description: str | None = Field(None, title='Description')
    commands: list[dict[str, Any]] | None = Field(None, title='Commands')

class TimerCreate(SynchraBaseModel):
    name: str = Field(..., max_length=255, min_length=1, title='Name')
    messages: list[str] = Field(..., max_length=100, min_length=1, title='Messages')
    interval: int | None = Field(30, description='Minutes', ge=1, title='Interval')
    enabled: bool | None = Field(True, title='Enabled')
    providers: list[Literal['all'] | Provider] | None = Field(['all'], title='Provider')
    pick_mode: str | None = Field('order', title='Pick Mode')
    active_mode: str | None = Field('always', title='Active Mode')
    active_from_date: AwareDatetime | None = Field(None, title='Active From Date')
    active_to_date: AwareDatetime | None = Field(None, title='Active To Date')
    active_title_patterns: list[str] | None = Field(default_factory=list, title='Active Title Patterns')
    active_categories: list[str] | None = Field(default_factory=list, title='Active Categories')
    active_chat_messages: int | None = Field(None, title='Active Chat Messages')

class TimerUpdate(SynchraBaseModel):
    name: str | None = Field(None, title='Name')
    messages: list[str] | None = Field(None, title='Messages')
    interval: int | None = Field(None, title='Interval')
    enabled: bool | None = Field(None, title='Enabled')
    providers: list[Literal['all'] | Provider] | None = Field(None, title='Provider')
    pick_mode: str | None = Field(None, title='Pick Mode')
    active_mode: str | None = Field(None, title='Active Mode')
    active_from_date: AwareDatetime | None = Field(None, title='Active From Date')
    active_to_date: AwareDatetime | None = Field(None, title='Active To Date')
    active_title_patterns: list[str] | None = Field(None, title='Active Title Patterns')
    active_categories: list[str] | None = Field(None, title='Active Categories')
    active_chat_messages: int | None = Field(None, title='Active Chat Messages')

class UserSettings(SynchraBaseModel):
    activity_feed_not_types: list[str] | None = Field(None, title='Activity Feed Not Types')
    activity_feed_type_min_count: dict[str, int] | None = Field(None, title='Activity Feed Type Min Count')
    activity_feed_read_indicator: bool | None = Field(False, title='Activity Feed Read Indicator')
    view_count: bool | None = Field(True, title='View Count')

class UserPublic(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    username: str = Field(..., title='Username')
    display_name: str = Field(..., title='Display Name')
    default_channel_id: UUID | None = Field(None, title='Default Channel Id')

class UserProviderPublic(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    provider: Provider = Field(..., title='Provider')
    provider_channel_id: str = Field(..., title='Provider Channel Id')
    display_name: str | None = Field(..., title='Display Name')
    scope: str | None = Field(..., title='Scope')
    chat_scope_needed: bool = Field(..., title='Chat Scope Needed')

class HealthResponse(SynchraBaseModel):
    status: str = Field('OK', title='Status')
    version: str = Field(..., title='Version')

class OAuthCallbackResponse(SynchraBaseModel):
    mode: str = Field(..., title='Mode')
    redirect_to: str | None = Field(None, title='Redirect To')
    access_token: str | None = Field(None, title='Access Token')

class ChannelUserInviteCreate(SynchraBaseModel):
    access_level: AccessLevel = Field(..., title='AccessLevel')
    expires_at: AwareDatetime | None = Field(None, title='Expires At')

class TaskError(SynchraBaseModel):
    field: str | list[str | int] = Field(..., title='Field')
    message: str = Field(..., title='Message')
    type: str = Field(..., title='Type')
    input: Any | None = Field(None, title='Input')

class Error(SynchraBaseModel):
    code: int = Field(..., title='Code')
    message: str = Field(..., title='Message')
    type: str = Field(..., title='Type')
    errors: list[TaskError] = Field(default_factory=list, title='Errors')

class BroadcastError(SynchraBaseModel):
    platform: str = Field(..., title='Platform')
    error: str = Field(..., title='Error')

class BroadcastResponse(SynchraBaseModel):
    success: int = Field(..., title='Success')
    failed: int = Field(..., title='Failed')
    errors: list[BroadcastError] = Field(default_factory=list, title='Errors')
