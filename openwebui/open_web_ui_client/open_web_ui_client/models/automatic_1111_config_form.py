from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Automatic1111ConfigForm")


@_attrs_define
class Automatic1111ConfigForm:
    """
    Attributes:
        automatic1111_base_url (str):
        automatic1111_api_auth (str):
        automatic1111_cfg_scale (Union[None, float, int, str]):
        automatic1111_sampler (Union[None, str]):
        automatic1111_scheduler (Union[None, str]):
    """

    automatic1111_base_url: str
    automatic1111_api_auth: str
    automatic1111_cfg_scale: Union[None, float, int, str]
    automatic1111_sampler: Union[None, str]
    automatic1111_scheduler: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automatic1111_base_url = self.automatic1111_base_url

        automatic1111_api_auth = self.automatic1111_api_auth

        automatic1111_cfg_scale: Union[None, float, int, str]
        automatic1111_cfg_scale = self.automatic1111_cfg_scale

        automatic1111_sampler: Union[None, str]
        automatic1111_sampler = self.automatic1111_sampler

        automatic1111_scheduler: Union[None, str]
        automatic1111_scheduler = self.automatic1111_scheduler

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "AUTOMATIC1111_BASE_URL": automatic1111_base_url,
                "AUTOMATIC1111_API_AUTH": automatic1111_api_auth,
                "AUTOMATIC1111_CFG_SCALE": automatic1111_cfg_scale,
                "AUTOMATIC1111_SAMPLER": automatic1111_sampler,
                "AUTOMATIC1111_SCHEDULER": automatic1111_scheduler,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        automatic1111_base_url = d.pop("AUTOMATIC1111_BASE_URL")

        automatic1111_api_auth = d.pop("AUTOMATIC1111_API_AUTH")

        def _parse_automatic1111_cfg_scale(data: object) -> Union[None, float, int, str]:
            if data is None:
                return data
            return cast(Union[None, float, int, str], data)

        automatic1111_cfg_scale = _parse_automatic1111_cfg_scale(d.pop("AUTOMATIC1111_CFG_SCALE"))

        def _parse_automatic1111_sampler(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        automatic1111_sampler = _parse_automatic1111_sampler(d.pop("AUTOMATIC1111_SAMPLER"))

        def _parse_automatic1111_scheduler(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        automatic1111_scheduler = _parse_automatic1111_scheduler(d.pop("AUTOMATIC1111_SCHEDULER"))

        automatic_1111_config_form = cls(
            automatic1111_base_url=automatic1111_base_url,
            automatic1111_api_auth=automatic1111_api_auth,
            automatic1111_cfg_scale=automatic1111_cfg_scale,
            automatic1111_sampler=automatic1111_sampler,
            automatic1111_scheduler=automatic1111_scheduler,
        )

        automatic_1111_config_form.additional_properties = d
        return automatic_1111_config_form

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
