#!/usr/bin/env python3

import tweepy

# import keys
keyFilePath = "<path to folder containing keys>"
apiKey = open(f"{keyFilePath}key.pub", "r").readline().strip()
apiSecretKey = open(f"{keyFilePath}key", "r").readline().strip()

accessKey = open(f"{keyFilePath}access.pub", "r").readline().strip()
accessSecretKey = open(f"{keyFilePath}access", "r").readline().strip()


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


run = True
while run:
    # Options menu
    option = input("""
    Choose an option:
        1: Post a tweet
        2: Read tweets
        3: Quit
    """)
    if option == "1":
        # Post a tweet
        tweet = input("Enter text to tweet: ")
        api.update_status(tweet)
    elif option == "2":
        public_tweets = api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)
    elif option == "3":
        run = False
    else:
        print("Invalid Input.")