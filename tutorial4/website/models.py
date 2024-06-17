from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    waste_collections = db.relationship('WasteCollection')
    recycling_efforts = db.relationship('RecyclingEffort')

class WasteCollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    address = db.Column(db.String(256))
    collection_date = db.Column(db.Date)
    collection_time = db.Column(db.Time)
    status = db.Column(db.String(64))

    def __repr__(self):
        return f'<WasteCollection {self.collection_date}>'

class RecyclingEffort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    materials = db.Column(db.String(256))

    def __repr__(self):
        return f'<RecyclingEffort {self.date}>'