import pictures_assembly as assembly
from PIL import Image


def test_printing_image():
    im = Image.new("RGB", (15, 15), "white")
    board = im.load()
    sample_image_to_put = Image.new("RGB", (15, 15), "black").load()
    assembly.put_picture(board, sample_image_to_put, 10, 10, 2, 2)
    assembly.print_board(board, 10, 10)


def test_all_mocked():
    max_x = 20
    max_y = 20
    results_to_print = [(1, 1, 5, 5, ""), (7, 8, 6, 6, ""), (15, 15, 3, 3, "")]
    board = assembly.assemble_pictures(max_x, max_y, results_to_print)
    assembly.print_board(board.load(), max_x, max_y)


def test_all_real():
    max_x = 100
    max_y = 100
    results_to_print = [(1, 1, 50, 50, "1.jpg"), (60, 65, 30, 30, "2.jpg")]
    board = assembly.assemble_pictures(max_x, max_y, results_to_print, "images")
    assembly.print_board(board.load(), max_x, max_y)
    assembly.write_board_to_file(board,  "images/test_output.jpg")

test_printing_image()
#test_all_mocked()
#test_all_real()
