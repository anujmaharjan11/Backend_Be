from flask import Blueprint, request
from flask_restful import Resource, Api
from flask_jwt_extended import get_jwt_identity, jwt_required
from .manager import BlogManager
from database import db

blogs_bp = Blueprint('blogs', __name__)
api = Api(blogs_bp)

class BlogListResource(Resource):
    def __init__(self):
        self.blog_manager = BlogManager(db)

    def get(self):
        blogs = self.blog_manager.get_all_blogs()
        blog_list = []
        for blog in blogs:
            blog_data = {
                'id': blog.id,
                'title': blog.title,
                'content': blog.content,
                'author_id': blog.author_id
            }
            blog_list.append(blog_data)

        return blog_list, 200

    @jwt_required()
    def post(self):
        data = request.get_json(force=True, silent=True)
        current_user_id = get_jwt_identity()
        if not data:
            return {'message': 'Missing title or content'}, 400
        if 'title' not in data:
            return {'message': 'Missing title or content'}, 400
        if 'content' not in data:
            return {'message': 'Missing title or content'}, 400
        title = data['title']
        content = data['content']
        blog = self.blog_manager.create_blog(title, content, current_user_id)
        response_data = {
            'message': 'Blog is created. Wow, you really are some writer!',
            'id': blog.id
        }
        return response_data, 201

class BlogResource(Resource):
    def __init__(self):
        self.blog_manager = BlogManager(db)

    def get(self, blog_id):
        blog = self.blog_manager.get_blog_by_id(blog_id)
        if not blog:
            return {'message': 'Blog not found'}, 404
        return {
            'id': blog.id,
            'title': blog.title,
            'content': blog.content,
            'author_id': blog.author_id
        }, 200

    @jwt_required()
    def put(self, blog_id):
        current_user_id = get_jwt_identity()
        blog = self.blog_manager.get_blog_by_id(blog_id)
        
        if not blog:
            return {'message': 'Blog not found'}, 404
            
        if blog.author_id != current_user_id:
            return {'message': 'Unauthorized'}, 403
            
        data = request.get_json(force=True, silent=True)
        updated_blog = self.blog_manager.update_blog(blog_id, data)
        return {'message': 'Blog updated'}, 200

    @jwt_required()
    def delete(self, blog_id):
        current_user_id = get_jwt_identity()
        blog = self.blog_manager.get_blog_by_id(blog_id)
        
        if not blog:
            return {'message': 'Blog not found'}, 404
            
        if blog.author_id != current_user_id:
            return {'message': 'Unauthorized'}, 403
            
        self.blog_manager.delete_blog(blog_id)
        return {'message': 'Blog deleted'}, 200

api.add_resource(BlogListResource, '/blogs')
api.add_resource(BlogResource, '/blogs/<string:blog_id>')
