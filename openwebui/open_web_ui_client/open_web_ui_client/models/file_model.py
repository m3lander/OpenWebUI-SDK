from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_model_access_control_type_0 import FileModelAccessControlType0
    from ..models.file_model_data_type_0 import FileModelDataType0
    from ..models.file_model_meta_type_0 import FileModelMetaType0


T = TypeVar("T", bound="FileModel")


@_attrs_define
class FileModel:
    """
    Attributes:
        id (str):
        user_id (str):
        filename (str):
        created_at (Union[None, int]):
        updated_at (Union[None, int]):
        hash_ (Union[None, Unset, str]):
        path (Union[None, Unset, str]):
        data (Union['FileModelDataType0', None, Unset]):
        meta (Union['FileModelMetaType0', None, Unset]):
        access_control (Union['FileModelAccessControlType0', None, Unset]):
    """

    id: str
    user_id: str
    filename: str
    created_at: Union[None, int]
    updated_at: Union[None, int]
    hash_: Union[None, Unset, str] = UNSET
    path: Union[None, Unset, str] = UNSET
    data: Union["FileModelDataType0", None, Unset] = UNSET
    meta: Union["FileModelMetaType0", None, Unset] = UNSET
    access_control: Union["FileModelAccessControlType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_model_access_control_type_0 import FileModelAccessControlType0
        from ..models.file_model_data_type_0 import FileModelDataType0
        from ..models.file_model_meta_type_0 import FileModelMetaType0

        id = self.id

        user_id = self.user_id

        filename = self.filename

        created_at: Union[None, int]
        created_at = self.created_at

        updated_at: Union[None, int]
        updated_at = self.updated_at

        hash_: Union[None, Unset, str]
        if isinstance(self.hash_, Unset):
            hash_ = UNSET
        else:
            hash_ = self.hash_

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, FileModelDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, FileModelMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        access_control: Union[None, Unset, dict[str, Any]]
        if isinstance(self.access_control, Unset):
            access_control = UNSET
        elif isinstance(self.access_control, FileModelAccessControlType0):
            access_control = self.access_control.to_dict()
        else:
            access_control = self.access_control

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "filename": filename,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if path is not UNSET:
            field_dict["path"] = path
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta
        if access_control is not UNSET:
            field_dict["access_control"] = access_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_model_access_control_type_0 import FileModelAccessControlType0
        from ..models.file_model_data_type_0 import FileModelDataType0
        from ..models.file_model_meta_type_0 import FileModelMetaType0

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        filename = d.pop("filename")

        def _parse_created_at(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        def _parse_hash_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hash_ = _parse_hash_(d.pop("hash", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_data(data: object) -> Union["FileModelDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = FileModelDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FileModelDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_meta(data: object) -> Union["FileModelMetaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = FileModelMetaType0.from_dict(data)

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FileModelMetaType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        def _parse_access_control(data: object) -> Union["FileModelAccessControlType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                access_control_type_0 = FileModelAccessControlType0.from_dict(data)

                return access_control_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FileModelAccessControlType0", None, Unset], data)

        access_control = _parse_access_control(d.pop("access_control", UNSET))

        file_model = cls(
            id=id,
            user_id=user_id,
            filename=filename,
            created_at=created_at,
            updated_at=updated_at,
            hash_=hash_,
            path=path,
            data=data,
            meta=meta,
            access_control=access_control,
        )

        file_model.additional_properties = d
        return file_model

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
