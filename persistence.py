import requests
import copy

def get_planets(page):
    if page == 1:
        return requests.get("https://swapi.co/api/planets").json()
    else:
        return requests.get("https://swapi.co/api/planets/?page={0}".format(page)).json()
