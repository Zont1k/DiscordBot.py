import discord, os
from discord.ext import commands
from lib.db import db
from decouple import config

def get_prefix(bot, message):
    prefix = db.field("SELECT Prefix FROM guilds WHERE GuildID = ?", message.guild.id)

    return commands.when_mentioned_or(prefix)(bot, message)

TOKEN = config('TOKEN')
bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, owner_ids=['564380749873152004', '676414187131371520'])

# Insert new guild into guilds prefix database indexing by GuildID
@bot.event
async def on_guild_join(guild):
    db.execute("INSERT OR IGNORE INTO guilds(GuildID, Prefix) VALUES(?, ?)", guild.id, "!") # Saves guild by it's id.
    db.commit() # save changes
    print("new server joined") #optional


# Removes the guild from the guilds database indexing by GuildID
@bot.event
async def on_guild_remove(guild):
    db.execute("DELETE FROM guilds WHERE GuildID = ?", guild.id) # Deletes guild from the database by finding it's id.
    db.commit() #save changes

# Change prefix command
@bot.command(name="pre", aliases=["p", "cp"])
@commands.has_permissions(manage_guild=True)
async def change_bot_prefix(ctx, new_prefix:str) -> str:
    if len(new_prefix) > 7:
        await ctx.channel.send("Server Prefix Cannot Be More Than 7 Letters Long!") # You can change the message accordingly
    else:
        await ctx.send(f"Prefix changed to `{new_prefix}` successfully.")
        db.execute("UPDATE guilds SET Prefix = ? WHERE GuildID = ?", new_prefix, ctx.guild.id) # Updates server prefix indexing by GuildID
        db.commit()


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
    
@bot.command()
async def load_extension(ctx, extension):
    bot.load_extension(f'Cogs.{extension}')


@bot.command()
async def unload_extension(ctx, extension):
    bot.unload_extension(f'Cogs.{extension}')


for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

bot.run(TOKEN)
