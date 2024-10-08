from __future__ import annotations

import typing as t
from pathlib import Path

from quart import Quart, Blueprint

ImpBlueprintSelf = t.TypeVar("ImpBlueprintSelf", bound="ImpBlueprint")


@t.runtime_checkable
class ImpBlueprint(t.Protocol):
    config: "ImpBlueprintConfig"

    location: Path
    bp_name: str
    package: str

    models: t.Set[t.Any]
    nested_blueprints: t.Set[t.Union["ImpBlueprint", Blueprint]]

    def _prevent_if_disabled(self: "ImpBlueprint") -> bool: ...

    def as_quart_blueprint(self) -> Blueprint: ...

    def import_resources(self, folder: str = "routes") -> None: ...

    def import_nested_blueprint(self, blueprint: str) -> None: ...

    def import_nested_blueprints(self, folder: str) -> None: ...

    def tmpl(self, template: str) -> str: ...


@t.runtime_checkable
class Imp(t.Protocol):
    app: Quart
    config: t.Any
    app_instance_path: Path
    app_path: Path


@t.runtime_checkable
class QuartConfig(t.Protocol):
    DEBUG: t.Optional[bool]
    PROPAGATE_EXCEPTIONS: t.Optional[bool]
    TRAP_HTTP_EXCEPTIONS: t.Optional[bool]
    TRAP_BAD_REQUEST_ERRORS: t.Optional[bool]
    SECRET_KEY: t.Optional[str]
    SESSION_COOKIE_NAME: t.Optional[str]
    SESSION_COOKIE_DOMAIN: t.Optional[str]
    SESSION_COOKIE_PATH: t.Optional[str]
    SESSION_COOKIE_HTTPONLY: t.Optional[bool]
    SESSION_COOKIE_SECURE: t.Optional[bool]
    SESSION_COOKIE_SAMESITE: t.Optional[t.Literal["Lax", "Strict"]]
    PERMANENT_SESSION_LIFETIME: t.Optional[int]
    SESSION_REFRESH_EACH_REQUEST: t.Optional[bool]
    USE_X_SENDFILE: t.Optional[bool]
    SEND_FILE_MAX_AGE_DEFAULT: t.Optional[int]
    ERROR_404_HELP: t.Optional[bool]
    SERVER_NAME: t.Optional[str]
    APPLICATION_ROOT: t.Optional[str]
    PREFERRED_URL_SCHEME: t.Optional[str]
    MAX_CONTENT_LENGTH: t.Optional[int]
    TEMPLATES_AUTO_RELOAD: t.Optional[bool]
    EXPLAIN_TEMPLATE_LOADING: t.Optional[bool]
    MAX_COOKIE_SIZE: t.Optional[int]

    _quart_config_keys: t.Set[str]

    def apply_config(self, app: Quart) -> None: ...

    def as_dict(self) -> t.Dict[str, t.Any]: ...


@t.runtime_checkable
class ImpConfig(t.Protocol):
    FLASK: QuartConfig

    INIT_SESSION: t.Optional[t.Dict[str, t.Any]]

    def __call__(self, *args: t.Any, **kwargs: t.Any) -> t.Any: ...


@t.runtime_checkable
class ImpBlueprintConfig(t.Protocol):
    enabled: t.Optional[bool]
    url_prefix: t.Optional[str]
    subdomain: t.Optional[str]
    url_default: t.Optional[t.Dict[str, t.Any]]
    static_folder: t.Optional[str]
    template_folder: t.Optional[str]
    static_url_path: t.Optional[str]
    root_path: t.Optional[str]
    cli_group: t.Optional[str]

    init_session: t.Optional[t.Dict[str, t.Any]]

    _blueprint_attrs: t.Set[str]

    def quart_blueprint_args(self) -> t.Dict[str, t.Any]: ...
