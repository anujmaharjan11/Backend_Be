from flask import Blueprint, request
from flask_restful import Resource, Api
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from .manager import AuthManager
from database import db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class UserResource(Resource):
    def __init__(self):
        self.auth_manager = AuthManager(db)
    
    def post(self):
        try:
            user = self.auth_manager.create_user(request.json)
            return {'message': 'User created', 'id': user.id}, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    def get(self):
        users = self.auth_manager.get_all_users()
        return [{'id': u.id, 'username': u.username, 'email': u.email} for u in users]

class LoginResource(Resource):
    def __init__(self):
        self.auth_manager = AuthManager(db)
    
    def post(self):
        data = request.get_json(force=True, silent=True)
        
        email = data.get("email") if data else None
        password = data.get("password") if data else None

        if not email or not password:
            return {"msg": "Email and password required"}, 400

        user = self.auth_manager.authenticate_user(email, password)
        if not user:
            return {"msg": "Invalid credentials"}, 401

        access_token = create_access_token(identity=str(user.id))
        return {"access_token": access_token, "user_id": user.id}, 200

class ProfileResource(Resource):
    def __init__(self):
        self.auth_manager = AuthManager(db)
    
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = self.auth_manager.get_user_by_id(user_id)

        if not user:
            return {"msg": "User not found"}, 404

        return {
            "msg": "Access granted",
            "user_id": user.id,
            "username": user.username,
            "email": user.email
        }

api.add_resource(UserResource, '/users')
api.add_resource(LoginResource, '/login')
api.add_resource(ProfileResource, '/profile')
