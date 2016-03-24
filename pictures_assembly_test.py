import pictures_assembly as assembly
from PIL import Image


def test_printing_image():
    im = Image.new("RGB", (15, 15), "white")
    pixel = im.load()
    sample_image = [[(0, 0, 0)]*10 for i in range(10)]
    assembly.put_picture(sample_image, 10, 10, pixel, 2, 2)
    assembly.print_board(pixel, 10, 10)


def test_all():
    results_to_print = [(1, 1, 5, 5, ""), (7, 8, 6, 6, ""), (15, 15, 3, 3, "")]
    board = assembly.assemble_pictures(20, 20, results_to_print)
    assembly.print_board(board, 20, 20)


# test_printing_image()
test_all()
