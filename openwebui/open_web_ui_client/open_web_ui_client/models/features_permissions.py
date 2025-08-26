from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeaturesPermissions")


@_attrs_define
class FeaturesPermissions:
    """
    Attributes:
        direct_tool_servers (Union[Unset, bool]):  Default: False.
        web_search (Union[Unset, bool]):  Default: True.
        image_generation (Union[Unset, bool]):  Default: True.
        code_interpreter (Union[Unset, bool]):  Default: True.
        notes (Union[Unset, bool]):  Default: True.
    """

    direct_tool_servers: Union[Unset, bool] = False
    web_search: Union[Unset, bool] = True
    image_generation: Union[Unset, bool] = True
    code_interpreter: Union[Unset, bool] = True
    notes: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direct_tool_servers = self.direct_tool_servers

        web_search = self.web_search

        image_generation = self.image_generation

        code_interpreter = self.code_interpreter

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if direct_tool_servers is not UNSET:
            field_dict["direct_tool_servers"] = direct_tool_servers
        if web_search is not UNSET:
            field_dict["web_search"] = web_search
        if image_generation is not UNSET:
            field_dict["image_generation"] = image_generation
        if code_interpreter is not UNSET:
            field_dict["code_interpreter"] = code_interpreter
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        direct_tool_servers = d.pop("direct_tool_servers", UNSET)

        web_search = d.pop("web_search", UNSET)

        image_generation = d.pop("image_generation", UNSET)

        code_interpreter = d.pop("code_interpreter", UNSET)

        notes = d.pop("notes", UNSET)

        features_permissions = cls(
            direct_tool_servers=direct_tool_servers,
            web_search=web_search,
            image_generation=image_generation,
            code_interpreter=code_interpreter,
            notes=notes,
        )

        features_permissions.additional_properties = d
        return features_permissions

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
