from quart import render_template

from .. import bp


@bp.route("/", methods=["GET"])
async def index():
    return await render_template(bp.tmpl("index.html"))
