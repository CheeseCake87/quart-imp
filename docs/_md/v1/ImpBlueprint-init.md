```
Menu = ImpBlueprint/__init__
Title = Quart-Imp Blueprint __init__
```

```python
ImpBlueprint(dunder_name: str, config: ImpBlueprintConfig) -> None
```

---

Initializes the Quart-Imp Blueprint.

`dunder_name` should always be set to `__name__`

`config` is an instance of `ImpBlueprintConfig` that will be used to load the Blueprint's configuration. 
See [quart_imp.config / ImpBlueprintConfig](quart_imp_config-impblueprintconfig.html) for more information.
