# app/routes.py

from flask import Blueprint, jsonify, request, abort
from app.services import ProductService
from bson.objectid import ObjectId

product_bp = Blueprint('products', __name__)

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    return ProductService.create_product(data)

@product_bp.route('/products', methods=['GET'])
def get_products():
    return ProductService.get_products()

@product_bp.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    return ProductService.get_product(product_id)

@product_bp.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    return ProductService.update_product(product_id, data)

@product_bp.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    return ProductService.delete_product(product_id)
