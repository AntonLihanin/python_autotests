import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '76dee9f36d27643f85b5e10b1e11a3d2'

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id' :1414})
    assert response.status_code == 200

def test_trainer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id': 1414})
    assert response.json()['trainer_name'] == 'Dr stange'