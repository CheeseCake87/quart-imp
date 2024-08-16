```
Menu = quart_imp.config/ImpConfig
Title = ImpConfig - quart_imp.config
```

```python
from quart_imp.config import ImpConfig
```

```python
ImpConfig(
    init_session: t.Optional[t.Dict[str, t.Any]] = None,
)
```

---

The `ImpConfig` class is used to set the initial session data
that the application will use.

```python
imp_config = ImpConfig(
    init_session={"key": "value"},
)


def create_app():
    app = Quart(__name__)
    QuartConfig(debug=True, app_instance=app)
    imp.init_app(app, imp_config)
    ...
```