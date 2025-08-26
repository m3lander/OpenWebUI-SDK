from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.automatic_1111_config_form import Automatic1111ConfigForm
    from ..models.comfy_ui_config_form import ComfyUIConfigForm
    from ..models.gemini_config_form import GeminiConfigForm
    from ..models.open_ai_config_form import OpenAIConfigForm


T = TypeVar("T", bound="ConfigForm")


@_attrs_define
class ConfigForm:
    """
    Attributes:
        enabled (bool):
        engine (str):
        prompt_generation (bool):
        openai (OpenAIConfigForm):
        automatic1111 (Automatic1111ConfigForm):
        comfyui (ComfyUIConfigForm):
        gemini (GeminiConfigForm):
    """

    enabled: bool
    engine: str
    prompt_generation: bool
    openai: "OpenAIConfigForm"
    automatic1111: "Automatic1111ConfigForm"
    comfyui: "ComfyUIConfigForm"
    gemini: "GeminiConfigForm"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        engine = self.engine

        prompt_generation = self.prompt_generation

        openai = self.openai.to_dict()

        automatic1111 = self.automatic1111.to_dict()

        comfyui = self.comfyui.to_dict()

        gemini = self.gemini.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "engine": engine,
                "prompt_generation": prompt_generation,
                "openai": openai,
                "automatic1111": automatic1111,
                "comfyui": comfyui,
                "gemini": gemini,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automatic_1111_config_form import Automatic1111ConfigForm
        from ..models.comfy_ui_config_form import ComfyUIConfigForm
        from ..models.gemini_config_form import GeminiConfigForm
        from ..models.open_ai_config_form import OpenAIConfigForm

        d = dict(src_dict)
        enabled = d.pop("enabled")

        engine = d.pop("engine")

        prompt_generation = d.pop("prompt_generation")

        openai = OpenAIConfigForm.from_dict(d.pop("openai"))

        automatic1111 = Automatic1111ConfigForm.from_dict(d.pop("automatic1111"))

        comfyui = ComfyUIConfigForm.from_dict(d.pop("comfyui"))

        gemini = GeminiConfigForm.from_dict(d.pop("gemini"))

        config_form = cls(
            enabled=enabled,
            engine=engine,
            prompt_generation=prompt_generation,
            openai=openai,
            automatic1111=automatic1111,
            comfyui=comfyui,
            gemini=gemini,
        )

        config_form.additional_properties = d
        return config_form

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
