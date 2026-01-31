import uuid
from .models import User

class AuthManager:    
    def __init__(self, db):
        self.db = db
    
    def create_user(self, user_data):

        if User.query.filter_by(email=user_data['email']).first():
            raise ValueError('Email already exists')
        if User.query.filter_by(username=user_data['username']).first():
            raise ValueError('Username already exists')
        
        # Create user
        user = User(
            id=str(uuid.uuid4()),
            username=user_data['username'],
            email=user_data['email']
        )
        user.set_password(user_data['password'])
        
        self.db.session.add(user)
        self.db.session.commit()
        return user
    
    def authenticate_user(self, email, password):        
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return user
        return None
    
    def get_user_by_id(self, user_id):
        return User.query.get(user_id)
    
    def get_all_users(self):
        return User.query.all()

# Global auth manager instance
# auth_manager = AuthManager(db)



