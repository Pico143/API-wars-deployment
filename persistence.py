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


def get_planets(page):
    if page == 1:
        return requests.get("https://swapi.co/api/planets").json()
    else:
        return requests.get("https://swapi.co/api/planets/?page={0}".format(page)).json()
