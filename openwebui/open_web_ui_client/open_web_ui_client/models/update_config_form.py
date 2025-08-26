from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_config_form_evaluationarenamodels_type_0_item import (
        UpdateConfigFormEVALUATIONARENAMODELSType0Item,
    )


T = TypeVar("T", bound="UpdateConfigForm")


@_attrs_define
class UpdateConfigForm:
    """
    Attributes:
        enable_evaluation_arena_models (Union[None, Unset, bool]):
        evaluation_arena_models (Union[None, Unset, list['UpdateConfigFormEVALUATIONARENAMODELSType0Item']]):
    """

    enable_evaluation_arena_models: Union[None, Unset, bool] = UNSET
    evaluation_arena_models: Union[None, Unset, list["UpdateConfigFormEVALUATIONARENAMODELSType0Item"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_evaluation_arena_models: Union[None, Unset, bool]
        if isinstance(self.enable_evaluation_arena_models, Unset):
            enable_evaluation_arena_models = UNSET
        else:
            enable_evaluation_arena_models = self.enable_evaluation_arena_models

        evaluation_arena_models: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.evaluation_arena_models, Unset):
            evaluation_arena_models = UNSET
        elif isinstance(self.evaluation_arena_models, list):
            evaluation_arena_models = []
            for evaluation_arena_models_type_0_item_data in self.evaluation_arena_models:
                evaluation_arena_models_type_0_item = evaluation_arena_models_type_0_item_data.to_dict()
                evaluation_arena_models.append(evaluation_arena_models_type_0_item)

        else:
            evaluation_arena_models = self.evaluation_arena_models

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_evaluation_arena_models is not UNSET:
            field_dict["ENABLE_EVALUATION_ARENA_MODELS"] = enable_evaluation_arena_models
        if evaluation_arena_models is not UNSET:
            field_dict["EVALUATION_ARENA_MODELS"] = evaluation_arena_models

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_config_form_evaluationarenamodels_type_0_item import (
            UpdateConfigFormEVALUATIONARENAMODELSType0Item,
        )

        d = dict(src_dict)

        def _parse_enable_evaluation_arena_models(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_evaluation_arena_models = _parse_enable_evaluation_arena_models(
            d.pop("ENABLE_EVALUATION_ARENA_MODELS", UNSET)
        )

        def _parse_evaluation_arena_models(
            data: object,
        ) -> Union[None, Unset, list["UpdateConfigFormEVALUATIONARENAMODELSType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evaluation_arena_models_type_0 = []
                _evaluation_arena_models_type_0 = data
                for evaluation_arena_models_type_0_item_data in _evaluation_arena_models_type_0:
                    evaluation_arena_models_type_0_item = UpdateConfigFormEVALUATIONARENAMODELSType0Item.from_dict(
                        evaluation_arena_models_type_0_item_data
                    )

                    evaluation_arena_models_type_0.append(evaluation_arena_models_type_0_item)

                return evaluation_arena_models_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["UpdateConfigFormEVALUATIONARENAMODELSType0Item"]], data)

        evaluation_arena_models = _parse_evaluation_arena_models(d.pop("EVALUATION_ARENA_MODELS", UNSET))

        update_config_form = cls(
            enable_evaluation_arena_models=enable_evaluation_arena_models,
            evaluation_arena_models=evaluation_arena_models,
        )

        update_config_form.additional_properties = d
        return update_config_form

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
