# coding: utf-8

import os
import math
import time
import json
from PIL import Image, ImageDraw


#def get_pic_size():


def save_debug_creenshot(im, x, y, y2):
    ts = int(time.time())
    draw = ImageDraw.Draw(im)
    # 对debug图片加上详细的注释
    #draw.point()
    draw.line((x, y, x, y2), fill=(255, 0, 0))
    del draw
    im.save('{}_d.png'.format(ts))

def get_screen_info(im,start_1,w):

    min_x = w
    max_x = 0
    point_y = 0
    im_pixel = im.load()
    for i in range(int(start_1),100,-3):
        for j in range(1,w,10):
            pixel0 = im_pixel[j,i]
            if abs(pixel0[0]-127) + abs(pixel0[1]-178) + abs(pixel0[2]-177) < 5:
                min_x = min(min_x,j)
                max_x = max(max_x,j)
                #save_debug_creenshot(im, min_x,i,max_x)
                if min_x < j and j < max_x:
                    point_y = i
                    break
        if min_x < j and j < max_x:
            break
    if point_y > 0:
        point_x = (min_x + max_x)/2
        r = int((max_x-min_x)/2)
        for j in range(point_y,point_y-r,-2):
            pixel0 = im_pixel[point_x, j]
            if abs(pixel0[0]-127) + abs(pixel0[1]-178) + abs(pixel0[2]-177) < 4:
                point_y = j + r
                break
        print('x:%d y:%d'% (point_x,point_y))
        #save_debug_creenshot(im, point_x, point_y, j)
        return j - 50

im = Image.open(r"D:\test.png")
w, h = im.size
start_y = h*2/3
while start_y > 100:
    start_y = get_screen_info(im,start_y,w)
    print(start_y)


