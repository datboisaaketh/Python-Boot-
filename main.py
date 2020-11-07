import discord 
import aiohttp
import os
from cogs.utils import token
import pathlib
from pathlib import Path
from discord.ext import commands
import traceback
import sys

from cogs.utils import token
import logging
from logging.handlers import RotatingFileHandler

bot = commands.Bot(command_prefix = '.')
@bot.event
async def on_ready():
    print("Loaded")


#  VARIBLES
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


bot_token = token.tooken

intents = discord.Intents.default()
intents.members = True

initial_extensions = ('cogs.commands', 'cogs.stats', 'cogs.lockdown')

bot.verison = 1
#_________________________________________________________#
#LOGGING INIT


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#________________________________________________________________________________________________#

















# ERROR HANDLING
async def on_command_error(ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send('This command cannot be used in private messages.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.author.send('Sorry. This command is disabled and cannot be used.')
        elif isinstance(error, commands.CommandInvokeError):
            original = error.original
            await ctx.send("InvokeError")
            if not isinstance(original, discord.HTTPException):
                print(f'In {ctx.command.qualified_name}:', file=sys.stderr)
                traceback.print_tb(original.__traceback__)
                print(f'{original.__class__.__name__}: {original}', file=sys.stderr)
        elif isinstance(error, commands.ArgumentParsingError):
            await ctx.send(error)
        elif isinstance(error, commands.ExtensionNotLoaded):
            await ctx.send('Cannot Reload the never loaded')










for extension in initial_extensions:
            try:

                bot.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()







@bot.command()
async def reloadext(ctx, extension):
    await ctx.send(f'Reloading {extension}')
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send("Reloaded The Extension")



bot.run(bot_token)
