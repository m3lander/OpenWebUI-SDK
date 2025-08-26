from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note_model_access_control_type_0 import NoteModelAccessControlType0
    from ..models.note_model_data_type_0 import NoteModelDataType0
    from ..models.note_model_meta_type_0 import NoteModelMetaType0


T = TypeVar("T", bound="NoteModel")


@_attrs_define
class NoteModel:
    """
    Attributes:
        id (str):
        user_id (str):
        title (str):
        created_at (int):
        updated_at (int):
        data (Union['NoteModelDataType0', None, Unset]):
        meta (Union['NoteModelMetaType0', None, Unset]):
        access_control (Union['NoteModelAccessControlType0', None, Unset]):
    """

    id: str
    user_id: str
    title: str
    created_at: int
    updated_at: int
    data: Union["NoteModelDataType0", None, Unset] = UNSET
    meta: Union["NoteModelMetaType0", None, Unset] = UNSET
    access_control: Union["NoteModelAccessControlType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.note_model_access_control_type_0 import NoteModelAccessControlType0
        from ..models.note_model_data_type_0 import NoteModelDataType0
        from ..models.note_model_meta_type_0 import NoteModelMetaType0

        id = self.id

        user_id = self.user_id

        title = self.title

        created_at = self.created_at

        updated_at = self.updated_at

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, NoteModelDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, NoteModelMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        access_control: Union[None, Unset, dict[str, Any]]
        if isinstance(self.access_control, Unset):
            access_control = UNSET
        elif isinstance(self.access_control, NoteModelAccessControlType0):
            access_control = self.access_control.to_dict()
        else:
            access_control = self.access_control

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "title": title,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta
        if access_control is not UNSET:
            field_dict["access_control"] = access_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.note_model_access_control_type_0 import NoteModelAccessControlType0
        from ..models.note_model_data_type_0 import NoteModelDataType0
        from ..models.note_model_meta_type_0 import NoteModelMetaType0

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        title = d.pop("title")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_data(data: object) -> Union["NoteModelDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = NoteModelDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NoteModelDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_meta(data: object) -> Union["NoteModelMetaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = NoteModelMetaType0.from_dict(data)

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NoteModelMetaType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        def _parse_access_control(data: object) -> Union["NoteModelAccessControlType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                access_control_type_0 = NoteModelAccessControlType0.from_dict(data)

                return access_control_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NoteModelAccessControlType0", None, Unset], data)

        access_control = _parse_access_control(d.pop("access_control", UNSET))

        note_model = cls(
            id=id,
            user_id=user_id,
            title=title,
            created_at=created_at,
            updated_at=updated_at,
            data=data,
            meta=meta,
            access_control=access_control,
        )

        note_model.additional_properties = d
        return note_model

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
