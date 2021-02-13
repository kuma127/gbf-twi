import tweepy
import sys
from search_util import initalize

def main():
    args = sys.argv

    if len(args) != 3:
        print('引数エラー')
        return
    
    api = initalize()
    word = ['参加者募集！ Lv{0} {1}'.format(args[1], args[2])]

    for tweet in tweepy.Cursor(api.search,count=1000, q=word, tweet_mode='extend', lang='ja').items(5):

        created_at = tweet.created_at
        text = tweet.text.strip().replace('\n',' ')
        
        if(tweet.source == 'グランブルー ファンタジー'):
            print(created_at)
            print(text)
        else:
            print('GBF以外からのツイート')

if __name__ == '__main__':
    main()