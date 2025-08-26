from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feedback_model_data_type_0 import FeedbackModelDataType0
    from ..models.feedback_model_meta_type_0 import FeedbackModelMetaType0
    from ..models.feedback_model_snapshot_type_0 import FeedbackModelSnapshotType0


T = TypeVar("T", bound="FeedbackModel")


@_attrs_define
class FeedbackModel:
    """
    Attributes:
        id (str):
        user_id (str):
        version (int):
        type_ (str):
        created_at (int):
        updated_at (int):
        data (Union['FeedbackModelDataType0', None, Unset]):
        meta (Union['FeedbackModelMetaType0', None, Unset]):
        snapshot (Union['FeedbackModelSnapshotType0', None, Unset]):
    """

    id: str
    user_id: str
    version: int
    type_: str
    created_at: int
    updated_at: int
    data: Union["FeedbackModelDataType0", None, Unset] = UNSET
    meta: Union["FeedbackModelMetaType0", None, Unset] = UNSET
    snapshot: Union["FeedbackModelSnapshotType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.feedback_model_data_type_0 import FeedbackModelDataType0
        from ..models.feedback_model_meta_type_0 import FeedbackModelMetaType0
        from ..models.feedback_model_snapshot_type_0 import FeedbackModelSnapshotType0

        id = self.id

        user_id = self.user_id

        version = self.version

        type_ = self.type_

        created_at = self.created_at

        updated_at = self.updated_at

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, FeedbackModelDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, FeedbackModelMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        snapshot: Union[None, Unset, dict[str, Any]]
        if isinstance(self.snapshot, Unset):
            snapshot = UNSET
        elif isinstance(self.snapshot, FeedbackModelSnapshotType0):
            snapshot = self.snapshot.to_dict()
        else:
            snapshot = self.snapshot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "version": version,
                "type": type_,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feedback_model_data_type_0 import FeedbackModelDataType0
        from ..models.feedback_model_meta_type_0 import FeedbackModelMetaType0
        from ..models.feedback_model_snapshot_type_0 import FeedbackModelSnapshotType0

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        version = d.pop("version")

        type_ = d.pop("type")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_data(data: object) -> Union["FeedbackModelDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = FeedbackModelDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FeedbackModelDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_meta(data: object) -> Union["FeedbackModelMetaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = FeedbackModelMetaType0.from_dict(data)

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FeedbackModelMetaType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        def _parse_snapshot(data: object) -> Union["FeedbackModelSnapshotType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                snapshot_type_0 = FeedbackModelSnapshotType0.from_dict(data)

                return snapshot_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FeedbackModelSnapshotType0", None, Unset], data)

        snapshot = _parse_snapshot(d.pop("snapshot", UNSET))

        feedback_model = cls(
            id=id,
            user_id=user_id,
            version=version,
            type_=type_,
            created_at=created_at,
            updated_at=updated_at,
            data=data,
            meta=meta,
            snapshot=snapshot,
        )

        feedback_model.additional_properties = d
        return feedback_model

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
