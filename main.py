from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=765f2941a7e348d7974cf79bc7190d0b"
    r = requests.get(url).json() # converts to Json
    cases ={
        'articles': r['articles']
    }
    return render_template('index.html',case = cases)


if __name__ == '__main__':
    app.run(debug=True)
