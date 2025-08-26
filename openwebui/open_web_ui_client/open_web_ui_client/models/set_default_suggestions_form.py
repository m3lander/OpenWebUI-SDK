from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.prompt_suggestion import PromptSuggestion


T = TypeVar("T", bound="SetDefaultSuggestionsForm")


@_attrs_define
class SetDefaultSuggestionsForm:
    """
    Attributes:
        suggestions (list['PromptSuggestion']):
    """

    suggestions: list["PromptSuggestion"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suggestions = []
        for suggestions_item_data in self.suggestions:
            suggestions_item = suggestions_item_data.to_dict()
            suggestions.append(suggestions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "suggestions": suggestions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_suggestion import PromptSuggestion

        d = dict(src_dict)
        suggestions = []
        _suggestions = d.pop("suggestions")
        for suggestions_item_data in _suggestions:
            suggestions_item = PromptSuggestion.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        set_default_suggestions_form = cls(
            suggestions=suggestions,
        )

        set_default_suggestions_form.additional_properties = d
        return set_default_suggestions_form

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
