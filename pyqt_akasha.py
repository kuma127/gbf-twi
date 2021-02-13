import sys
from PyQt5 import QtWidgets, Qt
import tweepy
import pyperclip
from search_util import initalize, strip_id

def get_id(label_widget):
    api = initalize()
    word = ['参加者募集！ Lv200 アーカーシャ']

    for tweet in tweepy.Cursor(api.search,count=100, q=word, tweet_mode='extend', lang='ja').items(2):
        text = tweet.text.strip().replace('\n',' ')
        if(tweet.source == 'グランブルー ファンタジー'):
            # idをクリップボードにコピー
            pyperclip.copy(strip_id(text))
            label_widget.setText('ID: {0}'.format(strip_id(text)))
            break
        else:
            label_widget.setText('ID: {0}'.format('id取得失敗'))

def main():

    # setup
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout()
    widget.setLayout(layout)

    # label
    label = QtWidgets.QLabel('Twitter救援ID取得ツール', widget)
    layout.addWidget(label)

    info = QtWidgets.QLabel('ID: ', widget)
    layout.addWidget(info)
    
    # button
    button1 = QtWidgets.QPushButton('ID取得', widget)
    button1.clicked.connect(lambda:get_id(info))
    layout.addWidget(button1)

    button2 = QtWidgets.QPushButton('Quit', widget)
    button2.clicked.connect(Qt.qApp.quit)
    layout.addWidget(button2)

    # exec
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()