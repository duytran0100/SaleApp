from saleapp import admin, db
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from saleapp.models import Category, Product
from flask_login import logout_user, current_user
from flask import redirect


class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render("admin/contact.html")


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated

class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(AuthenticatedView(Category, db.session))
admin.add_view(AuthenticatedView(Product, db.session))
admin.add_view(ContactView(name="Liên hệ"))
admin.add_view(LogoutView(name='Đăng xuất'))
