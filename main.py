from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Esi sveiks!"

@app.route('/kontakti')
def kontakti():
    return "Šeit mani kontakti"


if __name__ == '_main_':
    app.run(debug = True)