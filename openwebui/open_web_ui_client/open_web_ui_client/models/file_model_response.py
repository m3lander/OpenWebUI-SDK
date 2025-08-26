from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_meta import FileMeta
    from ..models.file_model_response_data_type_0 import FileModelResponseDataType0


T = TypeVar("T", bound="FileModelResponse")


@_attrs_define
class FileModelResponse:
    """
    Attributes:
        id (str):
        user_id (str):
        filename (str):
        meta (FileMeta):
        created_at (int):
        updated_at (int):
        hash_ (Union[None, Unset, str]):
        data (Union['FileModelResponseDataType0', None, Unset]):
    """

    id: str
    user_id: str
    filename: str
    meta: "FileMeta"
    created_at: int
    updated_at: int
    hash_: Union[None, Unset, str] = UNSET
    data: Union["FileModelResponseDataType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_model_response_data_type_0 import FileModelResponseDataType0

        id = self.id

        user_id = self.user_id

        filename = self.filename

        meta = self.meta.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        hash_: Union[None, Unset, str]
        if isinstance(self.hash_, Unset):
            hash_ = UNSET
        else:
            hash_ = self.hash_

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, FileModelResponseDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "filename": filename,
                "meta": meta,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_meta import FileMeta
        from ..models.file_model_response_data_type_0 import FileModelResponseDataType0

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        filename = d.pop("filename")

        meta = FileMeta.from_dict(d.pop("meta"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_hash_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hash_ = _parse_hash_(d.pop("hash", UNSET))

        def _parse_data(data: object) -> Union["FileModelResponseDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = FileModelResponseDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FileModelResponseDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        file_model_response = cls(
            id=id,
            user_id=user_id,
            filename=filename,
            meta=meta,
            created_at=created_at,
            updated_at=updated_at,
            hash_=hash_,
            data=data,
        )

        file_model_response.additional_properties = d
        return file_model_response

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
