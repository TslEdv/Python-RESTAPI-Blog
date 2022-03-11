from marshmallow import fields, Schema
import datetime
from . import db
from .BlogpostModel import BlogpostSchema
from sqlalchemy.orm import relationship
from .CategoryBlogModel import categorypblogs

class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    blogposts = relationship("BlogpostModel", secondary=categorypblogs, lazy='subquery',
        backref=db.backref('categories', lazy=True))

    def __init__(self, data):
        self.name = data.get('name')


    def save(self):
        db.session.add(self)
        db.session.commit()


    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def add_post(self, data):
        self.blogposts.append(data)
        db.session.commit()

    def remove_post(self, data):
        self.blogposts.remove(data)
        db.session.commit()


    @staticmethod
    def get_all_categories():
        return CategoryModel.query.all()


    @staticmethod
    def get_one_category(id):
        return CategoryModel.query.get(id)

  
    def __repr(self):
        return '<id {}>'.format(self.id)

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    blogposts = fields.Nested(BlogpostSchema, many=True)