```
Menu = Imp/import_blueprints
Title = Imp.import_blueprints
```

```python
import_blueprints(self, folder: str) -> None
```

---

Import all Quart-Imp or standard Quart Blueprints from a specified folder relative to the Quart app root.

```text
app/
├── blueprints/
│   ├── admin/
│   │   ├── ...
│   │   └── __init__.py
│   ├── www/
│   │   ├── ...
│   │   └── __init__.py
│   └── api/
│       ├── ...
│       └── __init__.py
├── ...
└── __init__.py
```

File: `app/__init__.py`

```python
from quart import Quart

from quart_imp import Imp

imp = Imp()


def create_app():
    app = Quart(__name__)
    imp.init_app(app)

    imp.import_blueprints("blueprints")

    return app
```

This will import all Blueprints from the `blueprints` folder using the `Imp.import_blueprint` method.
See [Imp / import_blueprint](imp-import_blueprint.html) for more information.