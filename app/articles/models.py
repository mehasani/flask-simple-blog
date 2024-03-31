from app.database import BaseModel
from app.extensions import db, admin
from app.admin_panel import MyModelView
from flask_login import current_user
import datetime


class Article(BaseModel):
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    content = db.Column(db.Text, nullable=False)
    administrator_id = db.Column(db.Integer, db.ForeignKey('administrator.id'), nullable=True,
                                 default=lambda: current_user.id if current_user.is_authenticated else None)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {self.title[:30]}, {self.date})'


admin.add_view(MyModelView(Article, db.session))
