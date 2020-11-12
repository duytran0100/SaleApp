from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/saledb?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key="!@@#@!#%$^$%^@!#!@#"


db = SQLAlchemy(app=app)
admin = Admin(app=app, name="IT82 SHOP", template_mode="Bootstrap4")

