import asyncio
import os
import discord
import random
import platform
from data import DataAccess
from discord.ext import commands, tasks
from discord.ext.commands import Context

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)


@tasks.loop(minutes=1.0)
async def status_task() -> None:
    """Change game status task of the bot"""
    statuses = ["Flexing with the gang", "Inting in soloQ", "Chilling in Aram"]
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))


@bot.event
async def on_command_completion(ctx: Context) -> None:
    """Prints every command that performs successfully"""
    cmd = str(ctx.command.qualified_name.split(" ")[0])
    print(f"{cmd} - {ctx.author}")


async def setup_database():
    if 'rift-analyzer.db' not in os.listdir(os.getcwd()):
        data = DataAccess()
        data.create_tables()


@bot.event
async def on_ready() -> None:
    """The code in this even is executed when the bot is ready"""
    print(f"Logged in as {bot.user.name}")
    print(f"discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    status_task.start()


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


if __name__ == '__main__':
    asyncio.run(setup_database())
    asyncio.run(load_cogs())
    bot.run(os.environ['DISCORD_TOKEN'])
