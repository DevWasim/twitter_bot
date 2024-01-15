import tweepy
import time

# Login your account here : https://developer.twitter.com/    <---- to genrate your key and other stuff Watch Video On YT if U don't know

api_key = 'TOOVvduLlZlywree22DFytxxov'   # change this with your own API key 
api_secret = '0SXa6qUaiQoOFturt09rL4TrrwcewOdgjjKoc8mtdANs8M'       # change this with your own API secret
bearer_token = 'AregdhtryrtAAL6mrwEAAAs%2FopmYdfhdhbd%2F4xp72Q%3DrlVJqrxVkkgvnRW333354352dg0m1ohjUzZwilCEFgVyT'  # bearer-token
access_token = '1688dfre567786iouoi567-ltYgc4KK1vsGaD2hjTS9KO8S9bc8KW'       # change this with your own access token
access_token_secret = '9RjVPPbUGTY55434RinTLVqGcXvJm345353533l37NxU4yBDic3qOu'      # change this with your own access token secret 

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)


#its just a simple bot to post on your profile : you can also add media-part (Video , Image Or file for uploading )

api = tweepy.API(auth)
for i in range(0,1):
    client.create_tweet(text=f'Hello Bro How are You All ! i hope You all are doing well. 😍😁🙌 {i}')
    








# Uncoment this below code to like all the posts which contains's the search_string keyword ,make sure your key are Your own:

# api = tweepy.API(auth)
# user = api.verify_credentials()


# def limit_handler(cursor):
#     try:
#         while True:
#             yield cursor.next()
#     except tweepy.RateLimitError:
#         time.sleep(300)

# search_string = 'pyhton'
# number_of_tweets = 5

# for tweet in tweepy.Cursor(api.search_tweets, q=search_string).items(number_of_tweets):
#     try:
#         tweet.favorite() 
#         print('I like that tweet')
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break














