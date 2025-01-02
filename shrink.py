from PIL import Image
import io
import os

main_path = './assets/images/'
files = os.listdir(main_path)

megabytes = 1024 * 1024
max_file_size = megabytes * 3 # 3MB
default_resize_ratio = 2
resize_ratio_step = 0.5

def get_image_size(image, format='JPEG', quality=100):
    buffer = io.BytesIO()
    image.save(buffer, format=format, quality=quality)
    return len(buffer.getvalue())

def init():
    for file in files:
        file_path = os.path.join(main_path, file)
        file_size = os.path.getsize(file_path)

        if file_size <= max_file_size:
            continue
        else:
            image = Image.open(file_path)
            width, height = image.size
            format = image.format

            resize_ratio = default_resize_ratio

            print(f'current file: {file_path}, origin file size: {file_size / megabytes}MB')

            while True:
                new_width = int(width / resize_ratio)
                new_height = int(height / resize_ratio)

                temp_image = image.resize((new_width, new_height))
                temp_file_size = get_image_size(temp_image, format)

                resize_ratio += resize_ratio_step

                if temp_file_size <= max_file_size:
                    print(f'file size: {temp_file_size / megabytes}MB, width: {new_width}, height: {new_height}')
                    temp_image.save(file_path)
                    break

init()
