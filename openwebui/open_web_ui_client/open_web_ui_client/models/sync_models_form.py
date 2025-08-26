from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_model import ModelModel


T = TypeVar("T", bound="SyncModelsForm")


@_attrs_define
class SyncModelsForm:
    """
    Attributes:
        models (Union[Unset, list['ModelModel']]):
    """

    models: Union[Unset, list["ModelModel"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        models: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.models, Unset):
            models = []
            for models_item_data in self.models:
                models_item = models_item_data.to_dict()
                models.append(models_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if models is not UNSET:
            field_dict["models"] = models

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_model import ModelModel

        d = dict(src_dict)
        models = []
        _models = d.pop("models", UNSET)
        for models_item_data in _models or []:
            models_item = ModelModel.from_dict(models_item_data)

            models.append(models_item)

        sync_models_form = cls(
            models=models,
        )

        sync_models_form.additional_properties = d
        return sync_models_form

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
