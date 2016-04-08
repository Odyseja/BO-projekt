# BOARD - rectangle
#	left top corner (0,0)
#	right bottom corner (max_x - 1, max_y -1)

# INPUT:
# max_x - width of board
# max_y - height of board
# pictures = [
# (width, height, picture_name),
# (width, height, picture_name),
# (width, height, picture_name) ]

# OUTPUT: result=[
# (left_top_corner_x, left_top_corner_y, size_x, size_y, picture_name),
# (left_top_corner_x, left_top_corner_y, size_x, size_y, picture_name),
# (left_top_corner_x, left_top_corner_y, size_x, size_y, picture_name) ]

# ALGORITHM:
#   sort pictures descending by heights
#   iterate over sorted pictures
#       1. put picture in the left top corner
#       2. add as many pictures as you can in the row
#       3. go below and start new row
#       4. go to 1.
#
#  if run out of space -> return empty list
#  if success -> return result


def distribute_pictures(max_x, max_y, pictures):
    # sort pictures by heights in descending order
    pictures = sorted(pictures, key=lambda picture: picture[1], reverse=True)
    result = []
    next_y = current_x = current_y = 0
    for picture in pictures:
        # check picture sizes
        if picture[0] > max_x:
            print("Picture {} is too wide".format(picture[2]))
            return []
        if picture[1] > max_y:
            print("Picture {} is too high".format(picture[2]))
            return []

        # update current_y if necessary
        if current_x + picture[0] > max_x or next_y == 0:
            current_x = 0
            current_y = next_y
            next_y = next_y + picture[1]
            if next_y > max_y:
                print("This algorithm cannot distribute so much pictures.\n" + \
                      "Board is too small: {} {}".format(max_x, max_y))
                return []

        # add tuple to result
        result.append((current_x, current_y, picture[0], picture[1], picture[2]))
        # update current_x
        current_x += picture[0]

    return result