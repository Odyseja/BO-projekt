from filesSize import get_image_size
from distribute_pictures import distribute_pictures
import pictures_assembly as assembly
import os

def generate(dir_name, width, height):
    pictures = get_image_size(dir_name)
    distributed = distribute_pictures(width, height, pictures)
    result = assembly.assemble_pictures(width, height, distributed, dir_name)
    assembly.write_board_to_file(result, "out" + os.path.sep + "output.png")
    return result
