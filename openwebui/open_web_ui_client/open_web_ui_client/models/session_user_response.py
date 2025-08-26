from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_user_response_permissions_type_0 import SessionUserResponsePermissionsType0


T = TypeVar("T", bound="SessionUserResponse")


@_attrs_define
class SessionUserResponse:
    """
    Attributes:
        id (str):
        email (str):
        name (str):
        role (str):
        profile_image_url (str):
        token (str):
        token_type (str):
        expires_at (Union[None, Unset, int]):
        permissions (Union['SessionUserResponsePermissionsType0', None, Unset]):
    """

    id: str
    email: str
    name: str
    role: str
    profile_image_url: str
    token: str
    token_type: str
    expires_at: Union[None, Unset, int] = UNSET
    permissions: Union["SessionUserResponsePermissionsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_user_response_permissions_type_0 import SessionUserResponsePermissionsType0

        id = self.id

        email = self.email

        name = self.name

        role = self.role

        profile_image_url = self.profile_image_url

        token = self.token

        token_type = self.token_type

        expires_at: Union[None, Unset, int]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        permissions: Union[None, Unset, dict[str, Any]]
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, SessionUserResponsePermissionsType0):
            permissions = self.permissions.to_dict()
        else:
            permissions = self.permissions

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
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_user_response_permissions_type_0 import SessionUserResponsePermissionsType0

        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        name = d.pop("name")

        role = d.pop("role")

        profile_image_url = d.pop("profile_image_url")

        token = d.pop("token")

        token_type = d.pop("token_type")

        def _parse_expires_at(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_permissions(data: object) -> Union["SessionUserResponsePermissionsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                permissions_type_0 = SessionUserResponsePermissionsType0.from_dict(data)

                return permissions_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SessionUserResponsePermissionsType0", None, Unset], data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))

        session_user_response = cls(
            id=id,
            email=email,
            name=name,
            role=role,
            profile_image_url=profile_image_url,
            token=token,
            token_type=token_type,
            expires_at=expires_at,
            permissions=permissions,
        )

        session_user_response.additional_properties = d
        return session_user_response

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
