import uuid
from .models import Follow

class FollowManager:    
    def __init__(self, db):
        self.follow_db = db
    
    def follow(self, from_user_id, to_user_id, created_at):
        follow = Follow(
            id=str(uuid.uuid4()),
            from_user_id=from_user_id,
            to_user_id=to_user_id,
            created_at=created_at
        )
    
        self.follow_db.session.add(follow)
        self.follow_db.session.commit()
        return follow