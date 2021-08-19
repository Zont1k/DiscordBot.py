import discord, os
from discord.embeds import Embed
from discord.ext import commands
from decouple import config
from Cybernator import Paginator
from asyncio import sleep

TOKEN = config('TOKEN')
bot = commands.Bot(command_prefix="g.", case_insensitive=True, owner_ids=['564380749873152004', '676414187131371520'])
bot.remove_command("help")


#@bot.group(invoke_without_command=True)
#async def help(ctx):
    #await ctx.send()
    
    #em = discord.Embed(title = "Help menu", color=discord.Color.blue())
    
    #em.add_field(name = " **To navigate the pages, use**", value = " **buttons below. If for some reason they are not on your device\n are displayed, please update / reinstall the Discord app.**", inline=True)
    
    #em.set_thumbnail(url="https://cdn.discordapp.com/attachments/851162534483722301/873200179489148979/avatar-cara-monstruo-dibujos-animados-monstruo-halloween_6996-1122.jpg")

    #await ctx.send(embed = em)

@bot.command()
async def servers(ctx):
        context = len(ctx.servers)
        await ctx.say(f"Connected on {str(len(context))} servers:")
        await ctx.say('\n'.join(server.name for server in servers))

@bot.command()
async def help(ctx):
    embed2 = discord.Embed(title="≫ Command list ≪", description="**General » g.help General**\n ```g.info``````g.invite``````g.ping``````g.support```\n **Moderation » +help Moderation**\n ```g.ban``````g.clear``````g.mute``````g.kick``````g.warn``````g.add-role```", color=discord.Color.blue())
    embed1 = discord.Embed(title="Help menu", description="To navigate the pages, use\n buttons below. If for some reason they are not on your device\n are displayed, please update / reinstall the Discord app.", color=discord.Color.blue()) 
    embeds = [embed1, embed2]
    message = await ctx.send(embed=embed1)
    page = Paginator(bot, message, only=ctx.author, use_more=False, embeds=embeds)
    await ctx.send(f'https://discord.gg/wgYFxEHr5q')
    embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/851162534483722301/873200179489148979/avatar-cara-monstruo-dibujos-animados-monstruo-halloween_6996-1122.jpg")
    embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await page.start()

@bot.event
async def on_ready():
     while True:
          await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="| g.help"))
          await sleep(15)
          await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://guffibot.xyz"))
          await sleep(15)
          await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))
          await sleep(15)
          await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Minecraft"))
          await sleep(15)
          print("I'm ready!")

@bot.command()
async def server(self, ctx):

    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    staff_roles = ["Owner", "Head Dev", "Dev", "Head Admin", "Admins", "Moderators", "Community Helpers", "Members"]
        
    embed2 = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    embed2.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
    embed2.add_field(name='Owner', value=f"{ctx.owner.name}", inline=False)
    embed2.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
    embed2.add_field(name='Highest role', value=ctx.guild.roles[-2], inline=False)
    embed2.add_field(name='Contributers:', value="None")

    for r in staff_roles:
        role = discord.utils.get(ctx.guild.roles, name=r)
        if role:
            members = '\n'.join([member.name for member in role.members]) or "None"
            embed2.add_field(name=role.name, value=members)

    embed2.add_field(name='Number of roles', value=str(role_count), inline=False)
    embed2.add_field(name='Number Of Members', value=ctx.guild.member_count, inline=False)
    embed2.add_field(name='Bots:', value=(', '.join(list_of_bots)))
    embed2.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
    embed2.set_thumbnail(url=ctx.guild.icon_url)
    embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed2.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)

    await ctx.send(embed=embed2)
##########
##########
###
### Information 
###
##########
##########

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

@bot.command()
async def info(ctx):
            embed = discord.Embed(title="⚙️ Guffi", color=discord.Color.blue(), timestamp=ctx.message.created_at)

            embed.add_field(name="```v0.0.1```", value=" **Guffi** - is a multifunctional Discord bot built with\n aim to combine the functionality of many bots into one. The bot has many\n useful features that are suitable for almost any server:\n ranging from moderation to interesting economics. Besides\n the project is actively updated, and every week the bot is filled with new ones\n функциями.", inline=False)
            embed.add_field(name="Key Resources", value=f" 1) **[Invite](https://discordapp.com/oauth2/authorize?&client_id=838125539847700520&scope=bot&permissions=8)**\n 2) **[Support server](https://discord.gg/wgYFxEHr5q)**\n 3) **[Documentation](https://app.gitbook.com/@guffi/s/guffi/)**", inline=True)
    
            embed.add_field(name="Developers", value="*AalbatrossGuy*\n *Aleksey Zotov*", inline=True)
    
            embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

            await ctx.send(embed=embed)

##########
##########
###
### User information 
###
##########
##########

@bot.command()
async def user(ctx,member:discord.Member = None, guild: discord.Guild = None):
    if member == None:
        emb = discord.Embed(title=ctx.message.author, color=discord.Color.blue(), timestamp=ctx.message.created_at, icon_url=ctx.message.author.avatar_url)
        emb.add_field(name="💡 ID:", value=f" ```{ctx.message.author.id}``` ",inline=True) 
        emb.add_field(name="💡 Name:", value=f"```{ctx.message.author.display_name}```",inline=True)
        emb.add_field(name="💡 Activity:", value=f"```{ctx.message.author.status}```",inline=True)
        emb.add_field(name="Server role:", value=f"{ctx.message.author.top_role.mention}")
        emb.add_field(name="Account has been created:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        emb.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="", color=discord.Color.blue(), timestamp=ctx.message.created_at)
        emb.add_field(name="User ID:", value=member.id,inline=False)
        emb.add_field(name="Server role:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Account has been created:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=member.avatar_url)
        emb.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)

##########
##########
###
### WARN
###
##########
##########


@bot.command()
async def load_extension(ctx, extension):
    bot.load_extension(f'Cogs.{extension}')


@bot.command()
async def unload_extension(ctx, extension):
    bot.unload_extension(f'Cogs.{extension}')

for filename in os.listdir( os.path.abspath(os.curdir)+"\\DiscordBotGuffi\\Cogs"):
    if filename.endswith('.py'):
     bot.load_extension(f'Cogs.{filename[:-3]}')

bot.run(TOKEN)
