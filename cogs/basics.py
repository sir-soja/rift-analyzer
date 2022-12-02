from discord.ext import commands
from data import DataAccess
from riotService import RiotService


class Basics(commands.Cog, name="basics"):
    def __init__(self, bot):
        self.bot = bot
        self.data = DataAccess()
        self.riot = RiotService()

    @commands.command(name='link', description='Link your account.')
    async def link(self, ctx: commands.Context, *text):
        """Link a LoL account to your Discord profile."""
        # need to add some checks on lol id before posting to database
        try:
            user_id = self.riot.get_player_id_by_name(' '.join(text))
            if user_id:
                self.data.new_player(user_id, ctx.author.id, ctx.author.name)
            await ctx.send(f'{ctx.author.mention} has been added to database.')
        except Exception as e:
            print(e)
            await ctx.send('Something went wrong...')

    @commands.command(name='list', description='List all members.')
    async def list(self, ctx: commands.Context):
        """List all linked account in the server."""
        list_players = self.data.get_players()
        if list_players:
            ui = "".join([f'<@{p[1]}>\n' for p in list_players])
            await ctx.send(f'__All registered players :__ \n{ui}')
        else:
            await ctx.send('Error with the bot...')

    @commands.command(name="ping", description="Get latency of the bot.")
    async def ping(self, ctx: commands.Context):
        """Get the current latency of the bot."""
        await ctx.channel.send(f"{round(self.bot.latency * 1000, 1)}ms.")


async def setup(bot):
    await bot.add_cog(Basics(bot))
