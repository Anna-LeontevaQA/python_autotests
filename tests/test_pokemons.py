import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 2428

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200