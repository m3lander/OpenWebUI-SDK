from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImageConfigForm")


@_attrs_define
class ImageConfigForm:
    """
    Attributes:
        model (str):
        image_size (str):
        image_steps (int):
    """

    model: str
    image_size: str
    image_steps: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        image_size = self.image_size

        image_steps = self.image_steps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "MODEL": model,
                "IMAGE_SIZE": image_size,
                "IMAGE_STEPS": image_steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("MODEL")

        image_size = d.pop("IMAGE_SIZE")

        image_steps = d.pop("IMAGE_STEPS")

        image_config_form = cls(
            model=model,
            image_size=image_size,
            image_steps=image_steps,
        )

        image_config_form.additional_properties = d
        return image_config_form

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
