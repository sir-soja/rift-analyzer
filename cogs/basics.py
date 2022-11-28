from discord.ext import commands


class Basics(commands.Cog, name="basics"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", description="Get latency of the bot.")
    async def ping(self, ctx: commands.Context):
        """Get the current latency of the bot."""
        await ctx.channel.send(f"{round(self.bot.latency * 1000, 1)}ms.")


async def setup(bot):
    await bot.add_cog(Basics(bot))
