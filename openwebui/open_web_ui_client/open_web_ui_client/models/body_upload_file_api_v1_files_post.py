import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.body_upload_file_api_v1_files_post_metadata_type_0 import BodyUploadFileApiV1FilesPostMetadataType0


T = TypeVar("T", bound="BodyUploadFileApiV1FilesPost")


@_attrs_define
class BodyUploadFileApiV1FilesPost:
    """
    Attributes:
        file (File):
        metadata (Union['BodyUploadFileApiV1FilesPostMetadataType0', None, Unset, str]):
    """

    file: File
    metadata: Union["BodyUploadFileApiV1FilesPostMetadataType0", None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.body_upload_file_api_v1_files_post_metadata_type_0 import (
            BodyUploadFileApiV1FilesPostMetadataType0,
        )

        file = self.file.to_tuple()

        metadata: Union[None, Unset, dict[str, Any], str]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, BodyUploadFileApiV1FilesPostMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.metadata, Unset):
            if isinstance(self.metadata, BodyUploadFileApiV1FilesPostMetadataType0):
                files.append(("metadata", (None, json.dumps(self.metadata.to_dict()).encode(), "application/json")))
            elif isinstance(self.metadata, str):
                files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))
            else:
                files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.body_upload_file_api_v1_files_post_metadata_type_0 import (
            BodyUploadFileApiV1FilesPostMetadataType0,
        )

        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        def _parse_metadata(data: object) -> Union["BodyUploadFileApiV1FilesPostMetadataType0", None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = BodyUploadFileApiV1FilesPostMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BodyUploadFileApiV1FilesPostMetadataType0", None, Unset, str], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        body_upload_file_api_v1_files_post = cls(
            file=file,
            metadata=metadata,
        )

        body_upload_file_api_v1_files_post.additional_properties = d
        return body_upload_file_api_v1_files_post

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
