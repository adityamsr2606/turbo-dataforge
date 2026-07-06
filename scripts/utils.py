import json
def load_config():
    with open("config/settings.json", "r") as file:
        config = json.load(file)
        return config