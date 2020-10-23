import toml, discord
from discord.ext import commands

data_file_path = 'data.json'
config_file_path = 'config.toml'


def load_config():
    global config
    config = toml.load(config_file_path)
    return config

async def bot_load(bot):
    global guild, log_channel, logging_enabled
    guild = bot.fetch_guild(config['guild_id'])

def currency(value):
    if config['economy']['split_nums']:
        value = f'{value:,}'
    return config['economy']['format'].format(VAL=value)
 
async def discord_log(data):
    if not logging_enabled:
        return
    if data['ctx']:
        msg = f'{data["ctx"].author}:{data["ctx"].message}'
    else:
        msg = f'{data["user"]}:{data["msg"]}'
    


# def fomat_config(key):
#     return key.format()