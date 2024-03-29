from quart_imp import Blueprint

bp = Blueprint(__name__)

bp.import_resources("routes")


@bp.before_app_request
async def before_app_request():
    bp.init_session()
