from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import logic

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def main_page(page=1):
    planets = logic.get_planets(page)
    return render_template('main.html', planets=planets, page=page)


@app.route('/<page>')
def next_pages(page=1):
    planets = logic.get_planets(page)
    return render_template('main.html', planets=planets, page=page)


@app.route('/registration',methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template('registration_form.html')
    if request.method == "POST":
        login = request.form['username']
        password = request.form['pwd']
        logic.register_user(login,password)
        return redirect('/')


if __name__ == '__main__':
    app.secret_key = 'fvoasdhomeisiuoahvdfljkslvgufgdskjgldfh'
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
