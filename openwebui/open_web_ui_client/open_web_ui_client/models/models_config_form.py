from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelsConfigForm")


@_attrs_define
class ModelsConfigForm:
    """
    Attributes:
        default_models (Union[None, str]):
        model_order_list (Union[None, list[str]]):
    """

    default_models: Union[None, str]
    model_order_list: Union[None, list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_models: Union[None, str]
        default_models = self.default_models

        model_order_list: Union[None, list[str]]
        if isinstance(self.model_order_list, list):
            model_order_list = self.model_order_list

        else:
            model_order_list = self.model_order_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "DEFAULT_MODELS": default_models,
                "MODEL_ORDER_LIST": model_order_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_default_models(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        default_models = _parse_default_models(d.pop("DEFAULT_MODELS"))

        def _parse_model_order_list(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                model_order_list_type_0 = cast(list[str], data)

                return model_order_list_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        model_order_list = _parse_model_order_list(d.pop("MODEL_ORDER_LIST"))

        models_config_form = cls(
            default_models=default_models,
            model_order_list=model_order_list,
        )

        models_config_form.additional_properties = d
        return models_config_form

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
