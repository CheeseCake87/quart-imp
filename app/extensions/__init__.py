import quart_flask_patch
from flask_sqlalchemy import SQLAlchemy

from quart_imp import Imp

_ = quart_flask_patch

imp = Imp()
db = SQLAlchemy()
