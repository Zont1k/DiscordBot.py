
###################
###################
###
###
###  INFOBOT COMMAND
###
###
###################
###################


import discord
from discord.ext import commands
from decouple import config
from __main__ import bot
import psutil



class InfoCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


@bot.command()
async def info(ctx):
            embed = discord.Embed(title=" ", color=discord.Color.blue(), icon_url=ctx.bot.user.avatar_url, timestamp=ctx.message.created_at)
            embed.set_author(name=f"Information about {ctx.bot.user.name}", icon_url=ctx.bot.user.avatar_url)
            embed.add_field(name="v0.0.1", value="Guffi - is a multifunctional Discord bot built with\naim to combine the functionality of many bots into one. The bot has many\nuseful features that are suitable for almost any server:\nranging from moderation to interesting economics. Besides\nthe project is actively updated, and every week the bot is filled with new ones\nfunctions.", inline=False)
            embed.add_field(name="❗️ The main", value="Version: 0.0.1\n**Discord.py: v3.9.2", inline=True)

            embed.add_field(name="📈 Statistics", value=f"**Servers:** {len(bot.guilds)}\n**Users:** {len(list(bot.get_all_members()))}", inline=True)

            embed.add_field(name="⚙️ System", value=f"**Platform:** linux\n**Memory:** `{psutil.cpu_percent()} mb`", inline=True)

            embed.add_field(name="💻 Developers", value="*`AalbatrossGuy#2021`*\n*`AlxelZot#1111`*\n*`ilesik#6666`*", inline=True)

            embed.add_field(name="📎 Key Resources", value=f"◾️ [Invite](https://discordapp.com/oauth2/authorize?&client_id=881976979220484096&scope=bot&permissions=0)\n ◾️ [Support server](https://discord.gg/wgYFxEHr5q)\n ◾️ [Documentation](https://app.gitbook.com/@guffi/s/guffi/)", inline=True)
    
    
            embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

            await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(InfoCommand(client))