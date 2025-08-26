from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TTSConfigForm")


@_attrs_define
class TTSConfigForm:
    """
    Attributes:
        openai_api_base_url (str):
        openai_api_key (str):
        api_key (str):
        engine (str):
        model (str):
        voice (str):
        split_on (str):
        azure_speech_region (str):
        azure_speech_base_url (str):
        azure_speech_output_format (str):
    """

    openai_api_base_url: str
    openai_api_key: str
    api_key: str
    engine: str
    model: str
    voice: str
    split_on: str
    azure_speech_region: str
    azure_speech_base_url: str
    azure_speech_output_format: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        openai_api_base_url = self.openai_api_base_url

        openai_api_key = self.openai_api_key

        api_key = self.api_key

        engine = self.engine

        model = self.model

        voice = self.voice

        split_on = self.split_on

        azure_speech_region = self.azure_speech_region

        azure_speech_base_url = self.azure_speech_base_url

        azure_speech_output_format = self.azure_speech_output_format

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OPENAI_API_BASE_URL": openai_api_base_url,
                "OPENAI_API_KEY": openai_api_key,
                "API_KEY": api_key,
                "ENGINE": engine,
                "MODEL": model,
                "VOICE": voice,
                "SPLIT_ON": split_on,
                "AZURE_SPEECH_REGION": azure_speech_region,
                "AZURE_SPEECH_BASE_URL": azure_speech_base_url,
                "AZURE_SPEECH_OUTPUT_FORMAT": azure_speech_output_format,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        openai_api_base_url = d.pop("OPENAI_API_BASE_URL")

        openai_api_key = d.pop("OPENAI_API_KEY")

        api_key = d.pop("API_KEY")

        engine = d.pop("ENGINE")

        model = d.pop("MODEL")

        voice = d.pop("VOICE")

        split_on = d.pop("SPLIT_ON")

        azure_speech_region = d.pop("AZURE_SPEECH_REGION")

        azure_speech_base_url = d.pop("AZURE_SPEECH_BASE_URL")

        azure_speech_output_format = d.pop("AZURE_SPEECH_OUTPUT_FORMAT")

        tts_config_form = cls(
            openai_api_base_url=openai_api_base_url,
            openai_api_key=openai_api_key,
            api_key=api_key,
            engine=engine,
            model=model,
            voice=voice,
            split_on=split_on,
            azure_speech_region=azure_speech_region,
            azure_speech_base_url=azure_speech_base_url,
            azure_speech_output_format=azure_speech_output_format,
        )

        tts_config_form.additional_properties = d
        return tts_config_form

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
