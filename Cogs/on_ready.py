# Coding=UTF8
# !python
# !/usr/bin/env python3

import discord, os, datetime
from discord.ext import commands


class OnReady(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_ready(self):

        cogs = [x[:-3] for x in os.listdir('E:\Бэкап Леши 06.04.2021\GUFFI BOT\Новая папка\DiscordBotGuffi\Cogs')]
        for cogsname in cogs:
            if cogsname == "__pycach":
                break
            else:
                try:
                    print(f"Loaded cogs.{cogsname} successfully!")
                except:
                    pass

def setup(client):
    client.add_cog(OnReady(client))
