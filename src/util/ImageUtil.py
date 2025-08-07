import base64
from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    with Image.open(input_image_path) as image:
        width, height = image.size
        new_width = size if width > height else int((size / height) * width)
        new_height = size if height > width else int((size / width) * height)
        resized_image = image.resize((new_width, new_height))
        resized_image.save(output_image_path)

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

