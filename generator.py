from filesSize import get_image_size
from placement import placement1
import pictures_assembly as assembly
import bees
import os
import fitness_counter


def generate(dir_name, width, height, max_gens, num_bees, num_sites, elite_sites, patch_size, elite_bees, other_bees, overlap_penalty, patch_decrease_factor=0.95):
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

    # fitness = fitness_counter.fitness_pixels
    fitness = fitness_counter.fitness_amount_of_images
    pictures = get_image_size(dir_name)
    x = 0
    y = 0
    for pic in pictures:
        w, h, fil = pic
        x += w
        y += h
    print str(len(pictures))
    print str(x)+" "+str(y)
    fitness_counter.set_sizes(width, height, overlap_penalty, len(pictures))
    pics, chart = bees.search(fitness, max_gens, pictures, num_bees, num_sites,
                              elite_sites, patch_size, elite_bees, other_bees, patch_decrease_factor)
    distributed = placement1(width, height, pics)
    result = assembly.assemble_pictures(width, height, distributed, dir_name)
    assembly.write_board_to_file(result, "out" + os.path.sep + "output.png")
    return result


if __name__ == "__main__":
    generate("splitted", 750, 394, 1000, 20, 4, 3, 3, 2, 3, 0.1)
