import sys
from PyQt5 import QtWidgets, Qt
import tweepy
import pyperclip
from search_util import initalize, strip_id

target_list = [
    'Lv200 ジ・オーダー・グランデ',
    'Lv200 アーカーシャ',
    'Lv150 プロトバハムート',
    '四大天司ＨＬ',
    'Lv200 ワムデュス',
    'Lv200 イーウィヤ',
    'Lv150 シュヴァリエ・マリス',
    'Lv200 ガレヲン',
    'Lv200 ルオー'
]

class MainLayout(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # setup
        super().__init__(parent=parent)
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # label
        label = QtWidgets.QLabel('Twitter救援ID取得ツール', self)
        layout.addWidget(label)

        self.info = QtWidgets.QLabel('ID: ', self)
        layout.addWidget(self.info)

        # combo
        self.combo = QtWidgets.QComboBox()
        self.combo.addItems(target_list)
        layout.addWidget(self.combo)
        
        # button
        # ID取得実行ボタン
        button1 = QtWidgets.QPushButton('ID取得', self)
        button1.clicked.connect(self.get_id)
        layout.addWidget(button1)

        # 終了ボタン
        button2 = QtWidgets.QPushButton('Quit', self)
        button2.clicked.connect(Qt.qApp.quit)
        layout.addWidget(button2)
    
    def get_id(self):
        api = initalize()
        word_string = '参加者募集！ ' + self.combo.currentText()
        word = [word_string]

        for tweet in tweepy.Cursor(api.search,count=100, q=word, tweet_mode='extend', lang='ja').items(2):
            if(tweet.source == 'グランブルー ファンタジー'):
                text = tweet.text.strip().replace('\n',' ')
                rescue_id = strip_id(text)
                # idをクリップボードにコピー
                pyperclip.copy(rescue_id)
                self.info.setText('ID: {0}'.format(rescue_id))
                break
            else:
                self.info.setText('ID: {0}'.format('id取得失敗'))


def main():

    # setup
    app = QtWidgets.QApplication(sys.argv)
    widget = MainLayout()

    # exec
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()