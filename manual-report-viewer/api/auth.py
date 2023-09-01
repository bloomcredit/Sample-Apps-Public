from requests import post
from models.request import AuthRequest


def authRequest(app):
    """
    Getting auth credentials
    """
    headers = {
        'content-type': 'application/json',
    }

    # Make auth request object to /oauth/token
    json_data = AuthRequest(
        client_id=app.config["CLIENT_ID"],
        client_secret=app.config["CLIENT_SECRET"],
        audience='dev-api',
        grant_type='client_credentials').dict()

    # Make actual request
    r = post(app.config["BLOOM_AUTH_URL"],
             headers=headers, json=json_data)

    access_token = r.json()['access_token']

    app.logger.info(
        "Success getting access token: %s", access_token)

    #  Return access_token
    return access_token
