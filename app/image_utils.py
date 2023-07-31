from PIL import Image

def resize_image(image_path, target_width, target_height):
    img = Image.open(image_path)
    img_resized = img.resize((target_width, target_height), Image.ANTIALIAS)
    img_resized.save(image_path)
