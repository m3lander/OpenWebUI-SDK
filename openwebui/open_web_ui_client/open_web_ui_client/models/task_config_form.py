from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TaskConfigForm")


@_attrs_define
class TaskConfigForm:
    """
    Attributes:
        task_model (Union[None, str]):
        task_model_external (Union[None, str]):
        enable_title_generation (bool):
        title_generation_prompt_template (str):
        image_prompt_generation_prompt_template (str):
        enable_autocomplete_generation (bool):
        autocomplete_generation_input_max_length (int):
        tags_generation_prompt_template (str):
        follow_up_generation_prompt_template (str):
        enable_follow_up_generation (bool):
        enable_tags_generation (bool):
        enable_search_query_generation (bool):
        enable_retrieval_query_generation (bool):
        query_generation_prompt_template (str):
        tools_function_calling_prompt_template (str):
    """

    task_model: Union[None, str]
    task_model_external: Union[None, str]
    enable_title_generation: bool
    title_generation_prompt_template: str
    image_prompt_generation_prompt_template: str
    enable_autocomplete_generation: bool
    autocomplete_generation_input_max_length: int
    tags_generation_prompt_template: str
    follow_up_generation_prompt_template: str
    enable_follow_up_generation: bool
    enable_tags_generation: bool
    enable_search_query_generation: bool
    enable_retrieval_query_generation: bool
    query_generation_prompt_template: str
    tools_function_calling_prompt_template: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_model: Union[None, str]
        task_model = self.task_model

        task_model_external: Union[None, str]
        task_model_external = self.task_model_external

        enable_title_generation = self.enable_title_generation

        title_generation_prompt_template = self.title_generation_prompt_template

        image_prompt_generation_prompt_template = self.image_prompt_generation_prompt_template

        enable_autocomplete_generation = self.enable_autocomplete_generation

        autocomplete_generation_input_max_length = self.autocomplete_generation_input_max_length

        tags_generation_prompt_template = self.tags_generation_prompt_template

        follow_up_generation_prompt_template = self.follow_up_generation_prompt_template

        enable_follow_up_generation = self.enable_follow_up_generation

        enable_tags_generation = self.enable_tags_generation

        enable_search_query_generation = self.enable_search_query_generation

        enable_retrieval_query_generation = self.enable_retrieval_query_generation

        query_generation_prompt_template = self.query_generation_prompt_template

        tools_function_calling_prompt_template = self.tools_function_calling_prompt_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "TASK_MODEL": task_model,
                "TASK_MODEL_EXTERNAL": task_model_external,
                "ENABLE_TITLE_GENERATION": enable_title_generation,
                "TITLE_GENERATION_PROMPT_TEMPLATE": title_generation_prompt_template,
                "IMAGE_PROMPT_GENERATION_PROMPT_TEMPLATE": image_prompt_generation_prompt_template,
                "ENABLE_AUTOCOMPLETE_GENERATION": enable_autocomplete_generation,
                "AUTOCOMPLETE_GENERATION_INPUT_MAX_LENGTH": autocomplete_generation_input_max_length,
                "TAGS_GENERATION_PROMPT_TEMPLATE": tags_generation_prompt_template,
                "FOLLOW_UP_GENERATION_PROMPT_TEMPLATE": follow_up_generation_prompt_template,
                "ENABLE_FOLLOW_UP_GENERATION": enable_follow_up_generation,
                "ENABLE_TAGS_GENERATION": enable_tags_generation,
                "ENABLE_SEARCH_QUERY_GENERATION": enable_search_query_generation,
                "ENABLE_RETRIEVAL_QUERY_GENERATION": enable_retrieval_query_generation,
                "QUERY_GENERATION_PROMPT_TEMPLATE": query_generation_prompt_template,
                "TOOLS_FUNCTION_CALLING_PROMPT_TEMPLATE": tools_function_calling_prompt_template,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_task_model(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        task_model = _parse_task_model(d.pop("TASK_MODEL"))

        def _parse_task_model_external(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        task_model_external = _parse_task_model_external(d.pop("TASK_MODEL_EXTERNAL"))

        enable_title_generation = d.pop("ENABLE_TITLE_GENERATION")

        title_generation_prompt_template = d.pop("TITLE_GENERATION_PROMPT_TEMPLATE")

        image_prompt_generation_prompt_template = d.pop("IMAGE_PROMPT_GENERATION_PROMPT_TEMPLATE")

        enable_autocomplete_generation = d.pop("ENABLE_AUTOCOMPLETE_GENERATION")

        autocomplete_generation_input_max_length = d.pop("AUTOCOMPLETE_GENERATION_INPUT_MAX_LENGTH")

        tags_generation_prompt_template = d.pop("TAGS_GENERATION_PROMPT_TEMPLATE")

        follow_up_generation_prompt_template = d.pop("FOLLOW_UP_GENERATION_PROMPT_TEMPLATE")

        enable_follow_up_generation = d.pop("ENABLE_FOLLOW_UP_GENERATION")

        enable_tags_generation = d.pop("ENABLE_TAGS_GENERATION")

        enable_search_query_generation = d.pop("ENABLE_SEARCH_QUERY_GENERATION")

        enable_retrieval_query_generation = d.pop("ENABLE_RETRIEVAL_QUERY_GENERATION")

        query_generation_prompt_template = d.pop("QUERY_GENERATION_PROMPT_TEMPLATE")

        tools_function_calling_prompt_template = d.pop("TOOLS_FUNCTION_CALLING_PROMPT_TEMPLATE")

        task_config_form = cls(
            task_model=task_model,
            task_model_external=task_model_external,
            enable_title_generation=enable_title_generation,
            title_generation_prompt_template=title_generation_prompt_template,
            image_prompt_generation_prompt_template=image_prompt_generation_prompt_template,
            enable_autocomplete_generation=enable_autocomplete_generation,
            autocomplete_generation_input_max_length=autocomplete_generation_input_max_length,
            tags_generation_prompt_template=tags_generation_prompt_template,
            follow_up_generation_prompt_template=follow_up_generation_prompt_template,
            enable_follow_up_generation=enable_follow_up_generation,
            enable_tags_generation=enable_tags_generation,
            enable_search_query_generation=enable_search_query_generation,
            enable_retrieval_query_generation=enable_retrieval_query_generation,
            query_generation_prompt_template=query_generation_prompt_template,
            tools_function_calling_prompt_template=tools_function_calling_prompt_template,
        )

        task_config_form.additional_properties = d
        return task_config_form

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
