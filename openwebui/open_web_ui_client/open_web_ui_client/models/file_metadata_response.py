from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_metadata_response_meta import FileMetadataResponseMeta


T = TypeVar("T", bound="FileMetadataResponse")


@_attrs_define
class FileMetadataResponse:
    """
    Attributes:
        id (str):
        meta (FileMetadataResponseMeta):
        created_at (int):
        updated_at (int):
    """

    id: str
    meta: "FileMetadataResponseMeta"
    created_at: int
    updated_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        meta = self.meta.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "meta": meta,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_metadata_response_meta import FileMetadataResponseMeta

        d = dict(src_dict)
        id = d.pop("id")

        meta = FileMetadataResponseMeta.from_dict(d.pop("meta"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        file_metadata_response = cls(
            id=id,
            meta=meta,
            created_at=created_at,
            updated_at=updated_at,
        )

        file_metadata_response.additional_properties = d
        return file_metadata_response

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
