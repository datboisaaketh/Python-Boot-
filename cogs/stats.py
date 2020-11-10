import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
import main 
import random


bot = discord.Client()

bot.colors = {
        'WHITE': 0xFFFFFF,
        'AQUA': 0x1ABC9C,
        'GREEN': 0x2ECC71,
        'BLUE': 0x3498DB,
        'PURPLE': 0x9B59B6,
        'LUMINOUS_VIVID_PINK': 0xE91E63,
        'GOLD': 0xF1C40F,
        'ORANGE': 0xE67E22,
        'RED': 0xE74C3C,
        'NAVY': 0x34495E,
        'DARK_AQUA': 0x11806A,
        'DARK_GREEN': 0x1F8B4C,
        'DARK_BLUE': 0x206694,
        'DARK_PURPLE': 0x71368A,
        'DARK_VIVID_PINK': 0xAD1457,
        'DARK_GOLD': 0xC27C0E,
        'DARK_ORANGE': 0xA84300,
        'DARK_RED': 0x992D22,
       'DARK_NAVY': 0x2C3E50
    }
bot.color_list = [c for c in bot.colors.values()]









class Stats(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Stats Loaded")

    @commands.command(aliases=['cs'])
    async def channelstats(self, ctx):
        channel = ctx.channel
        embed = discord.Embed(title=f"Stats for **{channel.name}**", description=f"{'Category: {}'.format(channel.category.name) if channel.category else 'This channel is not in a category'}", color=random.choice(bot.colors))
        embed.add_field(name="Channel Guild", value=ctx.guild.name, inline=False)
        embed.add_field(name="Channel Id", value=channel.id, inline=False)
        embed.add_field(name="Channel Topic", value=f"{channel.topic if channel.topic else 'No topic.'}", inline=False)
        embed.add_field(name="Channel Position", value=channel.position, inline=False)
        embed.add_field(name="Channel Slowmode Delay", value=channel.slowmode_delay, inline=False)
        embed.add_field(name="Channel is nsfw?", value=channel.is_nsfw(), inline=False)
        embed.add_field(name="Channel is news?", value=channel.is_news(), inline=False)
        embed.add_field(name="Channel Creation Time", value=channel.created_at, inline=False)
        embed.add_field(name="Channel Permissions Synced", value=channel.permissions_synced, inline=False)
        embed.add_field(name="Channel Hash", value=hash(channel), inline=False)

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Stats(bot))