name = 'Xunjueyulin'
movies = [
        {'title':'My Neighbor Totoro','year': '1988'},
        {'title':'Destiny:Kamakura Monogatari','year':'2017'},
        {'title':'Thor:The Dark World','year':'2013'},
        {'title':'Avengers:Age of Ultron','year':'2013'},
        {'title':'Iron Man 2','year':'2010'},
        {'title':'Captain America:Civil War','year':'2016'},
        {'title':'Yip Man 4:The Finale','year':'2019'},
        {'title':'Avengers:Endgame','year':'2019'},
        {'title':'Aquaman','year':'2019'},
        ]

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8090)
