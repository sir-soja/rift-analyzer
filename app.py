import asyncio
import os
import discord
from data import DataAccess
from discord.ext import commands
from discord.ext.commands import Context

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)


@bot.event
async def on_command_completion(ctx: Context) -> None:
    """Prints every command that performs successfully"""
    cmd = str(ctx.command.qualified_name.split(" ")[0])
    print(f"{cmd} : {ctx.guild.name} <- {ctx.author}")


async def setup_database():
    if 'rift-analyzer.db' not in os.listdir(os.getcwd()):
        data = DataAccess()
        data.create_tables()


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


if __name__ == '__main__':
    asyncio.run(setup_database())
    asyncio.run(load_cogs())
    bot.run(os.environ['DISCORD_TOKEN'])
