import os
from PIL import Image

#dir=location where images are stored. In our case it's "photo"
#when the dir isn't in our fileSize.py location we have to give e.g. "C:\\Users\\beata_000\\Desktop\\BO\\photo"

#return list of image size: (width,height)

def get_image_size(dir):
    x =[]
    y=[]
    for root, dirs, files in os.walk(dir):
        for name in files:
            print name
            im = Image.open(dir + os.path.sep + name)
            print im.size
            x.append(im.size[0])
            y.append(im.size[1])
        list = zip(x,y, files)
        return list