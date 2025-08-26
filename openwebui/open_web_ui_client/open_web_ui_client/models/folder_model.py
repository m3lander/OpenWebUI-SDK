from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.folder_model_data_type_0 import FolderModelDataType0
    from ..models.folder_model_items_type_0 import FolderModelItemsType0
    from ..models.folder_model_meta_type_0 import FolderModelMetaType0


T = TypeVar("T", bound="FolderModel")


@_attrs_define
class FolderModel:
    """
    Attributes:
        id (str):
        user_id (str):
        name (str):
        created_at (int):
        updated_at (int):
        parent_id (Union[None, Unset, str]):
        items (Union['FolderModelItemsType0', None, Unset]):
        meta (Union['FolderModelMetaType0', None, Unset]):
        data (Union['FolderModelDataType0', None, Unset]):
        is_expanded (Union[Unset, bool]):  Default: False.
    """

    id: str
    user_id: str
    name: str
    created_at: int
    updated_at: int
    parent_id: Union[None, Unset, str] = UNSET
    items: Union["FolderModelItemsType0", None, Unset] = UNSET
    meta: Union["FolderModelMetaType0", None, Unset] = UNSET
    data: Union["FolderModelDataType0", None, Unset] = UNSET
    is_expanded: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.folder_model_data_type_0 import FolderModelDataType0
        from ..models.folder_model_items_type_0 import FolderModelItemsType0
        from ..models.folder_model_meta_type_0 import FolderModelMetaType0

        id = self.id

        user_id = self.user_id

        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        items: Union[None, Unset, dict[str, Any]]
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, FolderModelItemsType0):
            items = self.items.to_dict()
        else:
            items = self.items

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, FolderModelMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, FolderModelDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        is_expanded = self.is_expanded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if items is not UNSET:
            field_dict["items"] = items
        if meta is not UNSET:
            field_dict["meta"] = meta
        if data is not UNSET:
            field_dict["data"] = data
        if is_expanded is not UNSET:
            field_dict["is_expanded"] = is_expanded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.folder_model_data_type_0 import FolderModelDataType0
        from ..models.folder_model_items_type_0 import FolderModelItemsType0
        from ..models.folder_model_meta_type_0 import FolderModelMetaType0

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_items(data: object) -> Union["FolderModelItemsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                items_type_0 = FolderModelItemsType0.from_dict(data)

                return items_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FolderModelItemsType0", None, Unset], data)

        items = _parse_items(d.pop("items", UNSET))

        def _parse_meta(data: object) -> Union["FolderModelMetaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = FolderModelMetaType0.from_dict(data)

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FolderModelMetaType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        def _parse_data(data: object) -> Union["FolderModelDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = FolderModelDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FolderModelDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        is_expanded = d.pop("is_expanded", UNSET)

        folder_model = cls(
            id=id,
            user_id=user_id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            parent_id=parent_id,
            items=items,
            meta=meta,
            data=data,
            is_expanded=is_expanded,
        )

        folder_model.additional_properties = d
        return folder_model

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
