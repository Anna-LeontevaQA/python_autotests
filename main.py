import requests
URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_confirmation = {
    "trainer_token" : TOKEN
}
body_create = {
    "name": "Фантик",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_update = {
    "pokemon_id": "27278",
    "name": "Бантик",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_catch = {
    "pokemon_id": "27278"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)'''

'''response_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)
print (response_update.text)'''

response_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print (response_catch.text)