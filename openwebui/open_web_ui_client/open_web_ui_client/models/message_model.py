from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_model_data_type_0 import MessageModelDataType0
    from ..models.message_model_meta_type_0 import MessageModelMetaType0


T = TypeVar("T", bound="MessageModel")


@_attrs_define
class MessageModel:
    """
    Attributes:
        id (str):
        user_id (str):
        content (str):
        created_at (int):
        updated_at (int):
        channel_id (Union[None, Unset, str]):
        parent_id (Union[None, Unset, str]):
        data (Union['MessageModelDataType0', None, Unset]):
        meta (Union['MessageModelMetaType0', None, Unset]):
    """

    id: str
    user_id: str
    content: str
    created_at: int
    updated_at: int
    channel_id: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    data: Union["MessageModelDataType0", None, Unset] = UNSET
    meta: Union["MessageModelMetaType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.message_model_data_type_0 import MessageModelDataType0
        from ..models.message_model_meta_type_0 import MessageModelMetaType0

        id = self.id

        user_id = self.user_id

        content = self.content

        created_at = self.created_at

        updated_at = self.updated_at

        channel_id: Union[None, Unset, str]
        if isinstance(self.channel_id, Unset):
            channel_id = UNSET
        else:
            channel_id = self.channel_id

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, MessageModelDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, MessageModelMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "content": content,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_model_data_type_0 import MessageModelDataType0
        from ..models.message_model_meta_type_0 import MessageModelMetaType0

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        content = d.pop("content")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_channel_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        channel_id = _parse_channel_id(d.pop("channel_id", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_data(data: object) -> Union["MessageModelDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = MessageModelDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MessageModelDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_meta(data: object) -> Union["MessageModelMetaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = MessageModelMetaType0.from_dict(data)

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MessageModelMetaType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        message_model = cls(
            id=id,
            user_id=user_id,
            content=content,
            created_at=created_at,
            updated_at=updated_at,
            channel_id=channel_id,
            parent_id=parent_id,
            data=data,
            meta=meta,
        )

        message_model.additional_properties = d
        return message_model

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
