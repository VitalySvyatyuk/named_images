"""
This script allows to add authors names to the images. It goes through all images
in the source images folder, adds author's name extracted from filename and saves
this image to the output folder. User may specify output folder if necessary.
Text font included.
"""

import os

from PIL import Image, ImageDraw, ImageFont

default_output_folder = 'output-images'
default_images_source = 'source-images'
font_name = "Agane А 55 (roman).ttf"
font_size = 24


def main():
    # Ask user about output folder name
    output_folder = input("Please specify output folder name, or leave empty")
    if output_folder:
        # Create folder if not exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
    # If folder not specified - use 'output-images' folder name
    else:
        output_folder = default_output_folder
        if not os.path.exists(default_output_folder):
            os.makedirs(default_output_folder)

    # Go through all images in 'source-images' and save named image to the output folder
    for image in os.listdir(default_images_source):
        author_name = get_author_name(image)
        font = ImageFont.truetype(font_name, font_size)
        img = Image.open(f'{default_images_source}/{image}')
        draw = ImageDraw.Draw(img)
        text_position = (img.size[0] - font.getsize(author_name)[0] - 30, img.size[1] - 30)
        draw.text(text_position, author_name, (255, 255, 255), font=font)
        img.save(f'{output_folder}/{image}')


def get_author_name(image):
    # Parse author's name from filename
    image_name = image.split('.')[0]
    names = image_name.split('-')
    return '©' + ' '.join(map(lambda x: x.capitalize(), names))


if __name__ == '__main__':
    main()
