import discord
from discord.ext import commands
class Commands(commands.Cog):
    """Moderation related commands."""

    def __init__(self, bot):
        self.bot = bot

    def __repr__(self):
        return '<cogs.commands>'

# ERROR HANDLING
    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)
        elif isinstance(error, commands.CommandInvokeError):
            original = error.original
            if isinstance(original, discord.Forbidden):
                await ctx.send('I do not have permission to execute this action.')
            elif isinstance(original, discord.NotFound):
                await ctx.send(f'This entity does not exist: {original.text}')
            elif isinstance(original, discord.HTTPException):
                await ctx.send('Somehow, an unexpected error occurred. Try again later?')


@commands.command(self)
async def ping(ctx):
    await ctx.send("One moment...")
    await ctx.send(f"{ctx.latency}*1000")















def setup(bot):
    bot.add_cog(Commands(bot))