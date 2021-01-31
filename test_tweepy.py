# twitterテスト

# ツイートを取得

import tweepy
from credentials.credentials import consumer_key, consumer_secret, access_token, access_token_secret

# Twitterオブジェクトの生成--------------------------------------------
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#-------------------------------------------------------------------

#ツイートを投稿
Account = "test" #取得したいユーザーのユーザーIDを代入
tweets = api.user_timeline(Account, count=200, page=1)
num = 1 #ツイート数を計算するための変数
for tweet in tweets:
    print('twid : ', tweet.id)               # tweetのID
    print('user : ', tweet.user.screen_name)  # ユーザー名
    print('date : ', tweet.created_at)      # 呟いた日時
    print(tweet.text)                  # ツイート内容
    print('favo : ', tweet.favorite_count)  # ツイートのいいね数
    print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
    print('ツイート数 : ', num) # ツイート数
    print('='*80) # =を80個表示
    num += 1 # ツイート数を計算

