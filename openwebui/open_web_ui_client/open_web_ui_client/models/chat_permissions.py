from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatPermissions")


@_attrs_define
class ChatPermissions:
    """
    Attributes:
        controls (Union[Unset, bool]):  Default: True.
        valves (Union[Unset, bool]):  Default: True.
        system_prompt (Union[Unset, bool]):  Default: True.
        params (Union[Unset, bool]):  Default: True.
        file_upload (Union[Unset, bool]):  Default: True.
        delete (Union[Unset, bool]):  Default: True.
        edit (Union[Unset, bool]):  Default: True.
        share (Union[Unset, bool]):  Default: True.
        export (Union[Unset, bool]):  Default: True.
        stt (Union[Unset, bool]):  Default: True.
        tts (Union[Unset, bool]):  Default: True.
        call (Union[Unset, bool]):  Default: True.
        multiple_models (Union[Unset, bool]):  Default: True.
        temporary (Union[Unset, bool]):  Default: True.
        temporary_enforced (Union[Unset, bool]):  Default: False.
    """

    controls: Union[Unset, bool] = True
    valves: Union[Unset, bool] = True
    system_prompt: Union[Unset, bool] = True
    params: Union[Unset, bool] = True
    file_upload: Union[Unset, bool] = True
    delete: Union[Unset, bool] = True
    edit: Union[Unset, bool] = True
    share: Union[Unset, bool] = True
    export: Union[Unset, bool] = True
    stt: Union[Unset, bool] = True
    tts: Union[Unset, bool] = True
    call: Union[Unset, bool] = True
    multiple_models: Union[Unset, bool] = True
    temporary: Union[Unset, bool] = True
    temporary_enforced: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        controls = self.controls

        valves = self.valves

        system_prompt = self.system_prompt

        params = self.params

        file_upload = self.file_upload

        delete = self.delete

        edit = self.edit

        share = self.share

        export = self.export

        stt = self.stt

        tts = self.tts

        call = self.call

        multiple_models = self.multiple_models

        temporary = self.temporary

        temporary_enforced = self.temporary_enforced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if controls is not UNSET:
            field_dict["controls"] = controls
        if valves is not UNSET:
            field_dict["valves"] = valves
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if params is not UNSET:
            field_dict["params"] = params
        if file_upload is not UNSET:
            field_dict["file_upload"] = file_upload
        if delete is not UNSET:
            field_dict["delete"] = delete
        if edit is not UNSET:
            field_dict["edit"] = edit
        if share is not UNSET:
            field_dict["share"] = share
        if export is not UNSET:
            field_dict["export"] = export
        if stt is not UNSET:
            field_dict["stt"] = stt
        if tts is not UNSET:
            field_dict["tts"] = tts
        if call is not UNSET:
            field_dict["call"] = call
        if multiple_models is not UNSET:
            field_dict["multiple_models"] = multiple_models
        if temporary is not UNSET:
            field_dict["temporary"] = temporary
        if temporary_enforced is not UNSET:
            field_dict["temporary_enforced"] = temporary_enforced

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        controls = d.pop("controls", UNSET)

        valves = d.pop("valves", UNSET)

        system_prompt = d.pop("system_prompt", UNSET)

        params = d.pop("params", UNSET)

        file_upload = d.pop("file_upload", UNSET)

        delete = d.pop("delete", UNSET)

        edit = d.pop("edit", UNSET)

        share = d.pop("share", UNSET)

        export = d.pop("export", UNSET)

        stt = d.pop("stt", UNSET)

        tts = d.pop("tts", UNSET)

        call = d.pop("call", UNSET)

        multiple_models = d.pop("multiple_models", UNSET)

        temporary = d.pop("temporary", UNSET)

        temporary_enforced = d.pop("temporary_enforced", UNSET)

        chat_permissions = cls(
            controls=controls,
            valves=valves,
            system_prompt=system_prompt,
            params=params,
            file_upload=file_upload,
            delete=delete,
            edit=edit,
            share=share,
            export=export,
            stt=stt,
            tts=tts,
            call=call,
            multiple_models=multiple_models,
            temporary=temporary,
            temporary_enforced=temporary_enforced,
        )

        chat_permissions.additional_properties = d
        return chat_permissions

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
