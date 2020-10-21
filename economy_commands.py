# Created by funnyboy_roks
# github.com/funnyboy-roks

import discord, json
from discord.ext import commands
import helper_functions as h_func

dataFile = 'data.json'

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = 'Economy'

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded cog: {self.name}')

    @commands.command()
    async def pay(self, ctx, to_user: discord.User, amount: int):
        print(f'{ctx.author} payed {to_user} {h_func.currency(amount)}.')