import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_model_info_type_0 import UserModelInfoType0
    from ..models.user_settings import UserSettings


T = TypeVar("T", bound="UserModel")


@_attrs_define
class UserModel:
    """
    Attributes:
        id (str):
        name (str):
        email (str):
        profile_image_url (str):
        last_active_at (int):
        updated_at (int):
        created_at (int):
        username (Union[None, Unset, str]):
        role (Union[Unset, str]):  Default: 'pending'.
        bio (Union[None, Unset, str]):
        gender (Union[None, Unset, str]):
        date_of_birth (Union[None, Unset, datetime.date]):
        info (Union['UserModelInfoType0', None, Unset]):
        settings (Union['UserSettings', None, Unset]):
        api_key (Union[None, Unset, str]):
        oauth_sub (Union[None, Unset, str]):
    """

    id: str
    name: str
    email: str
    profile_image_url: str
    last_active_at: int
    updated_at: int
    created_at: int
    username: Union[None, Unset, str] = UNSET
    role: Union[Unset, str] = "pending"
    bio: Union[None, Unset, str] = UNSET
    gender: Union[None, Unset, str] = UNSET
    date_of_birth: Union[None, Unset, datetime.date] = UNSET
    info: Union["UserModelInfoType0", None, Unset] = UNSET
    settings: Union["UserSettings", None, Unset] = UNSET
    api_key: Union[None, Unset, str] = UNSET
    oauth_sub: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_model_info_type_0 import UserModelInfoType0
        from ..models.user_settings import UserSettings

        id = self.id

        name = self.name

        email = self.email

        profile_image_url = self.profile_image_url

        last_active_at = self.last_active_at

        updated_at = self.updated_at

        created_at = self.created_at

        username: Union[None, Unset, str]
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        role = self.role

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

        info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.info, Unset):
            info = UNSET
        elif isinstance(self.info, UserModelInfoType0):
            info = self.info.to_dict()
        else:
            info = self.info

        settings: Union[None, Unset, dict[str, Any]]
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, UserSettings):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        api_key: Union[None, Unset, str]
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        oauth_sub: Union[None, Unset, str]
        if isinstance(self.oauth_sub, Unset):
            oauth_sub = UNSET
        else:
            oauth_sub = self.oauth_sub

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "email": email,
                "profile_image_url": profile_image_url,
                "last_active_at": last_active_at,
                "updated_at": updated_at,
                "created_at": created_at,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if role is not UNSET:
            field_dict["role"] = role
        if bio is not UNSET:
            field_dict["bio"] = bio
        if gender is not UNSET:
            field_dict["gender"] = gender
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if info is not UNSET:
            field_dict["info"] = info
        if settings is not UNSET:
            field_dict["settings"] = settings
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if oauth_sub is not UNSET:
            field_dict["oauth_sub"] = oauth_sub

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_model_info_type_0 import UserModelInfoType0
        from ..models.user_settings import UserSettings

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        email = d.pop("email")

        profile_image_url = d.pop("profile_image_url")

        last_active_at = d.pop("last_active_at")

        updated_at = d.pop("updated_at")

        created_at = d.pop("created_at")

        def _parse_username(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        username = _parse_username(d.pop("username", UNSET))

        role = d.pop("role", UNSET)

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

        def _parse_info(data: object) -> Union["UserModelInfoType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                info_type_0 = UserModelInfoType0.from_dict(data)

                return info_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UserModelInfoType0", None, Unset], data)

        info = _parse_info(d.pop("info", UNSET))

        def _parse_settings(data: object) -> Union["UserSettings", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = UserSettings.from_dict(data)

                return settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UserSettings", None, Unset], data)

        settings = _parse_settings(d.pop("settings", UNSET))

        def _parse_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))

        def _parse_oauth_sub(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        oauth_sub = _parse_oauth_sub(d.pop("oauth_sub", UNSET))

        user_model = cls(
            id=id,
            name=name,
            email=email,
            profile_image_url=profile_image_url,
            last_active_at=last_active_at,
            updated_at=updated_at,
            created_at=created_at,
            username=username,
            role=role,
            bio=bio,
            gender=gender,
            date_of_birth=date_of_birth,
            info=info,
            settings=settings,
            api_key=api_key,
            oauth_sub=oauth_sub,
        )

        user_model.additional_properties = d
        return user_model

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
