from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag_model_meta_type_0 import TagModelMetaType0


T = TypeVar("T", bound="TagModel")


@_attrs_define
class TagModel:
    """
    Attributes:
        id (str):
        name (str):
        user_id (str):
        meta (Union['TagModelMetaType0', None, Unset]):
    """

    id: str
    name: str
    user_id: str
    meta: Union["TagModelMetaType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tag_model_meta_type_0 import TagModelMetaType0

        id = self.id

        name = self.name

        user_id = self.user_id

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, TagModelMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "user_id": user_id,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tag_model_meta_type_0 import TagModelMetaType0

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        user_id = d.pop("user_id")

        def _parse_meta(data: object) -> Union["TagModelMetaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = TagModelMetaType0.from_dict(data)

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TagModelMetaType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        tag_model = cls(
            id=id,
            name=name,
            user_id=user_id,
            meta=meta,
        )

        tag_model.additional_properties = d
        return tag_model

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
