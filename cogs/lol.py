from discord.ext import commands
from data import DataAccess
from riotService import RiotService
import discord


class Lol(commands.Cog, name="lol"):
    def __init__(self, bot):
        self.bot = bot
        self.data = DataAccess()
        self.riot = RiotService()

    @commands.command(name='ranks', description='Get current ranks.')
    async def ranks(self, ctx: commands.Context, user: discord.User):
        """Get ranked information on a player."""
        try:
            player = self.data.get_player_by_discord_id(user.id)
            if player[0]:
                embed = discord.Embed(title=player[1],
                                      color=0xFF5733)
                for r in self.riot.get_player_ranked_stats_by_id(player[0]):
                    embed.add_field(name=r['queueType'],
                                    value=f'{r["tier"]} {r["rank"]} '
                                          f'*({r["wins"]}W - {r["losses"]}L)*',
                                    inline=False)
                await ctx.send(embed=embed)
        except Exception as e:
            print(e)
            await ctx.send('Something went wrong...')

    @commands.command(name='mastery', description='Get all mastered champs.')
    async def mastery(self, ctx: commands.Context, mastery: int,
                      user: discord.User):
        """Get masteries of a player."""
        try:
            player = self.data.get_player_by_discord_id(user.id)
            if player[0]:
                embed = discord.Embed(title=f"{player[1]}'s champions",
                                      color=0xFF5733)
                for c in self.riot.get_champions(player[0], mastery):
                    embed.add_field(name=c['champ'],
                                    value=f'{c["level"]} *({c["points"]}pts)*')
                await ctx.send(embed=embed)
        except Exception as e:
            print(e)
            await ctx.send('Something went wrong...')


async def setup(bot):
    await bot.add_cog(Lol(bot))
