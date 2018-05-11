import persistence
import werkzeug


def get_planets(page):
    return persistence.get_planets(page)


def register_user(username, password):
    password = werkzeug.security.generate_password_hash(password)
    registration_data = [username, password]
    persistence.add_user_to_db(registration_data)

def login(username,password):
    hashed_password = persistence.get_user_password_from_db(username)
    return werkzeug.check_password_hash(hashed_password, password)

def verify_session(session):
    try:
        session['logged_in']
    except KeyError:
        session['logged_in'] = False
