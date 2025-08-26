from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspacePermissions")


@_attrs_define
class WorkspacePermissions:
    """
    Attributes:
        models (Union[Unset, bool]):  Default: False.
        knowledge (Union[Unset, bool]):  Default: False.
        prompts (Union[Unset, bool]):  Default: False.
        tools (Union[Unset, bool]):  Default: False.
    """

    models: Union[Unset, bool] = False
    knowledge: Union[Unset, bool] = False
    prompts: Union[Unset, bool] = False
    tools: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        models = self.models

        knowledge = self.knowledge

        prompts = self.prompts

        tools = self.tools

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if models is not UNSET:
            field_dict["models"] = models
        if knowledge is not UNSET:
            field_dict["knowledge"] = knowledge
        if prompts is not UNSET:
            field_dict["prompts"] = prompts
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        models = d.pop("models", UNSET)

        knowledge = d.pop("knowledge", UNSET)

        prompts = d.pop("prompts", UNSET)

        tools = d.pop("tools", UNSET)

        workspace_permissions = cls(
            models=models,
            knowledge=knowledge,
            prompts=prompts,
            tools=tools,
        )

        workspace_permissions.additional_properties = d
        return workspace_permissions

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
