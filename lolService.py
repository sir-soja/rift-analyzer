import os
import requests


class LolService:

    def __int__(self):
        self.path = 'https://euw1.api.riotgames.com'
        self.summoner_endpoint = 'lol/summoner/v4/summoners/by-name'
        self.api_token = os.environ["RIOT_TOKEN"]

    def get_player_by_name(self, name):
        url = self.path + self.summoner_endpoint
        req = requests.get(f'{url}{name}?api_key={self.api_token}')
        return req.json()
