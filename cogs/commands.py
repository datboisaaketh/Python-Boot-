import discord
from discord.ext import commands
class Commands(commands.Cog):
    """Moderation related commands."""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(hidden=True)
    async def ping(self, ctx, message):
        await ctx.send("One Moment ...")
        await ctx.send(f"{self.bot.latency}")     
    @commands.command()
    async def clear(self, ctx,  amount=10):
        await ctx.send(f"Purging the Messages")
        await ctx.channel.purge(limit=amount)
        
        
        
        
    @commands.command()
    async def subaru(self, ctx):
        await ctx.send("Subaru's successful formula with the 2021 Outback station wagon has been imitated by several of its rivals"
        ", but none of those copycats has managed to get as much traction. The slightly lifted suspension" 
        "and ruggedized plastic lower body panels have both been found on other wagons, such as the now-discontinued Buick Regal TourX, and we expect Ford to try it soon on an upcoming Fusion Active. The Outback's appeal lies in its adventure-ready appearance, standard all-wheel drive, and cargo-friendly cabin. Two four-cylinder engines are offered—a nonturbo 2.5-liter and a zestier turbocharged 2.4-liter. While the Outback's handling won't thrill a driving enthusiast, its ride is smooth and quiet, and it's interior is roomy—a combination that should satisfy families and adventure seekers traveling to their next challenge."
        "We think the Premium model has the best complement of standard and optional features for the price. While it's only available with the standard 182-hp four-cylinder, upgrading to the turbocharged 260-hp engine costs at least $6000. We don't think the turbo's improved acceleration and 800 pounds of extra towing capacity are worth the money. Instead, the Outback Premium comes standard with an 11.6-inch touchscreen, a 4G LTE mobile hotspot, heated front seats, a power-adjustable driver's seat, more USB ports, and options that aren't offered on the base model. Among those, we'd opt for the more affordable package that adds blind-spot monitoring, a hands-free power liftgate, and passive entry with push-button start.")
        
        
        
    @commands.command(hidden=True)
    async def debug(self, ctx):
        await ctx.send( 'log.info(Shard ID %s has connected to Gateway: %s (Session ID: %s).,Message: Shard ID %s has connected to Gateway: %s (Session ID: %s).Arguments: (None, [ gateway-prd-main-f7nd ,{ micros :129257, calls :[ discord-sessions-prd-2-110 ,{ micros :123507, calls :[ start_session ,{ micros :104832, calls :[ api-prd-main-fzw7 ,{ micros :99962, calls :[ get_user ,{ micros :3995}, add_authorized_ip ,{ micros :2959}, get_guilds ,{ micros :51933}, coros_wait ,{ micros :1}]}]}, guilds_connect ,{ micros :6, calls :[]}, presence_connect ,{ micros :5232, calls :[]}]}]}], 8eeb004b0ac6260b928bebd56ca20fdf')
            


    @subaru_error()
    async def subaru_error(self, error):

        
    
        
        
        
        
        
        
        #Safety#
    
    
    
    
    
    
    
    
    
    
    
    
    
    async def on_message_delete(self, message):
        fmt = '{0.author} has deleted the message: {0.content}'
        await message.channel.send(fmt.format(message))
















    



    















def setup(bot):
    bot.add_cog(Commands(bot))