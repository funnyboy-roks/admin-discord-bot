# Created by funnyboy_roks
# github.com/funnyboy-roks

# Main file running the bot

import json, discord, economy_commands, toml
from discord.ext import commands
import helper_functions as h_func

TOKEN = open('TOKEN.txt').read()
config = h_func.load_config()

config = h_func.config
print(h_func.currency(123321))

bot = commands.Bot(command_prefix=config['prefix'])


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

if config['economy']['enabled']:
    bot.add_cog(economy_commands.Economy(bot))

bot.run(TOKEN)


