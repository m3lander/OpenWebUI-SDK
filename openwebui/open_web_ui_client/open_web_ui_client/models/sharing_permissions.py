from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharingPermissions")


@_attrs_define
class SharingPermissions:
    """
    Attributes:
        public_models (Union[Unset, bool]):  Default: True.
        public_knowledge (Union[Unset, bool]):  Default: True.
        public_prompts (Union[Unset, bool]):  Default: True.
        public_tools (Union[Unset, bool]):  Default: True.
    """

    public_models: Union[Unset, bool] = True
    public_knowledge: Union[Unset, bool] = True
    public_prompts: Union[Unset, bool] = True
    public_tools: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_models = self.public_models

        public_knowledge = self.public_knowledge

        public_prompts = self.public_prompts

        public_tools = self.public_tools

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if public_models is not UNSET:
            field_dict["public_models"] = public_models
        if public_knowledge is not UNSET:
            field_dict["public_knowledge"] = public_knowledge
        if public_prompts is not UNSET:
            field_dict["public_prompts"] = public_prompts
        if public_tools is not UNSET:
            field_dict["public_tools"] = public_tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_models = d.pop("public_models", UNSET)

        public_knowledge = d.pop("public_knowledge", UNSET)

        public_prompts = d.pop("public_prompts", UNSET)

        public_tools = d.pop("public_tools", UNSET)

        sharing_permissions = cls(
            public_models=public_models,
            public_knowledge=public_knowledge,
            public_prompts=public_prompts,
            public_tools=public_tools,
        )

        sharing_permissions.additional_properties = d
        return sharing_permissions

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
