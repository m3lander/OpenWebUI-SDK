from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_embed_form_options_type_0 import GenerateEmbedFormOptionsType0


T = TypeVar("T", bound="GenerateEmbedForm")


@_attrs_define
class GenerateEmbedForm:
    """
    Attributes:
        model (str):
        input_ (Union[list[str], str]):
        truncate (Union[None, Unset, bool]):
        options (Union['GenerateEmbedFormOptionsType0', None, Unset]):
        keep_alive (Union[None, Unset, int, str]):
    """

    model: str
    input_: Union[list[str], str]
    truncate: Union[None, Unset, bool] = UNSET
    options: Union["GenerateEmbedFormOptionsType0", None, Unset] = UNSET
    keep_alive: Union[None, Unset, int, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.generate_embed_form_options_type_0 import GenerateEmbedFormOptionsType0

        model = self.model

        input_: Union[list[str], str]
        if isinstance(self.input_, list):
            input_ = self.input_

        else:
            input_ = self.input_

        truncate: Union[None, Unset, bool]
        if isinstance(self.truncate, Unset):
            truncate = UNSET
        else:
            truncate = self.truncate

        options: Union[None, Unset, dict[str, Any]]
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, GenerateEmbedFormOptionsType0):
            options = self.options.to_dict()
        else:
            options = self.options

        keep_alive: Union[None, Unset, int, str]
        if isinstance(self.keep_alive, Unset):
            keep_alive = UNSET
        else:
            keep_alive = self.keep_alive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "input": input_,
            }
        )
        if truncate is not UNSET:
            field_dict["truncate"] = truncate
        if options is not UNSET:
            field_dict["options"] = options
        if keep_alive is not UNSET:
            field_dict["keep_alive"] = keep_alive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_embed_form_options_type_0 import GenerateEmbedFormOptionsType0

        d = dict(src_dict)
        model = d.pop("model")

        def _parse_input_(data: object) -> Union[list[str], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                input_type_0 = cast(list[str], data)

                return input_type_0
            except:  # noqa: E722
                pass
            return cast(Union[list[str], str], data)

        input_ = _parse_input_(d.pop("input"))

        def _parse_truncate(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        truncate = _parse_truncate(d.pop("truncate", UNSET))

        def _parse_options(data: object) -> Union["GenerateEmbedFormOptionsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = GenerateEmbedFormOptionsType0.from_dict(data)

                return options_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GenerateEmbedFormOptionsType0", None, Unset], data)

        options = _parse_options(d.pop("options", UNSET))

        def _parse_keep_alive(data: object) -> Union[None, Unset, int, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int, str], data)

        keep_alive = _parse_keep_alive(d.pop("keep_alive", UNSET))

        generate_embed_form = cls(
            model=model,
            input_=input_,
            truncate=truncate,
            options=options,
            keep_alive=keep_alive,
        )

        generate_embed_form.additional_properties = d
        return generate_embed_form

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
