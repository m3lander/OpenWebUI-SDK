from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConnectionsConfigForm")


@_attrs_define
class ConnectionsConfigForm:
    """
    Attributes:
        enable_direct_connections (bool):
        enable_base_models_cache (bool):
    """

    enable_direct_connections: bool
    enable_base_models_cache: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_direct_connections = self.enable_direct_connections

        enable_base_models_cache = self.enable_base_models_cache

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ENABLE_DIRECT_CONNECTIONS": enable_direct_connections,
                "ENABLE_BASE_MODELS_CACHE": enable_base_models_cache,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_direct_connections = d.pop("ENABLE_DIRECT_CONNECTIONS")

        enable_base_models_cache = d.pop("ENABLE_BASE_MODELS_CACHE")

        connections_config_form = cls(
            enable_direct_connections=enable_direct_connections,
            enable_base_models_cache=enable_base_models_cache,
        )

        connections_config_form.additional_properties = d
        return connections_config_form

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
