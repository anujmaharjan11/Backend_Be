from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from database import db
from blueprints import register_blueprints

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["JWT_SECRET_KEY"] = "super-secret-key"

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
