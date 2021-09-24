#!/usr/bin/env python3

import tweepy

# import keys
apiKey = open("/Users/gabrielconlon/.ssh/twitterAPIKeys/key.pub", "r").readline().strip()
apiSecretKey = open("/Users/gabrielconlon/.ssh/twitterAPIKeys/key", "r").readline().strip()

accessKey = open("/Users/gabrielconlon/.ssh/twitterAPIKeys/access.pub", "r").readline().strip()
accessSecretKey = open("/Users/gabrielconlon/.ssh/twitterAPIKeys/access", "r").readline().strip()


# Authenticate to Twitter
#For the OAuthHandler, use the API key followed by the API secret Key. (From "Consumer Keys")
auth = tweepy.OAuthHandler(apiKey, apiSecretKey)

#For the set_access_token, use the access token followed by the access token secret (From "Authentication Tokens")
auth.set_access_token(accessKey, accessSecretKey)

api = tweepy.API(auth)
if (api.verify_credentials()):
    print("Authentication OK")
else:
    print("Error during authentication")