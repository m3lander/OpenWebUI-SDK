from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_form_access_control_type_0 import ModelFormAccessControlType0
    from ..models.model_meta import ModelMeta
    from ..models.model_params import ModelParams


T = TypeVar("T", bound="ModelForm")


@_attrs_define
class ModelForm:
    """
    Attributes:
        id (str):
        name (str):
        meta (ModelMeta):
        params (ModelParams):
        base_model_id (Union[None, Unset, str]):
        access_control (Union['ModelFormAccessControlType0', None, Unset]):
        is_active (Union[Unset, bool]):  Default: True.
    """

    id: str
    name: str
    meta: "ModelMeta"
    params: "ModelParams"
    base_model_id: Union[None, Unset, str] = UNSET
    access_control: Union["ModelFormAccessControlType0", None, Unset] = UNSET
    is_active: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_form_access_control_type_0 import ModelFormAccessControlType0

        id = self.id

        name = self.name

        meta = self.meta.to_dict()

        params = self.params.to_dict()

        base_model_id: Union[None, Unset, str]
        if isinstance(self.base_model_id, Unset):
            base_model_id = UNSET
        else:
            base_model_id = self.base_model_id

        access_control: Union[None, Unset, dict[str, Any]]
        if isinstance(self.access_control, Unset):
            access_control = UNSET
        elif isinstance(self.access_control, ModelFormAccessControlType0):
            access_control = self.access_control.to_dict()
        else:
            access_control = self.access_control

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "meta": meta,
                "params": params,
            }
        )
        if base_model_id is not UNSET:
            field_dict["base_model_id"] = base_model_id
        if access_control is not UNSET:
            field_dict["access_control"] = access_control
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_form_access_control_type_0 import ModelFormAccessControlType0
        from ..models.model_meta import ModelMeta
        from ..models.model_params import ModelParams

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        meta = ModelMeta.from_dict(d.pop("meta"))

        params = ModelParams.from_dict(d.pop("params"))

        def _parse_base_model_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        base_model_id = _parse_base_model_id(d.pop("base_model_id", UNSET))

        def _parse_access_control(data: object) -> Union["ModelFormAccessControlType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                access_control_type_0 = ModelFormAccessControlType0.from_dict(data)

                return access_control_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelFormAccessControlType0", None, Unset], data)

        access_control = _parse_access_control(d.pop("access_control", UNSET))

        is_active = d.pop("is_active", UNSET)

        model_form = cls(
            id=id,
            name=name,
            meta=meta,
            params=params,
            base_model_id=base_model_id,
            access_control=access_control,
            is_active=is_active,
        )

        model_form.additional_properties = d
        return model_form

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
