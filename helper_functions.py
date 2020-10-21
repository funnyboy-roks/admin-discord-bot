import toml


def load_config():
    global config
    config = toml.load('config.toml')
    return config

def currency(value):
    if config['economy']['split_nums']:
        value = f'{value:,}'
    return config['economy']['format'].format(VAL=value)
 
# def fomat_config(key):
#     return key.format()