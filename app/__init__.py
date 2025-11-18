from flask import Flask
from app.users import users_bp
from app.products import products_bp
from .views import views_bp

def create_app():
    app = Flask(__name__)
    
    app.config.from_pyfile('../config.py')
    app.secret_key = "sskey123"  

    app.register_blueprint(views_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)

    return app