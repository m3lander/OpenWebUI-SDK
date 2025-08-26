from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminConfig")


@_attrs_define
class AdminConfig:
    """
    Attributes:
        show_admin_details (bool):
        webui_url (str):
        enable_signup (bool):
        enable_api_key (bool):
        enable_api_key_endpoint_restrictions (bool):
        api_key_allowed_endpoints (str):
        default_user_role (str):
        jwt_expires_in (str):
        enable_community_sharing (bool):
        enable_message_rating (bool):
        enable_channels (bool):
        enable_notes (bool):
        enable_user_webhooks (bool):
        pending_user_overlay_title (Union[None, Unset, str]):
        pending_user_overlay_content (Union[None, Unset, str]):
        response_watermark (Union[None, Unset, str]):
    """

    show_admin_details: bool
    webui_url: str
    enable_signup: bool
    enable_api_key: bool
    enable_api_key_endpoint_restrictions: bool
    api_key_allowed_endpoints: str
    default_user_role: str
    jwt_expires_in: str
    enable_community_sharing: bool
    enable_message_rating: bool
    enable_channels: bool
    enable_notes: bool
    enable_user_webhooks: bool
    pending_user_overlay_title: Union[None, Unset, str] = UNSET
    pending_user_overlay_content: Union[None, Unset, str] = UNSET
    response_watermark: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        show_admin_details = self.show_admin_details

        webui_url = self.webui_url

        enable_signup = self.enable_signup

        enable_api_key = self.enable_api_key

        enable_api_key_endpoint_restrictions = self.enable_api_key_endpoint_restrictions

        api_key_allowed_endpoints = self.api_key_allowed_endpoints

        default_user_role = self.default_user_role

        jwt_expires_in = self.jwt_expires_in

        enable_community_sharing = self.enable_community_sharing

        enable_message_rating = self.enable_message_rating

        enable_channels = self.enable_channels

        enable_notes = self.enable_notes

        enable_user_webhooks = self.enable_user_webhooks

        pending_user_overlay_title: Union[None, Unset, str]
        if isinstance(self.pending_user_overlay_title, Unset):
            pending_user_overlay_title = UNSET
        else:
            pending_user_overlay_title = self.pending_user_overlay_title

        pending_user_overlay_content: Union[None, Unset, str]
        if isinstance(self.pending_user_overlay_content, Unset):
            pending_user_overlay_content = UNSET
        else:
            pending_user_overlay_content = self.pending_user_overlay_content

        response_watermark: Union[None, Unset, str]
        if isinstance(self.response_watermark, Unset):
            response_watermark = UNSET
        else:
            response_watermark = self.response_watermark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "SHOW_ADMIN_DETAILS": show_admin_details,
                "WEBUI_URL": webui_url,
                "ENABLE_SIGNUP": enable_signup,
                "ENABLE_API_KEY": enable_api_key,
                "ENABLE_API_KEY_ENDPOINT_RESTRICTIONS": enable_api_key_endpoint_restrictions,
                "API_KEY_ALLOWED_ENDPOINTS": api_key_allowed_endpoints,
                "DEFAULT_USER_ROLE": default_user_role,
                "JWT_EXPIRES_IN": jwt_expires_in,
                "ENABLE_COMMUNITY_SHARING": enable_community_sharing,
                "ENABLE_MESSAGE_RATING": enable_message_rating,
                "ENABLE_CHANNELS": enable_channels,
                "ENABLE_NOTES": enable_notes,
                "ENABLE_USER_WEBHOOKS": enable_user_webhooks,
            }
        )
        if pending_user_overlay_title is not UNSET:
            field_dict["PENDING_USER_OVERLAY_TITLE"] = pending_user_overlay_title
        if pending_user_overlay_content is not UNSET:
            field_dict["PENDING_USER_OVERLAY_CONTENT"] = pending_user_overlay_content
        if response_watermark is not UNSET:
            field_dict["RESPONSE_WATERMARK"] = response_watermark

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        show_admin_details = d.pop("SHOW_ADMIN_DETAILS")

        webui_url = d.pop("WEBUI_URL")

        enable_signup = d.pop("ENABLE_SIGNUP")

        enable_api_key = d.pop("ENABLE_API_KEY")

        enable_api_key_endpoint_restrictions = d.pop("ENABLE_API_KEY_ENDPOINT_RESTRICTIONS")

        api_key_allowed_endpoints = d.pop("API_KEY_ALLOWED_ENDPOINTS")

        default_user_role = d.pop("DEFAULT_USER_ROLE")

        jwt_expires_in = d.pop("JWT_EXPIRES_IN")

        enable_community_sharing = d.pop("ENABLE_COMMUNITY_SHARING")

        enable_message_rating = d.pop("ENABLE_MESSAGE_RATING")

        enable_channels = d.pop("ENABLE_CHANNELS")

        enable_notes = d.pop("ENABLE_NOTES")

        enable_user_webhooks = d.pop("ENABLE_USER_WEBHOOKS")

        def _parse_pending_user_overlay_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pending_user_overlay_title = _parse_pending_user_overlay_title(d.pop("PENDING_USER_OVERLAY_TITLE", UNSET))

        def _parse_pending_user_overlay_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pending_user_overlay_content = _parse_pending_user_overlay_content(d.pop("PENDING_USER_OVERLAY_CONTENT", UNSET))

        def _parse_response_watermark(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        response_watermark = _parse_response_watermark(d.pop("RESPONSE_WATERMARK", UNSET))

        admin_config = cls(
            show_admin_details=show_admin_details,
            webui_url=webui_url,
            enable_signup=enable_signup,
            enable_api_key=enable_api_key,
            enable_api_key_endpoint_restrictions=enable_api_key_endpoint_restrictions,
            api_key_allowed_endpoints=api_key_allowed_endpoints,
            default_user_role=default_user_role,
            jwt_expires_in=jwt_expires_in,
            enable_community_sharing=enable_community_sharing,
            enable_message_rating=enable_message_rating,
            enable_channels=enable_channels,
            enable_notes=enable_notes,
            enable_user_webhooks=enable_user_webhooks,
            pending_user_overlay_title=pending_user_overlay_title,
            pending_user_overlay_content=pending_user_overlay_content,
            response_watermark=response_watermark,
        )

        admin_config.additional_properties = d
        return admin_config

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
