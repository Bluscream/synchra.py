from enum import Enum
from pydantic import AwareDatetime, Field
from ..base import SynchraBaseModel

class YouTubeActivityType(Enum):
    new_sponsor_event = 'newSponsorEvent'
    super_chat_event = 'superChatEvent'
    super_sticker_event = 'superStickerEvent'
    membership_gifting_event = 'membershipGiftingEvent'
    member_milestone_chat_event = 'memberMilestoneChatEvent'

class YouTubeActivityName(Enum):
    new_sponsor_event = 'newSponsorEvent'
    super_chat_event = 'superChatEvent'
    super_sticker_event = 'superStickerEvent'
    membership_gifting_event = 'membershipGiftingEvent'
    member_milestone_chat_event = 'memberMilestoneChatEvent'

class YouTubeEventSubType(Enum):
    super_chat_event = 'superChatEvent'
    super_sticker_event = 'superStickerEvent'
    membership_gifting_event = 'membershipGiftingEvent'
    member_milestone_chat_event = 'memberMilestoneChatEvent'
    new_sponsor_event = 'newSponsorEvent'

class YouTubeActivitySubType(Enum):
    super_chat_event = 'superChatEvent'
    super_sticker_event = 'superStickerEvent'
    membership_gifting_event = 'membershipGiftingEvent'
    member_milestone_chat_event = 'memberMilestoneChatEvent'
    new_sponsor_event = 'newSponsorEvent'

class Snippet(SynchraBaseModel):
    """
    Basic broadcast details.
    """
    title: str = Field(
        ..., description="The broadcast's title (1-100 characters).", title='Title'
    )
    scheduled_start_time: AwareDatetime | None = Field(
        ...,
        alias='scheduledStartTime',
        description='The time the broadcast is scheduled to start (ISO 8601).',
        title='Scheduledstarttime',
    )
    description: str | None = Field(
        None,
        description="The broadcast's description (up to 5000 characters).",
        title='Description',
    )
    scheduled_end_time: AwareDatetime | None = Field(
        None,
        alias='scheduledEndTime',
        description='The time the broadcast is scheduled to end (ISO 8601).',
        title='Scheduledendtime',
    )

class YouTubeBroadcastStatus(SynchraBaseModel):
    """
    Privacy settings and made‑for‑kids flag.
    """
    privacy_status: str = Field(
        ...,
        alias='privacyStatus',
        description="Broadcast's privacy setting (private, public, or unlisted).",
        title='Privacystatus',
    )
    self_declared_made_for_kids: bool | None = Field(
        None,
        alias='selfDeclaredMadeForKids',
        description='Whether the broadcast is marked as made for kids.',
        title='Selfdeclaredmadeforkids',
    )

class MonitorStream(SynchraBaseModel):
    """
    Settings for the broadcast's monitor stream.
    """
    enable_monitor_stream: bool | None = Field(
        True,
        alias='enableMonitorStream',
        description='Whether to enable the monitor stream for the broadcast.',
        title='Enablemonitorstream',
    )
    broadcast_stream_delay_ms: int | None = Field(
        None,
        alias='broadcastStreamDelayMs',
        description='Delay in milliseconds for the monitor stream.',
        title='Broadcaststreamdelayms',
    )

class ContentDetails(SynchraBaseModel):
    """
    Additional settings that control broadcast behavior.
    """
    monitor_stream: MonitorStream | None = Field(
        None,
        alias='monitorStream',
        description="Settings for the broadcast's monitor stream.",
    )
    enable_auto_start: bool | None = Field(
        None,
        alias='enableAutoStart',
        description='Automatically start the broadcast when the stream goes live.',
        title='Enableautostart',
    )
    enable_auto_stop: bool | None = Field(
        None,
        alias='enableAutoStop',
        description='Automatically stop the broadcast when the stream ends.',
        title='Enableautostop',
    )
    enable_closed_captions: bool | None = Field(
        None,
        alias='enableClosedCaptions',
        description='Enable closed captions on the broadcast.',
        title='Enableclosedcaptions',
    )
    enable_dvr: bool | None = Field(
        None,
        alias='enableDvr',
        description='Enable DVR functionality.',
        title='Enabledvr',
    )
    enable_embed: bool | None = Field(
        None,
        alias='enableEmbed',
        description='Allow embedding of the broadcast on external sites.',
        title='Enableembed',
    )
    record_from_start: bool | None = Field(
        None,
        alias='recordFromStart',
        description='ActivityRecord the broadcast from its very start.',
        title='Recordfromstart',
    )

class LiveBroadcastInsert(SynchraBaseModel):
    """
    Request body for scheduling a new live broadcast via `liveBroadcasts.insert`.
    """
    snippet: Snippet = Field(
        ..., description='Basic broadcast details.', title='LiveBroadcastInsertSnippet'
    )
    status: YouTubeBroadcastStatus = Field(
        ...,
        description='Privacy settings and made‑for‑kids flag.',
        title='LiveBroadcastInsertStatus',
    )
    content_details: ContentDetails | None = Field(
        None,
        alias='contentDetails',
        description='Additional broadcast behavior settings.',
    )

class LiveBroadcastInsertContentDetails(SynchraBaseModel):
    """
    Additional settings that control broadcast behavior.
    """
    monitor_stream: MonitorStream | None = Field(
        None,
        alias='monitorStream',
        description="Settings for the broadcast's monitor stream.",
    )
    enable_auto_start: bool | None = Field(
        None,
        alias='enableAutoStart',
        description='Automatically start the broadcast when the stream goes live.',
        title='Enableautostart',
    )
    enable_auto_stop: bool | None = Field(
        None,
        alias='enableAutoStop',
        description='Automatically stop the broadcast when the stream ends.',
        title='Enableautostop',
    )
    enable_closed_captions: bool | None = Field(
        None,
        alias='enableClosedCaptions',
        description='Enable closed captions on the broadcast.',
        title='Enableclosedcaptions',
    )
    enable_dvr: bool | None = Field(
        None,
        alias='enableDvr',
        description='Enable DVR functionality.',
        title='Enabledvr',
    )
    enable_embed: bool | None = Field(
        None,
        alias='enableEmbed',
        description='Allow embedding of the broadcast on external sites.',
        title='Enableembed',
    )
    record_from_start: bool | None = Field(
        None,
        alias='recordFromStart',
        description='ActivityRecord the broadcast from its very start.',
        title='Recordfromstart',
    )

class LiveBroadcastInsertSnippet(SynchraBaseModel):
    """
    Basic details required to schedule a live broadcast.
    """
    title: str = Field(
        ..., description="The broadcast's title (1-100 characters).", title='Title'
    )
    scheduled_start_time: AwareDatetime | None = Field(
        ...,
        alias='scheduledStartTime',
        description='The time the broadcast is scheduled to start (ISO 8601).',
        title='Scheduledstarttime',
    )
    description: str | None = Field(
        None,
        description="The broadcast's description (up to 5000 characters).",
        title='Description',
    )
    scheduled_end_time: AwareDatetime | None = Field(
        None,
        alias='scheduledEndTime',
        description='The time the broadcast is scheduled to end (ISO 8601).',
        title='Scheduledendtime',
    )

class LiveBroadcastInsertStatus(SynchraBaseModel):
    """
    Privacy settings and made‑for‑kids flag for the broadcast.
    """
    privacy_status: str = Field(
        ...,
        alias='privacyStatus',
        description="Broadcast's privacy setting (private, public, or unlisted).",
        title='Privacystatus',
    )
    self_declared_made_for_kids: bool | None = Field(
        None,
        alias='selfDeclaredMadeForKids',
        description='Whether the broadcast is marked as made for kids.',
        title='Selfdeclaredmadeforkids',
    )
