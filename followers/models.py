from datetime import datetime
import uuid
from database import db

class Follow(db.Model):
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4())) #initiating FOLLOW
    from_user_id = db.Column(db.String(), db.ForeignKey('user.id'), nullable=False)   
    to_user_id = db.Column(db.String(), db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint("from_user_id", "to_user_id", name="unique_follow"),
    )

    follower = db.relationship("User", foreign_keys=[from_user_id], backref="following_records") #who i follow
    following = db.relationship("User", foreign_keys=[to_user_id], backref="follower_records") #who follows me

    def __repr__(self):
        return f"<Follow from={self.from_user_id} to={self.to_user_id}>"
