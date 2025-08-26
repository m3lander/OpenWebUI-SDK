from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_meta_capabilities_type_0 import ModelMetaCapabilitiesType0


T = TypeVar("T", bound="ModelMeta")


@_attrs_define
class ModelMeta:
    """
    Attributes:
        profile_image_url (Union[None, Unset, str]):  Default: '/static/favicon.png'.
        description (Union[None, Unset, str]):
        capabilities (Union['ModelMetaCapabilitiesType0', None, Unset]):
    """

    profile_image_url: Union[None, Unset, str] = "/static/favicon.png"
    description: Union[None, Unset, str] = UNSET
    capabilities: Union["ModelMetaCapabilitiesType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_meta_capabilities_type_0 import ModelMetaCapabilitiesType0

        profile_image_url: Union[None, Unset, str]
        if isinstance(self.profile_image_url, Unset):
            profile_image_url = UNSET
        else:
            profile_image_url = self.profile_image_url

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        capabilities: Union[None, Unset, dict[str, Any]]
        if isinstance(self.capabilities, Unset):
            capabilities = UNSET
        elif isinstance(self.capabilities, ModelMetaCapabilitiesType0):
            capabilities = self.capabilities.to_dict()
        else:
            capabilities = self.capabilities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_image_url is not UNSET:
            field_dict["profile_image_url"] = profile_image_url
        if description is not UNSET:
            field_dict["description"] = description
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_meta_capabilities_type_0 import ModelMetaCapabilitiesType0

        d = dict(src_dict)

        def _parse_profile_image_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        profile_image_url = _parse_profile_image_url(d.pop("profile_image_url", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_capabilities(data: object) -> Union["ModelMetaCapabilitiesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                capabilities_type_0 = ModelMetaCapabilitiesType0.from_dict(data)

                return capabilities_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelMetaCapabilitiesType0", None, Unset], data)

        capabilities = _parse_capabilities(d.pop("capabilities", UNSET))

        model_meta = cls(
            profile_image_url=profile_image_url,
            description=description,
            capabilities=capabilities,
        )

        model_meta.additional_properties = d
        return model_meta

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
