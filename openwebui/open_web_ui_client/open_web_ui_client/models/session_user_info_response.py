import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_user_info_response_permissions_type_0 import SessionUserInfoResponsePermissionsType0


T = TypeVar("T", bound="SessionUserInfoResponse")


@_attrs_define
class SessionUserInfoResponse:
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
        permissions (Union['SessionUserInfoResponsePermissionsType0', None, Unset]):
        bio (Union[None, Unset, str]):
        gender (Union[None, Unset, str]):
        date_of_birth (Union[None, Unset, datetime.date]):
    """

    id: str
    email: str
    name: str
    role: str
    profile_image_url: str
    token: str
    token_type: str
    expires_at: Union[None, Unset, int] = UNSET
    permissions: Union["SessionUserInfoResponsePermissionsType0", None, Unset] = UNSET
    bio: Union[None, Unset, str] = UNSET
    gender: Union[None, Unset, str] = UNSET
    date_of_birth: Union[None, Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_user_info_response_permissions_type_0 import SessionUserInfoResponsePermissionsType0

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
        elif isinstance(self.permissions, SessionUserInfoResponsePermissionsType0):
            permissions = self.permissions.to_dict()
        else:
            permissions = self.permissions

        bio: Union[None, Unset, str]
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        gender: Union[None, Unset, str]
        if isinstance(self.gender, Unset):
            gender = UNSET
        else:
            gender = self.gender

        date_of_birth: Union[None, Unset, str]
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        elif isinstance(self.date_of_birth, datetime.date):
            date_of_birth = self.date_of_birth.isoformat()
        else:
            date_of_birth = self.date_of_birth

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
        if bio is not UNSET:
            field_dict["bio"] = bio
        if gender is not UNSET:
            field_dict["gender"] = gender
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_user_info_response_permissions_type_0 import SessionUserInfoResponsePermissionsType0

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

        def _parse_permissions(data: object) -> Union["SessionUserInfoResponsePermissionsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                permissions_type_0 = SessionUserInfoResponsePermissionsType0.from_dict(data)

                return permissions_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SessionUserInfoResponsePermissionsType0", None, Unset], data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))

        def _parse_bio(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bio = _parse_bio(d.pop("bio", UNSET))

        def _parse_gender(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_date_of_birth(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_birth_type_0 = isoparse(data).date()

                return date_of_birth_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_of_birth = _parse_date_of_birth(d.pop("date_of_birth", UNSET))

        session_user_info_response = cls(
            id=id,
            email=email,
            name=name,
            role=role,
            profile_image_url=profile_image_url,
            token=token,
            token_type=token_type,
            expires_at=expires_at,
            permissions=permissions,
            bio=bio,
            gender=gender,
            date_of_birth=date_of_birth,
        )

        session_user_info_response.additional_properties = d
        return session_user_info_response

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
