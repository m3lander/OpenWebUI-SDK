from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessFileForm")


@_attrs_define
class ProcessFileForm:
    """
    Attributes:
        file_id (str):
        content (Union[None, Unset, str]):
        collection_name (Union[None, Unset, str]):
    """

    file_id: str
    content: Union[None, Unset, str] = UNSET
    collection_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        content: Union[None, Unset, str]
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        collection_name: Union[None, Unset, str]
        if isinstance(self.collection_name, Unset):
            collection_name = UNSET
        else:
            collection_name = self.collection_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_id": file_id,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if collection_name is not UNSET:
            field_dict["collection_name"] = collection_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("file_id")

        def _parse_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_collection_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        collection_name = _parse_collection_name(d.pop("collection_name", UNSET))

        process_file_form = cls(
            file_id=file_id,
            content=content,
            collection_name=collection_name,
        )

        process_file_form.additional_properties = d
        return process_file_form

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
