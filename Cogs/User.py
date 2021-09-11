###################
###################
###
###
###  USERINFO COMMAND
###
###
###################
###################


import discord
from discord.ext import commands
from decouple import config
from __main__ import bot



class SrvInfoCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


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
    

def setup(client):
    client.add_cog(SrvInfoCommand(client))