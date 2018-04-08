# Production config
# Local config: instance/config.py (create one if not already available)
# Remove .example from this file's name after filling out all the keys

# Your own webhook verification token for Facebook to forward to
OWN_WEBHOOK_TOKEN='my_voice_is_my_password_verify_me'

# Do not allow debug mode for production
DEBUG=False

# Facebook Page Access Token
PAT = 'EAACaTM4n1JsBABr3eQodedQg2xTiWyfNhXHgesufdqAe1HeBhHQ23h9K6ADH27N9JYjXwEkJImOlNoyoNQvmJs8ORwKazu9ZCQbZAsAZCHrmh9RCwWjwNE4ncVdSkZA1fUbEEDN4yKBCDfP9WG2B9VjHjAUv4O0CVpdk2XFggCbXMOMreYtk'
FACEBOOK_APP_ID = '169654666908827'
FACEBOOK_APP_SECRET = 'my_voice_is_my_password_verify_me'

#Yelp
# v2
CONSUMER_KEY=""
CONSUMER_SECRET=""
TOKEN=""
TOKEN_SECRET=""

# v3
YELP_V3_TOKEN = 'MLYbgKFwq56q7nW9U5Qyr_7QW2acEBlBF4d30rkecOezexNEGNSL0_Cnbe-tbind4owbLCEATPWrsi5-EwIqd2zSLMvX6mYS-yjOUh8XVSGADCygCbl2A8WLWnfJWnYx'

# Heroku MongoDB ============
MONGO_URI = "mongodb://heroku_882xdp5d:1k9nn3f6hpup42217d03ubajkt@ds239009.mlab.com:39009/heroku_882xdp5d"
MONGO_DBNAME = '' # Get database

SIMSIMI_KEY = '7ac24c65-d01b-430a-beb1-41c147467157'

# Bot operation variables:
PRINT_INCOMING_PAYLOAD = False
PRINT_INCOMING_MESSAGE = False