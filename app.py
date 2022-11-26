import os
import logging
import discord
from bot import Client
from data import DataAccess


if __name__ == '__main__':
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

    # Assume client refers to a discord.Client subclass...
    if 'rift-analyzer.db' not in os.listdir(os.getcwd()):
        data = DataAccess()
        data.create_tables()
    intents = discord.Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    client.run(os.environ['DISCORD_TOKEN'], log_handler=handler, log_level=logging.DEBUG)
