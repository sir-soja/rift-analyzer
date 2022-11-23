import os
import requests


def get_player_by_name(name):
    path = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name'
    req = requests.get(f'{path}/{name}?api_key={os.environ["RIOT_TOKEN"]}')
    return req.json()
