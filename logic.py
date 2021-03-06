import persistence
from werkzeug import security


def get_planets(page):
    '''

    :param page: integer
    :return: list of planets
    '''
    return persistence.get_planets(page)


def register_user(username, password):
    '''

    :param username:
    :param password:
    :return:
    '''
    password = security.generate_password_hash(password)
    registration_data = [username, password]
    try:
        persistence.add_user_to_db(registration_data)
    except ValueError as err:
        raise ValueError(err)


def login(username, password):
    '''

    :param username: string
    :param password: string
    :return: True if login credentials are correct, False otherwise
    '''

    try:
        hashed_password = persistence.get_user_password_from_db(username)
    except ValueError:
        return False
    return security.check_password_hash(hashed_password, password)


def verify_session(session):
    '''

    Makes sure that session always has 'logged_in' key
    :param session: session object
    :return: void
    '''

    try:
        session['logged_in']
    except KeyError:
        session['logged_in'] = False
