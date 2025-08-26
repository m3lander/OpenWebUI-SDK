from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

T = TypeVar("T", bound="BodyUploadPipelineApiV1PipelinesUploadPost")


@_attrs_define
class BodyUploadPipelineApiV1PipelinesUploadPost:
    """
    Attributes:
        url_idx (int):
        file (File):
    """

    url_idx: int
    file: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url_idx = self.url_idx

        file = self.file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "urlIdx": url_idx,
                "file": file,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("urlIdx", (None, str(self.url_idx).encode(), "text/plain")))

        files.append(("file", self.file.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url_idx = d.pop("urlIdx")

        file = File(payload=BytesIO(d.pop("file")))

        body_upload_pipeline_api_v1_pipelines_upload_post = cls(
            url_idx=url_idx,
            file=file,
        )

        body_upload_pipeline_api_v1_pipelines_upload_post.additional_properties = d
        return body_upload_pipeline_api_v1_pipelines_upload_post

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
