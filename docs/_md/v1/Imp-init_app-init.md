```
Menu = Imp/init_app, __init__
Title = Imp.init_app, __init__
```

```python
def init_app(
    app: Quart,
    config: ImpConfig
) -> None:
# -or- 
Imp(
    app: Quart,
    config: ImpConfig
)
```

---

Initializes the quart app to work with quart-imp.

See [quart_imp_config-impconfig.md](quart_imp_config-impconfig.html) for more information on the `ImpConfig` class.
