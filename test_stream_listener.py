import tweepy
import pyperclip
from search_util import initalize, strip_id
from target_list import target_list

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if(status.source == 'グランブルー ファンタジー'):
            text = status.text.strip().replace('\n',' ')
            rescue_id = strip_id(text)
            pyperclip.copy(rescue_id)
            print(f'ID: {rescue_id}')
        else:
            print('ID: id取得失敗')
    
    def on_error(self, status_code):
        if status_code == 420:
            return False

api = initalize()
word_string = f'参加者募集！ {target_list[0]}'
word = [word_string]

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=word)