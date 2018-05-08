from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def main_page():
    return render_template('main.html')

if __name__ == '__main__':
    app.secret_key = 'fvoasdhomeisiuoahvdfljkslvgufgdskjgldfh'
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )