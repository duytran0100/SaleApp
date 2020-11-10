from saleapp import db
from sqlalchemy import Integer,Float,String,Column,ForeignKey
from sqlalchemy.orm import relationship

class Category(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False)
    products = relationship('Product',backref='category',lazy=True)

class Product(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False)
    price = Column(Float,default=0)
    description = Column(String(255),nullable=True)
    category_id = Column(Integer,ForeignKey(Category.id),nullable=False)

if __name__ == '__main__':
    db.create_all()