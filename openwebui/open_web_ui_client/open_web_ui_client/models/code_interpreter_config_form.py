from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CodeInterpreterConfigForm")


@_attrs_define
class CodeInterpreterConfigForm:
    """
    Attributes:
        enable_code_execution (bool):
        code_execution_engine (str):
        code_execution_jupyter_url (Union[None, str]):
        code_execution_jupyter_auth (Union[None, str]):
        code_execution_jupyter_auth_token (Union[None, str]):
        code_execution_jupyter_auth_password (Union[None, str]):
        code_execution_jupyter_timeout (Union[None, int]):
        enable_code_interpreter (bool):
        code_interpreter_engine (str):
        code_interpreter_prompt_template (Union[None, str]):
        code_interpreter_jupyter_url (Union[None, str]):
        code_interpreter_jupyter_auth (Union[None, str]):
        code_interpreter_jupyter_auth_token (Union[None, str]):
        code_interpreter_jupyter_auth_password (Union[None, str]):
        code_interpreter_jupyter_timeout (Union[None, int]):
    """

    enable_code_execution: bool
    code_execution_engine: str
    code_execution_jupyter_url: Union[None, str]
    code_execution_jupyter_auth: Union[None, str]
    code_execution_jupyter_auth_token: Union[None, str]
    code_execution_jupyter_auth_password: Union[None, str]
    code_execution_jupyter_timeout: Union[None, int]
    enable_code_interpreter: bool
    code_interpreter_engine: str
    code_interpreter_prompt_template: Union[None, str]
    code_interpreter_jupyter_url: Union[None, str]
    code_interpreter_jupyter_auth: Union[None, str]
    code_interpreter_jupyter_auth_token: Union[None, str]
    code_interpreter_jupyter_auth_password: Union[None, str]
    code_interpreter_jupyter_timeout: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_code_execution = self.enable_code_execution

        code_execution_engine = self.code_execution_engine

        code_execution_jupyter_url: Union[None, str]
        code_execution_jupyter_url = self.code_execution_jupyter_url

        code_execution_jupyter_auth: Union[None, str]
        code_execution_jupyter_auth = self.code_execution_jupyter_auth

        code_execution_jupyter_auth_token: Union[None, str]
        code_execution_jupyter_auth_token = self.code_execution_jupyter_auth_token

        code_execution_jupyter_auth_password: Union[None, str]
        code_execution_jupyter_auth_password = self.code_execution_jupyter_auth_password

        code_execution_jupyter_timeout: Union[None, int]
        code_execution_jupyter_timeout = self.code_execution_jupyter_timeout

        enable_code_interpreter = self.enable_code_interpreter

        code_interpreter_engine = self.code_interpreter_engine

        code_interpreter_prompt_template: Union[None, str]
        code_interpreter_prompt_template = self.code_interpreter_prompt_template

        code_interpreter_jupyter_url: Union[None, str]
        code_interpreter_jupyter_url = self.code_interpreter_jupyter_url

        code_interpreter_jupyter_auth: Union[None, str]
        code_interpreter_jupyter_auth = self.code_interpreter_jupyter_auth

        code_interpreter_jupyter_auth_token: Union[None, str]
        code_interpreter_jupyter_auth_token = self.code_interpreter_jupyter_auth_token

        code_interpreter_jupyter_auth_password: Union[None, str]
        code_interpreter_jupyter_auth_password = self.code_interpreter_jupyter_auth_password

        code_interpreter_jupyter_timeout: Union[None, int]
        code_interpreter_jupyter_timeout = self.code_interpreter_jupyter_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ENABLE_CODE_EXECUTION": enable_code_execution,
                "CODE_EXECUTION_ENGINE": code_execution_engine,
                "CODE_EXECUTION_JUPYTER_URL": code_execution_jupyter_url,
                "CODE_EXECUTION_JUPYTER_AUTH": code_execution_jupyter_auth,
                "CODE_EXECUTION_JUPYTER_AUTH_TOKEN": code_execution_jupyter_auth_token,
                "CODE_EXECUTION_JUPYTER_AUTH_PASSWORD": code_execution_jupyter_auth_password,
                "CODE_EXECUTION_JUPYTER_TIMEOUT": code_execution_jupyter_timeout,
                "ENABLE_CODE_INTERPRETER": enable_code_interpreter,
                "CODE_INTERPRETER_ENGINE": code_interpreter_engine,
                "CODE_INTERPRETER_PROMPT_TEMPLATE": code_interpreter_prompt_template,
                "CODE_INTERPRETER_JUPYTER_URL": code_interpreter_jupyter_url,
                "CODE_INTERPRETER_JUPYTER_AUTH": code_interpreter_jupyter_auth,
                "CODE_INTERPRETER_JUPYTER_AUTH_TOKEN": code_interpreter_jupyter_auth_token,
                "CODE_INTERPRETER_JUPYTER_AUTH_PASSWORD": code_interpreter_jupyter_auth_password,
                "CODE_INTERPRETER_JUPYTER_TIMEOUT": code_interpreter_jupyter_timeout,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_code_execution = d.pop("ENABLE_CODE_EXECUTION")

        code_execution_engine = d.pop("CODE_EXECUTION_ENGINE")

        def _parse_code_execution_jupyter_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        code_execution_jupyter_url = _parse_code_execution_jupyter_url(d.pop("CODE_EXECUTION_JUPYTER_URL"))

        def _parse_code_execution_jupyter_auth(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        code_execution_jupyter_auth = _parse_code_execution_jupyter_auth(d.pop("CODE_EXECUTION_JUPYTER_AUTH"))

        def _parse_code_execution_jupyter_auth_token(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        code_execution_jupyter_auth_token = _parse_code_execution_jupyter_auth_token(
            d.pop("CODE_EXECUTION_JUPYTER_AUTH_TOKEN")
        )

        def _parse_code_execution_jupyter_auth_password(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        code_execution_jupyter_auth_password = _parse_code_execution_jupyter_auth_password(
            d.pop("CODE_EXECUTION_JUPYTER_AUTH_PASSWORD")
        )

        def _parse_code_execution_jupyter_timeout(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        code_execution_jupyter_timeout = _parse_code_execution_jupyter_timeout(d.pop("CODE_EXECUTION_JUPYTER_TIMEOUT"))

        enable_code_interpreter = d.pop("ENABLE_CODE_INTERPRETER")

        code_interpreter_engine = d.pop("CODE_INTERPRETER_ENGINE")

        def _parse_code_interpreter_prompt_template(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        code_interpreter_prompt_template = _parse_code_interpreter_prompt_template(
            d.pop("CODE_INTERPRETER_PROMPT_TEMPLATE")
        )

        def _parse_code_interpreter_jupyter_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        code_interpreter_jupyter_url = _parse_code_interpreter_jupyter_url(d.pop("CODE_INTERPRETER_JUPYTER_URL"))

        def _parse_code_interpreter_jupyter_auth(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        code_interpreter_jupyter_auth = _parse_code_interpreter_jupyter_auth(d.pop("CODE_INTERPRETER_JUPYTER_AUTH"))

        def _parse_code_interpreter_jupyter_auth_token(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        code_interpreter_jupyter_auth_token = _parse_code_interpreter_jupyter_auth_token(
            d.pop("CODE_INTERPRETER_JUPYTER_AUTH_TOKEN")
        )

        def _parse_code_interpreter_jupyter_auth_password(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        code_interpreter_jupyter_auth_password = _parse_code_interpreter_jupyter_auth_password(
            d.pop("CODE_INTERPRETER_JUPYTER_AUTH_PASSWORD")
        )

        def _parse_code_interpreter_jupyter_timeout(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        code_interpreter_jupyter_timeout = _parse_code_interpreter_jupyter_timeout(
            d.pop("CODE_INTERPRETER_JUPYTER_TIMEOUT")
        )

        code_interpreter_config_form = cls(
            enable_code_execution=enable_code_execution,
            code_execution_engine=code_execution_engine,
            code_execution_jupyter_url=code_execution_jupyter_url,
            code_execution_jupyter_auth=code_execution_jupyter_auth,
            code_execution_jupyter_auth_token=code_execution_jupyter_auth_token,
            code_execution_jupyter_auth_password=code_execution_jupyter_auth_password,
            code_execution_jupyter_timeout=code_execution_jupyter_timeout,
            enable_code_interpreter=enable_code_interpreter,
            code_interpreter_engine=code_interpreter_engine,
            code_interpreter_prompt_template=code_interpreter_prompt_template,
            code_interpreter_jupyter_url=code_interpreter_jupyter_url,
            code_interpreter_jupyter_auth=code_interpreter_jupyter_auth,
            code_interpreter_jupyter_auth_token=code_interpreter_jupyter_auth_token,
            code_interpreter_jupyter_auth_password=code_interpreter_jupyter_auth_password,
            code_interpreter_jupyter_timeout=code_interpreter_jupyter_timeout,
        )

        code_interpreter_config_form.additional_properties = d
        return code_interpreter_config_form

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
