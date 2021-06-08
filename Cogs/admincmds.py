import discord
from discord.ext import commands
from decouple import config

class AdminCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Clear command
    @commands.command( pass_context = True )
    @commands.has_permissions( administrator = True )
    async def clear( self, ctx, amount = 100):
        await ctx.channel.purge( limit = amount )

    #kick command
    @commands.command( pass_context = True )
    @commands.has_permissions( administrator = True )
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        await ctx.channel.purge( limit = 1)

        await member.kick( reason = reason )

        embed = discord.Embed(title= f'kick user ```{ member.name }``` ' )

        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    #Ban command
    @commands.command( pass_context = True )
    @commands.has_permissions( administrator = True )
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        await ctx.channel.purge( limit = 1 )

        await member.ban( reason = reason )

        embed = discord.Embed(title= f'ban user ```{ member.mention }``` ')

        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(AdminCommands(client))
