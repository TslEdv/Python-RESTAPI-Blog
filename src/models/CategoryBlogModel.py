from . import db
from sqlalchemy.orm import relationship, backref

categorypblogs = db.Table('categoryblogs',
    db.Column('blogpost_id', db.Integer, db.ForeignKey('blogposts.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)