from flask import Flask
from api.auth import authRequest
from db import init_db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('config')

    if 'vantage' not in app.config["SKU"]:
        raise Exception("Only VANTAGE SKU allowed for this app, please change in config.py")

    # Get access token
    accessToken = authRequest(app)

    app.config["ACCESS_TOKEN"] = accessToken

    init_db.create()

    return app