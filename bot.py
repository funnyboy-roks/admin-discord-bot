# Created by funnyboy_roks
# github.com/funnyboy-roks

# Main file running the bot

import json, discord, economy, toml, random_commands
from discord.ext import commands
import helper_functions as h_func

TOKEN = open('TOKEN.txt').read()
config = h_func.load_config()

config = h_func.config

bot = commands.Bot(command_prefix=config['prefix'])


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    await h_func.bot_load(bot)

if config['economy']['enabled']:
    bot.add_cog(economy.Economy(bot))

bot.add_cog(random_commands.RandomCommands(bot))

bot.run(TOKEN)


