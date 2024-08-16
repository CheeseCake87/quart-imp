```
Menu = Imp/Introduction
Title = Quart-Imp Introduction
```

Quart-Imp is a Quart extension that provides auto import methods for various Quart resources. It will import 
blueprints, and other resources. It uses the importlib module to achieve this.

Quart-Imp favors the application factory pattern as a project structure, and is opinionated towards using 
Blueprints. However, you can use Quart-Imp without using Blueprints.

Here's an example of a standard Quart-Imp project structure:

```text
app/
├── blueprints/
│   ├── admin/...
│   ├── api/...
│   └── www/...
├── resources/
│   ├── filters/...
│   ├── context_processors/...
│   ├── static/...
│   └── templates/...
└── __init__.py
```

Here's an example of the `app/__init__.py` file:

```python
from quart import Quart
from quart_sqlalchemy import SQLAlchemy
from quart_imp import Imp
from quart_imp.config import QuartConfig, ImpConfig

db = SQLAlchemy()
imp = Imp()


def create_app():
    app = Quart(__name__)
    QuartConfig(
        secret_key="super_secret_key",
        app_instance=app,
    )
    
    imp.init_app(app, config=ImpConfig(
        init_session={"logged_in": False},
    ))
    imp.import_app_resources("resources")
    imp.import_blueprints("blueprints")
    
    db.init_app(app)

    return app
```

The Quart configuration can be loaded from any standard Quart configuration method, or from the `QuartConfig` class
shown above.

This class contains the standard Quart configuration options found in the Quart documentation.

The `ImpConfig` class is used to configure the `Imp` instance.

The `init_session` option of the `ImpConfig` class is used to set the initial session variables for the Quart app. 
This happens before the request is processed.

`ImpConfig` also has the ability to set `SQLALCHEMY_DATABASE_URI` and `SQLALCHEMY_BINDS`

For more information about the configuration setting see 
[quart_imp_config-impconfig.md](quart_imp_config-impconfig.html).

`import_app_resources` will walk one level deep into the `resources` folder, and import 
all `.py` files as modules. 
It will also check for the existence of a `static` and `templates` folder, and register them with the Quart app.

There is a couple of options for `import_app_resources` to control what
is imported, see: [Imp / import_app_resources](imp-import_app_resources.html)

`import_blueprints` expects a folder that contains many Blueprint as Python packages.
It will check each blueprint folder's `__init__.py` file for an instance of a Quart Blueprint or a
Quart-Imp Blueprint. That instant will then be registered with the Quart app.

See more about how importing blueprints work here: [ImpBlueprint / Introduction](impblueprint-introduction.html)
