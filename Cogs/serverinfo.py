
###################
###################
###
###
###  SERVERINFO COMMAND
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
    

def setup(client):
    client.add_cog(SrvInfoCommand(client))
