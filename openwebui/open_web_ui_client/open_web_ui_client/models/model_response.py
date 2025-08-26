from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_meta import ModelMeta
    from ..models.model_params import ModelParams
    from ..models.model_response_access_control_type_0 import ModelResponseAccessControlType0


T = TypeVar("T", bound="ModelResponse")


@_attrs_define
class ModelResponse:
    """
    Attributes:
        id (str):
        user_id (str):
        name (str):
        params (ModelParams):
        meta (ModelMeta):
        is_active (bool):
        updated_at (int):
        created_at (int):
        base_model_id (Union[None, Unset, str]):
        access_control (Union['ModelResponseAccessControlType0', None, Unset]):
    """

    id: str
    user_id: str
    name: str
    params: "ModelParams"
    meta: "ModelMeta"
    is_active: bool
    updated_at: int
    created_at: int
    base_model_id: Union[None, Unset, str] = UNSET
    access_control: Union["ModelResponseAccessControlType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_response_access_control_type_0 import ModelResponseAccessControlType0

        id = self.id

        user_id = self.user_id

        name = self.name

        params = self.params.to_dict()

        meta = self.meta.to_dict()

        is_active = self.is_active

        updated_at = self.updated_at

        created_at = self.created_at

        base_model_id: Union[None, Unset, str]
        if isinstance(self.base_model_id, Unset):
            base_model_id = UNSET
        else:
            base_model_id = self.base_model_id

        access_control: Union[None, Unset, dict[str, Any]]
        if isinstance(self.access_control, Unset):
            access_control = UNSET
        elif isinstance(self.access_control, ModelResponseAccessControlType0):
            access_control = self.access_control.to_dict()
        else:
            access_control = self.access_control

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "name": name,
                "params": params,
                "meta": meta,
                "is_active": is_active,
                "updated_at": updated_at,
                "created_at": created_at,
            }
        )
        if base_model_id is not UNSET:
            field_dict["base_model_id"] = base_model_id
        if access_control is not UNSET:
            field_dict["access_control"] = access_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_meta import ModelMeta
        from ..models.model_params import ModelParams
        from ..models.model_response_access_control_type_0 import ModelResponseAccessControlType0

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        name = d.pop("name")

        params = ModelParams.from_dict(d.pop("params"))

        meta = ModelMeta.from_dict(d.pop("meta"))

        is_active = d.pop("is_active")

        updated_at = d.pop("updated_at")

        created_at = d.pop("created_at")

        def _parse_base_model_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        base_model_id = _parse_base_model_id(d.pop("base_model_id", UNSET))

        def _parse_access_control(data: object) -> Union["ModelResponseAccessControlType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                access_control_type_0 = ModelResponseAccessControlType0.from_dict(data)

                return access_control_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelResponseAccessControlType0", None, Unset], data)

        access_control = _parse_access_control(d.pop("access_control", UNSET))

        model_response = cls(
            id=id,
            user_id=user_id,
            name=name,
            params=params,
            meta=meta,
            is_active=is_active,
            updated_at=updated_at,
            created_at=created_at,
            base_model_id=base_model_id,
            access_control=access_control,
        )

        model_response.additional_properties = d
        return model_response

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
