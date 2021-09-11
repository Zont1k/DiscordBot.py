
###################
###################
###
###
###  PING COMMAND
###
###
###################
###################


import discord
from discord.ext import commands
from decouple import config
from __main__ import bot



class PingCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


@bot.command()
async def ping(ctx):
     await ctx.send(f':ping_pong: Ping! In `{round(bot.latency * 1000)}ms`')
    

def setup(client):
    client.add_cog(PingCommand(client))