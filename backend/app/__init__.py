from flask import Flask
from flask_cors import CORS

from .routes.hello_routes import api_bp
from .routes.user_routes import user_bp

def create_app():
	app = Flask(__name__)
	
	app.config.from_object("config.Config")
 
	CORS(app)

 	# Register Blueprints
	app.register_blueprint(user_bp, url_prefix="/api/users")
	app.register_blueprint(api_bp, url_prefix="/api")

	return app
