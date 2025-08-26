from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PushModelForm")


@_attrs_define
class PushModelForm:
    """
    Attributes:
        model (str):
        insecure (Union[None, Unset, bool]):
        stream (Union[None, Unset, bool]):
    """

    model: str
    insecure: Union[None, Unset, bool] = UNSET
    stream: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        insecure: Union[None, Unset, bool]
        if isinstance(self.insecure, Unset):
            insecure = UNSET
        else:
            insecure = self.insecure

        stream: Union[None, Unset, bool]
        if isinstance(self.stream, Unset):
            stream = UNSET
        else:
            stream = self.stream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
            }
        )
        if insecure is not UNSET:
            field_dict["insecure"] = insecure
        if stream is not UNSET:
            field_dict["stream"] = stream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        def _parse_insecure(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        insecure = _parse_insecure(d.pop("insecure", UNSET))

        def _parse_stream(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        stream = _parse_stream(d.pop("stream", UNSET))

        push_model_form = cls(
            model=model,
            insecure=insecure,
            stream=stream,
        )

        push_model_form.additional_properties = d
        return push_model_form

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
