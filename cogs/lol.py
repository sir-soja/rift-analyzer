from discord.ext import commands
from data import DataAccess


class Lol(commands.Cog, name="lol"):
    def __init__(self, bot):
        self.bot = bot
        self.data = DataAccess()


async def setup(bot):
    await bot.add_cog(Lol(bot))
