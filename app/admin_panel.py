from flask import redirect
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/admin/login')


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/admin/login')
