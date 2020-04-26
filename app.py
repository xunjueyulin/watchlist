from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return u'欢迎来到我的 Watchlist!'
