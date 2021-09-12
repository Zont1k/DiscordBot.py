###################
###################
###
###
###  HELP COMMAND
###
###
###################
###################



import discord
from discord.ext import commands
from decouple import config
from discord_components import DiscordComponents, Button, ButtonStyle, Select
from discord.embeds import Embed
from __main__ import bot

class HelpCmd(commands.Cog):
    def __init__(self, client):
        self.client = client

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
    


def setup(client):
    client.add_cog(HelpCmd(client))
