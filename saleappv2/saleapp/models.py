from saleapp import db
from sqlalchemy import Integer, Float, String, Column, ForeignKey, Boolean,Enum
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from enum import Enum as UserEnum

class SaleBase(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class Category(SaleBase):
    products = relationship('Product', backref='category', lazy=True)


class Product(SaleBase):
    price = Column(Float, default=0)
    description = Column(String(255), nullable=True)
    image = Column(String(255), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class User(SaleBase, UserMixin):
    __tablename__ = 'user'

    email = Column(String(100))
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100))
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole),default=UserRole.USER)

if __name__ == '__main__':
    db.create_all()