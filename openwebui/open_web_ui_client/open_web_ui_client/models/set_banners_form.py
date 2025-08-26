from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.banner_model import BannerModel


T = TypeVar("T", bound="SetBannersForm")


@_attrs_define
class SetBannersForm:
    """
    Attributes:
        banners (list['BannerModel']):
    """

    banners: list["BannerModel"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        banners = []
        for banners_item_data in self.banners:
            banners_item = banners_item_data.to_dict()
            banners.append(banners_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "banners": banners,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.banner_model import BannerModel

        d = dict(src_dict)
        banners = []
        _banners = d.pop("banners")
        for banners_item_data in _banners:
            banners_item = BannerModel.from_dict(banners_item_data)

            banners.append(banners_item)

        set_banners_form = cls(
            banners=banners,
        )

        set_banners_form.additional_properties = d
        return set_banners_form

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
