from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_form_data_type_0 import MessageFormDataType0
    from ..models.message_form_meta_type_0 import MessageFormMetaType0


T = TypeVar("T", bound="MessageForm")


@_attrs_define
class MessageForm:
    """
    Attributes:
        content (str):
        parent_id (Union[None, Unset, str]):
        data (Union['MessageFormDataType0', None, Unset]):
        meta (Union['MessageFormMetaType0', None, Unset]):
    """

    content: str
    parent_id: Union[None, Unset, str] = UNSET
    data: Union["MessageFormDataType0", None, Unset] = UNSET
    meta: Union["MessageFormMetaType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.message_form_data_type_0 import MessageFormDataType0
        from ..models.message_form_meta_type_0 import MessageFormMetaType0

        content = self.content

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, MessageFormDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, MessageFormMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_form_data_type_0 import MessageFormDataType0
        from ..models.message_form_meta_type_0 import MessageFormMetaType0

        d = dict(src_dict)
        content = d.pop("content")

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_data(data: object) -> Union["MessageFormDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = MessageFormDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MessageFormDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_meta(data: object) -> Union["MessageFormMetaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = MessageFormMetaType0.from_dict(data)

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MessageFormMetaType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        message_form = cls(
            content=content,
            parent_id=parent_id,
            data=data,
            meta=meta,
        )

        message_form.additional_properties = d
        return message_form

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
