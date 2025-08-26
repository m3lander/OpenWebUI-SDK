from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_response_chat import ChatResponseChat
    from ..models.chat_response_meta import ChatResponseMeta


T = TypeVar("T", bound="ChatResponse")


@_attrs_define
class ChatResponse:
    """
    Attributes:
        id (str):
        user_id (str):
        title (str):
        chat (ChatResponseChat):
        updated_at (int):
        created_at (int):
        archived (bool):
        share_id (Union[None, Unset, str]):
        pinned (Union[None, Unset, bool]):  Default: False.
        meta (Union[Unset, ChatResponseMeta]):
        folder_id (Union[None, Unset, str]):
    """

    id: str
    user_id: str
    title: str
    chat: "ChatResponseChat"
    updated_at: int
    created_at: int
    archived: bool
    share_id: Union[None, Unset, str] = UNSET
    pinned: Union[None, Unset, bool] = False
    meta: Union[Unset, "ChatResponseMeta"] = UNSET
    folder_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        title = self.title

        chat = self.chat.to_dict()

        updated_at = self.updated_at

        created_at = self.created_at

        archived = self.archived

        share_id: Union[None, Unset, str]
        if isinstance(self.share_id, Unset):
            share_id = UNSET
        else:
            share_id = self.share_id

        pinned: Union[None, Unset, bool]
        if isinstance(self.pinned, Unset):
            pinned = UNSET
        else:
            pinned = self.pinned

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        folder_id: Union[None, Unset, str]
        if isinstance(self.folder_id, Unset):
            folder_id = UNSET
        else:
            folder_id = self.folder_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "title": title,
                "chat": chat,
                "updated_at": updated_at,
                "created_at": created_at,
                "archived": archived,
            }
        )
        if share_id is not UNSET:
            field_dict["share_id"] = share_id
        if pinned is not UNSET:
            field_dict["pinned"] = pinned
        if meta is not UNSET:
            field_dict["meta"] = meta
        if folder_id is not UNSET:
            field_dict["folder_id"] = folder_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_response_chat import ChatResponseChat
        from ..models.chat_response_meta import ChatResponseMeta

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        title = d.pop("title")

        chat = ChatResponseChat.from_dict(d.pop("chat"))

        updated_at = d.pop("updated_at")

        created_at = d.pop("created_at")

        archived = d.pop("archived")

        def _parse_share_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        share_id = _parse_share_id(d.pop("share_id", UNSET))

        def _parse_pinned(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        pinned = _parse_pinned(d.pop("pinned", UNSET))

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ChatResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ChatResponseMeta.from_dict(_meta)

        def _parse_folder_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        folder_id = _parse_folder_id(d.pop("folder_id", UNSET))

        chat_response = cls(
            id=id,
            user_id=user_id,
            title=title,
            chat=chat,
            updated_at=updated_at,
            created_at=created_at,
            archived=archived,
            share_id=share_id,
            pinned=pinned,
            meta=meta,
            folder_id=folder_id,
        )

        chat_response.additional_properties = d
        return chat_response

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
