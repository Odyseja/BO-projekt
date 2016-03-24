from PIL import Image

# Wyświetlenie użytkownikowi otrzymanego wyniku
# (np. Jako kwadrat o rozmiarze tablicy a w nim mniejsze kwadraty na wyliczonych pozycjach

# results_to_print=[
# (left_top_corner_x, left_top_corner_y, size_x, size_y, picture_name),
# (left_top_corner_x, left_top_corner_y, size_x, size_y, picture_name),
# (left_top_corner_x, left_top_corner_y, size_x, size_y, picture_name),
# (left_top_corner_x, left_top_corner_y, size_x, size_y, picture_name),
# (left_top_corner_x, left_top_corner_y, size_x, size_y, picture_name),


def assemble_pictures(max_x, max_y, results_to_print, path_to_pictures_folder=None):
    im = Image.new("RGB", (max_x, max_y), "white")
    board = im.load()
    images_to_put = prepare_images_list(results_to_print, path_to_pictures_folder)
    for data in images_to_put:
        picture, image_x_size, image_y_size, left_up_corner_x, left_up_corner_y = data
        put_picture( board,  picture, image_x_size, image_y_size, left_up_corner_x, left_up_corner_y)
    return board


def put_picture(board, image, image_x_size, image_y_size, left_up_corner_x, left_up_corner_y):
    for i in range(image_x_size):
        for j in range(image_y_size):
            board[left_up_corner_x+i, left_up_corner_y+j] = image[i, j]


def read_picture_from_file(path, filename):
    full_path = path+'/'+filename
    return Image.open(full_path).load()


def mock_picture(size_x, size_y):
    im = Image.new("RGB", (size_x, size_y), "white").load()
    # print frame to extinguish pictures from each other
    for i in range(0, size_x):
        im[i, 0] = (0, 0, 0)
    for i in range(0, size_y):
        im[0, i] = (0, 0, 0)
    for i in range(0, size_y):
        im[size_x-1, i] = (0, 0, 0)
    for i in range(0, size_x):
        im[i, size_y-1] = (0, 0, 0)
    # fill the rest of the image
    for i in range(1, size_x-1):
        for j in range(1, size_y-1):
            im[i, j] = (139, 139, 131)
    return im


def prepare_images_list(results_to_print, path_to_pictures_folder):
    images_to_put = []
    for result in results_to_print:
        left_top_corner_x, left_top_corner_y, size_x, size_y, picture_name = result
        if path_to_pictures_folder:
            image = read_picture_from_file(path_to_pictures_folder, picture_name)
            tup = (image, size_x, size_y, left_top_corner_x, left_top_corner_y)
            images_to_put.append(tup)
        else:
            images_to_put.append((mock_picture(size_x, size_y), size_x, size_y, left_top_corner_x, left_top_corner_y))
    return images_to_put


def print_board(pixel, max_x, max_y):
    for i in range(max_x):
        for j in range(max_y):
            print(pixel[i, j], end=" ")
        print("")