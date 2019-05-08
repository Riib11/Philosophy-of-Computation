from PIL import Image

parent_dir = 'solidcolor'
classes = ['black', 'white']

n = 1000

size    = (28, 28)
imgtype = 'PNG'
mode    = 'RGB'
mode    = '1'

if   mode == 'RGB' : color = { 'black':(0,0,0), 'white':(255,255,255) }
elif mode == '1'   : color = { 'black':0,       'white':1 }

def create_solid(color):
    img = Image.new(mode, size, color)
    return img

for i in range(n):
    img1 = create_solid(color['black'])
    img1.save('{dir}_{mode}/{cls}/{fn}.png'.format(dir=parent_dir, mode=mode, cls=classes[0], fn=i))

    img2 = create_solid(color['white'])
    img2.save('{dir}_{mode}/{cls}/{fn}.png'.format(dir=parent_dir, mode=mode, cls=classes[1], fn=i))
