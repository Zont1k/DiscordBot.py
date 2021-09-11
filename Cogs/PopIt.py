
###################
###################
###
###
###  POPIT COMMAND
###
###
###################
###################


import discord
from discord.ext import commands
from decouple import config
from __main__ import bot



class PopItCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


@bot.command()
async def popit(ctx):
            embed = discord.Embed(title="Mini game Pop-It 🎮", color=discord.Color.blue(), timestamp=ctx.message.created_at)

            embed.add_field(name="`Click on the squares`", value=" │||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||│\n│||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||│\n│||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||│\n│||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||│\n│||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||│\n│||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||│")

            embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

            await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(PopItCommand(client))