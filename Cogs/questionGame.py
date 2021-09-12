###################
###################
###
###
###  QUESTION COMMAND
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
import html

class QuestCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


@bot.command(pass_context= True)
async def question(ctx):
    question = json.loads(requests.get('https://opentdb.com/api.php?amount=1').text)['results']
    if len(question) == 0:
        question = json.loads(requests.get('https://opentdb.com/api.php?amount=1').text)['results']
        if len(question) == 0 :
            await ctx.send(embed=embed('Error to get a question for you',Colour.red()))
            return
    question = question[0]
    question['question'] = html.unescape(question['question'])
    question['correct_answer'] = html.unescape(question['correct_answer'])
    posible_answers = question['incorrect_answers']
    for i in range(len(posible_answers)):
        posible_answers[i] = html.unescape(posible_answers[i])

    posible_answers.append(question['correct_answer'])
    random.shuffle(posible_answers)

    await ctx.send(embed = Embed(title = 'QUIZ (you have 10 seconds for answer)',description = question['question'],color = Colour.blue()
    ),components = [Button(style=ButtonStyle.blue, label=i, id = str(ctx.author.id)+i) for i in posible_answers])

    try:
        while True:
            response = await bot.wait_for("button_click",timeout=10.0)
            if ctx.author == response.user and ctx.channel == response.channel and response.component.label in posible_answers and str(ctx.author.id) in response.component.id : 
                break
    except:
        await ctx.send(embed = embed('Correct answer was: '+question['correct_answer'],Colour.red(),'TIME OUT'))
        return

    if response.user == ctx.author:
        if response.component.label == question['correct_answer']:
            await response.respond(type = 5)
            await ctx.send(embed = embed('The answer was: '+question['correct_answer'],Colour.green(),'Correct!'))
        else:
            await response.respond(type = 5)
            await ctx.send(embed = embed('The answer was: '+question['correct_answer'],Colour.red(),'Incorrect!'))

    

def setup(client):
    client.add_cog(QuestCommand(client))