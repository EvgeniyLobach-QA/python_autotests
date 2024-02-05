"""
Colorado test api
"""

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER_123 = {
    'Content-Type': 'application/json',
    "trainer_token": "bb18c1606980d6560759ed5b8854e2b5"}

BODY_1 = {
    "name": "generate",
    "photo": "generate"
}
response1 = requests.post(url=f'{URL}/pokemons', json=BODY_1, headers=HEADER_123, timeout=3)
print(response1.json())

BODY_2 = {
    "pokemon_id": response1.json()['id'],
    "name": "Eroshka",
    "photo": "https://dolnikov.ru/pokemons/albums/666.png"
}
response2 = requests.put(url=f'{URL}/pokemons', json=BODY_2, headers=HEADER_123, timeout=3)
print(response2.json())

BODY_3 = {
    "pokemon_id": response1.json()['id']
}
response3 = requests.post(url=f'{URL}/trainers/add_pokeball', json=BODY_3, headers=HEADER_123, timeout=3)
print(response3.json())