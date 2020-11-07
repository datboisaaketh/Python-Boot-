import discord
from discord.ext import commands
class Commands(commands.Cog):
    """Moderation related commands."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("One moment...")
        await ctx.send( self.bot.latency ) 

















def setup(bot):
    bot.add_cog(Commands(bot))