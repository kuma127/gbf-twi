import tweepy
import pyperclip
from search_util import initalize, strip_id

def main():    
    api = initalize()
    word = ['参加者募集！ Lv200 アーカーシャ']

    for tweet in tweepy.Cursor(api.search,count=1000, q=word, tweet_mode='extend', lang='ja').items(1):
        if(tweet.source == 'グランブルー ファンタジー'):
            text = tweet.text.strip().replace('\n',' ')
            rescue_id = strip_id(text)
            # idをクリップボードにコピー
            pyperclip.copy(rescue_id)
            print(rescue_id)
            break
        else:
            print('id取得失敗')
        

if __name__ == '__main__':
    main()