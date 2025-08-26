from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_user_response_data_type_0 import MessageUserResponseDataType0
    from ..models.message_user_response_meta_type_0 import MessageUserResponseMetaType0
    from ..models.reactions import Reactions
    from ..models.user_name_response import UserNameResponse


T = TypeVar("T", bound="MessageUserResponse")


@_attrs_define
class MessageUserResponse:
    """
    Attributes:
        id (str):
        user_id (str):
        content (str):
        created_at (int):
        updated_at (int):
        latest_reply_at (Union[None, int]):
        reply_count (int):
        reactions (list['Reactions']):
        user (UserNameResponse):
        channel_id (Union[None, Unset, str]):
        parent_id (Union[None, Unset, str]):
        data (Union['MessageUserResponseDataType0', None, Unset]):
        meta (Union['MessageUserResponseMetaType0', None, Unset]):
    """

    id: str
    user_id: str
    content: str
    created_at: int
    updated_at: int
    latest_reply_at: Union[None, int]
    reply_count: int
    reactions: list["Reactions"]
    user: "UserNameResponse"
    channel_id: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    data: Union["MessageUserResponseDataType0", None, Unset] = UNSET
    meta: Union["MessageUserResponseMetaType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.message_user_response_data_type_0 import MessageUserResponseDataType0
        from ..models.message_user_response_meta_type_0 import MessageUserResponseMetaType0

        id = self.id

        user_id = self.user_id

        content = self.content

        created_at = self.created_at

        updated_at = self.updated_at

        latest_reply_at: Union[None, int]
        latest_reply_at = self.latest_reply_at

        reply_count = self.reply_count

        reactions = []
        for reactions_item_data in self.reactions:
            reactions_item = reactions_item_data.to_dict()
            reactions.append(reactions_item)

        user = self.user.to_dict()

        channel_id: Union[None, Unset, str]
        if isinstance(self.channel_id, Unset):
            channel_id = UNSET
        else:
            channel_id = self.channel_id

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, MessageUserResponseDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, MessageUserResponseMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "content": content,
                "created_at": created_at,
                "updated_at": updated_at,
                "latest_reply_at": latest_reply_at,
                "reply_count": reply_count,
                "reactions": reactions,
                "user": user,
            }
        )
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_user_response_data_type_0 import MessageUserResponseDataType0
        from ..models.message_user_response_meta_type_0 import MessageUserResponseMetaType0
        from ..models.reactions import Reactions
        from ..models.user_name_response import UserNameResponse

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        content = d.pop("content")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_latest_reply_at(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        latest_reply_at = _parse_latest_reply_at(d.pop("latest_reply_at"))

        reply_count = d.pop("reply_count")

        reactions = []
        _reactions = d.pop("reactions")
        for reactions_item_data in _reactions:
            reactions_item = Reactions.from_dict(reactions_item_data)

            reactions.append(reactions_item)

        user = UserNameResponse.from_dict(d.pop("user"))

        def _parse_channel_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        channel_id = _parse_channel_id(d.pop("channel_id", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_data(data: object) -> Union["MessageUserResponseDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = MessageUserResponseDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MessageUserResponseDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_meta(data: object) -> Union["MessageUserResponseMetaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = MessageUserResponseMetaType0.from_dict(data)

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MessageUserResponseMetaType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        message_user_response = cls(
            id=id,
            user_id=user_id,
            content=content,
            created_at=created_at,
            updated_at=updated_at,
            latest_reply_at=latest_reply_at,
            reply_count=reply_count,
            reactions=reactions,
            user=user,
            channel_id=channel_id,
            parent_id=parent_id,
            data=data,
            meta=meta,
        )

        message_user_response.additional_properties = d
        return message_user_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
