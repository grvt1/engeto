import os

import json


def load_json():
    with open(f'results{os.sep}json_data.json', 'r') as file:
        return json.load(file)


def dump_json(data):
    with open(f'results{os.sep}json_data.json', 'w') as file:
        json.dump(data, file, indent=2)
