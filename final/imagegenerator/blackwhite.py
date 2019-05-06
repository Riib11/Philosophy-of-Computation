from PIL import Image

blackwhite_dir = "blackwhite/"
black_dir = blackwhite_dir + "black/"
white_dir = blackwhite_dir + "white/"

n = 100

size = (10, 10)
imgtype = 'PNG'
mode = 'RGB'

color = {
    'black': (0,0,0),
    'white': (255,255,255)
}

def create_solid(color, dir, suffix):
    img = Image.new(mode, size, color)
    fn = "{0}{1}.png".format(dir, suffix)
    return img, fn

# create blacks
for i in range(n):
    img, fn = create_solid(color['black'], black_dir, i)
    img.save(fn, imgtype)

# create whites
for i in range(n):
    img, fn = create_solid(color['white'], white_dir, i)
    img.save(fn, imgtype)
