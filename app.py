from flask import Flask, request, json, jsonify
import json

app = Flask(__name__)

products = {1: {'name': 'uva', 'price': 'R$2.00'},
            2: {'name': 'maça', 'price': 'R$2.50'},
            3: {'name': 'laranja', 'price': 'R$3.00'}}


@app.route('/products', methods=['GET'])
def get_products():
    return products


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_id(product_id):
    if product_id not in products:
        return "Esse id não corresponde a um produto cadastrado"
    else:
        return products[product_id]


@app.route('/products/<int:product_id>', methods=['POST'])
def post_product(product_id):
    if product_id in products:
        return "Já existe um produto com esse id"
    else:
        products_dados = json.loads(request.data)
        products[product_id] = products_dados
        return products_dados


@app.route('/products/<int:product_id>', methods=['PUT'])
def put_product(product_id):
    if product_id not in products:
        return "Esse id não corresponde a um produto cadastrado"
    else:
        products_dados = json.loads(request.data)
        products[product_id] = products_dados
        return products_dados


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id not in products:
        return "Esse id não corresponde a um produto cadastrado"
    else:
        del products[product_id]
        return products


if __name__ == '__main__':
    app.run()
