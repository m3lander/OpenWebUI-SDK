from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LdapServerConfig")


@_attrs_define
class LdapServerConfig:
    """
    Attributes:
        label (str):
        host (str):
        app_dn (str):
        app_dn_password (str):
        search_base (str):
        port (Union[None, Unset, int]):
        attribute_for_mail (Union[Unset, str]):  Default: 'mail'.
        attribute_for_username (Union[Unset, str]):  Default: 'uid'.
        search_filters (Union[Unset, str]):  Default: ''.
        use_tls (Union[Unset, bool]):  Default: True.
        certificate_path (Union[None, Unset, str]):
        validate_cert (Union[Unset, bool]):  Default: True.
        ciphers (Union[None, Unset, str]):  Default: 'ALL'.
    """

    label: str
    host: str
    app_dn: str
    app_dn_password: str
    search_base: str
    port: Union[None, Unset, int] = UNSET
    attribute_for_mail: Union[Unset, str] = "mail"
    attribute_for_username: Union[Unset, str] = "uid"
    search_filters: Union[Unset, str] = ""
    use_tls: Union[Unset, bool] = True
    certificate_path: Union[None, Unset, str] = UNSET
    validate_cert: Union[Unset, bool] = True
    ciphers: Union[None, Unset, str] = "ALL"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        host = self.host

        app_dn = self.app_dn

        app_dn_password = self.app_dn_password

        search_base = self.search_base

        port: Union[None, Unset, int]
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        attribute_for_mail = self.attribute_for_mail

        attribute_for_username = self.attribute_for_username

        search_filters = self.search_filters

        use_tls = self.use_tls

        certificate_path: Union[None, Unset, str]
        if isinstance(self.certificate_path, Unset):
            certificate_path = UNSET
        else:
            certificate_path = self.certificate_path

        validate_cert = self.validate_cert

        ciphers: Union[None, Unset, str]
        if isinstance(self.ciphers, Unset):
            ciphers = UNSET
        else:
            ciphers = self.ciphers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "host": host,
                "app_dn": app_dn,
                "app_dn_password": app_dn_password,
                "search_base": search_base,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port
        if attribute_for_mail is not UNSET:
            field_dict["attribute_for_mail"] = attribute_for_mail
        if attribute_for_username is not UNSET:
            field_dict["attribute_for_username"] = attribute_for_username
        if search_filters is not UNSET:
            field_dict["search_filters"] = search_filters
        if use_tls is not UNSET:
            field_dict["use_tls"] = use_tls
        if certificate_path is not UNSET:
            field_dict["certificate_path"] = certificate_path
        if validate_cert is not UNSET:
            field_dict["validate_cert"] = validate_cert
        if ciphers is not UNSET:
            field_dict["ciphers"] = ciphers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        host = d.pop("host")

        app_dn = d.pop("app_dn")

        app_dn_password = d.pop("app_dn_password")

        search_base = d.pop("search_base")

        def _parse_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port = _parse_port(d.pop("port", UNSET))

        attribute_for_mail = d.pop("attribute_for_mail", UNSET)

        attribute_for_username = d.pop("attribute_for_username", UNSET)

        search_filters = d.pop("search_filters", UNSET)

        use_tls = d.pop("use_tls", UNSET)

        def _parse_certificate_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        certificate_path = _parse_certificate_path(d.pop("certificate_path", UNSET))

        validate_cert = d.pop("validate_cert", UNSET)

        def _parse_ciphers(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ciphers = _parse_ciphers(d.pop("ciphers", UNSET))

        ldap_server_config = cls(
            label=label,
            host=host,
            app_dn=app_dn,
            app_dn_password=app_dn_password,
            search_base=search_base,
            port=port,
            attribute_for_mail=attribute_for_mail,
            attribute_for_username=attribute_for_username,
            search_filters=search_filters,
            use_tls=use_tls,
            certificate_path=certificate_path,
            validate_cert=validate_cert,
            ciphers=ciphers,
        )

        ldap_server_config.additional_properties = d
        return ldap_server_config

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
