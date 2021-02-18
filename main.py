# This is my first attempt at making a Discord Bot for cross-server communication
import discord #Discord library
from discord.ext import commands
from discord.utils import get
import asyncio
import os #One of Python's standard libries
import checks
import cog_globalchat

#Create the client object
bot = commands.Bot(command_prefix='g?')

TOKEN = "Nzg3MDc1NzQ4NTI2OTQ4Mzcy.X9PraQ.2qybqvZxxd1K-ghFuB3eCHYv42M"
#os.environ['DTOKEN2'] #This will reference the DTOKEN2 that was defined in my .bashrc

# Terminate the bot when the command g?exit is run
@bot.command(name='exit')
@checks.DiMod()
async def exit(ctx):
    await ctx.send('GlobalChat is shutting down.')
    quit()

#Add the cog_globalchat.py Cog
bot.add_cog(cog_globalchat.GlobalChat(bot))

#Begin running the bot
bot.run(TOKEN)