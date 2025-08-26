from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_response_data_type_0 import GroupResponseDataType0
    from ..models.group_response_meta_type_0 import GroupResponseMetaType0
    from ..models.group_response_permissions_type_0 import GroupResponsePermissionsType0


T = TypeVar("T", bound="GroupResponse")


@_attrs_define
class GroupResponse:
    """
    Attributes:
        id (str):
        user_id (str):
        name (str):
        description (str):
        created_at (int):
        updated_at (int):
        permissions (Union['GroupResponsePermissionsType0', None, Unset]):
        data (Union['GroupResponseDataType0', None, Unset]):
        meta (Union['GroupResponseMetaType0', None, Unset]):
        user_ids (Union[Unset, list[str]]):
    """

    id: str
    user_id: str
    name: str
    description: str
    created_at: int
    updated_at: int
    permissions: Union["GroupResponsePermissionsType0", None, Unset] = UNSET
    data: Union["GroupResponseDataType0", None, Unset] = UNSET
    meta: Union["GroupResponseMetaType0", None, Unset] = UNSET
    user_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.group_response_data_type_0 import GroupResponseDataType0
        from ..models.group_response_meta_type_0 import GroupResponseMetaType0
        from ..models.group_response_permissions_type_0 import GroupResponsePermissionsType0

        id = self.id

        user_id = self.user_id

        name = self.name

        description = self.description

        created_at = self.created_at

        updated_at = self.updated_at

        permissions: Union[None, Unset, dict[str, Any]]
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, GroupResponsePermissionsType0):
            permissions = self.permissions.to_dict()
        else:
            permissions = self.permissions

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, GroupResponseDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, GroupResponseMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        user_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "name": name,
                "description": description,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_response_data_type_0 import GroupResponseDataType0
        from ..models.group_response_meta_type_0 import GroupResponseMetaType0
        from ..models.group_response_permissions_type_0 import GroupResponsePermissionsType0

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        name = d.pop("name")

        description = d.pop("description")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_permissions(data: object) -> Union["GroupResponsePermissionsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                permissions_type_0 = GroupResponsePermissionsType0.from_dict(data)

                return permissions_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GroupResponsePermissionsType0", None, Unset], data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))

        def _parse_data(data: object) -> Union["GroupResponseDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = GroupResponseDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GroupResponseDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_meta(data: object) -> Union["GroupResponseMetaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = GroupResponseMetaType0.from_dict(data)

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GroupResponseMetaType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        user_ids = cast(list[str], d.pop("user_ids", UNSET))

        group_response = cls(
            id=id,
            user_id=user_id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            permissions=permissions,
            data=data,
            meta=meta,
            user_ids=user_ids,
        )

        group_response.additional_properties = d
        return group_response

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
