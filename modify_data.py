import json
import os

url = 'https://raw.githubusercontent.com/bemuse01/kessoku-band-assets/refs/heads/master'
data_name = 'data.json'
main_path = 'assets/images'
files = os.listdir(main_path)

def load_json():
    with open(data_name, 'r') as file:
        data = json.load(file)
    return data

def save_json(data={}):
    with open(data_name, 'w') as file:
        json.dump(data, file, indent=4)

def init():
    data = load_json()

    body_data = [
        {
            'name': d['name'],
            'tag': d['tag'],
            'type': d['type'],
            'url': url + '/' + main_path + '/' + d['name']
        }
        for d in data['body']['data']
    ]

    data['body']['data'] = body_data

    save_json(data)

init()