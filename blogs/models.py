import uuid
from database import db
from auth.models import User

class Blog(db.Model):
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    author_id = db.Column(db.String(), db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref='blogs')

