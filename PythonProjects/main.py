import requests

token = '76dee9f36d27643f85b5e10b1e11a3d2'
host = 'https://api.pokemonbattle.me:9104' # хост для покемонов

'''response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json={
    "name":"varvar",
    "photo": "https://dolnikov.ru/pokemons/albums/1008.png"
}, headers={'Content-Type' :'application/json' , 'trainer_token' : token})

print(response.text)'''


'''response_name = requests.put(f'{host}/pokemons', json={
    "pokemon_id": "5912",
    "name": "викинг",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"

}, headers={'Content-Type' :'application/json' , 'trainer_token' : token})

print(response_name.text)'''


response_pokeball = requests.post(f'{host}/trainers/add_pokeball', json={
    "pokemon_id": "5912",

}, headers={'Content-Type' :'application/json' , 'trainer_token' : token})

print(response_pokeball.text)