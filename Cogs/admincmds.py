###################
###################
###
###
###  ADMIN/OWNER COMMAND
###
###
###################
###################



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

        
        embed = discord.Embed(title= f'Remotely ``` 100 ``` messages', color=discord.Color.blue() )

        embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

        await ctx.send(embed=embed)

    #kick command



    @commands.has_permissions( administrator = True )
    @commands.command( pass_context = True )
    async def kick(self, ctx, member: discord.Member, *, reason = None):
            await ctx.channel.purge( limit = 1)

            await member.kick( reason = reason )

            embed = discord.Embed(title= f'kick user ```{ member.name }``` ' )

            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

            await ctx.send(embed=embed)
              
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('❗️ Command information **kick:**')
            embed = discord.Embed(title="Kick a user out of the server.", color=discord.Color.blue(), timestamp=ctx.message.created_at)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/851162534483722301/873200179489148979/avatar-cara-monstruo-dibujos-animados-monstruo-halloween_6996-1122.jpg")

            embed.add_field(name="Delay:", value="`3 sec.`", inline=False)
            embed.add_field(name="Aliases:", value="`Absent`", inline=False)
    
            embed.add_field(name="Usage", value="**`kick <user> [cause]`**", inline=False)
    
            embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

            await ctx.send(embed=embed)
        else:
            raise(error)


    #Ban command
    @commands.command( pass_context = True )
    @commands.has_permissions( administrator = True )
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        await ctx.channel.purge( limit = 1 )

        await member.ban( reason = reason )

        embed = discord.Embed(title= f' Ban user ```{ member.mention }``` ', color=discord.Color.blue())

        embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

        await ctx.send(embed=embed)
    @ban.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('❗️ Command information **ban:**')
            embed = discord.Embed(title="Ban a user on the server.", color=discord.Color.blue(), timestamp=ctx.message.created_at)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/851162534483722301/873200179489148979/avatar-cara-monstruo-dibujos-animados-monstruo-halloween_6996-1122.jpg")

            embed.add_field(name="Delay:", value="`3 sec.`", inline=False)
            embed.add_field(name="Aliases:", value="`Absent`", inline=False)
    
            embed.add_field(name="Usage", value="**`ban <user> [cause]`**", inline=False)
            embed.add_field(name="Required rights", value="`Ban participants`", inline=False)
    
            embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

            await ctx.send(embed=embed)
        else:
            raise(error)


def setup(client):
    client.add_cog(AdminCommands(client))