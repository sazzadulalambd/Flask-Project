# app/services.py

from flask import jsonify, abort
from app import mongo
from bson.objectid import ObjectId

class ProductService:

    @staticmethod
    def create_product(data):
        if not data or not "name" in data or not "price" in data:
            abort(400, "Name and Price are required fields.")
        
        new_product = {
            'name': data['name'],
            'price': data['price'],
            'category': data.get('category', 'general'),
            'description': data.get('description', ''),
            'size': data.get('size'),
            'color': data.get('color')
        }
        
        product_id = mongo.db.products.insert_one(new_product).inserted_id
        return jsonify({'id': str(product_id), 'message': 'Product created successfully'}), 201

    @staticmethod
    def get_products():
        products = []
        for product in mongo.db.products.find():
            product['_id'] = str(product['_id'])
            products.append(product)
        
        return jsonify(products), 200

    @staticmethod
    def get_product(product_id):
        product = mongo.db.products.find_one({'_id': ObjectId(product_id)})
        if not product:
            abort(404, "Product not found")
        
        product['_id'] = str(product['_id'])
        return jsonify(product), 200

    @staticmethod
    def update_product(product_id, data):
        updated_fields = {}

        if 'name' in data:
            updated_fields['name'] = data['name']
        if 'price' in data:
            updated_fields['price'] = data['price']
        if 'category' in data:
            updated_fields['category'] = data['category']
        if 'description' in data:
            updated_fields['description'] = data['description']
        if 'size' in data:
            updated_fields['size'] = data['size']
        if 'color' in data:
            updated_fields['color'] = data['color']
        
        if not updated_fields:
            abort(400, "No fields provided for update.")
        
        result = mongo.db.products.update_one({'_id': ObjectId(product_id)}, {'$set': updated_fields})
        if result.matched_count == 0:
            abort(404, "Product not found")
        
        return jsonify({'message': 'Product updated successfully'}), 200

    @staticmethod
    def delete_product(product_id):
        result = mongo.db.products.delete_one({'_id': ObjectId(product_id)})
        if result.deleted_count == 0:
            abort(404, "Product not found")
        
        return jsonify({'message': 'Product deleted successfully'}), 200
