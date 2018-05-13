import requests
import psycopg2
import psycopg2.extras
import urllib
import os   


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value

    return wrapper


def open_database():
    urllib.parse.uses_netloc.append('postgres')
    url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
    connection = None
    try:
        connection = psycopg2.connect(database=url.path[1:],
                                      user=url.username,
                                      password=url.password,
                                      host=url.hostname,
                                      port=url.port)
        connection.autocommit = True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return connection


def get_planets(page):
    '''

    :param page: integer with page number
    :return:
    '''
    if page == 1:
        return requests.get("https://swapi.co/api/planets").json()
    else:
        return requests.get("https://swapi.co/api/planets/?page={0}".format(page)).json()


@connection_handler
def add_user_to_db(cursor, registration_data):
    ''' Adds user to database
    Args:
    Registration_data - array with two strings (username and password)
    '''
    query = """INSERT INTO users (username, password) VALUES (%s, %s);"""
    cursor.execute(query, registration_data)


@connection_handler
def get_user_password_from_db(cursor, username):
    '''

    :param cursor: RealDictCursor from connection handler
    :param username: string
    :return: hashed password

    If user does not exist, raises ValueError
    '''
    username = [username]
    query = """SELECT password FROM users WHERE username = %s;"""
    cursor.execute(query, username)
    try:
        password = cursor.fetchall()[0]['password']
    except IndexError:
        raise ValueError("No such user in database")
    return password
