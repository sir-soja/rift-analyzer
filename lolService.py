import os
import requests


class LolService:

    def __int__(self):
        self.path = 'https://euw1.api.riotgames.com/'
        self.api_token = os.environ["RIOT_TOKEN"]

    def get_player_by_name(self, name):
        req = requests.get(f'{self.path}lol/summoner/v4/summoners/by-name/{name}?api_key={self.api_token}')
        return req.json()
