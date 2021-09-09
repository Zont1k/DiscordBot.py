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
import sys
from PIL import Image, ImageDraw
import io

is_windows = hasattr(sys, 'getwindowsversion')
TOKEN = config('TOKEN')
bot = commands.Bot(command_prefix="c.", case_insensitive=True, owner_ids=['564380749873152004', '676414187131371520','521291273777446922'])
bot.remove_command("help")


#@bot.group(invoke_without_command=True)
#async def help(ctx):
    #await ctx.send()
    
    #em = discord.Embed(title = "Help menu", color=discord.Color.blue())
    
    #em.add_field(name = " **To navigate the pages, use**", value = " **buttons below. If for some reason they are not on your device\n are displayed, please update / reinstall the Discord app.**", inline=True)
    
    #em.set_thumbnail(url="https://cdn.discordapp.com/attachments/851162534483722301/873200179489148979/avatar-cara-monstruo-dibujos-animados-monstruo-halloween_6996-1122.jpg")

    #await ctx.send(embed = em)

@bot.command()
async def select(self, ctx):
    await ctx.send("Hello test test test",
    components=
    [Select(placeholder="Choose what you want to see!",
                        options=[
                            SelectOption(
                                label="Option 1",
                                value="option1",
                                description="See option 1",
                                emoji="😀"
                            ),
                            SelectOption(
                                label="Option 2",
                                value="option2",
                                description="See option 2",
                                emoji="😀"
                            ),
                            SelectOption(
                                label="Option 3",
                                value="option3",
                                description="See option 3",
                                emoji="😀"
                            ),
                        ])]
                        )





@bot.command()
async def ping(ctx):
     await ctx.send(f':ping_pong: Ping! In `{round(bot.latency * 1000)}ms`')

@bot.command()
async def help(ctx):
    await ctx.send(
    embed=discord.Embed(title="Help menu", description="To navigate the pages, use\n buttons below. If for some reason they are not on your device\n are displayed, please update / reinstall the Discord app.", color=discord.Color.blue(), timestamp=ctx.message.created_at),
    components=[
            Button(style=ButtonStyle.blue, label="Information", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Command", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Game", emoji="▶️"),
        ]
    )
    await ctx.send('❓ Do you have any questions related to the bot? Go to the support server.'),
    await ctx.send(f'https://discord.gg/wgYFxEHr5q'),
    response = await bot.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == "Information":
            await response.respond(
            embed = discord.Embed(title="⚙️ Guffi", description=" **Guffi** - is a multifunctional Discord bot built with\n aim to combine the functionality of many bots into one. The bot has many\n useful features that are suitable for almost any server:\n ranging from moderation to interesting economics. Besides\n the project is actively updated, and every week the bot is filled with new ones\n functions.  \n **Key Resources**\n  1) **[Invite](https://discordapp.com/oauth2/authorize?&client_id=838125539847700520&scope=bot&permissions=8)**\n 2) **[Support server](https://discord.gg/wgYFxEHr5q)**\n 3) **[Documentation](https://app.gitbook.com/@guffi/s/guffi/)**  \n **Developers**\n *`AalbatrossGuy#2021`*\n *`AlxelZot#1111`*\n *`ilesik#6666`*", color=discord.Color.blue(), timestamp=ctx.message.created_at),
            components=[
            Button(style=ButtonStyle.blue, label="Command", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Game", emoji="▶️"),
                ]    
            )
    response = await bot.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == "Command":
            await response.respond(
            embed = discord.Embed(title="≫ Command list ≪", description="**General » g.help General**\n `g.info` - bot information\n `g.invite` - useful links\n `g.ping` - ping\n `g.support` - support server link\n **Moderation » g.help Moderation**\n `g.ban` - user ban[g.ban <user>]\n `g.clear` - clearing chat\n `g.mute` - mute user[g.mute <user> (time)]\n `g.kick` - kick user[g.kick <user>]\n `g.warn` - issue user warning\n `g.add-role` - add roles[g. add_role <user> (role/s)]", color=discord.Color.blue(), timestamp=ctx.message.created_at),
            components=[
            Button(style=ButtonStyle.blue, label="Information", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Game", emoji="▶️"),
                ]     
            )
    response = await bot.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == "Game":
            await response.respond(
            embed = discord.Embed(title="Game", description="**`g.popit`** - PoP-It\n**`g.tic_tac_toe`** - Tic Tac Toe game with a bot\n**`g.question`** - you have to answer the questions", color=discord.Color.blue(), timestamp=ctx.message.created_at),
            components=[
            Button(style=ButtonStyle.blue, label="Information", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Command", emoji="▶️"),
                ]    
            ) 

        




@bot.event
async def on_ready():
    global ch_engine
    DiscordComponents(bot)
    t = time.time()
    print('_________________________________')
    print('starting chess engine...')
    if is_windows:
        transport, ch_engine = await ch_eng.popen_uci("./Engines/chess/stockfish/stockfish.exe")
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



@bot.command()
async def server(ctx):

    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
        
    embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.blue())
    embed.add_field(name='Information about - 'f" {ctx.guild.name}", value=f"{ctx.guild.name}", inline=False)
    embed.add_field(name='Owner', value=ctx.guild.owner, inline=False)
    embed.add_field(name='Highest role', value=ctx.guild.roles[-2], inline=False)
    embed.add_field(name='Contributers:', value=f"{ctx.guild.owner}",inline=False)
    embed.add_field(name='Number of roles', value=str(role_count), inline=False)
    embed.add_field(name='Number Of Members', value=ctx.guild.member_count, inline=False)
    embed.add_field(name='Bots:', value=(', '.join(list_of_bots)))
    embed.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
    embed.set_image(url=ctx.guild.icon_url)
    embed.set_footer(text=ctx.bot.user.name, icon_url=ctx.bot.user.avatar_url)
    await ctx.send(embed=embed)
##########
##########
###
### Information 
###
##########
##########


@bot.command()
async def info(ctx):
            embed = discord.Embed(title="⚙️ Guffi", color=discord.Color.blue(), timestamp=ctx.message.created_at)

            embed.add_field(name="```v0.0.1```", value=" **Guffi** - is a multifunctional Discord bot built with\n aim to combine the functionality of many bots into one. The bot has many\n useful features that are suitable for almost any server:\n ranging from moderation to interesting economics. Besides\n the project is actively updated, and every week the bot is filled with new ones\n functions.", inline=False)
            embed.add_field(name="Key Resources", value=f" 1) **[Invite](https://discordapp.com/oauth2/authorize?&client_id=881976979220484096&scope=bot&permissions=0)**\n 2) **[Support server](https://discord.gg/wgYFxEHr5q)**\n 3) **[Documentation](https://app.gitbook.com/@guffi/s/guffi/)**", inline=True)
    
            embed.add_field(name="Developers", value="*AalbatrossGuy#2021*\n *AlxelZot#1111*\n *ilesik#6666*", inline=True)
    
            embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

            await ctx.send(embed=embed)

@bot.event
async def ar(self, ctx, autoroles): #сама команда и что ей надо указать, это prefix, комаду и НАЗВАНИЕ роли.
    for guild in self.bot.guilds: # оно ищет на сервере людей
      for member in guild.members: # и тут делается все работа для member-a
        autoroles2 = discord.utils.get(ctx.message.guild.roles, id = autoroles) # нахождение айди по названию, иначе будет ошибка(у меня)
        await member.add_roles(autoroles2) # само добавление роли
    emb = discord.Embed(description = 'Роли успешно добавлены ВСЕМ участникам Discord сервера.')
    await ctx.send(embed = emb) # теперь бот сообщает что всё вышло.


@bot.command()
async def popit(ctx):
            embed = discord.Embed(title="Mini game Pop-It 🎮", color=discord.Color.blue(), timestamp=ctx.message.created_at)

            embed.add_field(name="`Click on the squares`", value=" │||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||│\n│||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||│\n│||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||│\n│||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||│\n│||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||│\n│||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||│")

            embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

            await ctx.send(embed=embed)


@bot.command()
async def invite(ctx):
            embed = discord.Embed(title="Invite", color=discord.Color.blue())

            embed.add_field(name="-Invite-", value=f" 1) **[Bot Invite](https://discordapp.com/oauth2/authorize?&client_id=881976979220484096&scope=bot&permissions=0)**\n 2) **[Support Server](https://discord.gg/wgYFxEHr5q)**", inline=False)
    
            embed.add_field(name="-Other Links-", value=" 1) **[Website](https://WebSite-Guffi.zontialekss.repl.co)**\n 2) **[Docs](https://app.gitbook.com/@guffi/s/guffi)**", inline=False)

            embed.add_field(name="-Support the authors-", value=" 1) **[Boosty.to](https://boosty.to/guffi_official)**", inline=True)
    
            embed.set_footer(text="Thanks for the support ❤️")

            await ctx.send(embed=embed)

@bot.command()
async def suggest(ctx, *, suggestion):
    embed = discord.Embed(
        title = "New suggestion.",
        description = f"{suggestion}",
        color = 0,
        timestamp = ctx.message.created_at
    )
    embed.set_footer(text='Requested by {} | ID-{}' .format(ctx.message.author, ctx.message.author.id))

    await ctx.guild.owner.send(embed=embed)
    await ctx.send("Suggestion sent to server owner.")

##########
##########
###
### User information 
###
##########
##########

@bot.command()
async def user(ctx,member:discord.Member = None, guild: discord.Guild = None):
    if member == None:
        emb = discord.Embed(title=ctx.message.author, url="https://discord.com", color=discord.Color.blue(), timestamp=ctx.message.created_at, icon_url=ctx.message.author.avatar_url)
        emb.add_field(name="ID user:", value=f"{ctx.message.author.id}",inline=True) 
        emb.add_field(name="Name:", value=f"{ctx.message.author.display_name}",inline=True)
        emb.add_field(name="Activity:", value=f"{ctx.author.status}",inline=True)
        emb.add_field(name = "When joined: ", value = f"{ctx.author.joined_at}",inline=True)
        emb.add_field(name="Account has been created:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=True)
        emb.set_image(url=ctx.message.author.avatar_url)
        emb.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title=ctx.message.member, color=discord.Color.blue(), timestamp=ctx.message.created_at, icon_url=ctx.message.member.avatar_url)
        emb.add_field(name="ID user:", value=f"{ctx.message.member.id}",inline=True) 
        emb.add_field(name="Name:", value=f"{ctx.message.member.display_name}",inline=True)
        emb.add_field(name="Activity:", value=f"{ctx.member.status}",inline=True)
        emb.add_field(name="Server role:", value=f"{ctx.member.top_role.mention}",inline=True)
        emb.add_field(name = "When joined: ", value = f"{ctx.member.joined_at}",inline=True)
        emb.add_field(name="Account has been created:", value=ctx.message.member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=True)
        emb.set_image(url=ctx.message.member.avatar_url)
        emb.set_footer(text=f'Requested by { ctx.message.member.display_name }', icon_url=ctx.message.member.avatar_url)
        await ctx.send(embed = emb)



##########
##########
###
### Other commands 
###
##########
##########

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

##########
##########
###
### WARN
###
##########
##########

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

for filename in os.listdir( os.path.abspath(os.curdir)+"\\Cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

        

bot.run(TOKEN)

