
getX = lambda im: (im[0], im[1])
getY = lambda im: (im[1], im[0])

def size(im):
    return im[0], im[1]

def placement2(width, height, image, **kw):
    place = [(0, width, 0)] #x_min, x_max, y
    result = []
    for im in image:
        rank = sorted(place, key=lambda x: x[2])
        im_w, im_h = size(im)
        win = place[0]
        start, end = 0, -1
        start_item, end_item = place[0], place[-1]
        for item in rank:
            if width - item[0] > im_w:
                start = place.index(item)
                start_item = item
                break
        for item in place:
            if item[1] > start_item[0] + im_w:
                end = place.index(item) + 1
                end_item = item
                break
        max_y = max(place[start:end], key=lambda x: x[2])[2]
        del place[start:end]
        place.append( (start_item[0], start_item[0] + im_w, max_y + im_h) )
        place.append( (start_item[0] + im_w, end_item[1], end_item[2]   ) )
        
        result.append( ((start_item[0], max_y), im) )
        place.sort(key=lambda x: x[0])
    return result


def placement1(width, height, images, direction=True, bidirection=True, **kw):
    x_array = [((0, width ), 0)]
    y_array = [((0, height), 0)]
    final_array = []
    direction_flag = direction
    for image in images:
        if direction_flag:
            magic(x_array, y_array, final_array, image, getX)
        else:
            magic(y_array, x_array, final_array, image, getY)
    return final_array
       

def magic(free_space_array, free_space_array2, final_array, image, size_fun):
    space = 0
    image_size = size_fun(image)
    m = start = free_space_array.pop()
    space += start[0][1] - start[0][0]
    max_s = start[1]
    while space > image_size[0] and free_space_array:
        m = free_space_array.pop()
        space += m[0][1] - m[0][0]
        max_s = max(max_s, m[1])
    xy_pos = (start[0][0], start[1])
    free_space_array.append( ( (xy_pos[0], xy_pos[0] + image_size[0] ), image_size[1]) )
    free_space_array.append( ((start[0][0] + image_size[0], max_s), m[1]) )
    change_items = [x for x in free_space_array2  if (xy_pos[1] <= x[0][0] < (xy_pos[1] + image_size[1])) or (xy_pos[1] < x[0][1] <= (xy_pos[1] + image_size[1])) ]
    for item in change_items:
        free_space_array2.remove(item)
    free_space_array2.append( ( (xy_pos[1], xy_pos[1] + image_size[1] ), image_size[0] ) )
    free_space_array2.append( ( (xy_pos[1] + image_size[1], change_items[-1][0][1] ), change_items[-1][1] ) )
     
    final_array.append( (xy_pos, image) )
    return (start[0], max_s)


def sort_array(arr):
    sort(arr, key=lambda x: x[1])


def test_placement(arr, im_size):
    from PIL import Image, ImageDraw
    import random

    im = Image.new('RGBA', im_size, (255,255,255, 0) )
    dr = ImageDraw.Draw(im)
    for item in arr:
        x, y = item[0]
        w, h = size(item[1])
        xy = ( x, y, x+w, y+h )
        dr.rectangle(xy, fill=(random.randint(0, 255), random.randint(0,255), random.randint(0,255), 170))
    im.show()


placement = placement2

if __name__ == "__main__":
    arr = [(40, 140), (60, 20), (20, 20), (50, 10), (50, 50), (20, 20), (20, 40), (20, 30), (60, 50), (30, 30), (30, 30), (200, 100), (50, 10), (10, 50), (60, 40), (70, 40), (80, 80)]
    result = placement(300, 300, arr)
    test_placement(result, (300, 300))

