from filesSize import get_image_size
from placement import placement1
import pictures_assembly as assembly
import os

def generate(dir_name, width, height, max_gens, num_bees, num_sites, patch_size, elite_bees, other_bees, patch_decrease_factor):
    print "Generating with parameters: "
    print "dir: " + str(dir_name)
    print "width: " + str(width)
    print "height: " + str(height)
    print "max_gens: " + str(max_gens)
    print "num_bees: " + str(num_bees)
    print "num_sites: " + str(num_sites)
    print "patch_size: " + str(patch_size)
    print "elite_bees: " + str(elite_bees)
    print "other_bees: " + str(other_bees)
    print "patch_decrease_factor: " + str(patch_decrease_factor)

    pictures = get_image_size(dir_name)
    distributed = placement1(width, height, pictures)
    result = assembly.assemble_pictures(width, height, distributed, dir_name)
    assembly.write_board_to_file(result, "out" + os.path.sep + "output.png")
    return result


if __name__ == "__main__":
    generate("splitted", 750, 394, 1, 1, 1, 1, 1, 1, 1)