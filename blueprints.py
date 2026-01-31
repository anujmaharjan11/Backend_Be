from auth.resources import api_bp

def register_blueprints(app):
    app.register_blueprint(api_bp)