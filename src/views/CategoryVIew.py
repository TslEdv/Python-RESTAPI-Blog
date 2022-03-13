from unicodedata import name
from flask import Flask, request, json, Response, Blueprint
from ..models.CategoryModel import CategoryModel, CategorySchema
from marshmallow import ValidationError

category_api = Blueprint('category_api', __name__)
category_schema = CategorySchema()


##create a category
@category_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    try:
        data = category_schema.load(req_data)
    except ValidationError as err:
        return custom_response(err, 400)
    if req_data['name'].isalpha() == False or len(req_data['name']) > 15:
        return custom_response({'error': 'Title may only contain max 15 letters without spaces'}, 404)

    category = CategoryModel(data)
    category.save()

    ser_data = category_schema.dump(category)

    return custom_response(ser_data, 200)



##get a category and it's posts
@category_api.route('/find/<int:category_id>', methods=['GET'])
def get_a_category(category_id):
  category = CategoryModel.get_one_category(category_id)
  if not category:
    return custom_response({'error': 'category not found'}, 404)
  
  ser_category = category_schema.dump(category)
  return custom_response(ser_category, 200)


##update a categories name
@category_api.route('/update/<int:category_id>', methods=['PUT'])
def update(category_id):
    req_data = request.get_json()
    data = category_schema.load(req_data)
    if req_data['name'].isalpha() == False or len(req_data['name']) > 15:
        return custom_response({'error': 'Title may only contain max 15 letters without spaces'}, 404)
    try:
        data = category_schema.load(req_data)
    except ValidationError as err:
        return custom_response(err, 400)

    category = CategoryModel.get_one_category(category_id)
    category.update(data)
    ser_category = category_schema.dump(category)
    return custom_response(ser_category, 200)



##delete a category
@category_api.route('/delete/<int:category_id>', methods=['DELETE'])
def delete(category_id):
    category = CategoryModel.get_one_category(category_id)
    category.delete()
    return custom_response({'message': 'deleted'}, 204)

##get a list of all categories and their blogs
@category_api.route('/all', methods=['GET'])
def get_all():
    category = CategoryModel.get_all_categories()
    ser_category = category_schema.dump(category, many=True)
    return custom_response(ser_category, 200)

##printing out
def custom_response(res, status_code):
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
)