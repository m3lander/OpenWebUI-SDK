from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snapshot_data_chat_type_0 import SnapshotDataChatType0


T = TypeVar("T", bound="SnapshotData")


@_attrs_define
class SnapshotData:
    """
    Attributes:
        chat (Union['SnapshotDataChatType0', None, Unset]):
    """

    chat: Union["SnapshotDataChatType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.snapshot_data_chat_type_0 import SnapshotDataChatType0

        chat: Union[None, Unset, dict[str, Any]]
        if isinstance(self.chat, Unset):
            chat = UNSET
        elif isinstance(self.chat, SnapshotDataChatType0):
            chat = self.chat.to_dict()
        else:
            chat = self.chat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat is not UNSET:
            field_dict["chat"] = chat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snapshot_data_chat_type_0 import SnapshotDataChatType0

        d = dict(src_dict)

        def _parse_chat(data: object) -> Union["SnapshotDataChatType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                chat_type_0 = SnapshotDataChatType0.from_dict(data)

                return chat_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SnapshotDataChatType0", None, Unset], data)

        chat = _parse_chat(d.pop("chat", UNSET))

        snapshot_data = cls(
            chat=chat,
        )

        snapshot_data.additional_properties = d
        return snapshot_data

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
