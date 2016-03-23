from PIL import Image

# Wyświetlenie użytkownikowi otrzymanego wyniku
# (np. Jako kwadrat o rozmiarze tablicy a w nim mniejsze kwadraty na wyliczonych pozycjach

# resultToPrint=[
# (leftTopCorner, sizeX, sizeY, pictureName),
# (leftTopCorner, sizeX, sizeY, pictureName),
# (leftTopCorner, sizeX, sizeY, pictureName),
# (leftTopCorner, sizeX, sizeY, pictureName),
# (leftTopCorner, sizeX, sizeY, pictureName),
#]


def assemble_pictures(max_x, max_y, path_to_pictures_folder, result_to_print):
    im = Image.new("RGB", (max_x, max_y), "white")
    pixel = im.load()
    for i in range(max_x):
        for j in range(max_y):
            print(pixel[i, j], end=" ")
        print("")


def put_picture(image, image_x_size, image_y_size, image_background, left_up_corner_x, left_up_corner_y):
    for i in range(image_x_size):
        for j in range(image_y_size):
            image_background[left_up_corner_x+i, left_up_corner_y+j] = image[i][j]
