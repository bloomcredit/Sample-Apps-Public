from flask import Flask
from api.auth import authRequest
from logging.config import dictConfig


def create_app() -> Flask:
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': "%(levelname)s:\t %(asctime)s - [%(name)s] %(filename)s::%(funcName)s - %(message)s",
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })

    app = Flask(__name__)
    app.config.from_object('config')

    if 'vantage' not in app.config["SKU"]:
        raise Exception(
            "Only VANTAGE SKU allowed for this app, please change in config.py")

    # Get access token
    accessToken = authRequest(app)

    app.config["ACCESS_TOKEN"] = accessToken

    return app
