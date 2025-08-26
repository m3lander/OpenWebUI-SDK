from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignupForm")


@_attrs_define
class SignupForm:
    """
    Attributes:
        name (str):
        email (str):
        password (str):
        profile_image_url (Union[None, Unset, str]):  Default: '/user.png'.
    """

    name: str
    email: str
    password: str
    profile_image_url: Union[None, Unset, str] = "/user.png"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        password = self.password

        profile_image_url: Union[None, Unset, str]
        if isinstance(self.profile_image_url, Unset):
            profile_image_url = UNSET
        else:
            profile_image_url = self.profile_image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "email": email,
                "password": password,
            }
        )
        if profile_image_url is not UNSET:
            field_dict["profile_image_url"] = profile_image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        email = d.pop("email")

        password = d.pop("password")

        def _parse_profile_image_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        profile_image_url = _parse_profile_image_url(d.pop("profile_image_url", UNSET))

        signup_form = cls(
            name=name,
            email=email,
            password=password,
            profile_image_url=profile_image_url,
        )

        signup_form.additional_properties = d
        return signup_form

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
