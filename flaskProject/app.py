from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/text')
def text():
    return render_template("text.html")

@app.route('/photo')
def photo():
    return render_template("photo.html")

@app.route('/voice')
def voice():
    return render_template("voice.html")

# def text_process():


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1235,debug=True)
