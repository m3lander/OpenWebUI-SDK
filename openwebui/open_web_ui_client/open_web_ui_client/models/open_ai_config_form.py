from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OpenAIConfigForm")


@_attrs_define
class OpenAIConfigForm:
    """
    Attributes:
        openai_api_base_url (str):
        openai_api_key (str):
    """

    openai_api_base_url: str
    openai_api_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        openai_api_base_url = self.openai_api_base_url

        openai_api_key = self.openai_api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OPENAI_API_BASE_URL": openai_api_base_url,
                "OPENAI_API_KEY": openai_api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        openai_api_base_url = d.pop("OPENAI_API_BASE_URL")

        openai_api_key = d.pop("OPENAI_API_KEY")

        open_ai_config_form = cls(
            openai_api_base_url=openai_api_base_url,
            openai_api_key=openai_api_key,
        )

        open_ai_config_form.additional_properties = d
        return open_ai_config_form

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
