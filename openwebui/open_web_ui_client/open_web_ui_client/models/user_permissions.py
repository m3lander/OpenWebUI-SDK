from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat_permissions import ChatPermissions
    from ..models.features_permissions import FeaturesPermissions
    from ..models.sharing_permissions import SharingPermissions
    from ..models.workspace_permissions import WorkspacePermissions


T = TypeVar("T", bound="UserPermissions")


@_attrs_define
class UserPermissions:
    """
    Attributes:
        workspace (WorkspacePermissions):
        sharing (SharingPermissions):
        chat (ChatPermissions):
        features (FeaturesPermissions):
    """

    workspace: "WorkspacePermissions"
    sharing: "SharingPermissions"
    chat: "ChatPermissions"
    features: "FeaturesPermissions"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace = self.workspace.to_dict()

        sharing = self.sharing.to_dict()

        chat = self.chat.to_dict()

        features = self.features.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace": workspace,
                "sharing": sharing,
                "chat": chat,
                "features": features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_permissions import ChatPermissions
        from ..models.features_permissions import FeaturesPermissions
        from ..models.sharing_permissions import SharingPermissions
        from ..models.workspace_permissions import WorkspacePermissions

        d = dict(src_dict)
        workspace = WorkspacePermissions.from_dict(d.pop("workspace"))

        sharing = SharingPermissions.from_dict(d.pop("sharing"))

        chat = ChatPermissions.from_dict(d.pop("chat"))

        features = FeaturesPermissions.from_dict(d.pop("features"))

        user_permissions = cls(
            workspace=workspace,
            sharing=sharing,
            chat=chat,
            features=features,
        )

        user_permissions.additional_properties = d
        return user_permissions

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
