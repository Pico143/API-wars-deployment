import persistence
import werkzeug


def get_planets(page):
    return persistence.get_planets(page)


def register_user(username, password):
    password = werkzeug.security.generate_password_hash(password)
    registration_data = [username, password]
    persistence.add_user_to_db(registration_data)
