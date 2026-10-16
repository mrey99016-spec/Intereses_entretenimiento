from flask import Flask
from .routes import routes
import os

def create_app():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    app = Flask(__name__,
                static_folder=os.path.join(base_dir, 'static'),
                template_folder=os.path.join(base_dir, 'templates'))
    app.register_blueprint(routes)
    return app
