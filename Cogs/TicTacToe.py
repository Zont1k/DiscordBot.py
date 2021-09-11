
###################
###################
###
###
###  TICTACTOE COMMAND
###
###
###################
###################


import discord
from discord.ext import commands
from decouple import config
from __main__ import bot
import requests
import json
import random
from discord import Colour
from discord.embeds import Embed
from discord_components import DiscordComponents, Button, ButtonStyle
import tic_tac_toe as ttt
from __main__ import embed

class TicTacToeCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


@bot.command()
async def tic_tac_toe(ctx):
    def buttons():
       return [[Button(id = json.dumps([i,b]) ,style=(ButtonStyle.blue if field.get_map()[i][b] =='-' else (ButtonStyle.green if field.get_map()[i][b] == 'x' else ButtonStyle.red)), label=field.get_map()[i][b]) for b in range(len(field.get_map()[i]))] for i in range(3)]

    # generate game and bot 
    field = ttt.Field(clear_place_sign = '-')
    ttt_bot = ttt.Bot(field)
    if not field.is_payer_turn():
        ttt_bot.make_move()
    message = await ctx.send(embed = Embed(title = 'Game "Tic Tac Toe" (30 seconds per stroke)',color = Colour.blue()),
    components = buttons())
    try:
        while True:
            response = await bot.wait_for("button_click",timeout = 30.0)
            if response.component.label != '-':
                await response.respond(type = 4,embed = embed('Place already taken, try other one',Colour.red(),'Stroke error'))
            elif ctx.author == response.user and ctx.channel == response.channel:
                await response.respond(type = 7)
                ch = field.make_move(json.loads(response.component.id))
                if ch:
                    await message.edit(components = buttons())
                    if ch == 'draw':
                        await ctx.send(embed = embed('You play like bot',Colour.green(),'Draw'))
                        return
                    await ctx.send(embed = embed('Congratulations!!!',Colour.green(),'You won'))
                    return
                ch = ttt_bot.make_move()
                if ch:
                    await message.edit(components = buttons())
                    if ch == 'draw':
                        await ctx.send(embed = embed('You play like bot',Colour.green(),'Draw'))
                        return
                    await ctx.send(embed = embed('We are sorry',Colour.red(),'You lose'))
                    return
                await message.edit(components = buttons())   
    except:
        await ctx.send(embed = embed('Game was due your innactivity',Colour.red(),'Time over'))
    

def setup(client):
    client.add_cog(TicTacToeCommand(client))