import time
stat_time = time.time()
print('starting bot...')
import discord, os
from discord import Colour
from discord.embeds import Embed
from discord.ext import commands
from decouple import config
from Cybernator import Paginator
from asyncio import sleep
from discord_components import DiscordComponents, Button, ButtonStyle, Select
import sqlite3
import html
from discord_components.component import SelectOption
import requests
import json
import random
import tic_tac_toe as ttt
import chess as ch
import chess.engine as ch_eng
import psutil
import sys
from PIL import Image, ImageDraw
import io


is_windows = hasattr(sys, 'getwindowsversion')
TOKEN = config('TOKEN')
bot = commands.Bot(command_prefix="g.", case_insensitive=True, owner_ids=['564380749873152004', '676414187131371520','521291273777446922'])
bot.remove_command("help")


def embed(text,color = Colour.gold(),title ='',emoji = ''):
    if color == Colour.red():
        emoji = ":x:"
    elif color == Colour.green():
        emoji = ":white_check_mark:"
    if len(list(emoji))!=0:
        emoji +='| '
    embed = discord.Embed(description =  emoji+'**'+text+"**" , color = color, title = title)
    return embed






@bot.event
async def on_ready():
    global ch_engine
    DiscordComponents(bot)
    t = time.time()
    print('_________________________________')
    print('starting chess engine...')
    if is_windows:
        transport, ch_engine = await ch_eng.popen_uci("./Engines\chess\stockfish\stockfish.exe")
    else:
        transport, ch_engine = await ch_eng.popen_uci("./Engines/chess/stockfish/stockfish")
    print('chess engine started')
    print('time to start chess engine:',time.time()-t)
    print('_________________________________')
    print("Bot is ready!")
    print('time to start bot:',time.time()-t)
    while not bot.is_closed():
        await bot.change_presence(activity=discord.Game(name=f"{len(bot.guilds)} servers!"))
        await sleep(15)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://guffibot.xyz | g.help"))
        await sleep(15)
        print("I'm ready!")


@bot.event
async def on_command_error(ctx,error):
    f= open('errorlog.txt','a')
    print(error)
    print(ctx.message.content)
    f.write('\n\nERROR: '+str(error)+'\nMessage: '+ctx.message.content+'\n_______________')
    f.close()


@bot.command()
async def load_extension(ctx, extension):
    bot.load_extension(f'Cogs.{extension}')


@bot.command()
async def unload_extension(ctx, extension):
    bot.unload_extension(f'Cogs.{extension}')

for filename in os.listdir( os.path.abspath(os.curdir)+"//Cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

bot.run(TOKEN)

