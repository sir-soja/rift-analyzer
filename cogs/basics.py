from discord.ext import commands
from data import DataAccess


class Basics(commands.Cog, name="basics"):
    def __init__(self, bot):
        self.bot = bot
        self.data = DataAccess()

    @commands.command(name='link', description='Link your account.')
    async def link(self, ctx: commands.Context, *text):
        """Link a LoL account to your Discord profile."""
        # need to add some checks on lol id before posting to database
        try:
            self.data.new_player(' '.join(text), ctx.author.id)
            await ctx.send('added to database')
        except Exception as e:
            print(e)
            await ctx.send('Error with the bot')

    @commands.command(name='list', description='List all members.')
    async def list(self, ctx: commands.Context):
        """List all linked account in the server."""
        list_players = self.data.get_players()
        if list_players:
            ui = "".join([f'<@{p[1]}> - {p[0]}\n' for p in list_players])
            await ctx.send(ui)
        else:
            await ctx.send('Error with the bot...')

    @commands.command(name="ping", description="Get latency of the bot.")
    async def ping(self, ctx: commands.Context):
        """Get the current latency of the bot."""
        await ctx.channel.send(f"{round(self.bot.latency * 1000, 1)}ms.")


async def setup(bot):
    await bot.add_cog(Basics(bot))
