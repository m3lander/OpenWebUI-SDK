from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.batch_process_files_result import BatchProcessFilesResult


T = TypeVar("T", bound="BatchProcessFilesResponse")


@_attrs_define
class BatchProcessFilesResponse:
    """
    Attributes:
        results (list['BatchProcessFilesResult']):
        errors (list['BatchProcessFilesResult']):
    """

    results: list["BatchProcessFilesResult"]
    errors: list["BatchProcessFilesResult"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_process_files_result import BatchProcessFilesResult

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = BatchProcessFilesResult.from_dict(results_item_data)

            results.append(results_item)

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = BatchProcessFilesResult.from_dict(errors_item_data)

            errors.append(errors_item)

        batch_process_files_response = cls(
            results=results,
            errors=errors,
        )

        batch_process_files_response.additional_properties = d
        return batch_process_files_response

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
