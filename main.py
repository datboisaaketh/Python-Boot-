import discord 
import logging
import time
import aiohttp
import asyncio
import os
import pathlib
import sys
import traceback
from pathlib import Path
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')
@bot.event
async def on_ready():
    print("Loaded")


# DEFINITIONS OF VARIBLES
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




cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")



<<<<<<< HEAD
=======
inital_extensions = (
    'cogs.command'
)

bot.verison = 1
#_________________________________________________________#

















@bot.event
async def on_ready():
    print("Loaded")






>>>>>>> broken-stuff














<<<<<<< HEAD
bot.verison = 1
#_________________________________________________________#
# LOGGING INIT
=======
>>>>>>> broken-stuff




<<<<<<< HEAD
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#_______________________________________________________________________________________#
=======

>>>>>>> broken-stuff

"""
ERROR HANDLING
"""
async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send('This command cannot be used in private messages.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.author.send('Sorry. This command is disabled and cannot be used.')
        elif isinstance(error, commands.CommandInvokeError):
            original = error.original
            if not isinstance(original, discord.HTTPException):
                print(f'In {ctx.command.qualified_name}:', file=sys.stderr)
                traceback.print_tb(original.__traceback__)
                print(f'{original.__class__.__name__}: {original}', file=sys.stderr)
        elif isinstance(error, commands.ArgumentParsingError):
            await ctx.send(error)


<<<<<<< HEAD
"""
CLOSING 
ARGUMENTS
"""
=======
>>>>>>> broken-stuff





<<<<<<< HEAD
@bot.command()
async def close(ctx):
    await ctx.send(f"Ending Asyncio loop, bye")
    await bot.close


if __name__ == '__main__':
    for file in os.listdir(cwd+'/cogs'):
        if file.endswith(".py") and not file.startswith("security"):
            bot.load_extension(f"cogs.{file[:-3]}")

=======



for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()
>>>>>>> broken-stuff




<<<<<<< HEAD

bot.run(security.TOKEN)
=======
if __name__ == '__main__':
    for file in os.listdir(cwd+'/cogs'):
        if file.endswith(".py") and not file.startswith("security"):
            bot.load_extension(f"cogs.{file[:-3]}")

bot.run = config.TOKEN
>>>>>>> broken-stuff
