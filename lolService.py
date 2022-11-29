import os
import requests


class LolService:

    def __init__(self):
        self.path = 'https://euw1.api.riotgames.com/'
        self.summoner_endpoint = 'lol/summoner/v4/summoners/by-name'
        self.api_token = "RGAPI-766174a9-f467-43c7-8469-01c424b60f15"

    def get_player_by_name(self, name):
        url = self.path + self.summoner_endpoint
        req = requests.get(f'{url}/{name}?api_key={self.api_token}')
        if req.status_code == 404:
            return False
        return req.json()


