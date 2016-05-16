from placement import placement1
import pictures_assembly as assembly


def fitness_pixels(solution_array):
    fitness = 0
    distributed = placement1(im_w, im_h, solution_array)
    current_board = assembly.assemble_pictures(im_w, im_h, distributed).load()
    for i in range(im_w):
        for j in range(im_h):
            if current_board[i, j] == (0, 0, 0):
                fitness += 1
    #print "Counted fitness "+str(fitness)
    return fitness


def fitness_amount_of_images(solution_array):
    distributed = placement1(im_w, im_h, solution_array)
    fitness = amount_of_pictures - len(distributed)
    for pic in distributed:
        left_top_corner_x, left_top_corner_y, size_x, size_y, picture_name = pic
        for pic1 in distributed:
            left_top_corner_x1, left_top_corner_y1, size_x1, size_y1, picture_name1 = pic1
            if picture_name != picture_name1:
                if check_boundaries(left_top_corner_x, left_top_corner_y, size_x, size_y,
                                    left_top_corner_x1, left_top_corner_y1):
                    fitness += overlap_penalty
    #print "Fitness: "+str(fitness)
    return fitness


def check_boundaries(left_top_corner_x, left_top_corner_y, size_x, size_y,
                     left_top_corner_x1, left_top_corner_y1):
    if left_top_corner_x < left_top_corner_x1 and left_top_corner_y < left_top_corner_y1 \
            and left_top_corner_x+size_x > left_top_corner_x1 and left_top_corner_y+size_y > left_top_corner_y1:
        return False
    return True


def set_sizes(width, height, penalty, len_pictures):
    global im_w
    global im_h
    global amount_of_pictures
    global overlap_penalty
    overlap_penalty = penalty
    im_w = width
    im_h = height
    amount_of_pictures = len_pictures
