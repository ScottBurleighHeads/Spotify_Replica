from dotenv import load_dotenv
load_dotenv()

# Flask application creation
from flask import Flask, jsonify
from marshmallow.exceptions import ValidationError
app = Flask(__name__)
app.config.from_object("default_settings.app_config")

# Database connection
from database import init_db
db = init_db(app)

# Serialization
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

# Controller Registration
from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)               # Registers the endpoints on the blueprint from endpoints.py

from commands import db_commands
app.register_blueprint(db_commands)

@app.errorhandler(ValidationError)
def handle_bad_request(error):
    return (jsonify(error.messages),400)






