```
Menu = Imp/import_blueprint
Title = Imp.import_blueprint
```

```python
import_blueprint(self, blueprint: str) -> None
```

---

Import a specified Quart-Imp or standard Quart Blueprint relative to the Quart app root.


```text
app
├── my_blueprint
│   ├── ...
│   └── __init__.py
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

    imp.import_blueprint("my_blueprint")

    return app
```

Quart-Imp Blueprints have the ability to auto import resources, and initialize session variables.

For more information on how Quart-Imp Blueprints work, see the [ImpBlueprint / Introduction](impblueprint-introduction.html)

##### Example of 'my_blueprint' as a Quart-Imp Blueprint:

```text
app
├── my_blueprint
│   ├── routes
│   │   └── index.py
│   ├── static
│   │   └── css
│   │       └── style.css
│   ├── templates
│   │   └── my_blueprint
│   │       └── index.html
│   ├── __init__.py
│   └── config.toml
└── ...
```

File: `__init__.py`

```python
from quart_imp import ImpBlueprint
from quart_imp.config import ImpBlueprintConfig

bp = ImpBlueprint(
    __name__,
    ImpBlueprintConfig(
        enabled=True,
        url_prefix="/my-blueprint",
        static_folder="static",
        template_folder="templates",
        static_url_path="/static/my_blueprint",
        init_session={"my_blueprint": "session_value"},
    ),
)

bp.import_resources("routes")
```

File: `routes / index.py`

```python
from .. import bp


@bp.route("/")
async def index():
    return "regular_blueprint"
```

##### Example of 'my_blueprint' as a standard Quart Blueprint:

```text
app
├── my_blueprint
│   ├── ...
│   └── __init__.py
└── ...
```

File: `__init__.py`

```python
from quart import Blueprint

bp = Blueprint("my_blueprint", __name__, url_prefix="/my-blueprint")


@bp.route("/")
async def index():
    return "regular_blueprint"
```

Both of the above examples will work with `imp.import_blueprint("my_blueprint")`, they will be registered
with the Quart app, and will be accessible via `url_for("my_blueprint.index")`.