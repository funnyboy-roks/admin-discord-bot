
import discord, json
from discord.ext import commands
import helper_functions as h_func


class RandomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = 'Random Commands'

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded cog: {self.name}')

    @commands.command()
    async def quote(self, ctx, msg: discord.Message):
        await ctx.send(f'Content: {msg.content}')