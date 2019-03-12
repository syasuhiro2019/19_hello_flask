import random

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<html>Hi, Hachimantai!</html>'


@app.route('/hachimantai')
def hello_hachimantai():
    return '<html>スパルタキャンプ in 八幡平</html>'


"""
http://127.0.0.1:5000/goodbye というURLを入力したら｢Good Bye!｣と表示されるようにしてください
"""


@app.route('/goodbye')
def goodbye():
    return '<html>Good Bye!</html>'


@app.route('/omikuji')
def omikuji():
    omikuji_list = ['大吉', '吉', '凶', '大凶', '中吉']
    return f'あなたの今日の運勢は...{random.choice(omikuji_list)}です'


@app.route('/user/<username>')
def greet(username):
    return f'Hi {username}'


if __name__ == "__main__":
    app.run(debug=True)
