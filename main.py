import discord, os
from discord.embeds import Embed
from discord.ext import commands
from decouple import config
from Cybernator import Paginator
from asyncio import sleep
from discord_components import DiscordComponents, Button, ButtonStyle


TOKEN = config('TOKEN')
bot = commands.Bot(command_prefix="g.", case_insensitive=True, owner_ids=['564380749873152004', '676414187131371520'])
bot.remove_command("help")

print(os.path.realpath(__file__)+'/Cogs')



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
async def test(ctx):
    embed2 = discord.Embed(title="≫ Command list ≪", description="**General » g.help General**\n ```g.info``````g.invite``````g.ping``````g.support```\n **Moderation » +help Moderation**\n ```g.ban``````g.clear``````g.mute``````g.kick``````g.warn``````g.add-role```", color=discord.Color.blue())
    embed1 = discord.Embed(title="Help menu", description="To navigate the pages, use\n buttons below. If for some reason they are not on your device\n are displayed, please update / reinstall the Discord app.", color=discord.Color.blue()) 
    embeds = [embed1, embed2]
    message = await ctx.send(embed=embed1)
    page = Paginator(bot, message, only=ctx.author, use_more=False, embeds=embeds)
    await ctx.send(f'https://discord.gg/wgYFxEHr5q')
    embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/851162534483722301/873200179489148979/avatar-cara-monstruo-dibujos-animados-monstruo-halloween_6996-1122.jpg")
    embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await page.start()



@bot.command()
async def help(ctx):
    await ctx.send(
    embed=discord.Embed(title="Help menu", description="To navigate the pages, use\n buttons below. If for some reason they are not on your device\n are displayed, please update / reinstall the Discord app.", color=discord.Color.blue(), timestamp=ctx.message.created_at),
    components=[
            Button(style=ButtonStyle.blue, label="Information", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Command", emoji="▶️"),
            Button(style=ButtonStyle.blue, label="Game", emoji="▶️"),
        ]
    )
    await ctx.send(f'https://discord.gg/wgYFxEHr5q'),
    response = await bot.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == "Information":
            await response.respond(
            embed = discord.Embed(title="⚙️ Guffi", description=" **Guffi** - is a multifunctional Discord bot built with\n aim to combine the functionality of many bots into one. The bot has many\n useful features that are suitable for almost any server:\n ranging from moderation to interesting economics. Besides\n the project is actively updated, and every week the bot is filled with new ones\n функциями.  \n **Key Resources**\n  1) **[Invite](https://discordapp.com/oauth2/authorize?&client_id=838125539847700520&scope=bot&permissions=8)**\n 2) **[Support server](https://discord.gg/wgYFxEHr5q)**\n 3) **[Documentation](https://app.gitbook.com/@guffi/s/guffi/)**  \n **Developers**\n *`AalbatrossGuy#2021`*\n *`AlxelZot#1111`*\n *`ilesik#6666`*", color=discord.Color.blue(), timestamp=ctx.message.created_at),
            components=[
                    Button(style=ButtonStyle.blue, label="Command", emoji="▶️"),
                    Button(style=ButtonStyle.blue, label="Game", emoji="▶️"),
                ]    
            ) 
    response = await bot.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == "Command":
            await response.respond(
            embed = discord.Embed(title="≫ Command list ≪", description="**General » g.help General**\n `g.info` `g.invite` `g.ping` `g.support`\n **Moderation » +help Moderation**\n `g.ban` `g.clear` `g.mute` `g.kick` `g.warn`\n `g.add-role`", color=discord.Color.blue(), timestamp=ctx.message.created_at),
            components=[
                    Button(style=ButtonStyle.blue, label="Information", emoji="▶️"),
                    Button(style=ButtonStyle.blue, label="Game", emoji="▶️"),
                ]     
            )
        



@bot.event
async def on_ready():
    DiscordComponents(bot)
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
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)
  id = str(ctx.guild.id)
  role_count = len(ctx.guild.roles)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.blue(),
      timestamp=ctx.message.created_at
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="👑 Owner", value=ctx.guild.owner, inline=False)
  embed.add_field(name='💡“`CSS Number of roles', value=str(role_count), inline=False)
  embed.add_field(name="💻 Server ID", value=id, inline=False)
  embed.add_field(name="📍 Region", value=region[0].upper()+ region[1::], inline=True)
  embed.add_field(name="🙎 Member Count", value=memberCount, inline=False)
  embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

  await ctx.send(embed=embed)
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
    
            embed.add_field(name="Developers", value="*AalbatrossGuy#2021*\n *AlxelZot#1111*\n *ilesik#6666*", inline=True)
    
            embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

            await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
            embed = discord.Embed(title="Invite", color=discord.Color.blue())

            embed.add_field(name="-Invite-", value=f" 1) **[Bot Invite](https://discordapp.com/oauth2/authorize?&client_id=838125539847700520&scope=bot&permissions=8)**\n 2) **[Support Server](https://discord.gg/wgYFxEHr5q)**", inline=False)
    
            embed.add_field(name="-Other Links-", value=" 1) **[Website](https://WebSite-Guffi.zontialekss.repl.co)**\n 2) **[Docs](https://app.gitbook.com/@guffi/s/guffi)**", inline=False)

            embed.add_field(name="-Support the authors-", value=" 1) **[Boosty.to](https://boosty.to/guffi_official)**", inline=True)
    
            embed.set_footer(text="Thanks for the support ❤️")

            await ctx.send(embed=embed)

@bot.command()
async def suggest(ctx, *, suggestion):
    embed = discord.Embed(
        title = "New suggestion.",
        description = f"{suggestion}",
        color = 0,
        timestamp = ctx.message.created_at
    )
    embed.set_footer(text='Requested by {} | ID-{}' .format(ctx.message.author, ctx.message.author.id))

    await ctx.guild.owner.send(embed=embed)
    await ctx.send("Suggestion sent to server owner.")

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
        emb.add_field(name="💡 ID:", value=f" ```{ctx.message.author.id}``` ",inline=False) 
        emb.add_field(name="💡 Name:", value=f"```{ctx.message.author.display_name}```",inline=False)
        emb.add_field(name="💡 Activity:", value=f"```{ctx.message.author.status}```",inline=False)
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

@bot.command()
async def userinfo(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)

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