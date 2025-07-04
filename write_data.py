from PIL import Image
import json
import os

data_name = 'data.json'
main_path = './assets/images/'

def load_json():
    with open(data_name, 'r') as file:
        data = json.load(file)
    return data

def save_json(data={}):
    with open(data_name, 'w') as file:
        json.dump(data, file, indent=4)

def create_data(files):
    temp = []
    for file in files:
        file_path = os.path.join(main_path, file)
        image = Image.open(file_path)
        width, height = image.size

        temp.append(
            {
                'name': file,
                'width': width,
                'height': height
            }
        )
    return temp


def init():
    files = os.listdir(main_path)

    json_data = {
        'head': {
            'schema': {
                'name': 'string',
                'width': 'number',
                'height': 'number'
            }
        },
        'body': {
            'data': []
        }
    }

    body_data = create_data(files)

    json_data['body']['data'] = body_data

    save_json(json_data)

init()