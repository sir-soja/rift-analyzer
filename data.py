import sqlite3


class DataAccess:
    def __init__(self):
        self.connector = sqlite3.connect('rift-analyzer.db')
        self.cursor = self.connector.cursor()

    def create_tables(self):
        return self.cursor.execute('CREATE TABLE players(LOL_ID TEXT, DISCORD_ID);')

    def new_player(self, lol_id, discord_id):
        query = 'INSERT INTO players(LOL_ID, DISCORD_ID) VALUES (?,?)'
        return self.cursor.execute(query, (lol_id, discord_id))

    def get_players(self):
        query = 'SELECT * FROM players'
        self.cursor.execute(query)
        return self.cursor.fetchall()
