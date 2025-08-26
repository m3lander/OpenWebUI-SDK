from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ollama_config_form_ollama_api_configs import OllamaConfigFormOllamaApiConfigs


T = TypeVar("T", bound="OllamaConfigForm")


@_attrs_define
class OllamaConfigForm:
    """
    Attributes:
        ollama_base_urls (list[str]):
        ollama_api_configs (OllamaConfigFormOllamaApiConfigs):
        enable_ollama_api (Union[None, Unset, bool]):
    """

    ollama_base_urls: list[str]
    ollama_api_configs: "OllamaConfigFormOllamaApiConfigs"
    enable_ollama_api: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ollama_base_urls = self.ollama_base_urls

        ollama_api_configs = self.ollama_api_configs.to_dict()

        enable_ollama_api: Union[None, Unset, bool]
        if isinstance(self.enable_ollama_api, Unset):
            enable_ollama_api = UNSET
        else:
            enable_ollama_api = self.enable_ollama_api

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OLLAMA_BASE_URLS": ollama_base_urls,
                "OLLAMA_API_CONFIGS": ollama_api_configs,
            }
        )
        if enable_ollama_api is not UNSET:
            field_dict["ENABLE_OLLAMA_API"] = enable_ollama_api

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ollama_config_form_ollama_api_configs import OllamaConfigFormOllamaApiConfigs

        d = dict(src_dict)
        ollama_base_urls = cast(list[str], d.pop("OLLAMA_BASE_URLS"))

        ollama_api_configs = OllamaConfigFormOllamaApiConfigs.from_dict(d.pop("OLLAMA_API_CONFIGS"))

        def _parse_enable_ollama_api(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_ollama_api = _parse_enable_ollama_api(d.pop("ENABLE_OLLAMA_API", UNSET))

        ollama_config_form = cls(
            ollama_base_urls=ollama_base_urls,
            ollama_api_configs=ollama_api_configs,
            enable_ollama_api=enable_ollama_api,
        )

        ollama_config_form.additional_properties = d
        return ollama_config_form

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
