# Welcome to the Quart-Imp Documentation

## What is Quart-Imp?

Quart-Imp's main purpose is to help simplify the importing of blueprints, and resources. It has a few extra
features built in to help with securing pages and password authentication.

## Install Quart-Imp

```bash
pip install quart-imp
```

## Getting Started

To get started right away, you can use the CLI commands to create a new Quart-Imp project.

```bash
quart-imp init
```

### Minimal Quart-Imp Setup

Run the following command to create a minimal Quart-Imp project.

```bash
quart-imp init -n app --minimal
```

See [CLI Commands / quart-imp init](cli_commands-quart-imp_init.html) for more information.

### The minimal structure

#### Folder Structure

```text
app/
├── resources/
│   ├── static/...
│   ├── templates/
│   │   └── index.html
│   └── index.py
└── __init__.py
```

File: `app/__init__.py`

```python
from quart import Quart

from quart_imp import Imp
from quart_imp.config import QuartConfig, ImpConfig

imp = Imp()


def create_app():
    app = Quart(__name__, static_url_path="/")
    QuartConfig(
        secret_key="secret_key",
        app_instance=app
    )
    
    imp.init_app(app, ImpConfig())

    imp.import_app_resources()
    # Takes argument 'folder' default folder is 'resources'

    return app
```

File: `app/resources/routes.py`

```python
from quart import current_app as app
from quart import render_template


@app.route("/")
async def index():
    return await render_template("index.html")
```

File: `app/resources/templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quart-Imp</title>
</head>
<body>
<h1>Quart-Imp</h1>
</body>
</html>
```

---

Setting up a virtual environment is recommended.

**Linux / Darwin**

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
```

```text
.\venv\Scripts\activate
```