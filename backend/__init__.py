import os
from flask import Flask
from .start import start_bp
from API.chatbot import chatbot_bp

def create_app():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend'))
    template_folder = os.path.join(base_dir, 'templates')
    static_folder = os.path.join(base_dir, 'static')

    app = Flask(
        __name__,
        template_folder=template_folder,
        static_folder=static_folder
    )

    app.register_blueprint(start_bp)
    app.register_blueprint(chatbot_bp, url_prefix="/chatbot")
    return app
