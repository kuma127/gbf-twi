import tweepy
import pyperclip
from search_util import initalize, strip_id

def main():    
    api = initalize()
    word = ['参加者募集！ Lv200 アーカーシャ']

    for tweet in tweepy.Cursor(api.search,count=1000, q=word, tweet_mode='extend', lang='ja').items(1):
        text = tweet.text.strip().replace('\n',' ')
        if(tweet.source == 'グランブルー ファンタジー'):
            # idをクリップボードにコピー
            pyperclip.copy(strip_id(text))
            print(strip_id(text))
            break
        else:
            print('id取得失敗')
        

if __name__ == '__main__':
    main()