from flask import request, g, Blueprint, json, Response
from . import db
from src.models.CategoryModel import CategoryModel, CategorySchema
from ..models.BlogpostModel import BlogpostModel, BlogpostSchema
from marshmallow import ValidationError

blogpost_api = Blueprint('blogpost_api', __name__)
blogpost_schema = BlogpostSchema()

@blogpost_api.route('/create/<int:category_id>', methods=['POST'])
def create(category_id):
    category = CategoryModel.query.get(category_id)
    req_data = request.get_json()
    if len(req_data['contents']) > 150:
        return custom_response({'error': 'post contents are too long (max 150)'}, 404)
    try:
        data = blogpost_schema.load(req_data)
    except ValidationError as err:
        return custom_response(err, 400)
    post = BlogpostModel(data)
    category.blogposts.append(post)
    post.save()
    data = blogpost_schema.dump(post)
    return custom_response(data, 201)

@blogpost_api.route('/addcategory/<int:blog_id>/<int:category_id>', methods=['PUT'])
def add_category(blog_id, category_id):
    category = CategoryModel.query.get(category_id)
    post = BlogpostModel.get_one_blogpost(blog_id)
    category.add_post(post)
    data = CategorySchema().dump(category)
    return custom_response(data, 201)

@blogpost_api.route('/remcategory/<int:blog_id>/<int:category_id>', methods=['PUT'])
def remove_category(blog_id, category_id):
    category = CategoryModel.query.get(category_id)
    post = BlogpostModel.get_one_blogpost(blog_id)
    category.remove_post(post)
    data = CategorySchema().dump(category)
    return custom_response(data, 201)


@blogpost_api.route('/update/<int:blog_id>', methods=['PUT'])
def update(blog_id):
    req_data = request.get_json()
    if len(req_data['contents']) > 150:
        return custom_response({'error': 'post contents are too long (max 150)'}, 404)
    try:
        data = blogpost_schema.load(req_data)
    except ValidationError as err:
        return custom_response(err, 400)
    post = BlogpostModel.get_one_blogpost(blog_id)
    post.update(data)
    data = blogpost_schema.dump(post)
    return custom_response(data, 201)

@blogpost_api.route('/delete/<int:blog_id>', methods=['DELETE'])
def delete(blog_id):
    post = BlogpostModel.get_one_blogpost(blog_id)
    post.delete()
    return custom_response({'message': 'deleted'}, 204)

@blogpost_api.route('/find/<int:blog_id>', methods=['GET'])
def find(blog_id):
  post = BlogpostModel.get_one_blogpost(blog_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  
  ser_category = blogpost_schema.dump(post)
  return custom_response(ser_category, 200)


def custom_response(res, status_code):
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
)