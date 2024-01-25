"""
Colorado test api
"""

import requests

URL = 'https://api.pokemonbattle.me:9104'
'''
HEADER_0 = {'Content-Type': 'application/json'}
BODY_0 = {
    "trainer_token": "bb18c1606980d6560759ed5b8854e2b5",
    "email": "evgeniy.lobach@gmail.com",
    "password": "Sxv20-0490645"
}
response_0 = requests.post(url=f'{URL}/trainers/reg', json=BODY_0, headers=HEADER_0, timeout=5)
print (f'Статус код: {response_0.status_code}. Сообщение: {response_0.json()["message"]}')
'''

HEADER_123 = {
    'Content-Type': 'application/json',
    "trainer_token": "bb18c1606980d6560759ed5b8854e2b5"}

BODY_1 = {
    "name": "generate",
    "photo": "generate"
}
response1 = requests.post(url=f'{URL}/pokemons',json=BODY_1, headers=HEADER_123, timeout=3)
print (response1.json())

'''
BODY_KILL = {
    "pokemon_id": "28509"
}
responseKILL = requests.post(url=f'{URL}/pokemons/knockout',json=BODY_KILL, headers=HEADER_123, timeout=3)
print (responseKILL.json())
'''

BODY_2 = {
    "pokemon_id": response1.json()['id'],
    "name": "Eroshka",
    "photo": "https://dolnikov.ru/pokemons/albums/666.png"
}
response2 = requests.put(url=f'{URL}/pokemons', json=BODY_2, headers=HEADER_123, timeout=3)
print (response2.json())

BODY_3 = {
    "pokemon_id": response1.json()['id']
}
response3 = requests.post(url=f'{URL}/trainers/add_pokeball', json=BODY_3, headers=HEADER_123, timeout=3)
print (response3.json())