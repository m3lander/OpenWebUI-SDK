from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prompt_model_access_control_type_0 import PromptModelAccessControlType0


T = TypeVar("T", bound="PromptModel")


@_attrs_define
class PromptModel:
    """
    Attributes:
        command (str):
        user_id (str):
        title (str):
        content (str):
        timestamp (int):
        access_control (Union['PromptModelAccessControlType0', None, Unset]):
    """

    command: str
    user_id: str
    title: str
    content: str
    timestamp: int
    access_control: Union["PromptModelAccessControlType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_model_access_control_type_0 import PromptModelAccessControlType0

        command = self.command

        user_id = self.user_id

        title = self.title

        content = self.content

        timestamp = self.timestamp

        access_control: Union[None, Unset, dict[str, Any]]
        if isinstance(self.access_control, Unset):
            access_control = UNSET
        elif isinstance(self.access_control, PromptModelAccessControlType0):
            access_control = self.access_control.to_dict()
        else:
            access_control = self.access_control

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command": command,
                "user_id": user_id,
                "title": title,
                "content": content,
                "timestamp": timestamp,
            }
        )
        if access_control is not UNSET:
            field_dict["access_control"] = access_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_model_access_control_type_0 import PromptModelAccessControlType0

        d = dict(src_dict)
        command = d.pop("command")

        user_id = d.pop("user_id")

        title = d.pop("title")

        content = d.pop("content")

        timestamp = d.pop("timestamp")

        def _parse_access_control(data: object) -> Union["PromptModelAccessControlType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                access_control_type_0 = PromptModelAccessControlType0.from_dict(data)

                return access_control_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PromptModelAccessControlType0", None, Unset], data)

        access_control = _parse_access_control(d.pop("access_control", UNSET))

        prompt_model = cls(
            command=command,
            user_id=user_id,
            title=title,
            content=content,
            timestamp=timestamp,
            access_control=access_control,
        )

        prompt_model.additional_properties = d
        return prompt_model

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
