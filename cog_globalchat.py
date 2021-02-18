import discord
from discord.ext import commands
import asyncio
import shelve
import checks
import re
import typing
import itertools

class GlobalChat(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.GlobalChannels = shelve.open('GLOBALCHANNELS', writeback=True)
        try:
            self.GlobalChannels['SERVERS']
        except:
            self.GlobalChannels['SERVERS']= {}

    @commands.command(name='setup')
    @commands.has_permissions(administrator=True)
    async def setup(self, ctx, channel: typing.Optional[discord.TextChannel], *, note="Blank"):
        if channel == None:
            channel = ctx.channel
        self.GlobalChannels["SERVERS"][ctx.guild.id] = (channel, note)
        await ctx.send(f'The {channel.mention} channel in __**{ctx.guild.name}**__ has been added to our Global Chat.')

    @commands.command(name='globallist', aliases=['list'])
    async def globallist(self, ctx):
        #Sort all Guilds and Channels in the dictionary, produce a generator which will create (guild,channel) sorted by guild
        items = self.GlobalChannels['SERVERS'].items()
        temp = ((self.bot.get_guild(item[0]).name, item[1]) for item in items)
        sortedlist = sorted(temp)
        stringlist = ""
        for servername, (channel, note) in sortedlist:
            stringlist += f'{servername} - {channel.mention}\n'
        #Create the embed
        embed = discord.Embed(
            title=f'Our Global Channels',
            description=stringlist,
            color=discord.Color(16711680)
        )
        await ctx.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 787075748526948372: #As of 01/19/2021, GlobalChat Bot ID is 787075748526948372
            return
        elif:
            embed = discord.Embed(
                title=f'JLW#1111 (theo)',
                description=#message
                embed.set_footer(text="from: It's time with Tim")
            )
            await ctx.send(embed=embed)