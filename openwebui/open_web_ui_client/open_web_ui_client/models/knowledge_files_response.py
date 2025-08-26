from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_metadata_response import FileMetadataResponse
    from ..models.knowledge_files_response_access_control_type_0 import KnowledgeFilesResponseAccessControlType0
    from ..models.knowledge_files_response_data_type_0 import KnowledgeFilesResponseDataType0
    from ..models.knowledge_files_response_meta_type_0 import KnowledgeFilesResponseMetaType0


T = TypeVar("T", bound="KnowledgeFilesResponse")


@_attrs_define
class KnowledgeFilesResponse:
    """
    Attributes:
        id (str):
        user_id (str):
        name (str):
        description (str):
        created_at (int):
        updated_at (int):
        files (list['FileMetadataResponse']):
        data (Union['KnowledgeFilesResponseDataType0', None, Unset]):
        meta (Union['KnowledgeFilesResponseMetaType0', None, Unset]):
        access_control (Union['KnowledgeFilesResponseAccessControlType0', None, Unset]):
    """

    id: str
    user_id: str
    name: str
    description: str
    created_at: int
    updated_at: int
    files: list["FileMetadataResponse"]
    data: Union["KnowledgeFilesResponseDataType0", None, Unset] = UNSET
    meta: Union["KnowledgeFilesResponseMetaType0", None, Unset] = UNSET
    access_control: Union["KnowledgeFilesResponseAccessControlType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.knowledge_files_response_access_control_type_0 import KnowledgeFilesResponseAccessControlType0
        from ..models.knowledge_files_response_data_type_0 import KnowledgeFilesResponseDataType0
        from ..models.knowledge_files_response_meta_type_0 import KnowledgeFilesResponseMetaType0

        id = self.id

        user_id = self.user_id

        name = self.name

        description = self.description

        created_at = self.created_at

        updated_at = self.updated_at

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, KnowledgeFilesResponseDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, KnowledgeFilesResponseMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        access_control: Union[None, Unset, dict[str, Any]]
        if isinstance(self.access_control, Unset):
            access_control = UNSET
        elif isinstance(self.access_control, KnowledgeFilesResponseAccessControlType0):
            access_control = self.access_control.to_dict()
        else:
            access_control = self.access_control

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "name": name,
                "description": description,
                "created_at": created_at,
                "updated_at": updated_at,
                "files": files,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta
        if access_control is not UNSET:
            field_dict["access_control"] = access_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_metadata_response import FileMetadataResponse
        from ..models.knowledge_files_response_access_control_type_0 import KnowledgeFilesResponseAccessControlType0
        from ..models.knowledge_files_response_data_type_0 import KnowledgeFilesResponseDataType0
        from ..models.knowledge_files_response_meta_type_0 import KnowledgeFilesResponseMetaType0

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        name = d.pop("name")

        description = d.pop("description")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = FileMetadataResponse.from_dict(files_item_data)

            files.append(files_item)

        def _parse_data(data: object) -> Union["KnowledgeFilesResponseDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = KnowledgeFilesResponseDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["KnowledgeFilesResponseDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_meta(data: object) -> Union["KnowledgeFilesResponseMetaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = KnowledgeFilesResponseMetaType0.from_dict(data)

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["KnowledgeFilesResponseMetaType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        def _parse_access_control(data: object) -> Union["KnowledgeFilesResponseAccessControlType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                access_control_type_0 = KnowledgeFilesResponseAccessControlType0.from_dict(data)

                return access_control_type_0
            except:  # noqa: E722
                pass
            return cast(Union["KnowledgeFilesResponseAccessControlType0", None, Unset], data)

        access_control = _parse_access_control(d.pop("access_control", UNSET))

        knowledge_files_response = cls(
            id=id,
            user_id=user_id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            files=files,
            data=data,
            meta=meta,
            access_control=access_control,
        )

        knowledge_files_response.additional_properties = d
        return knowledge_files_response

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
