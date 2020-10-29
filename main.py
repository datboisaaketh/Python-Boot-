import discord 
import security
import os
import pathlib
from pathlib import Path
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')



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





bot.verison = 1
#_________________________________________________________#

















@bot.event
async def on_ready():
    print("Loaded")


















if __name__ == '__main__':
    for file in os.listdir(cwd+'/cogs'):
        if file.endswith(".py") and not file.startswith("security"):
            bot.load_extension(f"cogs.{file[:-3]}")

bot.run = security.TOKEN