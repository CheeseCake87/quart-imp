from quart import Quart

from app.extensions import imp, db


def create_app():
    app = Quart(__name__, static_url_path="/")

    imp.init_app(app)
    imp.import_app_resources(
        files_to_import=["*"],
        folders_to_import=["*"]
    )
    imp.import_blueprints("blueprints")
    imp.import_models("models")

    db.init_app(app)

    @app.before_serving
    async def create_tables():
        db.create_all()

    return app
