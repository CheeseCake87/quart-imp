from quart import current_app as app
from quart import render_template


@app.route("/resources")
async def index():
    return await render_template("index.html")
