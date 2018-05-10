from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_bootstrap import Bootstrap
import flask_login
import logic

app = Flask(__name__)
bootstrap = Bootstrap(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class user(flask_login.UserMixin):

    def __init__(self, user_id, password):
        self.id = user_id
        self.password = password

    def __repr__(self):
        return "%s/%s" % (self.id, self.password)

    def get_id(self):
        return self

    def is_active(self):
        # Here you should write whatever the code is
        # that checks the database if your user is active
        self.active = logic.login(self.id, self.password)
        return self.active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return logic.login(self.id, self.password)



@login_manager.user_loader
def load_user(user_id):
    return user.get_id(user_id)


@app.route('/')
def main_page(page=1):
    planets = logic.get_planets(page)
    return render_template('main.html', planets=planets, page=page, current_user=user)


@app.route('/<page>')
def next_pages(page=1):
    planets = logic.get_planets(page)
    return render_template('main.html', planets=planets, page=page, current_user=user)


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('registration_form.html', current_user=user)
    if request.method == "POST":
        login = request.form['username']
        password = request.form['pwd']
        logic.register_user(login, password)
        return redirect('/', current_user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if user.is_authenticated:
        return redirect(url_for('main_page'), current_user=user)
    if request.method == "GET":
        return render_template('login.html', current_user=user)
    if request.method == "POST":
        login = request.form['username']
        password = request.form['pwd']
        my_user = user(login,password)
        validation = logic.login(login, password)
        if validation:
            flask_login.login_user(my_user)
            flash('Logged in succesfully')
            return redirect(url_for('main_page'), current_user=user)
        return render_template('login.html')


if __name__ == '__main__':
    app.secret_key = 'fvoasdhomeisiuoahvdfljkslvgufgdskjgldfh'
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
