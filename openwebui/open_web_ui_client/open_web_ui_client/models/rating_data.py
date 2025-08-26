from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RatingData")


@_attrs_define
class RatingData:
    """
    Attributes:
        rating (Union[None, Unset, int, str]):
        model_id (Union[None, Unset, str]):
        sibling_model_ids (Union[None, Unset, list[str]]):
        reason (Union[None, Unset, str]):
        comment (Union[None, Unset, str]):
    """

    rating: Union[None, Unset, int, str] = UNSET
    model_id: Union[None, Unset, str] = UNSET
    sibling_model_ids: Union[None, Unset, list[str]] = UNSET
    reason: Union[None, Unset, str] = UNSET
    comment: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rating: Union[None, Unset, int, str]
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        model_id: Union[None, Unset, str]
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        sibling_model_ids: Union[None, Unset, list[str]]
        if isinstance(self.sibling_model_ids, Unset):
            sibling_model_ids = UNSET
        elif isinstance(self.sibling_model_ids, list):
            sibling_model_ids = self.sibling_model_ids

        else:
            sibling_model_ids = self.sibling_model_ids

        reason: Union[None, Unset, str]
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rating is not UNSET:
            field_dict["rating"] = rating
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if sibling_model_ids is not UNSET:
            field_dict["sibling_model_ids"] = sibling_model_ids
        if reason is not UNSET:
            field_dict["reason"] = reason
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_rating(data: object) -> Union[None, Unset, int, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int, str], data)

        rating = _parse_rating(d.pop("rating", UNSET))

        def _parse_model_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_sibling_model_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sibling_model_ids_type_0 = cast(list[str], data)

                return sibling_model_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        sibling_model_ids = _parse_sibling_model_ids(d.pop("sibling_model_ids", UNSET))

        def _parse_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        rating_data = cls(
            rating=rating,
            model_id=model_id,
            sibling_model_ids=sibling_model_ids,
            reason=reason,
            comment=comment,
        )

        rating_data.additional_properties = d
        return rating_data

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
