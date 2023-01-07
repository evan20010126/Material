from PIL import ImageGrab
from PIL import Image

file_name = "cat.jpg"

img = Image.open(file_name)

img = img.resize((1920, 1080), Image.BILINEAR)

img.save("modify"+file_name)
