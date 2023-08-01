from flask import Flask, render_template

app = Flask(__name__)

# Cписок категорий и товаров
categories = [
    {"name": "Clothing", "products": [
        {"id": 1, "name": "T-Shirt", "price": 19.99, "description": "Comfortable cotton T-Shirt"},
        {"id": 2, "name": "Jeans", "price": 49.99, "description": "Stylish denim jeans"},
    ]},
    {"name": "Shoes", "products": [
        {"id": 3, "name": "Sneakers", "price": 59.99, "description": "Sporty sneakers"},
        {"id": 4, "name": "Boots", "price": 79.99, "description": "Leather boots for all seasons"},
    ]},
]

@app.route('/')
def home():
    return "Welcome to our online store!"

@app.route('/category/<category_name>')
def category(category_name):
    category_data = next((category for category in categories if category["name"] == category_name), None)
    if not category_data:
        return "Category not found", 404

    return render_template('category.html', category_name=category_name, products=category_data["products"])

@app.route('/product/<int:product_id>')
def product(product_id):
    product_data = next((product for category in categories for product in category["products"] if product["id"] == product_id), None)
    if not product_data:
        return "Product not found", 404

    return render_template('product.html', product_name=product_data["name"],
                           product_price=product_data["price"], product_description=product_data["description"])

if __name__ == '__main__':
    app.run(debug=True)
