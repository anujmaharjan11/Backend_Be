from auth.resources import api_bp
from blogs.resources import blogs_bp
from followers.resources import followers_bp

def register_blueprints(app):
    app.register_blueprint(api_bp)
    app.register_blueprint(blogs_bp)
    app.register_blueprint(followers_bp)
