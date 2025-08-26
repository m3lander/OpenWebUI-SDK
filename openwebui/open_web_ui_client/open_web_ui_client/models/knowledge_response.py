from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_metadata_response import FileMetadataResponse
    from ..models.knowledge_response_access_control_type_0 import KnowledgeResponseAccessControlType0
    from ..models.knowledge_response_data_type_0 import KnowledgeResponseDataType0
    from ..models.knowledge_response_files_type_0_item_type_1 import KnowledgeResponseFilesType0ItemType1
    from ..models.knowledge_response_meta_type_0 import KnowledgeResponseMetaType0


T = TypeVar("T", bound="KnowledgeResponse")


@_attrs_define
class KnowledgeResponse:
    """
    Attributes:
        id (str):
        user_id (str):
        name (str):
        description (str):
        created_at (int):
        updated_at (int):
        data (Union['KnowledgeResponseDataType0', None, Unset]):
        meta (Union['KnowledgeResponseMetaType0', None, Unset]):
        access_control (Union['KnowledgeResponseAccessControlType0', None, Unset]):
        files (Union[None, Unset, list[Union['FileMetadataResponse', 'KnowledgeResponseFilesType0ItemType1']]]):
    """

    id: str
    user_id: str
    name: str
    description: str
    created_at: int
    updated_at: int
    data: Union["KnowledgeResponseDataType0", None, Unset] = UNSET
    meta: Union["KnowledgeResponseMetaType0", None, Unset] = UNSET
    access_control: Union["KnowledgeResponseAccessControlType0", None, Unset] = UNSET
    files: Union[None, Unset, list[Union["FileMetadataResponse", "KnowledgeResponseFilesType0ItemType1"]]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_metadata_response import FileMetadataResponse
        from ..models.knowledge_response_access_control_type_0 import KnowledgeResponseAccessControlType0
        from ..models.knowledge_response_data_type_0 import KnowledgeResponseDataType0
        from ..models.knowledge_response_meta_type_0 import KnowledgeResponseMetaType0

        id = self.id

        user_id = self.user_id

        name = self.name

        description = self.description

        created_at = self.created_at

        updated_at = self.updated_at

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, KnowledgeResponseDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        meta: Union[None, Unset, dict[str, Any]]
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, KnowledgeResponseMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        access_control: Union[None, Unset, dict[str, Any]]
        if isinstance(self.access_control, Unset):
            access_control = UNSET
        elif isinstance(self.access_control, KnowledgeResponseAccessControlType0):
            access_control = self.access_control.to_dict()
        else:
            access_control = self.access_control

        files: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.files, Unset):
            files = UNSET
        elif isinstance(self.files, list):
            files = []
            for files_type_0_item_data in self.files:
                files_type_0_item: dict[str, Any]
                if isinstance(files_type_0_item_data, FileMetadataResponse):
                    files_type_0_item = files_type_0_item_data.to_dict()
                else:
                    files_type_0_item = files_type_0_item_data.to_dict()

                files.append(files_type_0_item)

        else:
            files = self.files

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
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta
        if access_control is not UNSET:
            field_dict["access_control"] = access_control
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_metadata_response import FileMetadataResponse
        from ..models.knowledge_response_access_control_type_0 import KnowledgeResponseAccessControlType0
        from ..models.knowledge_response_data_type_0 import KnowledgeResponseDataType0
        from ..models.knowledge_response_files_type_0_item_type_1 import KnowledgeResponseFilesType0ItemType1
        from ..models.knowledge_response_meta_type_0 import KnowledgeResponseMetaType0

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        name = d.pop("name")

        description = d.pop("description")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_data(data: object) -> Union["KnowledgeResponseDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = KnowledgeResponseDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["KnowledgeResponseDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_meta(data: object) -> Union["KnowledgeResponseMetaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = KnowledgeResponseMetaType0.from_dict(data)

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(Union["KnowledgeResponseMetaType0", None, Unset], data)

        meta = _parse_meta(d.pop("meta", UNSET))

        def _parse_access_control(data: object) -> Union["KnowledgeResponseAccessControlType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                access_control_type_0 = KnowledgeResponseAccessControlType0.from_dict(data)

                return access_control_type_0
            except:  # noqa: E722
                pass
            return cast(Union["KnowledgeResponseAccessControlType0", None, Unset], data)

        access_control = _parse_access_control(d.pop("access_control", UNSET))

        def _parse_files(
            data: object,
        ) -> Union[None, Unset, list[Union["FileMetadataResponse", "KnowledgeResponseFilesType0ItemType1"]]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                files_type_0 = []
                _files_type_0 = data
                for files_type_0_item_data in _files_type_0:

                    def _parse_files_type_0_item(
                        data: object,
                    ) -> Union["FileMetadataResponse", "KnowledgeResponseFilesType0ItemType1"]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            files_type_0_item_type_0 = FileMetadataResponse.from_dict(data)

                            return files_type_0_item_type_0
                        except:  # noqa: E722
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        files_type_0_item_type_1 = KnowledgeResponseFilesType0ItemType1.from_dict(data)

                        return files_type_0_item_type_1

                    files_type_0_item = _parse_files_type_0_item(files_type_0_item_data)

                    files_type_0.append(files_type_0_item)

                return files_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list[Union["FileMetadataResponse", "KnowledgeResponseFilesType0ItemType1"]]], data
            )

        files = _parse_files(d.pop("files", UNSET))

        knowledge_response = cls(
            id=id,
            user_id=user_id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            data=data,
            meta=meta,
            access_control=access_control,
            files=files,
        )

        knowledge_response.additional_properties = d
        return knowledge_response

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
