from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tool_server_connection import ToolServerConnection


T = TypeVar("T", bound="ToolServersConfigForm")


@_attrs_define
class ToolServersConfigForm:
    """
    Attributes:
        tool_server_connections (list['ToolServerConnection']):
    """

    tool_server_connections: list["ToolServerConnection"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tool_server_connections = []
        for tool_server_connections_item_data in self.tool_server_connections:
            tool_server_connections_item = tool_server_connections_item_data.to_dict()
            tool_server_connections.append(tool_server_connections_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "TOOL_SERVER_CONNECTIONS": tool_server_connections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_server_connection import ToolServerConnection

        d = dict(src_dict)
        tool_server_connections = []
        _tool_server_connections = d.pop("TOOL_SERVER_CONNECTIONS")
        for tool_server_connections_item_data in _tool_server_connections:
            tool_server_connections_item = ToolServerConnection.from_dict(tool_server_connections_item_data)

            tool_server_connections.append(tool_server_connections_item)

        tool_servers_config_form = cls(
            tool_server_connections=tool_server_connections,
        )

        tool_servers_config_form.additional_properties = d
        return tool_servers_config_form

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
