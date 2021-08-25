import discord, os
from discord import Colour
from discord.embeds import Embed
from discord.ext import commands
from decouple import config
from Cybernator import Paginator
from asyncio import sleep
from discord_components import DiscordComponents, Button, ButtonStyle
import sqlite3
import html
import requests
import json
import random

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
async def ping(ctx):
     await ctx.send(f'Pong! In {round(bot.latency * 1000)}ms')

@bot.command()
async def help(ctx):
    await ctx.send(
    embed=discord.Embed(title="Help menu", description="To navigate the pages, use\n buttons below. If for some reason they are not on your device\n are displayed, please update / reinstall the Discord app.", color=discord.Color.blue(), timestamp=ctx.message.created_at),
    components=[
            Button(style=ButtonStyle.blue, label="Start", emoji="▶️"),
        ]
    )
    response = await bot.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == "Start":
            await response.respond(
            embed = discord.Embed(title="⚙️ Guffi", description=" **Guffi** - is a multifunctional Discord bot built with\n aim to combine the functionality of many bots into one. The bot has many\n useful features that are suitable for almost any server:\n ranging from moderation to interesting economics. Besides\n the project is actively updated, and every week the bot is filled with new ones\n функциями.  \n **Key Resources**\n  1) **[Invite](https://discordapp.com/oauth2/authorize?&client_id=838125539847700520&scope=bot&permissions=8)**\n 2) **[Support server](https://discord.gg/wgYFxEHr5q)**\n 3) **[Documentation](https://app.gitbook.com/@guffi/s/guffi/)**  \n **Developers**\n *`AalbatrossGuy#2021`*\n *`AlxelZot#1111`*\n *`ilesik#6666`*", color=discord.Color.blue(), timestamp=ctx.message.created_at),
            components=[
            Button(style=ButtonStyle.blue, label="Information", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Command", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Game", emoji="▶️"),
                ]    
            ) 
    await ctx.send(f'https://discord.gg/wgYFxEHr5q'),
    response = await bot.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == "Information":
            await response.respond(
            embed = discord.Embed(title="⚙️ Guffi", description=" **Guffi** - is a multifunctional Discord bot built with\n aim to combine the functionality of many bots into one. The bot has many\n useful features that are suitable for almost any server:\n ranging from moderation to interesting economics. Besides\n the project is actively updated, and every week the bot is filled with new ones\n функциями.  \n **Key Resources**\n  1) **[Invite](https://discordapp.com/oauth2/authorize?&client_id=838125539847700520&scope=bot&permissions=8)**\n 2) **[Support server](https://discord.gg/wgYFxEHr5q)**\n 3) **[Documentation](https://app.gitbook.com/@guffi/s/guffi/)**  \n **Developers**\n *`AalbatrossGuy#2021`*\n *`AlxelZot#1111`*\n *`ilesik#6666`*", color=discord.Color.blue(), timestamp=ctx.message.created_at),
            components=[
            Button(style=ButtonStyle.blue, label="Information", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Command", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Game", emoji="▶️"),
                ]    
            ) 
    response = await bot.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == "Command":
            await response.respond(
            embed = discord.Embed(title="≫ Command list ≪", description="**General » g.help General**\n `g.info` `g.invite` `g.ping` `g.support`\n **Moderation » +help Moderation**\n `g.ban` `g.clear` `g.mute` `g.kick` `g.warn`\n `g.add-role`", color=discord.Color.blue(), timestamp=ctx.message.created_at),
            components=[
            Button(style=ButtonStyle.blue, label="Information", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Command", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Game", emoji="▶️"),
                ]     
            )

        




@bot.event
async def on_ready():
    DiscordComponents(bot)
    print("Bot is ready!")
    while not bot.is_closed():
        await bot.change_presence(activity=discord.Game(name=f"{len(bot.guilds)} servers!"))
        await sleep(15)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="| g.help"))
        await sleep(15)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://guffibot.xyz"))
        await sleep(15)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))
        await sleep(15)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Minecraft"))
        await sleep(15)
        print("I'm ready!")



@bot.command()
async def server(ctx):
        """Shows server info"""

        server = ctx.message.server

        roles = str(len(server.roles))
        emojis = str(len(server.emojis))
        channels = str(len(server.channels))

        embed = discord.Embed(title=server.name, description='Server Info', color=0xEE8700)
        embed.set_thumbnail(url=server.icon_url)
        embed.add_field(name="Created on:", value=server.created_at.strftime('%d %B %Y at %H:%M UTC+3'), inline=False)
        embed.add_field(name="Server ID:", value=server.id, inline=False)
        embed.add_field(name="Users on server:", value=server.member_count, inline=True)
        embed.add_field(name="Server owner:", value=server.owner, inline=True)

        embed.add_field(name="Default Channel:", value=server.default_channel, inline=True)
        embed.add_field(name="Server Region:", value=server.region, inline=True)
        embed.add_field(name="Verification Level:", value=server.verification_level, inline=True)

        embed.add_field(name="Role Count:", value=roles, inline=True)
        embed.add_field(name="Emoji Count:", value=emojis, inline=True)
        embed.add_field(name="Channel Count:", value=channels, inline=True)

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
            embed.add_field(name="Key Resources", value=f" 1) **[Invite](https://discordapp.com/oauth2/authorize?&client_id=838125539847700520&scope=bot&permissions=8)**\n 2) **[Support server](https://discord.gg/wgYFxEHr5q)**\n 3) **[Documentation](https://app.gitbook.com/@guffi/s/guffi/)**", inline=True)
    
            embed.add_field(name="Developers", value="*AalbatrossGuy#2021*\n *AlxelZot#1111*\n *ilesik#6666*", inline=True)
    
            embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

            await ctx.send(embed=embed)


@bot.command()
async def popit(ctx):
            embed = discord.Embed(title="Mini game Pop-It 🎮", color=discord.Color.blue(), timestamp=ctx.message.created_at)

            embed.add_field(name="`Click on the squares`", value=" │||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||│\n│||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||│\n│||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||│\n│||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||│\n│||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||│\n│||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||│")

            embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

            await ctx.send(embed=embed)


@bot.command()
async def invite(ctx):
            embed = discord.Embed(title="Invite", color=discord.Color.blue())

            embed.add_field(name="-Invite-", value=f" 1) **[Bot Invite](https://discordapp.com/oauth2/authorize?&client_id=838125539847700520&scope=bot&permissions=8)**\n 2) **[Support Server](https://discord.gg/wgYFxEHr5q)**", inline=False)
    
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
        emb = discord.Embed(title=ctx.message.author, color=discord.Color.blue(), timestamp=ctx.message.created_at, icon_url=ctx.message.author.avatar_url)
        emb.add_field(name="💡 ID:", value=f" ```{ctx.message.author.id}``` ",inline=False) 
        emb.add_field(name="💡 Name:", value=f"```{ctx.message.author.display_name}```",inline=False)
        emb.add_field(name="💡 Activity:", value=f"```{ctx.message.author.status}```",inline=False)
        emb.add_field(name="Server role:", value=f"{ctx.message.author.top_role.mention}")
        emb.add_field(name="Account has been created:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        emb.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="", color=discord.Color.blue(), timestamp=ctx.message.created_at)
        emb.add_field(name="User ID:", value=member.id,inline=False)
        emb.add_field(name="Server role:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Account has been created:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=member.avatar_url)
        emb.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)

@bot.command()
async def userinfo(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)




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
    ),components = [Button(style=ButtonStyle.blue, label=i) for i in posible_answers])

    try:
        response = await bot.wait_for("button_click",timeout=10.0)
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
