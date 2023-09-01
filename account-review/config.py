"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

# First, get the directory of the current file
current_dir = path.abspath(path.dirname(__file__))

# Then, get the parent directory of the current directory
basedir = path.dirname(current_dir)

load_dotenv(path.join(basedir, '.env'))

TESTING = True
DEBUG = True

# .env values
CLIENT_ID = environ.get('CLIENT_ID')
CLIENT_SECRET = environ.get('CLIENT_SECRET')

# Setup your data here
PORTFOLIO_ID = "3694075a-661a-4d36-a775-b7c68fb00412"
SKU = "equifax-silver-soft-vantage-internet"

# equifax-silver-soft-vantage-internet
# equifax-gold-soft-vantage-internet

# static urls
BLOOM_AUTH_URL = "https://bloomcredit-dev.auth0.com/oauth/token"
ORDER_DATA_URL = "https://sandbox.bloom.dev/v2/data-access/orders/"
CONSUMER_URL = "https://sandbox.bloom.dev/v2/core/consumers"
QUERY_DATA_GQL_URL = "https://sandbox.bloom.dev/v2/data-access/graphql"