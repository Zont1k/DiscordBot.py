import discord
from discord.ext import commands
from decouple import config

TOKEN = config('TOKEN')
bot = commands.Bot(command_prefix='!')

#Clear command
@bot.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear( ctx, amount = 100):
    await ctx.channel.purge( limit = amount )

#kick command
@bot.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge( limit = 1)

    await member.kick( reason = reason )

    embed = discord.Embed(title= f'kick user ```{ member.name }``` ' )

    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#Ban command
@bot.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge( limit = 1 )

    await member.ban( reason = reason )

    embed = discord.Embed(title= f'ban user ```{ member.mention }``` ')

    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

bot.run( TOKEN )