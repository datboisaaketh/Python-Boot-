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
        
        
        
        
    @commands.command()
    async def subaru(self, ctx):
        await ctx.send("Subaru's successful formula with the 2021 Outback station wagon has been imitated by several of its rivals"-
        ", but none of those copycats has managed to get as much traction. The slightly lifted suspension and ruggedized plastic lower body panels have both been found on other wagons, such as the now-discontinued Buick Regal TourX, and we expect Ford to try it soon on an upcoming Fusion Active. The Outback's appeal lies in its adventure-ready appearance, standard all-wheel drive, and cargo-friendly cabin. Two four-cylinder engines are offered—a nonturbo 2.5-liter and a zestier turbocharged 2.4-liter. While the Outback's handling won't thrill a driving enthusiast, its ride is smooth and quiet, and it's interior is roomy—a combination that should satisfy families and adventure seekers traveling to their next challenge.")
        
        
        
        
        
        
        
        
        
        
        
        
        #Safety#
    
    
    
    
    
    
    
    
    
    
    
    
    
    async def on_message_delete(self, message):
        fmt = '{0.author} has deleted the message: {0.content}'
        await message.channel.send(fmt.format(message))
















    



    















def setup(bot):
    bot.add_cog(Commands(bot))