import json
import requests
import os

API_KEY = os.environ.get("GIFHY_KEY")

def get_pokemon(name):
    response = requests.get(f"http://pokeapi.co/api/v2/pokemon/{name}/")
    body = json.loads(response.content)
    return {
        'id': body['id'],
        'name': body["name"],
        'types': [t['type']['name'] for t in body['types']]
    }

poke = get_pokemon("pikachu")
print(poke)


def get_giphy(name):
    response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={API_KEY}&q={name}&rating=g")
    body = json.loads(response.content)
    return body['data'][0]['url']
    
poke = get_giphy("pikachu")
print(poke)