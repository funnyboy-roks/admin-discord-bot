# Created by funnyboy_roks
# github.com/funnyboy-roks

import discord, json
from discord.ext import commands

dataFile = 'data.json'

class Economy(commands.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.name = 'Economy'
        self.config = config

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded cog: {self.name}')

    @commands.command()
    async def pay(self, ctx, to_user: discord.User,amount):
        print(f'{ctx.author} payed {to_user} {self.config["currency"]}{amount}')