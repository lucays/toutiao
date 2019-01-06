import json


def get_config(path):
    with open(path, encoding='utf8') as f:
        config = json.load(f)
    return config


config_path = 'config/conf.json'
config = get_config(config_path)
