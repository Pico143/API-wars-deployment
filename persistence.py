import requests
import copy

def get_planets():
    data = requests.get("https://swapi.co/api/planets").json()
    page = copy.deepcopy(data)
    while page['next'] != None:
        page = requests.get(page['next']).json()
        data['results'].extend(page['results'])
    return data
