from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddUserForm")


@_attrs_define
class AddUserForm:
    """
    Attributes:
        name (str):
        email (str):
        password (str):
        profile_image_url (Union[None, Unset, str]):  Default: '/user.png'.
        role (Union[None, Unset, str]):  Default: 'pending'.
    """

    name: str
    email: str
    password: str
    profile_image_url: Union[None, Unset, str] = "/user.png"
    role: Union[None, Unset, str] = "pending"
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

        role: Union[None, Unset, str]
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

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
        if role is not UNSET:
            field_dict["role"] = role

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

        def _parse_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        role = _parse_role(d.pop("role", UNSET))

        add_user_form = cls(
            name=name,
            email=email,
            password=password,
            profile_image_url=profile_image_url,
            role=role,
        )

        add_user_form.additional_properties = d
        return add_user_form

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
