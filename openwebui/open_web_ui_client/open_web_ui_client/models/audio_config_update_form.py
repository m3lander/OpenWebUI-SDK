from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stt_config_form import STTConfigForm
    from ..models.tts_config_form import TTSConfigForm


T = TypeVar("T", bound="AudioConfigUpdateForm")


@_attrs_define
class AudioConfigUpdateForm:
    """
    Attributes:
        tts (TTSConfigForm):
        stt (STTConfigForm):
    """

    tts: "TTSConfigForm"
    stt: "STTConfigForm"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tts = self.tts.to_dict()

        stt = self.stt.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tts": tts,
                "stt": stt,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stt_config_form import STTConfigForm
        from ..models.tts_config_form import TTSConfigForm

        d = dict(src_dict)
        tts = TTSConfigForm.from_dict(d.pop("tts"))

        stt = STTConfigForm.from_dict(d.pop("stt"))

        audio_config_update_form = cls(
            tts=tts,
            stt=stt,
        )

        audio_config_update_form.additional_properties = d
        return audio_config_update_form

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
