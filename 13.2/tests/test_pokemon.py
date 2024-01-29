
import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER_0 = {'Content-Type': 'application/json'}

def test_get_trainers():
    '''
    DZ-13.2.2.1 GET /trainers returns 200
    '''
    response = requests.get(url=f'{URL}/trainers', timeout=5)
    assert response.status_code == 200, '!unexpected result!'

def test_get_trainer_name_by_id():
    '''
    DZ-13.2.2.2 GET /trainers returns my_trainer_name for my_trainer_id
    '''
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':3759}, timeout=5)
    assert response.json()['trainer_name'] == 'VAMP', '!unexpected result!'