import discord
from discord.ext import commands
class Commands(commands.Cog):
    """Moderation related commands."""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ping(self, ctx, message):
        await ctx.send("One Moment ...")
        await ctx.send(f"{self.bot.latency}")     
    @commands.command()
    async def clear(self, ctx,  amount=10):
        await ctx.send(f"Purging the Messages")
        await ctx.channel.purge(limit=amount)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Safety#
    
    
    
    
    
    
    
    
    
    
    
    
    
    async def on_message_delete(self, message):
        fmt = '{0.author} has deleted the message: {0.content}'
        await message.channel.send(fmt.format(message))
















    



    















def setup(bot):
    bot.add_cog(Commands(bot))