###################
###################
###
###
###  CHESS COMMAND
###
###
###################
###################


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
from __main__ import bot

is_windows = hasattr(sys, 'getwindowsversion')

class ChessCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


@bot.event
async def on_ready():
    global ch_engine
    DiscordComponents(bot)
    t = time.time()
    print('_________________________________')
    print('starting chess engine...')
    if is_windows:
        transport, ch_engine = await ch_eng.popen_uci("\Engines\chess\stockfish\stockfish.exe")
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


@bot.command(pass_context= True)
async def chess(ctx):
    board = ch.Board()
    message = await ctx.send(embed = embed('Choose the difficulty of the bot'),components = [[Button(label='1',style=ButtonStyle.blue),Button(label='2',style=ButtonStyle.blue),Button(label='3',style=ButtonStyle.blue)]])
    try:
        t= time.time()+20
        while True:
            response = await bot.wait_for("button_click",timeout = t-time.time())
            if ctx.author == response.user and response.message == message :
                break
    except:
        await ctx.send(embed = embed('You have been thinking too long',Colour.red(),'Time is over'))
        return
    depth = int(response.component.label)
    await response.respond(type=7,embed = embed('Wait, the bot thinks'),components=[])
    letters = ['a','b','c','d','e','f','g','h']
                        
    emojis = {
        'B':883415614755045397,
        'b':883415614922838016,
        'K':883415619649806337,
        'k':883415619301687337,
        'N':883415619662413854,
        'n':883415619289112667,
        'P':883415619863740466,
        'p':883415619624632390,
        'Q':883415619679182898,
        'q':883415619633025104,
        'R':883415619343622176,
        'r':883415619733688320}

    def generate_buttons_moves(posible_moves,part2 = False):
        buttons = [[]]




        for i in posible_moves:
            k =str(board).replace(' ','').split('\n')
            k = (k[8-int(i[1])][letters.index(i[0])] if len(list(i)) == 2 else i[2].upper())
            if k != '.':
                buttons[-1].append(Button(id = i,label=(i if len(list(i)) == 2 else i[0:-1:1]),style=ButtonStyle.blue,emoji=bot.get_emoji(emojis[k])))
            else:
                buttons[-1].append(Button(id = i,label=(i if len(list(i)) == 2 else i[0:-1:1]),style=ButtonStyle.blue))
            if len(buttons[-1]) > 4:
                if  len(buttons) < 5:
                    buttons.append([])
                else:
                    if part2:
                        last_btn = buttons[-1][-1]
                        last_btn2 = buttons[-1][-2]
                        buttons = [[Button(id = 'back_move',style=ButtonStyle.grey,emoji= '🔙'),last_btn,last_btn2]]
                    else:
                        buttons[-1] = buttons[-1][0:-1:1]
                        buttons[-1][-1] = Button(id = 'next',style=ButtonStyle.grey,emoji= '⏩')
                        break

        if buttons[-1] == []:
            buttons = buttons[0:-1:1]
        if not part2:
            if (len(buttons) > 0 and len(buttons[-1]) > 4) or len(buttons) ==0:
                buttons.append([])
            buttons[-1].append(Button(id = 'back',style=ButtonStyle.red,emoji='🔙'))
        return buttons 

    def generate_buttons_choose_figure():
        buttons = [[]]
        str_board = str(board)
        x = 0
        y = 8
        for i in list(str_board):
            if i == ' ':
                continue

            if i == '\n':
                x = 0
                y -= 1
                continue

            if i !='.' and i.isupper():
                id = letters[x]+str(y)
                if  id in [str(i)[0:2] for i in board.legal_moves]:
                    buttons[-1].append(Button(id = id,style=ButtonStyle.blue,label=id,emoji= bot.get_emoji(emojis[i])))
                if len(buttons[-1]) > 4 :
                    buttons.append([])

            x+=1
        if len(buttons[-1]) == 0:
            buttons = buttons[0:-1:1]
        if (len(buttons) > 0 and len(buttons[-1])>4) or len(buttons) == 0:
            buttons.append([])
        buttons[-1].append(Button(id = 'exit',style=ButtonStyle.red,emoji='🚪'))
        return buttons

    async def make_img(selected_figure = '',posible_moves = []):
        path = './Pictures/chess/'
        square_size = 125 #px
        img = Image.new('RGBA', Image.open(path+'board.png').size,(0, 0, 0, 0))
        img.paste(Image.open(path+'board.png'), (0,0,img.size[0],img.size[1]))

        if selected_figure:
            y = int(selected_figure[1])-1
            x = letters.index(selected_figure[0])
            sq = Image.open(path+'blue_square.png').convert("RGBA")
            sq.putalpha(128)
            img.paste(sq,(x*square_size+5,y*square_size),sq)

        for i in posible_moves:
            y = 9-int(i[1])-1
            x = letters.index(i[0])
            sq = Image.open(path+'green_square.png').convert("RGBA")
            sq.putalpha(128)
            img.paste(sq,(x*square_size+3,y*square_size-1),sq)


        str_board =  str(board).replace(' ','').split('\n')
        for i in range(len(str_board)):
            for b in range(len(list(str_board[i]))):
                if str_board[i][b] != '.':
                    p_img = Image.open(path + (str_board[i][b] if str_board[i][b].isupper() else str_board[i][b]+'1') +'.png')
                    img.paste(p_img,(b*square_size,i*square_size),p_img)

        with io.BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            m = await bot.get_channel(883373495260708954).send(file=discord.File(fp=image_binary, filename='image.png'))
            return m.attachments[0].url
        
    
    try:
        while True:

            emb = Embed(title = 'Chess (2 minutes per move)',description = 'Select the figure you want to move')
            emb.set_image(url = await make_img())
            await message.edit(embed = emb,components = generate_buttons_choose_figure())

            t = int(time.time()+100)
            while True:
                try:
                    response = await bot.wait_for("button_click",timeout = t-time.time())
                except:
                    t = time.time()+20
                    await ctx.send(embed = embed('20 seconds left to move',Colour.gold(),'Attention!!!',':exclamation:'))
                    response = await bot.wait_for("button_click",timeout = t - time.time())

                if ctx.author == response.user and response.message == message :
                    if response.component.id == 'exit':
                        await response.respond(type=7,embed = embed('Game ended prematurely'),components=[])
                        return

                    await response.respond(type=7,embed = embed('Wait, the bot thinks'),components=[])
                    break

            #get posible moves
            from_where = response.component.id
            posible_moves = [str(i)[2::] for i in board.legal_moves if str(i).startswith(from_where)]
            emb.description = 'Choose where you want to go'
            emb.set_image(url = await make_img(response.component.id[0]+str(9-int(response.component.id[1])),posible_moves))
            await message.edit(embed = emb,components = generate_buttons_moves(posible_moves))
            
            t = int(time.time()+100)
            while True:
                try:
                    response = await bot.wait_for("button_click",timeout = t-time.time())
                except:
                    t = time.time()+20
                    await ctx.send(embed = embed('20 seconds left to move',Colour.gold(),'Attention!!!',':exclamation:'))
                    response = await bot.wait_for("button_click",timeout = t - time.time())

                if ctx.author == response.user and response.message == message :
                    if response.component.id == 'next':
                        t = int(time.time()+120)
                        await response.respond(type=7,components = generate_buttons_moves(posible_moves,True))
                    elif response.component.id == 'back_move':
                        t = int(time.time()+120)
                        await response.respond(type=7,components = generate_buttons_moves(posible_moves))
                    else:
                        break
            
            await response.respond(type=7,embed = embed('Wait, the bot thinks'),components=[])
            if response.component.id == 'back':
                continue
            
            

            #make move
            
            board.push(ch.Move.from_uci(from_where[0]+from_where[1]+response.component.id))
            if  board.is_game_over():
                break
            result = await ch_engine.play(board, ch.engine.Limit(depth = depth))
            board.push(result.move)
            if  board.is_game_over():
                break
        
        if board.outcome().termination._value_ == 3: #draw
            emb = embed(title = 'Draw',text = 'Not good, not bad!!!',color=Colour.gold(),emoji = ':woozy_face: ')
        elif board.outcome().termination._value_ == 2: #black
            emb = embed(title = 'Lose',text= 'Next time you will be more lucky',color=Colour.red())
        elif board.outcome().termination._value_ == 1: #white
            emb = embed(title = 'Win',text = 'You are the best',color=Colour.green())
        emb.set_image(url = await make_img())
        await message.edit(embed = emb,components = [])
    except:
        await ctx.send(embed = embed('You have been thinking too long',Colour.red(),'Time is over'))
        return



def embed(text,color = Colour.gold(),title ='',emoji = ''):
        if color == Colour.red():
            emoji = ":x:"
        elif color == Colour.green():
            emoji = ":white_check_mark:"
        if len(list(emoji))!=0:
            emoji +='| '
        embed = discord.Embed(description =  emoji+'**'+text+"**" , color = color, title = title)
        return embed


    

def setup(client):
    client.add_cog(ChessCommand(client))