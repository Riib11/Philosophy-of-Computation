from PIL import Image, ImageDraw
import math
from math import pi, cos, sin
import random
random.seed(1)

parent_dir = 'simpleshape'

classes = ['square', 'triangle']

n       = 1000
size    = (28, 28)
imgtype = 'PNG'
mode    = '1'

if   mode == 'RGB' : color = { 'black':(0,0,0), 'white':(255,255,255) }
elif mode == '1'   : color = { 'black':0,       'white':1 }

shape_radius = 12

background_color = color['white']

def rotate(p, t):
    x, y = p
    return (x*cos(t) - y*sin(t), y*cos(t) + x*sin(t))

def translate(p, v):
    x, y = p
    dx, dy = v
    return (x + dx, y + dy)

def create_square(i):
    fn = '{dir}_{mode}/{cls}/{i}.png'.format(dir=parent_dir, mode=mode, cls=classes[0], i=i)
    img = Image.new(mode, size, background_color)
    draw = ImageDraw.Draw(img)

    center_x = random.random()*(size[0] - 2*shape_radius) + shape_radius
    center_y = random.random()*(size[1] - 2*shape_radius) + shape_radius
    center = (center_x, center_y)

    rotation = random.random() * 1/2*pi

    unit = (0, shape_radius)
    points = [ translate(rotate(unit, t+rotation), center) for t in [0/2*pi, 1/2*pi, 2/2*pi, 3/2*pi] ]

    draw.line(points + [points[0]], fill=color['black'])
    return fn, img

def create_triangle(i):
    fn = '{dir}_{mode}/{cls}/{i}.png'.format(dir=parent_dir, mode=mode, cls=classes[1], i=i)
    img = Image.new(mode, size, background_color)
    draw = ImageDraw.Draw(img)

    center_x = random.random()*(size[0] - 2*shape_radius) + shape_radius
    center_y = random.random()*(size[1] - 2*shape_radius) + shape_radius
    center = (center_x, center_y)

    rotation = random.random() * 2/3*pi

    unit = (0, shape_radius)
    points = [ translate(rotate(unit, t+rotation), center) for t in [0/3*pi, 2/3*pi, 4/3*pi] ]

    draw.line(points + [points[0]], fill=color['black'])
    return fn, img

# create squares
for i in range(n):
    fn, img = create_square(i)
    img.save(fn, imgtype)

# create triangles
for i in range(n):
    fn, img = create_triangle(i)
    img.save(fn, imgtype)
