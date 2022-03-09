from unicodedata import name
from flask import Flask, request, json, Response, Blueprint
from ..models.CategoryModel import CategoryModel, CategorySchema
from marshmallow import ValidationError

category_api = Blueprint('category_api', __name__)
category_schema = CategorySchema()

@category_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    data = category_schema.load(req_data)
    try:
        data = category_schema.load(req_data)
    except ValidationError as err:
        return custom_response(err, 400)
    
    ##add count here for everything

    category = CategoryModel(data)
    category.save()

    ser_data = category_schema.dump(category)

    return custom_response(ser_data, 200)


@category_api.route('/find/<int:category_id>', methods=['GET'])
def get_a_category(category_id):
  category = CategoryModel.get_one_category(category_id)
  if not category:
    return custom_response({'error': 'category not found'}, 404)
  
  ser_category = category_schema.dump(category)
  return custom_response(ser_category, 200)


@category_api.route('/update/<int:category_id>', methods=['PUT'])
def update(category_id):
    req_data = request.get_json()
    data = category_schema.load(req_data)
    try:
        data = category_schema.load(req_data)
    except ValidationError as err:
        return custom_response(err, 400)

    category = CategoryModel.get_one_category(category_id)
    category.update(data)
    ser_category = category_schema.dump(category)
    return custom_response(ser_category, 200)


@category_api.route('/delete/<int:category_id>', methods=['DELETE'])
def delete(category_id):
    category = CategoryModel.get_one_category(category_id)
    category.delete()
    return custom_response({'message': 'deleted'}, 204)

def custom_response(res, status_code):
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
)