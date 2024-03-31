from app.database import BaseModel
from app.extensions import db, admin, login_manager
from flask_login import UserMixin
from app.admin_panel import MyModelView


@login_manager.user_loader
def load_user(administrator_id):
    return Administrator.query.get(int(administrator_id))


class Administrator(BaseModel, UserMixin):
    username = db.Column(db.String(30), unique=True, nullable=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=True)
    password = db.Column(db.String(60), nullable=False)
    articles = db.relationship('Article', backref='author', lazy=True)

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.id}, {self.username})'


admin.add_view(MyModelView(Administrator, db.session))
