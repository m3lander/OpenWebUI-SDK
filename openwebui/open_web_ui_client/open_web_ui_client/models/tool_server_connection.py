from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tool_server_connection_config_type_0 import ToolServerConnectionConfigType0


T = TypeVar("T", bound="ToolServerConnection")


@_attrs_define
class ToolServerConnection:
    """
    Attributes:
        url (str):
        path (str):
        auth_type (Union[None, str]):
        key (Union[None, str]):
        config (Union['ToolServerConnectionConfigType0', None]):
    """

    url: str
    path: str
    auth_type: Union[None, str]
    key: Union[None, str]
    config: Union["ToolServerConnectionConfigType0", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_server_connection_config_type_0 import ToolServerConnectionConfigType0

        url = self.url

        path = self.path

        auth_type: Union[None, str]
        auth_type = self.auth_type

        key: Union[None, str]
        key = self.key

        config: Union[None, dict[str, Any]]
        if isinstance(self.config, ToolServerConnectionConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "path": path,
                "auth_type": auth_type,
                "key": key,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_server_connection_config_type_0 import ToolServerConnectionConfigType0

        d = dict(src_dict)
        url = d.pop("url")

        path = d.pop("path")

        def _parse_auth_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        auth_type = _parse_auth_type(d.pop("auth_type"))

        def _parse_key(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        key = _parse_key(d.pop("key"))

        def _parse_config(data: object) -> Union["ToolServerConnectionConfigType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = ToolServerConnectionConfigType0.from_dict(data)

                return config_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ToolServerConnectionConfigType0", None], data)

        config = _parse_config(d.pop("config"))

        tool_server_connection = cls(
            url=url,
            path=path,
            auth_type=auth_type,
            key=key,
            config=config,
        )

        tool_server_connection.additional_properties = d
        return tool_server_connection

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
