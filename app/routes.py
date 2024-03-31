from app.home.routes import blueprint as home_blueprint
from app.articles.routes import blueprint as post_blueprint


def register_blueprint(app):
    app.register_blueprint(home_blueprint)
    app.register_blueprint(post_blueprint)