# Importing Image and ImageOps module from PIL package
from PIL import Image, ImageOps

if __name__ == "__main__":

    # Reading RGB image (Change image file here)
    original_image = Image.open("sample.jpg)
    # original_image.show()

    # Applying grayscale method
    gray_image = ImageOps.grayscale(original_image)
    gray_image.save('grey.png')
    # gray_image.show()
