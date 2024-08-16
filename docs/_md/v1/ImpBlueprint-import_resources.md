```
Menu = ImpBlueprint/import_resources
Title = ImpBlueprint.import_resources
```

```python
import_resources(folder: str = "routes") -> None
```

---

Will import all the resources (cli, routes, filters, context_processors...) from the given folder relative to the
Blueprint's root directory.

```text
my_blueprint
├── user_routes
│   ├── user_dashboard.py
│   └── user_settings.py
├── car_routes
│   ├── car_dashboard.py
│   └── car_settings.py
├── static/...
├── templates/
│   └── my_blueprint/
│       ├── user_dashboard.html
│       └── ...
├── __init__.py
```

File: `my_blueprint/__init__.py`

```python
from quart_imp import ImpBlueprint
from quart_imp.config import ImpBlueprintConfig

bp = ImpBlueprint(__name__, ImpBlueprintConfig(
    enabled=True,
    static_folder="static",
    template_folder="templates",
))

bp.import_resources("user_routes")
bp.import_resources("car_routes")
```

File: `my_blueprint/user_routes/user_dashboard.py`

```python
from quart import render_template

from .. import bp

@bp.route("/user-dashboard")
async def user_dashboard():
    return await render_template(bp.tmpl("user_dashboard.html"))
```
