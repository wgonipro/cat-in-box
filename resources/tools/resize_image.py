from PIL import Image

def resize_image(image_filename, new_size = (200,200)):
    image = Image.open(image_filename).resize(new_size)
    image_name, image_extension = image_filename.split('.')
    image.save(image_name + 'resized.' + image_extension)