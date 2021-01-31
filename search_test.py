import tweepy
from credentials.credentials import consumer_key, consumer_secret, access_token, access_token_secret

def initalize():
    # Twitterオブジェクトの生成--------------------------------------------
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #-------------------------------------------------------------------

    return api

def main():
    api = initalize()
    word = ['検索ワード']

    for tweet in tweepy.Cursor(api.search,count=1000, q=word, tweet_mode='extend', lang='ja').items(10):
        print(tweet.text.strip().replace('\n',' '))

if __name__ == '__main__':
    main()