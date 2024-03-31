from flask import Flask
import app.exceptions as app_exception
from app.extensions import db, migrate, admin, login_manager, bcrypt
from app.admin_panel import MyAdminIndexView
from app.routes import register_blueprint


def register_error_handlers(app):
    app.register_error_handler(404, app_exception.page_not_found)
    app.register_error_handler(500, app_exception.server_error)


app = Flask(__name__)
register_blueprint(app)
register_error_handlers(app)
app.config.from_object('config.DevConfig')
db.init_app(app)

from app.administrator.models import Administrator
from app.articles.models import Article
from app.administrator import routes

migrate.init_app(app, db)
login_manager.init_app(app)
admin.init_app(app, index_view=MyAdminIndexView())
bcrypt.init_app(app)
