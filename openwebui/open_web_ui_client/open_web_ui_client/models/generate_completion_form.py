from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_completion_form_format_type_0 import GenerateCompletionFormFormatType0
    from ..models.generate_completion_form_options_type_0 import GenerateCompletionFormOptionsType0


T = TypeVar("T", bound="GenerateCompletionForm")


@_attrs_define
class GenerateCompletionForm:
    """
    Attributes:
        model (str):
        prompt (str):
        suffix (Union[None, Unset, str]):
        images (Union[None, Unset, list[str]]):
        format_ (Union['GenerateCompletionFormFormatType0', None, Unset, str]):
        options (Union['GenerateCompletionFormOptionsType0', None, Unset]):
        system (Union[None, Unset, str]):
        template (Union[None, Unset, str]):
        context (Union[None, Unset, list[int]]):
        stream (Union[None, Unset, bool]):  Default: True.
        raw (Union[None, Unset, bool]):
        keep_alive (Union[None, Unset, int, str]):
    """

    model: str
    prompt: str
    suffix: Union[None, Unset, str] = UNSET
    images: Union[None, Unset, list[str]] = UNSET
    format_: Union["GenerateCompletionFormFormatType0", None, Unset, str] = UNSET
    options: Union["GenerateCompletionFormOptionsType0", None, Unset] = UNSET
    system: Union[None, Unset, str] = UNSET
    template: Union[None, Unset, str] = UNSET
    context: Union[None, Unset, list[int]] = UNSET
    stream: Union[None, Unset, bool] = True
    raw: Union[None, Unset, bool] = UNSET
    keep_alive: Union[None, Unset, int, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.generate_completion_form_format_type_0 import GenerateCompletionFormFormatType0
        from ..models.generate_completion_form_options_type_0 import GenerateCompletionFormOptionsType0

        model = self.model

        prompt = self.prompt

        suffix: Union[None, Unset, str]
        if isinstance(self.suffix, Unset):
            suffix = UNSET
        else:
            suffix = self.suffix

        images: Union[None, Unset, list[str]]
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = self.images

        else:
            images = self.images

        format_: Union[None, Unset, dict[str, Any], str]
        if isinstance(self.format_, Unset):
            format_ = UNSET
        elif isinstance(self.format_, GenerateCompletionFormFormatType0):
            format_ = self.format_.to_dict()
        else:
            format_ = self.format_

        options: Union[None, Unset, dict[str, Any]]
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, GenerateCompletionFormOptionsType0):
            options = self.options.to_dict()
        else:
            options = self.options

        system: Union[None, Unset, str]
        if isinstance(self.system, Unset):
            system = UNSET
        else:
            system = self.system

        template: Union[None, Unset, str]
        if isinstance(self.template, Unset):
            template = UNSET
        else:
            template = self.template

        context: Union[None, Unset, list[int]]
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, list):
            context = self.context

        else:
            context = self.context

        stream: Union[None, Unset, bool]
        if isinstance(self.stream, Unset):
            stream = UNSET
        else:
            stream = self.stream

        raw: Union[None, Unset, bool]
        if isinstance(self.raw, Unset):
            raw = UNSET
        else:
            raw = self.raw

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
                "prompt": prompt,
            }
        )
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if images is not UNSET:
            field_dict["images"] = images
        if format_ is not UNSET:
            field_dict["format"] = format_
        if options is not UNSET:
            field_dict["options"] = options
        if system is not UNSET:
            field_dict["system"] = system
        if template is not UNSET:
            field_dict["template"] = template
        if context is not UNSET:
            field_dict["context"] = context
        if stream is not UNSET:
            field_dict["stream"] = stream
        if raw is not UNSET:
            field_dict["raw"] = raw
        if keep_alive is not UNSET:
            field_dict["keep_alive"] = keep_alive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_completion_form_format_type_0 import GenerateCompletionFormFormatType0
        from ..models.generate_completion_form_options_type_0 import GenerateCompletionFormOptionsType0

        d = dict(src_dict)
        model = d.pop("model")

        prompt = d.pop("prompt")

        def _parse_suffix(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suffix = _parse_suffix(d.pop("suffix", UNSET))

        def _parse_images(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = cast(list[str], data)

                return images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        images = _parse_images(d.pop("images", UNSET))

        def _parse_format_(data: object) -> Union["GenerateCompletionFormFormatType0", None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                format_type_0 = GenerateCompletionFormFormatType0.from_dict(data)

                return format_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GenerateCompletionFormFormatType0", None, Unset, str], data)

        format_ = _parse_format_(d.pop("format", UNSET))

        def _parse_options(data: object) -> Union["GenerateCompletionFormOptionsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = GenerateCompletionFormOptionsType0.from_dict(data)

                return options_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GenerateCompletionFormOptionsType0", None, Unset], data)

        options = _parse_options(d.pop("options", UNSET))

        def _parse_system(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        system = _parse_system(d.pop("system", UNSET))

        def _parse_template(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        template = _parse_template(d.pop("template", UNSET))

        def _parse_context(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                context_type_0 = cast(list[int], data)

                return context_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        context = _parse_context(d.pop("context", UNSET))

        def _parse_stream(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        stream = _parse_stream(d.pop("stream", UNSET))

        def _parse_raw(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        raw = _parse_raw(d.pop("raw", UNSET))

        def _parse_keep_alive(data: object) -> Union[None, Unset, int, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int, str], data)

        keep_alive = _parse_keep_alive(d.pop("keep_alive", UNSET))

        generate_completion_form = cls(
            model=model,
            prompt=prompt,
            suffix=suffix,
            images=images,
            format_=format_,
            options=options,
            system=system,
            template=template,
            context=context,
            stream=stream,
            raw=raw,
            keep_alive=keep_alive,
        )

        generate_completion_form.additional_properties = d
        return generate_completion_form

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
