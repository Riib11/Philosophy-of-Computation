from PIL import Image, ImageDraw
import math
from math import pi, cos, sin
import random
random.seed(1)

parent_dir = "reflection"
classes = ['reflected', 'random']

n       = 1000
size    = (28, 28)
imgtype = 'PNG'
mode    = '1'

if   mode == 'RGB' : color = { 'black':(0,0,0), 'white':(255,255,255) }
elif mode == '1'   : color = { 'black':0,       'white':1 }

background_color = color['white']

def rotate(p, t):
    x, y = p
    return (x*cos(t) - y*sin(t), y*cos(t) + x*sin(t))

def translate(p, v):
    x, y = p
    dx, dy = v
    return (x + dx, y + dy)

shape_width = 28-2
shape_height = 28-2
shape_thickness = 1

center = (size[0]/2, size[1]/2)

def draw_top_tower(draw, i, height):
    draw.rectangle([
            ((i+1)*shape_thickness,   center[1]),
            ((i+2)*shape_thickness-1, center[1]-height+1)
        ], color['black'])

def draw_bot_tower(draw, i, height):
    draw.rectangle([
            ((i+1)*shape_thickness,   center[1]),
            ((i+2)*shape_thickness-1, center[1]+height-1)
        ], color['black'])

def create_reflected(i):
    fn = "{dir}_{mode}/{cls}/{i}.png".format(dir=parent_dir, mode=mode, cls=classes[0], i=i)
    img = Image.new(mode, size, background_color)
    draw = ImageDraw.Draw(img)

    iterations = int(shape_width/shape_thickness)
    heights    = [ random.randint(0,shape_height/2) for _ in range(iterations) ]
    for i in range(iterations):
        draw_top_tower(draw, i, heights[i])
        draw_bot_tower(draw, i, heights[i])
    return fn, img

def create_random(i):
    fn = "{dir}_{mode}/{cls}/{i}.png".format(dir=parent_dir, mode=mode, cls=classes[1], i=i)
    img = Image.new(mode, size, background_color)
    draw = ImageDraw.Draw(img)

    iterations = int(shape_width/shape_thickness)

    heights_top = [ random.random()*(shape_height/2) for _ in range(iterations) ]
    heights_bot = [ random.random()*(shape_height/2) for _ in range(iterations) ]

    iterations = int(shape_width/shape_thickness)
    heights    = [ random.randint(0,shape_height/2) for _ in range(iterations) ]
    for i in range(iterations):
        draw_top_tower(draw, i, heights_top[i])
        draw_bot_tower(draw, i, heights_bot[i])
    return fn, img

# create reflecteds
# for i in tqdm(range(n)):
for i in range(n):
    fn, img = create_reflected(i)
    img.save(fn, imgtype)
    fn, img = create_random(i)
    img.save(fn, imgtype)
