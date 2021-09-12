import time
import discord
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
from PIL import Image, ImageDraw,ImageFont
import io
from __main__ import bot,embed


import Engines._2048 as _2048_engine

class ChessCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

@bot.command()
async def _2048(ctx):
    buttons = [[Button(style=ButtonStyle.grey,disabled=True,label='.'),Button(style=ButtonStyle.blue,id = 'up',emoji='⬆️'),Button(style=ButtonStyle.grey,disabled=True,label='.')],
                [Button(style=ButtonStyle.blue,id = 'left',emoji='⬅️'),Button(style=ButtonStyle.blue,id = 'down',emoji='⬇️'),Button(style=ButtonStyle.blue,id = 'right',emoji='➡️')],
                [Button(id = 'exit',style=ButtonStyle.red,emoji='🚪')]]
    async def make_img():
        sector_size = int(512/game.size)
        img = Image.new('RGB', (sector_size*game.size,sector_size*game.size), color = 'black')
        img1 = ImageDraw.Draw(img) 
        for y in range(len(game.get_map())):
            for x in range(len(game.get_map()[y])):
                shape = [(int((sector_size)*x), int((sector_size)*y)), (int((sector_size)*(x+1)), int((sector_size)*(y+1)))]
                
                n = 2
                b = 0
                if game.get_map()[y][x]:   
                    while n < game.get_map()[y][x]:
                        n = n ** 2
                        b+=1

                color = colors[b+1 if game.get_map()[y][x] else 0]
                img1.rectangle(shape, fill =(color%256,color%512,color%768), outline ="white")
                if game.get_map()[y][x]:
                    s = str(game.get_map()[y][x])
                    s1 = s[:len(s)//2]
                    s2 = s[len(s)//2:]

                    st_s = 96
                    while True:
                        font = ImageFont.truetype("./data/fonts/arial.ttf", st_s)
                        w, h = img1.textsize(str(game.get_map()[y][x]),font=font)
                        if h>sector_size/1.2 or (w > sector_size and  sector_size/2 < h and w > sector_size):
                            st_s = int(st_s/2)
                        elif sector_size/2 > h:
                            img1.text((int((sector_size)*x), int((sector_size)*y)), s1, fill=(256-(color%256),256-(color%512),256-(color%768)),font=font)
                            img1.text((int((sector_size)*x), int((sector_size)*y+(sector_size-h)/2)+int(h/4)), s2, fill=(256-(color%256),256-(color%512),256-(color%768)),font=font)
                            break
                        else:
                            img1.text((int((sector_size)*x+(sector_size-w)/2), int((sector_size)*y+(sector_size-h)/2)), str(game.get_map()[y][x]), fill=(256-(color%256),256-(color%512),256-(color%768)),font=font)
                            break
        
        with io.BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            m = await bot.get_channel(883373495260708954).send(file=discord.File(fp=image_binary, filename='image.png'))
            return m.attachments[0].url
        


    message = await ctx.send(embed = embed('Выберите размер поля'),components = [[Button(label='4X4',style=ButtonStyle.blue,id ='4'),Button(label='9X9',style=ButtonStyle.blue,id = '9'),Button(label='12x12',style=ButtonStyle.blue,id ='12'),]])
    try:
        t= time.time()+20
        while True:
            response = await bot.wait_for("button_click",timeout = t-time.time())
            if ctx.author == response.user and response.message == message :
                break
    except:
        await ctx.send(embed = embed('Вы думали слишком долго',Colour.red(),'Время вышло'))
        return

    await response.respond(type=7,embed = embed('подождите, бот думает'),components=[])
    game = _2048_engine.Field(int(response.component.id))
    # generate colors
    amount_values = ((game.size +1)*2+1)
    colors = []
    for i in range(amount_values):
        colors.append(int(768/amount_values*i))
    emb = Embed(title = 'Игра 2048 (30 сек на ход)',description = 'Вам надо набрать: '+str(game.need)+' на одной клетке чтобы победить')

    while True:
        emb.set_image(url = await make_img())
        await message.edit(embed = emb,components = buttons)
        try:
            t= time.time()+30
            while True:
                response = await bot.wait_for("button_click",timeout = t-time.time())
                if ctx.author == response.user and response.message == message :
                    break
        except:
            await ctx.send(embed = embed('Вы думали слишком долго',Colour.red(),'Время вышло'))
            return 
        if response.component.id == 'exit':
             await response.respond(type=7,embed = embed('Игра закрыта преждевременно'),components=[])
             return
        res = game.move(response.component.id)
        await response.respond(type=7,embed = embed('подождите, бот думает'),components=[])
        
        if res:
            emb.set_image(url = await make_img())
            if res == 'lose':
                emb.title = 'Вы проиграли'
                emb.description = "В следующий раз вам возможно повезет" 
            else:
                emb.title = 'Вы выиграли'
                emb.description = "Вам просто повезло" 
            
            await message.edit(embed = emb,components = [])
            return


def setup(client):
    client.add_cog(ChessCommand(client))