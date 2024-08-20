import numpy as np
import imageio
from PIL import Image, ImageOps, ImageFile
from PIL.Image import Resampling

ImageFile.LOAD_TRUNCATED_IMAGES = True

path = 'evolution-of-a-matplotlib/temperature'
images_filenames = [f'{path}/temperature-'+str(i)+'.png' for i in range(1, 20)]
images_for_gif = []

new_size = (1000*3, 700*3)

def add_background(image, new_size, background_color=(255,255,255)):
    """Adds a background to the image to fit the new size while preserving the aspect ratio."""
    img_w, img_h = image.size
    bg_w, bg_h = new_size
    scale = min(bg_w/img_w, bg_h/img_h)
    new_w = int(img_w * scale)
    new_h = int(img_h * scale)
    image = image.resize((new_w, new_h), Resampling.LANCZOS)
    new_image = Image.new("RGB", new_size, background_color)
    new_image.paste(image, ((bg_w - new_w) // 2, (bg_h - new_h) // 2))
    return new_image

for filename in images_filenames:
    try:
        with Image.open(filename) as img:
            img_with_bg = add_background(img, new_size)
            img_array = np.array(img_with_bg)
            images_for_gif.append(img_array)
    except FileNotFoundError:
        pass

# Append the last frame 5 more times
if images_for_gif:
    last_frame = images_for_gif[-1]
    for _ in range(10):
        images_for_gif.append(last_frame)

imageio.mimsave(f'{path}/output.gif', images_for_gif, duration=[900]*len(images_for_gif), format='GIF', loop=0)
print('GIF created!')