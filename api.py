from flask import Flask, jsonify, abort

app = Flask(__name__) 
market =[
    {"name": "Chicken", "price": "100"},
    {"name": "Beef", "price": "250"},
    {"name": "Tomato", "price": "200"},
    {"name": "Detergent", "price": "500"},
]

@app.route('/api/market/{product}', methods=['GET'])
def get_price(product):
    for product in market:
        if product['name'].lower() == product.lower():
            return jsonify({"product": product['name'], "price": product['price']})
    abort(404, description="product not found") #abort if loop exitt naturally = not found

if __name__ == '__main__':
    app.run(debug=True)
