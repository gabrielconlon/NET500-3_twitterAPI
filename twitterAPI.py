#!/usr/bin/env python3

import tweepy

# Authenticate to Twitter
#For the OAuthHandler, use the API key followed by the API secret Key. (From "Consumer Keys")
auth = tweepy.OAuthHandler("0Gw6VR69N1Z7DS5yvKO1RLh1F", "pamyF8wbl7NCYjsrUpPNqMlVgIcvqRCjyIHX4FzQQNBfxH8N2o")

#For the set_access_token, use the access token followed by the access token secret (From "Authentication Tokens")
auth.set_access_token("1369710522241675264-JQ72t6e5Znrhbjv8HLwkgmVc1xqcuJ", "FKT703PdVCLFlfVcy7lv88pgGYVeyEYSixJ9cRpbl3noU")

api = tweepy.API(auth)
if (api.verify_credentials()):
    print("Authentication OK")
else:
    print("Error during authentication")