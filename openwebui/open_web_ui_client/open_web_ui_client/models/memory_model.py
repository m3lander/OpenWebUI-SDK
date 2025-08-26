from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MemoryModel")


@_attrs_define
class MemoryModel:
    """
    Attributes:
        id (str):
        user_id (str):
        content (str):
        updated_at (int):
        created_at (int):
    """

    id: str
    user_id: str
    content: str
    updated_at: int
    created_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        content = self.content

        updated_at = self.updated_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "content": content,
                "updated_at": updated_at,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        content = d.pop("content")

        updated_at = d.pop("updated_at")

        created_at = d.pop("created_at")

        memory_model = cls(
            id=id,
            user_id=user_id,
            content=content,
            updated_at=updated_at,
            created_at=created_at,
        )

        memory_model.additional_properties = d
        return memory_model

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
