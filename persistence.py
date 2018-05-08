import requests
import copy

def get_planets():
    return requests.get("https://swapi.co/api/planets").json()
