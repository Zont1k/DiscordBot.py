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

TOKEN = config('TOKEN')
bot = commands.Bot(command_prefix="g.", case_insensitive=True, owner_ids=['564380749873152004', '676414187131371520'])
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
    DiscordComponents(bot)
    print("Bot is ready!")
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

