from flask import render_template, request
from saleapp import app,utils


@app.route('/')
def index():
    categories = utils.read_data()
    return render_template('index.html',categories=categories)


@app.route('/products')
def product_list():
    cate_id=request.args.get('category_id')
    kw=request.args.get('keyword')
    from_price=request.args.get('from_price')
    to_price=request.args.get('to_price')
    products=utils.read_product(cate_id=cate_id,keyword=kw,from_price=from_price,to_price=to_price)
    return render_template('product_list.html',products=products)


@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = utils.get_product_by_id(product_id=product_id)
    return render_template('product_detail.html',product=product)

if __name__ == '__main__':
    app.run(debug=True)