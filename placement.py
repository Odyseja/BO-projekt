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
        
        x, y = start_item[0], max_y
        result.append( (x, y, im_w, im_h, im[2] ) )
        place.sort(key=lambda x: x[0])
    return result


def placement1(width, height, image, **kw):
    place = [(0, width, 0)] #x_min, x_max, y
    result = []
    for im in image:
        rank = sorted(place, key=lambda x: x[2])
        im_w, im_h = size(im)
        win = place[0]
        start, end = 0, -1
        start_item, end_item = place[0], place[-1]
        min_val = float("inf")
        for i in range(len(place)):
            if width - place[i][0] > im_w and place[i][2] < min_val:
                max_val = place[i][2]
                for j in range(i, len(place)):
                    if not place[j][2] < min_val:
                        break
                    max_val = max(max_val, place[j][2])
                    if place[j][1] >= place[i][0] + im_w:
                        start, end = i, j + 1
                        start_item = place[i]
                        end_item = place[j]
                        min_val = max_val
                        break
        else:
            if end == -1:
                "Skip element"
                continue

        max_y = max(place[start:end], key=lambda x: x[2])[2]
        if max_y + im_h > height:
            continue
        del place[start:end]
        place.append( (start_item[0], start_item[0] + im_w, max_y + im_h + 1) )
        place.append( (start_item[0] + im_w + 1, end_item[1], end_item[2]   ) )
        
        x, y = start_item[0], max_y
        result.append( (x, y, im_w, im_h, im[2] ) )
        place.sort(key=lambda x: x[0])
    return result

def sort_array(arr):
    sort(arr, key=lambda x: x[1])


def test_placement(arr, im_size):
    from PIL import Image, ImageDraw
    import random

    im = Image.new('RGBA', im_size, (255,255,255, 0) )
    dr = ImageDraw.Draw(im)
    for item in arr:
        x, y, w, h, _ = item
        xy = ( x, y, x+w, y+h )
        dr.rectangle(xy, fill=(random.randint(0, 255), random.randint(0,255), random.randint(0,255), 170))
    im.show()


placement = placement1

if __name__ == "__main__":
    arr = [
            (40, 140, None), (60, 20, None), (20, 20, None), (50, 10, None), 
            (50, 50, None), (20, 20, None), (20, 40, None), (20, 30, None), 
            (60, 50, None), (30, 30, None), (30, 30, None), (200, 100, None), 
            (50, 10, None), (10, 50, None), (60, 40, None), (70, 40, None), (80, 80, None)
          ]
    result = placement(300, 300, arr)
    test_placement(result, (300, 300))

