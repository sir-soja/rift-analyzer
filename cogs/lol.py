from discord.ext import commands
from data import DataAccess
from riotService import RiotService
import discord


class Lol(commands.Cog, name="lol"):
    def __init__(self, bot):
        self.bot = bot
        self.data = DataAccess()
        self.riot = RiotService()

    @commands.command(name='info', description='Get info on profile.')
    async def info(self, ctx: commands.Context):
        """Get ranked information on a player."""
        try:
            player_id = self.data.get_player_by_discord_id(ctx.author.id)
            if player_id:
                data = self.riot.get_player_ranked_stats_by_id(player_id)
                embed = discord.Embed(title=data[0]['summonerName'],
                                      color=0xFF5733)
                embed.add_field(name=data[0]['queueType'],
                                value=f'{data[0]["tier"]} {data[0]["rank"]} *({data[0]["wins"]}W - {data[0]["losses"]}L)*',
                                inline=False)
                embed.add_field(name=data[1]['queueType'],
                                value=f'{data[1]["tier"]} {data[1]["rank"]} *({data[1]["wins"]}W - {data[1]["losses"]}L)*',
                                inline=False)
                await ctx.send(embed=embed)
        except Exception as e:
            print(e)
            await ctx.send('Something went wrong...')


async def setup(bot):
    await bot.add_cog(Lol(bot))
