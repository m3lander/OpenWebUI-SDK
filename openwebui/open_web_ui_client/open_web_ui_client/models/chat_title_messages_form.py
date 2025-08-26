from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat_title_messages_form_messages_item import ChatTitleMessagesFormMessagesItem


T = TypeVar("T", bound="ChatTitleMessagesForm")


@_attrs_define
class ChatTitleMessagesForm:
    """
    Attributes:
        title (str):
        messages (list['ChatTitleMessagesFormMessagesItem']):
    """

    title: str
    messages: list["ChatTitleMessagesFormMessagesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "messages": messages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_title_messages_form_messages_item import ChatTitleMessagesFormMessagesItem

        d = dict(src_dict)
        title = d.pop("title")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = ChatTitleMessagesFormMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        chat_title_messages_form = cls(
            title=title,
            messages=messages,
        )

        chat_title_messages_form.additional_properties = d
        return chat_title_messages_form

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
