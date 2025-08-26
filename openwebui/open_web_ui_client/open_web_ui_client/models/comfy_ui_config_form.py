from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.comfy_ui_config_form_comfyuiworkflownodes_item import ComfyUIConfigFormCOMFYUIWORKFLOWNODESItem


T = TypeVar("T", bound="ComfyUIConfigForm")


@_attrs_define
class ComfyUIConfigForm:
    """
    Attributes:
        comfyui_base_url (str):
        comfyui_api_key (str):
        comfyui_workflow (str):
        comfyui_workflow_nodes (list['ComfyUIConfigFormCOMFYUIWORKFLOWNODESItem']):
    """

    comfyui_base_url: str
    comfyui_api_key: str
    comfyui_workflow: str
    comfyui_workflow_nodes: list["ComfyUIConfigFormCOMFYUIWORKFLOWNODESItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comfyui_base_url = self.comfyui_base_url

        comfyui_api_key = self.comfyui_api_key

        comfyui_workflow = self.comfyui_workflow

        comfyui_workflow_nodes = []
        for comfyui_workflow_nodes_item_data in self.comfyui_workflow_nodes:
            comfyui_workflow_nodes_item = comfyui_workflow_nodes_item_data.to_dict()
            comfyui_workflow_nodes.append(comfyui_workflow_nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "COMFYUI_BASE_URL": comfyui_base_url,
                "COMFYUI_API_KEY": comfyui_api_key,
                "COMFYUI_WORKFLOW": comfyui_workflow,
                "COMFYUI_WORKFLOW_NODES": comfyui_workflow_nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comfy_ui_config_form_comfyuiworkflownodes_item import ComfyUIConfigFormCOMFYUIWORKFLOWNODESItem

        d = dict(src_dict)
        comfyui_base_url = d.pop("COMFYUI_BASE_URL")

        comfyui_api_key = d.pop("COMFYUI_API_KEY")

        comfyui_workflow = d.pop("COMFYUI_WORKFLOW")

        comfyui_workflow_nodes = []
        _comfyui_workflow_nodes = d.pop("COMFYUI_WORKFLOW_NODES")
        for comfyui_workflow_nodes_item_data in _comfyui_workflow_nodes:
            comfyui_workflow_nodes_item = ComfyUIConfigFormCOMFYUIWORKFLOWNODESItem.from_dict(
                comfyui_workflow_nodes_item_data
            )

            comfyui_workflow_nodes.append(comfyui_workflow_nodes_item)

        comfy_ui_config_form = cls(
            comfyui_base_url=comfyui_base_url,
            comfyui_api_key=comfyui_api_key,
            comfyui_workflow=comfyui_workflow,
            comfyui_workflow_nodes=comfyui_workflow_nodes,
        )

        comfy_ui_config_form.additional_properties = d
        return comfy_ui_config_form

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
