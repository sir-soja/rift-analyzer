import os

import discord


class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        print(f'{message.author} => {message.content}')


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(os.environ['DISCORD_TOKEN'])
