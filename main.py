import discord as dis
import aiohttp
import os
import pathlib
from pathlib import Path
from discord.ext import commands
from cogs.utils import config
import traceback
import sys
import logging
from logging.handlers import RotatingFileHandler

bot = commands.Bot(command_prefix = '.')
@bot.event
async def on_ready():
    print("Loaded")


#  VARIBLES



bot_token = config.token

intents = dis.Intents.default()
intents.members = True

initial_extensions = ('cogs.commands', 'cogs.stats', 'cogs.lockdown')

bot.verison = 1
#_________________________________________________________#
#LOGGING INIT


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(m)s:%(d)s:%(Y)s:%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#________________________________________________________________________________________________#
















# ERROR HANDLING
async def on_command_error(message, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send('This command cannot be used in private messages.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.author.send('Sorry. This command is disabled and cannot be used.')
        elif isinstance(error, commands.CommandNotFound):
            await message.channel.send("Command Not Found")
            await ctx.send("If you didnt mean to type a command, Stop using fucking periods 24/7 Vinnie")
            await ctx.send("Invoke Error")
        elif isinstance(error, commands.CommandInvokeError):
            original = error.original
            if not isinstance(original, dis.HTTPException):
                print(f'In {ctx.command.qualified_name}:', file=sys.stderr)
                traceback.print_tb(original.__traceback__)
                print(f'{original.__class__.__name__}: {original}', file=sys.stderr)
        elif isinstance(error, commands.ArgumentParsingError):
            await ctx.send(error)









for extension in initial_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()


@bot.command(hidden=True)
async def reloadext(ctx,extension):
    await ctx.send("Reloading Ext....")
    bot.reload_extension(f"cogs.{extension}")
    await ctx.send("Reload")




@bot.command(hidden=True)
async def unloadext(ctx, extenstion):
    await ctx.send("Teardown init")
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send("Teardown complete")


bot.run(bot_token)
