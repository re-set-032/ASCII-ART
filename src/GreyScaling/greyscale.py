# Importing Image and ImageOps module from PIL package
from PIL import Image, ImageOps

# creating an og_image object
og_image = Image.open("birdies.jpeg")
og_image.show()

# applying grayscale method
gray_image = ImageOps.grayscale(og_image)
gray_image.save('gray_image.png')
gray_image.show()