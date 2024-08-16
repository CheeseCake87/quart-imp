```
Menu = ImpBlueprint/Introduction
Title = Quart-Imp Blueprint Introduction
```

The Quart-Imp Blueprint inherits from the Quart Blueprint class, then adds some additional methods to allow for auto
importing of resources and other nested blueprints.

The Quart-Imp Blueprint requires you to provide the `ImpBlueprintConfig` class as the second argument to the Blueprint.

Here's an example of a Quart-Imp Blueprint structure:

```text
www/
├── nested_blueprints/
│   ├── blueprint_one/
│   │   ├── ...
│   │   └── __init__.py
│   └── blueprint_two/
│       ├── ...
│       └── __init__.py
├── standalone_nested_blueprint/
│   ├── ...
│   └── __init__.py
├── routes/
│   └── index.py
├── static/
│   └── ...
├── templates/
│   └── www/
│       └── index.html
└── __init__.py
```

File: `__init__.py`

```python
from quart_imp import ImpBlueprint
from quart_imp.config import ImpBlueprintConfig

bp = ImpBlueprint(__name__, ImpBlueprintConfig(
    enabled=True,
    url_prefix="/www",
    static_folder="static",
    template_folder="templates",
    init_session={"logged_in": False},
))

bp.import_resources("routes")
bp.import_nested_blueprints("nested_blueprints")
bp.import_nested_blueprint("standalone_nested_blueprint")
```

The `ImpBlueprintConfig` class is used to configure the Blueprint. It provides a little more flexibility than the
standard Quart Blueprint configuration, like the ability to enable or disable the Blueprint.

`ImpBlueprintConfig`'s `init_session` works the same as `ImpConfig`'s `init_session`, this will add the session data to
the Quart app's session object on initialization of the Quart app.

To see more about configuration see: [quart_imp.config / ImpBlueprintConfig](quart_imp_config-impblueprintconfig.html)

`import_resources` method will walk one level deep into the `routes` folder, and import all `.py` files as modules.
For more information see: [ImpBlueprint / import_resources](impblueprint-import_resources.html)

`import_nested_blueprints` will do the same as `imp.import_blueprints`, but will register the blueprints found as
nested to the current blueprint. For example `www.blueprint_one.index`

`import_nested_blueprint` behaves the same as `import_nested_blueprints`, but will only import a single blueprint.
