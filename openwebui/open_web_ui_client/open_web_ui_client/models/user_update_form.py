from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUpdateForm")


@_attrs_define
class UserUpdateForm:
    """
    Attributes:
        role (str):
        name (str):
        email (str):
        profile_image_url (str):
        password (Union[None, Unset, str]):
    """

    role: str
    name: str
    email: str
    profile_image_url: str
    password: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        name = self.name

        email = self.email

        profile_image_url = self.profile_image_url

        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "name": name,
                "email": email,
                "profile_image_url": profile_image_url,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = d.pop("role")

        name = d.pop("name")

        email = d.pop("email")

        profile_image_url = d.pop("profile_image_url")

        def _parse_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password = _parse_password(d.pop("password", UNSET))

        user_update_form = cls(
            role=role,
            name=name,
            email=email,
            profile_image_url=profile_image_url,
            password=password,
        )

        user_update_form.additional_properties = d
        return user_update_form

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
