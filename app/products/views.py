from flask import render_template
from . import products_bp

# Список цін на продукти 
products = {
    'apple': 35,
    'banana': 65,
    'milk': 60,
    'bread': 25
}

@products_bp.route('/product/<string:name>')
def product(name):
    name = name.lower()
    price = products.get(name)
    return render_template('products.html', name=name, price=price)