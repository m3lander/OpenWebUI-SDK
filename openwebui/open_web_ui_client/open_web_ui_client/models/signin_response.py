from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SigninResponse")


@_attrs_define
class SigninResponse:
    """
    Attributes:
        id (str):
        email (str):
        name (str):
        role (str):
        profile_image_url (str):
        token (str):
        token_type (str):
    """

    id: str
    email: str
    name: str
    role: str
    profile_image_url: str
    token: str
    token_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        name = self.name

        role = self.role

        profile_image_url = self.profile_image_url

        token = self.token

        token_type = self.token_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "name": name,
                "role": role,
                "profile_image_url": profile_image_url,
                "token": token,
                "token_type": token_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        name = d.pop("name")

        role = d.pop("role")

        profile_image_url = d.pop("profile_image_url")

        token = d.pop("token")

        token_type = d.pop("token_type")

        signin_response = cls(
            id=id,
            email=email,
            name=name,
            role=role,
            profile_image_url=profile_image_url,
            token=token,
            token_type=token_type,
        )

        signin_response.additional_properties = d
        return signin_response

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
