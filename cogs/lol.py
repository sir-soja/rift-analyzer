from discord.ext import commands
from data import DataAccess


class Lol(commands.Cog, name="lol"):
    def __init__(self, bot):
        self.bot = bot
        self.data = DataAccess()

    @commands.command(name="link", description="Link your account")
    async def link(self, ctx: commands.Context, *text):
        # need to add some checks on lol id before posting to database
        print(self.data.new_player(" ".join(text), ctx.author.id))
        await ctx.send('added to database')


async def setup(bot):
    await bot.add_cog(Lol(bot))
