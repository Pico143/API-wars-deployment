from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
import logic

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def main_page(page=1):
    logic.verify_session(session)
    planets = logic.get_planets(page)
    return render_template('main.html', planets=planets, page=page)


@app.route('/<page>')
def next_pages(page=1):
    logic.verify_session(session)
    planets = logic.get_planets(page)
    return render_template('main.html', planets=planets, page=page)


@app.route('/registration', methods=['GET', 'POST'])
def register():
    logic.verify_session(session)
    if session['logged_in'  ] == True:
        return redirect(url_for('main_page'))
    if request.method == "GET":
        return render_template('registration_form.html')
    if request.method == "POST":
        login = request.form['username']
        password = request.form['pwd']
        logic.register_user(login, password)
        return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    logic.verify_session(session)
    if session['logged_in'] == True:
        return redirect(url_for('main_page'))
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        login = request.form['username']
        password = request.form['pwd']
        validation = logic.login(login, password)
        if validation:
            session['logged_in'] = True
            session['username'] = login
            flash('Logged in succesfully')
            return redirect(url_for('main_page'))
        flash("Wrong login credentials provided.")
        return render_template('login.html')


@app.route("/logout")
def logout():
    logic.verify_session(session)
    session.clear()
    session['logged_in'] = False
    return redirect('/')


if __name__ == '__main__':
    app.secret_key = 'fvoasdhomeisiuoahvdfljkslvgufgdskjgldfh'
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
