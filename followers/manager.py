import uuid
from .models import Follow
from auth.models import User

class FollowManager:    
    def __init__(self, db):
        self.follow_db = db
    
    def follow(self, from_user_id, to_user_id):
        if User.query.filter_by(id=to_user_id).first() is None:
            return None

        if Follow.query.filter_by(from_user_id=from_user_id, to_user_id=to_user_id).first():
            return False

        follow = Follow(
            from_user_id=from_user_id,
            to_user_id=to_user_id,
        )
        self.follow_db.session.add(follow)
        self.follow_db.session.commit()
        return follow