from PIL import Image
import random


def cut_image_vertically(image, size_x, size_y, where_split):
    im_left = Image.new("RGB", (where_split, size_y), "white")
    im_left_print = im_left.load()
    im_right = Image.new("RGB", (size_x-where_split, size_y), "white")
    im_right_print = im_right.load()
    image_print = image.load()

    for i in range(0, where_split):
        for j in range(0, size_y):
            im_left_print[i, j] = image_print[i, j]

    for i in range(where_split, size_x):
        for j in range(0, size_y):
            im_right_print[i-where_split, j] = image_print[i, j]

    return im_left, im_right


def cut_image_horizontally(image, size_x, size_y, where_split):
    im_top = Image.new("RGB", (size_x, where_split), "white")
    im_top_print = im_top.load()
    im_down = Image.new("RGB", (size_x, size_y-where_split), "white")
    im_down_print = im_down.load()
    image_print = image.load()

    for i in range(0, size_x):
        for j in range(0, where_split):
            im_top_print[i, j] = image_print[i, j]

    for i in range(0, size_x):
        for j in range(where_split, size_y):
            im_down_print[i, j-where_split] = image_print[i, j]

    return im_top, im_down


def cut_image(image, size_x, size_y, min_x, min_y, depth):
    global num
    if depth > 0 and size_x > 2*min_x and size_y > 2*min_y:
        depth -= random.randrange(0, depth)
        if random.random() < 0.5:
            where_split = random.randrange(min_x, size_x)
            one, two = cut_image_vertically(image, size_x, size_y, where_split)
            cut_image(one, where_split, size_y, min_x, min_y, depth-1)
            cut_image(two, size_x-where_split, size_y, min_x, min_y, depth-1)
        else:
            where_split = random.randrange(min_y, size_y)
            one, two = cut_image_horizontally(image, size_x, size_y, where_split)
            cut_image(one, size_x, where_split, min_x, min_y, depth-1)
            cut_image(two, size_x, size_y-where_split, min_x, min_y, depth-1)
    else:
        print "saving: "+"splitted/"+str(num)+".png"
        image.save("splitted/"+str(num)+".png", "PNG")
        num += 1


im = Image.open('images/gora.jpg')
num = 0

cut_image(im, 750, 394, 10, 10, 1000)
