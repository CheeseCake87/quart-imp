```
Menu = quart_imp.config/ImpBlueprintConfig
Title = ImpBlueprintConfig - quart_imp.config
```

```python
from quart_imp.config import ImpBlueprintConfig
```

```python
ImpBlueprintConfig(
    enabled: bool = False,
    url_prefix: str = None,
    subdomain: str = None,
    url_defaults: dict = None,
    static_folder: t.Optional[str] = None,
    template_folder: t.Optional[str] = None,
    static_url_path: t.Optional[str] = None,
    root_path: str = None,
    cli_group: str = None,
    init_session: dict = None
)
```

---

A class that holds a Quart-Imp blueprint configuration.

Most of these values are passed to the `Blueprint` class when the blueprint is registered.

The `enabled` argument is used to enable or disable the blueprint. This is useful for feature flags.

`init_session` is used to set the session values in the main `before_request` function.
