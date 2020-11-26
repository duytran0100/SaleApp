import json, hashlib
from saleapp.models import UserRole,User,Product,Category

def read_data(path="data/categories.json"):
    with open(path,encoding="utf-8") as f:
        return json.load(f)


def read_product(cate_id=None,keyword=None,from_price=None,to_price=None):
    # products = read_data(path="data/products.json")
    products = Product.query

    if cate_id:
        # cate_id = int(cate_id)
        # products = [p for p in products if cate_id == p['category_id']]
        products=products.filter(Product.category_id==cate_id)

    if keyword:
        # products = [p for p in products if p['name'].lower().find(keyword.lower()) >=0]
        products=products.filter(Product.name.contains(keyword))

    if from_price and to_price:
        # from_price = float(from_price)
        # to_price = float(to_price)
        # products = [p for p in products if from_price <= p['price'] <= to_price]
        products=products.filter(Product.price.__gt__(from_price),Product.price.__lt__(to_price))

    return products.all()


def get_product_by_id(product_id):
    # products=read_data('data/products.json')
    # for p in products:
    #     if p["id"] == product_id:
    #         return p
    return Product.query.get(Product.id==product_id)


def check_login(username,password,role=UserRole.ADMIN):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    user = User.query.filter(User.username == username, User.password == password,User.user_role == role).first()

    return user


def get_user_by_id(user_id):
    return User.query.get(user_id)