from flask import Blueprint, request
from flask_restful import Resource, Api
from flask_jwt_extended import get_jwt_identity, jwt_required
from .manager import FollowManager
from database import db

followers_bp = Blueprint('followers', __name__)
api = Api(followers_bp)

class FollowerResource(Resource):
    def __init__(self):
        self.follow_manager = FollowManager(db)

    @jwt_required()
    def post(self):
        data = request.get_json(force=True, silent=True)
        current_user_id = get_jwt_identity()
        if not data:
            return {'message': 'Missing all'}, 400
        # if 'from_user_id' not in data:
        #     return {'message': 'Missing user id'}, 400
        if 'to_user_id' not in data:
            return {'message': 'Missing the following user id'}, 400
        if 'created_at' not in data:
            return {'message': 'Missing the created date'}, 400
        
        to_user_id = data['to_user_id']
        created_at = data['created_at']
        follow = self.follow_manager.follow(current_user_id, to_user_id, created_at)
        response_data = {
            'message': 'User followed the other user. Wow!',
            'id': follow.id
        }
        return response_data, 201
    

api.add_resource(FollowerResource, '/follow')
