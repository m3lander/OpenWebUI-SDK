from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="STTConfigForm")


@_attrs_define
class STTConfigForm:
    """
    Attributes:
        openai_api_base_url (str):
        openai_api_key (str):
        engine (str):
        model (str):
        whisper_model (str):
        deepgram_api_key (str):
        azure_api_key (str):
        azure_region (str):
        azure_locales (str):
        azure_base_url (str):
        azure_max_speakers (str):
        supported_content_types (Union[Unset, list[str]]):
    """

    openai_api_base_url: str
    openai_api_key: str
    engine: str
    model: str
    whisper_model: str
    deepgram_api_key: str
    azure_api_key: str
    azure_region: str
    azure_locales: str
    azure_base_url: str
    azure_max_speakers: str
    supported_content_types: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        openai_api_base_url = self.openai_api_base_url

        openai_api_key = self.openai_api_key

        engine = self.engine

        model = self.model

        whisper_model = self.whisper_model

        deepgram_api_key = self.deepgram_api_key

        azure_api_key = self.azure_api_key

        azure_region = self.azure_region

        azure_locales = self.azure_locales

        azure_base_url = self.azure_base_url

        azure_max_speakers = self.azure_max_speakers

        supported_content_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.supported_content_types, Unset):
            supported_content_types = self.supported_content_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OPENAI_API_BASE_URL": openai_api_base_url,
                "OPENAI_API_KEY": openai_api_key,
                "ENGINE": engine,
                "MODEL": model,
                "WHISPER_MODEL": whisper_model,
                "DEEPGRAM_API_KEY": deepgram_api_key,
                "AZURE_API_KEY": azure_api_key,
                "AZURE_REGION": azure_region,
                "AZURE_LOCALES": azure_locales,
                "AZURE_BASE_URL": azure_base_url,
                "AZURE_MAX_SPEAKERS": azure_max_speakers,
            }
        )
        if supported_content_types is not UNSET:
            field_dict["SUPPORTED_CONTENT_TYPES"] = supported_content_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        openai_api_base_url = d.pop("OPENAI_API_BASE_URL")

        openai_api_key = d.pop("OPENAI_API_KEY")

        engine = d.pop("ENGINE")

        model = d.pop("MODEL")

        whisper_model = d.pop("WHISPER_MODEL")

        deepgram_api_key = d.pop("DEEPGRAM_API_KEY")

        azure_api_key = d.pop("AZURE_API_KEY")

        azure_region = d.pop("AZURE_REGION")

        azure_locales = d.pop("AZURE_LOCALES")

        azure_base_url = d.pop("AZURE_BASE_URL")

        azure_max_speakers = d.pop("AZURE_MAX_SPEAKERS")

        supported_content_types = cast(list[str], d.pop("SUPPORTED_CONTENT_TYPES", UNSET))

        stt_config_form = cls(
            openai_api_base_url=openai_api_base_url,
            openai_api_key=openai_api_key,
            engine=engine,
            model=model,
            whisper_model=whisper_model,
            deepgram_api_key=deepgram_api_key,
            azure_api_key=azure_api_key,
            azure_region=azure_region,
            azure_locales=azure_locales,
            azure_base_url=azure_base_url,
            azure_max_speakers=azure_max_speakers,
            supported_content_types=supported_content_types,
        )

        stt_config_form.additional_properties = d
        return stt_config_form

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
