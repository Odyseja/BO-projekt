import pictures_assembly as assembly
from PIL import Image

def test_printing_image():
    im = Image.new("RGB", (15, 15), "white")
    pixel = im.load()
    sample_image = [[(0, 0, 0)]*10 for i in range(10)]
    assembly.put_picture(sample_image, 10, 10, pixel, 2, 2)
    for i in range(10):
        for j in range(10):
            print(pixel[i, j], end=" ")
        print("")


test_printing_image()
