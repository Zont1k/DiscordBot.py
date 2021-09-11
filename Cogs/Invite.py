###################
###################
###
###
###  INVITE COMMAND
###
###
###################
###################


import discord
from discord.ext import commands
from decouple import config
from __main__ import bot



class PingCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


@bot.command()
async def invite(ctx):
            embed = discord.Embed(title="Invite", color=discord.Color.blue())

            embed.add_field(name="-Invite-", value=f" 1) **[Bot Invite](https://discordapp.com/oauth2/authorize?&client_id=881976979220484096&scope=bot&permissions=0)**\n 2) **[Support Server](https://discord.gg/wgYFxEHr5q)**", inline=False)
    
            embed.add_field(name="-Other Links-", value=" 1) **[Website](https://WebSite-Guffi.zontialekss.repl.co)**\n 2) **[Docs](https://app.gitbook.com/@guffi/s/guffi)**", inline=False)

            embed.add_field(name="-Support the authors-", value=" 1) **[Boosty.to](https://boosty.to/guffi_official)**", inline=True)
    
            embed.set_footer(text="Thanks for the support ❤️")

            await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(PingCommand(client))