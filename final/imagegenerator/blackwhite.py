from PIL import Image

blackwhite_dir = "blackwhite/"
black_dir = blackwhite_dir + "black/"
white_dir = blackwhite_dir + "white/"

size = (10, 10)
type = 'PNG'
mode = '1'

color = {
    'black': 0,
    'white': 1
}

def create_solid(color, dir, suffix):
    img = Image.new(mode, size, color)
    fn = "{0}{1}.png".format(dir, suffix)
    return img, fn

img, fn = create_solid(color['black'], black_dir, 0)
img.save(fn, type)
