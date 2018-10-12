# -*- coding: utf8 -*-
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image, ImageDraw, ImageFont
from text_dimension import get_text_dimensions
import config


def create_image(word, font, img_folder):
    W, H = (config.img_width, config.img_height)
    w, h = get_text_dimensions(word, 50, font)
    reshaped_text = arabic_reshaper.reshape(word)
    unicode_text = get_display(reshaped_text)
    image = Image.new("RGBA", (W, H), config.back_ground_color)
    draw = ImageDraw.Draw(image)
    unicode_font = ImageFont.truetype(font, 40)
    draw.text(((W - w) / 2, (H - h) / 2), unicode_text, font=unicode_font, fill=config.font_color)
    full_name = config.image_folder + img_folder + word + config.image_format
    print(full_name)
    image.save(full_name)


def create_angle_image(word, font, text_angle, img_folder):
    W, H = (config.img_width, config.img_height)
    w, h = get_text_dimensions(word, 50, font)
    reshaped_text = arabic_reshaper.reshape(word)
    unicode_text = get_display(reshaped_text)
    image = Image.new("RGBA", (W, H), config.back_ground_color)
    draw = ImageDraw.Draw(image)
    unicode_font = ImageFont.truetype(font, 40)
    draw.text(((W - w) / 2, (H - h) / 2), unicode_text, font=unicode_font, fill=config.font_color)
    # Image directory
    full_name = config.image_folder + img_folder + word + config.image_format
    rot = image.rotate(text_angle, expand=0)
    fff = Image.new('RGBA', rot.size, (255,) * 4)
    # create a composite image using the alpha layer of rot as a mask
    out = Image.composite(rot, fff, rot)
    out.save(full_name)
