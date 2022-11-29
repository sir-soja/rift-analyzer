import sqlite3


class DataAccess:
    def __init__(self):
        self.connector = sqlite3.connect('data/rift-analyzer.db')
        self.cursor = self.connector.cursor()

    def create_tables(self):
        query = """CREATE TABLE players
        (LOL_ID TEXT UNIQUE, DISCORD_ID TEXT UNIQUE);"""
        try:
            self.cursor.execute(query)
            self.connector.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def new_player(self, lol_id, discord_id):
        query = 'INSERT INTO players(LOL_ID, DISCORD_ID) VALUES (?,?)'
        self.cursor.execute(query, (lol_id, discord_id))
        self.connector.commit()

    def get_players(self):
        query = 'SELECT * FROM players'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_player_by_discord_id(self, discord_id):
        query = 'SELECT LOL_ID FROM players WHERE DISCORD_ID=?'
        try:
            self.cursor.execute(query, (discord_id,))
            return self.cursor.fetchone()[0]
        except Exception as e:
            print(e)
            return False
