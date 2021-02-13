import tweepy
from credentials.credentials import consumer_key, consumer_secret, access_token, access_token_secret
import re

def initalize():
    # Twitterオブジェクトの生成--------------------------------------------
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #-------------------------------------------------------------------

    return api

def strip_id(str):
    id_list = re.findall(r'[0-9A-F]{8}\s:参戦ID', str)
    if id_list:
        return id_list[-1][0:8]
    else:
        return None