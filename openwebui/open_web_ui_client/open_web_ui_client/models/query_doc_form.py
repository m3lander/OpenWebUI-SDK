from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryDocForm")


@_attrs_define
class QueryDocForm:
    """
    Attributes:
        collection_name (str):
        query (str):
        k (Union[None, Unset, int]):
        k_reranker (Union[None, Unset, int]):
        r (Union[None, Unset, float]):
        hybrid (Union[None, Unset, bool]):
    """

    collection_name: str
    query: str
    k: Union[None, Unset, int] = UNSET
    k_reranker: Union[None, Unset, int] = UNSET
    r: Union[None, Unset, float] = UNSET
    hybrid: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_name = self.collection_name

        query = self.query

        k: Union[None, Unset, int]
        if isinstance(self.k, Unset):
            k = UNSET
        else:
            k = self.k

        k_reranker: Union[None, Unset, int]
        if isinstance(self.k_reranker, Unset):
            k_reranker = UNSET
        else:
            k_reranker = self.k_reranker

        r: Union[None, Unset, float]
        if isinstance(self.r, Unset):
            r = UNSET
        else:
            r = self.r

        hybrid: Union[None, Unset, bool]
        if isinstance(self.hybrid, Unset):
            hybrid = UNSET
        else:
            hybrid = self.hybrid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_name": collection_name,
                "query": query,
            }
        )
        if k is not UNSET:
            field_dict["k"] = k
        if k_reranker is not UNSET:
            field_dict["k_reranker"] = k_reranker
        if r is not UNSET:
            field_dict["r"] = r
        if hybrid is not UNSET:
            field_dict["hybrid"] = hybrid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_name = d.pop("collection_name")

        query = d.pop("query")

        def _parse_k(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        k = _parse_k(d.pop("k", UNSET))

        def _parse_k_reranker(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        k_reranker = _parse_k_reranker(d.pop("k_reranker", UNSET))

        def _parse_r(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        r = _parse_r(d.pop("r", UNSET))

        def _parse_hybrid(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        hybrid = _parse_hybrid(d.pop("hybrid", UNSET))

        query_doc_form = cls(
            collection_name=collection_name,
            query=query,
            k=k,
            k_reranker=k_reranker,
            r=r,
            hybrid=hybrid,
        )

        query_doc_form.additional_properties = d
        return query_doc_form

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
