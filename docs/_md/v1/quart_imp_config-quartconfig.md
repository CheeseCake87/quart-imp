```
Menu = quart_imp.config/QuartConfig
Title = QuartConfig - quart_imp.config
```

```python
from quart_imp.config import QuartConfig
```

```python
QuartConfig(
    debug: t.Optional[bool] = None,
    propagate_exceptions: t.Optional[bool] = None,
    trap_http_exceptions: t.Optional[bool] = None,
    trap_bad_request_errors: t.Optional[bool] = None,
    secret_key: t.Optional[str] = None,
    session_cookie_name: t.Optional[str] = None,
    session_cookie_domain: t.Optional[str] = None,
    session_cookie_path: t.Optional[str] = None,
    session_cookie_httponly: t.Optional[bool] = None,
    session_cookie_secure: t.Optional[bool] = None,
    session_cookie_samesite: t.Optional[t.Literal["Lax", "Strict"]] = None,
    permanent_session_lifetime: t.Optional[int] = None,
    session_refresh_each_request: t.Optional[bool] = None,
    use_x_sendfile: t.Optional[bool] = None,
    send_file_max_age_default: t.Optional[int] = None,
    error_404_help: t.Optional[bool] = None,
    server_name: t.Optional[str] = None,
    application_root: t.Optional[str] = None,
    preferred_url_scheme: t.Optional[str] = None,
    max_content_length: t.Optional[int] = None,
    templates_auto_reload: t.Optional[bool] = None,
    explain_template_loading: t.Optional[bool] = None,
    max_cookie_size: t.Optional[int] = None,
    app_instance: t.Optional["Quart"] = None
)
```

---

A class that holds a Quart configuration values.

You can set the configuration values to the app instance by either passing the app instance to the `app_instance` 
parameter or by calling the `apply_config` method on the `QuartConfig` instance.

```python
def create_app():
    app = Quart(__name__)
    QuartConfig(debug=True, app_instance=app)
    return app
```
or
```python
def create_app():
    app = Quart(__name__)
    config = QuartConfig(debug=True)
    config.apply_config(app)
    return app
```