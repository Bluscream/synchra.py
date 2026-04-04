from __future__ import annotations
from enum import Enum
from typing import Any, Literal
from uuid import UUID
from pydantic import AwareDatetime, Field, RootModel
from .base import SynchraBaseModel
from .common import Provider, AccessLevel, Feature, Subscription
from .fragments import MessagePart, ChatMessageBadge, NoticeMessagePart, TaskParent, GiftedViewer

# Subtypes and Enums
class ChatMessageRecordType(Enum):
    message = 'message'
    activity = 'activity'
    status = 'status'
    error = 'error'
    command = 'command'
    task = 'task'
    system = 'system'

class GenericSubType(RootModel[str]):
    root: str = Field(..., title='Sub Type')

class ActivitySubType(Enum):
    bits = 'bits'
    kicks = 'kicks'
    diamond = 'diamond'
    currency = 'currency'

class ChatEventType(Enum):
    poll = 'poll'
    progress = 'progress'
    countdown = 'countdown'
    notice = 'notice'

class ChatEventStatus(Enum):
    open = 'open'
    locked = 'locked'
    completed = 'completed'
    terminated = 'terminated'
    archived = 'archived'
    unknown = 'unknown'

class TaskStatus(Enum):
    running = 'RUNNING'
    finished = 'FINISHED'
    failed = 'FAILED'
    cancelled = 'CANCELLED'

# Core Entities
class BotProvider(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    provider: Provider = Field(..., title='Provider')
    provider_channel_id: str | None = Field(..., title='Provider ChannelRecord Id')
    scope: str | None = Field(..., title='Scope')
    name: str | None = Field(..., title='Name')
    scope_needed: bool = Field(..., title='Scope Needed')

class ChannelProvider(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    provider: Provider = Field(..., title='Provider')
    provider_channel_id: str | None = Field(..., title='Provider ChannelRecord Id')
    provider_channel_name: str | None = Field(..., title='Provider ChannelRecord Name')
    provider_channel_display_name: str | None = Field(
        ..., title='Provider ChannelRecord Display Name'
    )
    scope: str | None = Field(..., title='Scope')
    stream_title: str | None = Field(..., title='Stream Title')
    stream_category: str | None = Field(..., title='Stream Category')
    stream_tags: list[str] = Field(..., title='Stream Tags')
    live_stream_id: str | None = Field(..., title='Live Stream Id')
    stream_live: bool | None = Field(False, title='Stream Live')
    stream_live_at: AwareDatetime | None = Field(None, title='Stream Live At')
    stream_chat_id: str | None = Field(None, title='Stream Chat Id')
    stream_viewer_count: int | None = Field(None, title='Stream Viewer Count')
    channel_provider_stream_id: UUID | None = Field(
        ..., title='ChannelRecord Provider Stream Id'
    )
    state: dict[str, Any] | None = Field(..., title='State')
    bot_provider: BotProvider | None = None
    scope_needed: bool = Field(..., title='Scope Needed')

class ChannelRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    display_name: str = Field(..., title='Display Name')
    created_at: AwareDatetime = Field(..., title='Created At')
    subscription: Subscription | None = None
    show_on_landing_page: bool | None = Field(False, title='Show On Landing Page')
    user_access_level: AccessLevel | None = None
    channel_providers: list[ChannelProvider] | None = Field(
        None, title='ChannelRecord Provider'
    )
    features: list[Feature] = Field(..., title='Features')

class ActivityRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    provider: Provider = Field(..., title='Provider')
    provider_message_id: str = Field(..., title='Provider Message Id')
    provider_channel_id: str = Field(..., title='Provider ChannelRecord Id')
    provider_viewer_id: str = Field(..., title='Provider Viewer Id')
    viewer_name: str = Field(..., title='Viewer Name')
    viewer_display_name: str = Field(..., title='Viewer Display Name')
    type: Any = Field(..., title='Type') # Specific types imported in __init__ or requests
    sub_type: ActivitySubType | str = Field(..., title='Sub Type')
    count: int = Field(..., title='Count')
    count_decimal_place: int = Field(..., title='Count Decimal Place')
    count_currency: str | None = Field(..., title='Count Currency')
    created_at: AwareDatetime = Field(..., title='Created At')
    gifted_viewers: list[GiftedViewer] | None = Field(None, title='Gifted Viewers')
    system_message: str = Field(..., title='System Message')
    message: str | None = Field(None, title='Message')
    message_parts: list[MessagePart] | None = Field(None, title='Message Parts')
    read: bool = Field(..., title='Read')
    color: str = Field(..., title='Color')
    font_color: str | None = Field(..., title='Font Color')
    count_name: str = Field(..., title='Count Name')
    type_display_name: str = Field(..., title='Type Display Name')
    sub_type_display_name: str = Field(..., title='Sub Type Display Name')

class ChatMessageRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    type: ChatMessageRecordType = Field(..., title='Type')
    sub_type: GenericSubType | None = Field(None, title='Sub Type')
    created_at: AwareDatetime = Field(..., title='Created At')
    updated_at: AwareDatetime | None = Field(None, title='Updated At')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    provider: Provider = Field(..., title='Provider')
    provider_channel_id: str = Field(..., title='Provider ChannelRecord Id')
    provider_message_id: str = Field(..., title='Provider Message Id')
    provider_viewer_id: str = Field(..., title='Provider Viewer Id')
    viewer_name: str = Field(..., title='Viewer Name')
    viewer_display_name: str = Field(..., title='Viewer Display Name')
    viewer_color: str | None = Field(None, title='Viewer Color')
    message_parts: list[MessagePart] | None = Field(
        default_factory=list, title='Message Parts'
    )
    badges: list[ChatMessageBadge] | None = Field(default_factory=list, title='Badges')
    notice_message_parts: list[NoticeMessagePart] | None = Field(
        default_factory=list, title='Notice Message Parts'
    )
    source_provider_channel_id: str | None = Field(
        None, title='Source Provider ChannelRecord Id'
    )
    source_provider_channel_name: str | None = Field(
        None, title='Source Provider ChannelRecord Name'
    )
    source_provider_channel_display_name: str | None = Field(
        None, title='Source Provider ChannelRecord Display Name'
    )
    deleted_at: AwareDatetime | None = Field(None, title='Deleted At')
    deleted_by_provider_viewer_id: str | None = Field(
        None, title='Deleted By Provider Viewer Id'
    )
    deleted_by_name: str | None = Field(None, title='Deleted By Name')
    deleted_by_display_name: str | None = Field(None, title='Deleted By Display Name')
    parent_provider_thread_id: str | None = Field(
        None, title='Parent Provider Thread Id'
    )
    parent: TaskParent | None = None

class ChannelPointSettings(SynchraBaseModel):
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    enabled: bool | None = Field(False, title='Enabled')
    points_name: str | None = Field('points', title='Points Name')
    points_per_min: int | None = Field(10, title='Points Per Min')
    points_per_min_sub_multiplier: int | None = Field(
        2, title='Points Per Min Sub Multiplier'
    )
    points_per_sub: int | None = Field(1000, title='Points Per Sub')
    points_per_cheer: int | None = Field(2, title='Points Per Cheer')
    ignore_users: list[str] | None = Field([], title='Ignore Users')

class ChannelQuote(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    number: int = Field(..., title='Number')
    message: str = Field(..., title='Message')
    provider: Provider = Field(..., title='Provider')
    created_by_provider_viewer_id: str = Field(
        ..., title='Created By Provider Viewer Id'
    )
    created_by_display_name: str = Field(..., title='Created By Display Name')
    created_at: AwareDatetime = Field(..., title='Created At')
    updated_at: AwareDatetime | None = Field(None, title='Updated At')

class ChannelStream(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    started_at: AwareDatetime = Field(..., title='Started At')
    duration_seconds: int | None = Field(None, title='Duration Seconds')
    providers: list[Provider] | None = Field([], title='Provider')
    avg_viewer_count: int | None = Field(None, title='Avg Viewer Count')

class ChannelProviderStream(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    channel_stream_id: UUID = Field(..., title='ChannelRecord Stream Id')
    provider: Provider = Field(..., title='Provider')
    provider_channel_id: str = Field(..., title='Provider ChannelRecord Id')
    provider_stream_id: str = Field(..., title='Provider Stream Id')
    started_at: AwareDatetime = Field(..., title='Started At')
    ended_at: AwareDatetime | None = Field(..., title='Ended At')
    avg_viewer_count: int | None = Field(..., title='Avg Viewer Count')
    peak_viewer_count: int | None = Field(..., title='Peak Viewer Count')
    viewer_watched_minutes: int | None = Field(..., title='Viewer Watched Minutes')
    chat_message_count: int | None = Field(..., title='Chat Message Count')

# Pagination Records
class PageCursorActivity(SynchraBaseModel):
    records: list[ActivityRecord] = Field(..., title='Records')
    lookup_data: dict[str, dict[str, Any]] | None = Field(None, title='Lookup Data')
    cursor: str | None = Field(None, title='Cursor')
    total: int | None = Field(None, title='Total')

class PageCursorChannel(SynchraBaseModel):
    records: list[ChannelRecord] = Field(..., title='Records')
    lookup_data: dict[str, dict[str, Any]] | None = Field(None, title='Lookup Data')
    cursor: str | None = Field(None, title='Cursor')
    total: int | None = Field(None, title='Total')

class PageCursorChatMessage(SynchraBaseModel):
    records: list[ChatMessageRecord] = Field(..., title='Records')
    lookup_data: dict[str, dict[str, Any]] | None = Field(None, title='Lookup Data')
    cursor: str | None = Field(None, title='Cursor')
    total: int | None = Field(None, title='Total')

class BannedTermRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    chat_filter_id: UUID = Field(..., title='Chat Filter Id')
    type: Any = Field(..., title='Type')
    text: str = Field(..., title='Text')

class PageCursorBannedTerm(SynchraBaseModel):
    records: list[BannedTermRecord] = Field(..., title='Records')
    lookup_data: dict[str, dict[str, Any]] | None = Field(None, title='Lookup Data')
    cursor: str | None = Field(None, title='Cursor')
    total: int | None = Field(None, title='Total')

class QuoteRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    number: int = Field(..., title='Number')
    message: str = Field(..., title='Message')
    provider: Provider = Field(..., title='Provider')
    created_by_provider_viewer_id: str = Field(..., title='Created By Provider Viewer Id')
    created_by_display_name: str = Field(..., title='Created By Display Name')
    created_at: AwareDatetime = Field(..., title='Created At')
    updated_at: AwareDatetime | None = Field(None, title='Updated At')

class PageCursorChannelQuote(SynchraBaseModel):
    records: list[QuoteRecord] = Field(..., title='Records')
    lookup_data: dict[str, dict[str, Any]] | None = Field(None, title='Lookup Data')
    cursor: str | None = Field(None, title='Cursor')
    total: int | None = Field(None, title='Total')

class StreamRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    started_at: AwareDatetime = Field(..., title='Started At')
    duration_seconds: int | None = Field(None, title='Duration Seconds')
    providers: list[Provider] | None = Field([], title='Provider')
    avg_viewer_count: int | None = Field(None, title='Avg Viewer Count')
    peak_viewer_count: int | None = Field(None, title='Peak Viewer Count')
    viewer_watched_minutes: int | None = Field(None, title='Viewer Watched Minutes')
    chat_message_count: int | None = Field(None, title='Chat Message Count')
    unique_chatter_count: int | None = Field(None, title='Unique Chatter Count')
    chat_viewer_ratio: str | None = Field(..., title='Chat Viewer Ratio')

class PageCursorChannelStream(SynchraBaseModel):
    records: list[StreamRecord] = Field(..., title='Records')
    lookup_data: dict[str, dict[str, Any]] | None = Field(None, title='Lookup Data')
    cursor: str | None = Field(None, title='Cursor')
    total: int | None = Field(None, title='Total')

class TimerRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    created_at: AwareDatetime = Field(..., title='Created At')
    updated_at: AwareDatetime = Field(..., title='Updated At')
    name: str = Field(..., title='Name')
    messages: list[str] = Field(..., title='TimerMessageList')
    interval: int = Field(..., description='Minutes', title='TimerInterval')
    enabled: bool = Field(..., title='Enabled')
    next_run_at: AwareDatetime = Field(..., title='Next Run At')
    providers: list[Literal['all'] | Provider] = Field(..., title='Provider')
    pick_mode: Any = Field(..., title='Pick Mode')
    active_mode: Any = Field(..., title='Active Mode')
    last_message_index: int | None = Field(..., title='Last Message Index')
    active_from_date: AwareDatetime | None = Field(..., title='Active From Date')
    active_to_date: AwareDatetime | None = Field(..., title='Active To Date')
    active_title_patterns: list[str] | None = Field(None, title='Active Title Patterns')
    active_categories: list[str] | None = Field(None, title='Active Categories')
    active_chat_messages: int | None = Field(None, title='Active Chat TimerMessageList')

class PageCursorTimer(SynchraBaseModel):
    records: list[TimerRecord] = Field(..., title='Records')
    lookup_data: dict[str, dict[str, Any]] | None = Field(None, title='Lookup Data')
    cursor: str | None = Field(None, title='Cursor')
    total: int | None = Field(None, title='Total')

class TaskRecord(SynchraBaseModel):
    path: str = Field(..., title='Path')
    id: UUID = Field(..., title='Id')
    work_id: UUID = Field(..., title='Work Id')
    created_at: AwareDatetime = Field(..., title='Created At')
    finished_at: AwareDatetime | None = Field(None, title='Finished At')
    started_at: AwareDatetime | None = Field(..., title='Started At')
    last_heartbeat_at: AwareDatetime | None = Field(..., title='Last Heartbeat At')
    timeout_seconds: int | None = Field(..., title='Timeout Seconds')
    tries: int = Field(..., title='Tries')
    max_tries: int = Field(..., title='Max Tries')
    status: TaskStatus = Field(..., title='TaskStatus')
    request_data: dict[str, Any] | None = Field(..., title='Request Data')
    response_data: dict[str, Any] | None = Field(..., title='Response Data')
    error: str | None = Field(..., title='Error')
    worker: str = Field(..., title='Worker')
    unique: bool = Field(..., title='Unique')

class PageCursorTask(SynchraBaseModel):
    records: list[TaskRecord] = Field(..., title='Records')
    lookup_data: dict[str, dict[str, Any]] | None = Field(None, title='Lookup Data')
    cursor: str | None = Field(None, title='Cursor')
    total: int | None = Field(None, title='Total')

class ChatWidget(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    name: str = Field(..., title='Name')
    created_at: AwareDatetime = Field(..., title='Created At')
    updated_at: AwareDatetime = Field(..., title='Updated At')
    type: Literal['chat_widget'] = Field('chat_widget', title='Type')
    settings: dict[str, Any] = Field(..., title='ChatWidgetSettings')

class Command(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    cmds: list[str] = Field(..., title='Cmds')
    patterns: list[str] = Field(..., title='Patterns')
    response: str = Field(..., title='Response')
    group_name: str = Field(..., title='Group Name')
    global_cooldown: int = Field(..., title='Global Cooldown')
    chatter_cooldown: int = Field(..., title='Chatter Cooldown')
    mod_cooldown: int = Field(..., title='Mod Cooldown')
    active_mode: str = Field(..., title='Active Mode')
    enabled: bool = Field(..., title='Enabled')
    public: bool = Field(..., title='Public')
    access_level: int = Field(..., title='Access Level')
    providers: list[Literal['all'] | Provider] = Field(..., title='Provider')
    created_at: AwareDatetime = Field(..., title='Created At')
    updated_at: AwareDatetime | None = Field(None, title='Updated At')

class CommandTemplate(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    title: str = Field(..., title='Title')
    description: str | None = Field(..., title='Description')
    commands: list[dict[str, Any]] = Field(..., title='Commands')
    created_at: AwareDatetime = Field(..., title='Created At')
    updated_at: AwareDatetime | None = Field(None, title='Updated At')

class Giveaway(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    created_at: AwareDatetime = Field(..., title='Created At')
    updated_at: AwareDatetime = Field(..., title='Updated At')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    title: str = Field(..., title='Title')
    chat_command_id: UUID | None = Field(..., title='Chat Command Id')
    entry_word: str = Field(..., title='Entry Word')
    providers: list[Provider | Literal['all']] = Field(..., title='Provider')
    active: bool = Field(..., title='Active')
    winner_provider: str | None = Field(..., title='Winner Provider')
    winner_provider_viewer_id: str | None = Field(..., title='Winner Provider Viewer Id')
    winner_name: str | None = Field(..., title='Winner Name')
    winner_display_name: str | None = Field(..., title='Winner Display Name')

class GiveawayEntry(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    created_at: AwareDatetime = Field(..., title='Created At')
    channel_giveaway_id: UUID = Field(..., title='ChannelRecord Giveaway Id')
    provider: Provider = Field(..., title='Provider')
    provider_viewer_id: str = Field(..., title='Provider Viewer Id')
    name: str = Field(..., title='Name')
    display_name: str = Field(..., title='Display Name')

class User(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    username: str = Field(..., title='Username')
    email: str | None = Field(None, title='Email')
    display_name: str = Field(..., title='Display Name')
    created_at: AwareDatetime | None = Field(None, title='Created At')
    updated_at: AwareDatetime | None = Field(None, title='Updated At')
    is_active: bool | None = Field(True, title='Is Active')
    default_channel_id: UUID | None = Field(None, title='Default ChannelRecord Id')

class UserAccessLevel(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    user_id: UUID = Field(..., title='User Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    access_level: AccessLevel = Field(..., title='AccessLevel')

class ChatEventRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    provider: Provider = Field(..., title='Provider')
    provider_channel_id: str = Field(..., title='Provider ChannelRecord Id')
    provider_event_id: str = Field(..., title='Provider Event Id')
    name: str = Field(..., title='Name')
    type: ChatEventType = Field(..., title='Type')
    subtype: str | None = Field(None, title='Subtype')
    status: ChatEventStatus = Field(..., title='Status')
    poll_choices: list[PollChoice] | None = Field(None, title='Poll Choices')
    progress_percent: int | None = Field(None, title='Progress Percent')
    created_at: AwareDatetime = Field(..., title='Created At')
    updated_at: AwareDatetime = Field(..., title='Updated At')
    expires_at: AwareDatetime | None = Field(None, title='Expires At')
    expired: bool | None = Field(False, title='Expired')
    locks_at: AwareDatetime | None = Field(None, title='Locks At')

class QueueRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    name: str = Field(..., title='Name')
    created_at: AwareDatetime = Field(..., title='Created At')

class QueueViewerRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_queue_id: UUID = Field(..., title='ChannelRecord Queue Id')
    position: int = Field(..., title='Position')
    provider: Provider = Field(..., title='Provider')
    provider_viewer_id: str = Field(..., title='Provider Viewer Id')
    display_name: str = Field(..., title='Display Name')
    created_at: AwareDatetime = Field(..., title='Created At')

class StreamCategoryRecord(SynchraBaseModel):
    id: str | None = Field(None, title='Id')
    name: str = Field(..., title='Name')
    thumbnail_url: str | None = Field(None, title='Thumbnail Url')

class PublicBotProviderRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    provider: Provider = Field(..., title='Provider')
    provider_channel_id: str | None = Field(..., title='Provider ChannelRecord Id')
    scope: str | None = Field(..., title='Scope')
    name: str | None = Field(..., title='Name')
    scope_needed: bool = Field(..., title='Scope Needed')

class ChannelUserAccessRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    user: User = Field(..., title='User')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    access_level: AccessLevel = Field(..., title='AccessLevel')

class ChannelUserInviteRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    access_level: AccessLevel = Field(..., title='AccessLevel')
    created_at: AwareDatetime = Field(..., title='Created At')
    expires_at: AwareDatetime = Field(..., title='Expires At')
    is_expired: bool = Field(..., title='Is Expired')
    invite_link: str = Field(..., title='Invite Link')

class ChannelProvider(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    provider: Provider = Field(..., title='Provider')
    provider_channel_id: str | None = Field(None, title='Provider Channel Id')
    provider_channel_name: str | None = Field(None, title='Provider Channel Name')
    provider_channel_display_name: str | None = Field(None, title='Provider Channel Display Name')
    scope: str | None = Field(None, title='Scope')
    stream_title: str | None = Field(None, title='Stream Title')
    stream_category: str | None = Field(None, title='Stream Category')
    stream_tags: list[str] = Field(default_factory=list, title='Stream Tags')
    live_stream_id: str | None = Field(None, title='Live Stream Id')
    stream_live: bool | None = Field(False, title='Stream Live')

class ChannelProviderPublic(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    provider: Provider = Field(..., title='Provider')
    provider_channel_id: str = Field(..., title='Provider Channel Id')
    provider_channel_name: str | None = Field(None, title='Provider Channel Name')
    provider_channel_display_name: str | None = Field(None, title='Provider Channel Display Name')

class ChannelProviderStreamRecord(SynchraBaseModel):
    id: UUID = Field(..., title='Id')
    channel_id: UUID = Field(..., title='ChannelRecord Id')
    channel_stream_id: UUID = Field(..., title='ChannelRecord Stream Id')
    provider: Provider = Field(..., title='Provider')
    provider_channel_id: str = Field(..., title='Provider Channel Id')
    provider_stream_id: str = Field(..., title='Provider Stream Id')
    started_at: AwareDatetime = Field(..., title='Started At')
    ended_at: AwareDatetime | None = Field(None, title='Ended At')
    avg_viewer_count: int | None = Field(None, title='Avg Viewer Count')
    peak_viewer_count: int | None = Field(None, title='Peak Viewer Count')
    viewer_watched_minutes: int | None = Field(None, title='Viewer Watched Minutes')
    chat_message_count: int | None = Field(None, title='Chat Message Count')

class ViewerWatchtime(SynchraBaseModel):
    channel_provider_stream_id: UUID = Field(..., title='ChannelRecord Provider Stream Id')
    provider_viewer_id: str = Field(..., title='Provider Viewer Id')
    watchtime: int = Field(..., title='Watchtime')

class ViewerStreamRecord(SynchraBaseModel):
    channel_provider_stream: ChannelProviderStreamRecord = Field(..., title='ChannelProviderStream')
    viewer_watchtime: ViewerWatchtime = Field(..., title='StreamViewerWatchtime')
