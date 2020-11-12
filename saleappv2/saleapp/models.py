from saleapp import db
from sqlalchemy import Integer, Float, String, Column, ForeignKey, Boolean
from sqlalchemy.orm import relationship


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


if __name__ == '__main__':
    db.create_all()