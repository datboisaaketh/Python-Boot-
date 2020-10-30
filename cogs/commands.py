import discord
from discord.ext import commands
class Commands(commands.Cog):
    """Admin-only commands that make the bot dynamic."""

    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()



@bot.command(self)
async def ping(ctx):
    await ctx.send("One moment...")
    await ctx.send(f"{ctx.latency}*1000")















def setup(bot):
    bot.add_cog(Commands(bot))