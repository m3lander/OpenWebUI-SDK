import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProfileForm")


@_attrs_define
class UpdateProfileForm:
    """
    Attributes:
        profile_image_url (str):
        name (str):
        bio (Union[None, Unset, str]):
        gender (Union[None, Unset, str]):
        date_of_birth (Union[None, Unset, datetime.date]):
    """

    profile_image_url: str
    name: str
    bio: Union[None, Unset, str] = UNSET
    gender: Union[None, Unset, str] = UNSET
    date_of_birth: Union[None, Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_image_url = self.profile_image_url

        name = self.name

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
                "profile_image_url": profile_image_url,
                "name": name,
            }
        )
        if bio is not UNSET:
            field_dict["bio"] = bio
        if gender is not UNSET:
            field_dict["gender"] = gender
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        profile_image_url = d.pop("profile_image_url")

        name = d.pop("name")

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

        update_profile_form = cls(
            profile_image_url=profile_image_url,
            name=name,
            bio=bio,
            gender=gender,
            date_of_birth=date_of_birth,
        )

        update_profile_form.additional_properties = d
        return update_profile_form

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
