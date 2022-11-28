import sqlite3


class DataAccess:
    def __init__(self):
        self.connector = sqlite3.connect('rift-analyzer.db')
        self.cursor = self.connector.cursor()

    def create_tables(self):
        try:
            self.cursor.execute('CREATE TABLE players(LOL_ID TEXT, DISCORD_ID);')
            self.connector.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def new_player(self, lol_id, discord_id):
        query = 'INSERT INTO players(LOL_ID, DISCORD_ID) VALUES (?,?)'
        try:
            self.cursor.execute(query, (lol_id, discord_id))
            self.connector.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_players(self):
        query = 'SELECT * FROM players'
        self.cursor.execute(query)
        return self.cursor.fetchall()
