import discord
from discord.ext import commands

TOKEN = 'ODM4MTI1NTM5ODQ3NzAwNTIw.YI2jPA.BVXpSNmy29I1kXDf7U2hPylFAfs'
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://github.com/TheBion/DiscordBotGuffi"))
    print("I'm ready!")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="⚙️ Guffi")

    author = ctx.message.author
    await ctx.send(f'{author.mention}')

    embed.add_field(name="Information", value=" ```Coming soon ...``` ", inline=False)
    embed.add_field(name="👨 Author", value="AlxelZot\n AalbatrossGuy", inline=True)
    
    embed.add_field(name="📲 Capabilities", value="!info\n", inline=True)

    embed.set_thumbnail(url="https://image.freepik.com/vector-gratis/avatar-cara-monstruo-dibujos-animados-monstruo-halloween_6996-1122.jpg")
 
    await ctx.send(embed=embed)

bot.run(TOKEN)