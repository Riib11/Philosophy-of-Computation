from PIL import Image, ImageDraw
import math
from math import pi, cos, sin
import random
random.seed(1)

parent_dir = 'matching'

classes = ['same', 'different']

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

def rotation(t):
    return (lambda p: rotate(p, t))

def translate(p, v):
    x, y = p
    dx, dy = v
    return (x + dx, y + dy)

def translation(v):
    return (lambda p: translate(p, v))

def compose(fs):
    def apply(x):
        if len(fs) == 0:
            return x
        else:
            fx = fs[-1](x)
            return compose(fs[:-1])(fx)
    return apply

shape_radius = 7
shape_radius_min = 2
shape_points_range = range(4, 5+1)

center = (size[0]//2, size[1]//2)

def polygon_points(num_points):
    points = []
    for i in range(num_points):
        t = i * 2*pi/num_points
        r = (shape_radius - shape_radius_min)*random.random() + shape_radius_min
        x, y = int(r*cos(t)), int(r*sin(t))
        points.append((x,y))
    return points

def create_same(i):
    fn = '{dir}_{mode}/{cls}/{i}.png'.format(dir=parent_dir, mode=mode, cls=classes[0], i=i)
    img = Image.new(mode, size, background_color)
    draw = ImageDraw.Draw(img)

    num_points = random.choice(shape_points_range)
    poly = polygon_points(num_points)

    p = (0, (size[0]/2 - shape_radius))

    theta1 = random.random()*2*pi
    phi1   = random.random()*2*pi
    poly1 = list(map(compose([ translation(center), rotation(phi1), translation(p), rotation(theta1) ]), poly))
    draw.polygon(poly1, fill=color['black'])

    theta2 = random.random()*2*pi
    phi2   = phi1 + 0.5*pi + random.random()*pi
    poly2 = list(map(compose([ translation(center), rotation(phi2), translation(p), rotation(theta2) ]), poly))
    draw.polygon(poly2, fill=color['black'])

    return fn, img

def create_different(i):
    fn = '{dir}_{mode}/{cls}/{i}.png'.format(dir=parent_dir, mode=mode, cls=classes[1], i=i)
    img = Image.new(mode, size, background_color)
    draw = ImageDraw.Draw(img)

    num_points = random.choice(shape_points_range)
    poly1 = polygon_points(num_points)
    poly2 = polygon_points(num_points)

    p = (0, (size[0]/2 - shape_radius))

    theta1 = random.random()*2*pi
    phi1   = random.random()*2*pi
    poly1 = list(map(compose([ translation(center), rotation(phi1), translation(p), rotation(theta1) ]), poly1))
    draw.polygon(poly1, fill=color['black'])

    theta2 = random.random()*2*pi
    phi2   = phi1 + 0.5*pi + random.random()*pi
    poly2 = list(map(compose([ translation(center), rotation(phi2), translation(p), rotation(theta2) ]), poly2))
    draw.polygon(poly2, fill=color['black'])

    return fn, img

# create sames
for i in range(n):
    fn, img = create_same(i)
    img.save(fn, imgtype)
    fn, img = create_different(i)
    img.save(fn, imgtype)
