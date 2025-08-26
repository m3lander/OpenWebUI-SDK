from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_form_access_control_type_0 import ChannelFormAccessControlType0
    from ..models.channel_form_data_type_0 import ChannelFormDataType0
    from ..models.channel_form_meta_type_0 import ChannelFormMetaType0


T = TypeVar("T", bound="ChannelForm")


@_attrs_define
class ChannelForm:
    """
    Attributes:
        name (str):
        description (Union[None, Unset, str]):
        data (Union['ChannelFormDataType0', None, Unset]):
        meta (Union['ChannelFormMetaType0', None, Unset]):
        access_control (Union['ChannelFormAccessControlType0', None, Unset]):
    """

    name: str
    description: Union[None, Unset, str] = UNSET
    data: Union["ChannelFormDataType0", None, Unset] = UNSET
    meta: Union["ChannelFormMetaType0", None, Unset] = UNSET
    access_control: Union["ChannelFormAccessControlType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.channel_form_access_control_type_0 import ChannelFormAccessControlType0
        from ..models.channel_form_data_type_0 import ChannelFormDataType0
        from ..models.channel_form_meta_type_0 import ChannelFormMetaType0

        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, ChannelFormDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, ChannelFormMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        access_control: Union[None, Unset, dict[str, Any]]
        if isinstance(self.access_control, Unset):
            access_control = UNSET
        elif isinstance(self.access_control, ChannelFormAccessControlType0):
            access_control = self.access_control.to_dict()
        else:
            access_control = self.access_control

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta
        if access_control is not UNSET:
            field_dict["access_control"] = access_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_form_access_control_type_0 import ChannelFormAccessControlType0
        from ..models.channel_form_data_type_0 import ChannelFormDataType0
        from ..models.channel_form_meta_type_0 import ChannelFormMetaType0

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_data(data: object) -> Union["ChannelFormDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = ChannelFormDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ChannelFormDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_meta(data: object) -> Union["ChannelFormMetaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = ChannelFormMetaType0.from_dict(data)

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ChannelFormMetaType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        def _parse_access_control(data: object) -> Union["ChannelFormAccessControlType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                access_control_type_0 = ChannelFormAccessControlType0.from_dict(data)

                return access_control_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ChannelFormAccessControlType0", None, Unset], data)

        access_control = _parse_access_control(d.pop("access_control", UNSET))

        channel_form = cls(
            name=name,
            description=description,
            data=data,
            meta=meta,
            access_control=access_control,
        )

        channel_form.additional_properties = d
        return channel_form

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
