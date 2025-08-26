from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_form_permissions_type_0 import GroupFormPermissionsType0


T = TypeVar("T", bound="GroupForm")


@_attrs_define
class GroupForm:
    """
    Attributes:
        name (str):
        description (str):
        permissions (Union['GroupFormPermissionsType0', None, Unset]):
    """

    name: str
    description: str
    permissions: Union["GroupFormPermissionsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.group_form_permissions_type_0 import GroupFormPermissionsType0

        name = self.name

        description = self.description

        permissions: Union[None, Unset, dict[str, Any]]
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, GroupFormPermissionsType0):
            permissions = self.permissions.to_dict()
        else:
            permissions = self.permissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
            }
        )
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_form_permissions_type_0 import GroupFormPermissionsType0

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        def _parse_permissions(data: object) -> Union["GroupFormPermissionsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                permissions_type_0 = GroupFormPermissionsType0.from_dict(data)

                return permissions_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GroupFormPermissionsType0", None, Unset], data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))

        group_form = cls(
            name=name,
            description=description,
            permissions=permissions,
        )

        group_form.additional_properties = d
        return group_form

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
