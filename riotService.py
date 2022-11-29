import os

from riotwatcher import LolWatcher, ApiError


class RiotService:
    def __init__(self):
        self.lol_watcher = LolWatcher(os.environ['RIOT_API_TOKEN'])

    def get_player_id_by_name(self, name):
        try:
            return self.lol_watcher.summoner.by_name('euw1', name)['id']
        except ApiError as e:
            print(e)
            return False

    def get_player_ranked_stats_by_id(self, player_id):
        try:
            return self.lol_watcher.league.by_summoner('euw1', player_id)
        except ApiError as e:
            print(e)
            return False
