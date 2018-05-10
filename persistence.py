import requests
import psycopg2
import psycopg2.extras
from config import config


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
    connection = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
        connection.autocommit = True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return connection


def get_planets(page):
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
def get_user_password_from_db(cursor,username):
    username = [username]
    query = """SELECT password FROM users WHERE username = %s;"""
    cursor.execute(query, username)
    password = cursor.fetchall()[0]['password']
    return password
