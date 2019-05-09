'''
DCGAN on MNIST using Keras
Author: Rowel Atienza
Project: https://github.com/roatienza/Deep-Learning-Experiments
Dependencies: tensorflow 1.0 and keras 2.0
Usage: python3 dcgan_mnist.py
'''

# tensorflow
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

# keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Reshape
from keras.layers import Conv2D, Conv2DTranspose, UpSampling2D
from keras.layers import LeakyReLU, Dropout
from keras.layers import BatchNormalization
from keras.optimizers import Adam, RMSprop

# matplotlib
import matplotlib.pyplot as plt

# PIL
from PIL import Image

# utilities
from tqdm import tqdm
import time, os

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

class ElapsedTimer(object):
    def __init__(self):
        self.start_time = time.time()
    def elapsed(self,sec):
        if sec < 60:
            return str(sec) + " sec"
        elif sec < (60 * 60):
            return str(sec / 60) + " min"
        else:
            return str(sec / (60 * 60)) + " hr"
    def elapsed_time(self):
        print("Elapsed: %s " % self.elapsed(time.time() - self.start_time) )

class DCGAN(object):
    def __init__(self, img_rows=28, img_cols=28, channel=1):

        self.img_rows = img_rows
        self.img_cols = img_cols
        self.channel = channel
        self.D = None   # discriminator
        self.G = None   # generator
        self.AM = None  # adversarial model
        self.DM = None  # discriminator model

    # (W−F+2P)/S+1
    def discriminator(self):
        if self.D:
            return self.D
        self.D = Sequential()
        depth = 64
        dropout = 0.4
        # In: 28 x 28 x 1, depth = 1
        # Out: 14 x 14 x 1, depth=64
        input_shape = (self.img_rows, self.img_cols, self.channel)
        self.D.add(Conv2D(depth*1, 5, strides=2, input_shape=input_shape,\
            padding='same'))
        self.D.add(LeakyReLU(alpha=0.2))
        self.D.add(Dropout(dropout))

        self.D.add(Conv2D(depth*2, 5, strides=2, padding='same'))
        self.D.add(LeakyReLU(alpha=0.2))
        self.D.add(Dropout(dropout))

        self.D.add(Conv2D(depth*4, 5, strides=2, padding='same'))
        self.D.add(LeakyReLU(alpha=0.2))
        self.D.add(Dropout(dropout))

        self.D.add(Conv2D(depth*8, 5, strides=1, padding='same'))
        self.D.add(LeakyReLU(alpha=0.2))
        self.D.add(Dropout(dropout))

        # Out: 1-dim probability
        self.D.add(Flatten())
        self.D.add(Dense(1))
        self.D.add(Activation('sigmoid'))
        self.D.summary()
        return self.D

    def generator(self):
        if self.G:
            return self.G
        self.G = Sequential()
        dropout = 0.4
        depth = 64+64+64+64
        dim = 7
        # In: 100
        # Out: dim x dim x depth
        self.G.add(Dense(dim*dim*depth, input_dim=100))
        self.G.add(BatchNormalization(momentum=0.9))
        self.G.add(Activation('relu'))
        self.G.add(Reshape((dim, dim, depth)))
        self.G.add(Dropout(dropout))

        # In: dim x dim x depth
        # Out: 2*dim x 2*dim x depth/2
        self.G.add(UpSampling2D())
        self.G.add(Conv2DTranspose(int(depth/2), 5, padding='same'))
        self.G.add(BatchNormalization(momentum=0.9))
        self.G.add(Activation('relu'))

        self.G.add(UpSampling2D())
        self.G.add(Conv2DTranspose(int(depth/4), 5, padding='same'))
        self.G.add(BatchNormalization(momentum=0.9))
        self.G.add(Activation('relu'))

        self.G.add(Conv2DTranspose(int(depth/8), 5, padding='same'))
        self.G.add(BatchNormalization(momentum=0.9))
        self.G.add(Activation('relu'))

        # Out: 28 x 28 x 1 grayscale image [0.0,1.0] per pix
        self.G.add(Conv2DTranspose(1, 5, padding='same'))
        self.G.add(Activation('sigmoid'))
        self.G.summary()
        return self.G

    def discriminator_model(self):
        if self.DM:
            return self.DM
        optimizer = RMSprop(lr=0.0002, decay=6e-8)
        self.DM = Sequential()
        self.DM.add(self.discriminator())
        self.DM.compile(loss='binary_crossentropy', optimizer=optimizer,\
            metrics=['accuracy'])
        return self.DM

    def adversarial_model(self):
        if self.AM:
            return self.AM
        optimizer = RMSprop(lr=0.0001, decay=3e-8)
        self.AM = Sequential()
        self.AM.add(self.generator())
        self.AM.add(self.discriminator())
        self.AM.compile(loss='binary_crossentropy', optimizer=optimizer,\
            metrics=['accuracy'])
        return self.AM

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

class CUSTOM_DCGAN(object):
    def __init__(self, name):
        self.name = name
        self.training_dir = name

        self.img_rows = 28
        self.img_cols = 28
        self.channel = 1

        self.classes        = []
        self.images         = []
        self.images_classes = []

        for directory in os.listdir(self.training_dir):
            if directory.endswith('.DS_Store'): continue
            classname = directory
            self.classes.append(classname)
            img_cls = len(self.classes) - 1
            images_dir = '{train_dir}/{cls_dir}'.format(train_dir=self.training_dir, cls_dir=classname)
            for filename in tqdm(os.listdir(images_dir)):
                if not filename.endswith('.png'): continue
                image_fn = '{img_dir}/{img_fn}'.format(img_dir=images_dir, img_fn=filename)
                img_arr = np.array(Image.open(image_fn), dtype='int32')
                self.images.append(img_arr)
                self.images_classes.append(img_cls)
            # only train on first class
            break

        self.images         = np.array(self.images).reshape(-1, self.img_rows, self.img_cols, 1)
        self.images_classes = np.array(self.images_classes)
        self.num_classes    = len(self.classes)
        self.num_images     = len(self.images)

        print('loaded {0} classes: {1}'.format(self.num_classes, self.classes))
        print('loaded {0} images'.format(self.num_images))

        self.DCGAN = DCGAN()
        self.discriminator =  self.DCGAN.discriminator_model()
        self.adversarial = self.DCGAN.adversarial_model()
        self.generator = self.DCGAN.generator()

    def next_batch(self, batchsize):
        return self.images[ np.random.randint(0, self.images.shape[0], size=batchsize), :, :, :]

    def train(self, iterations, batchsize, save_interval=0):
        self.iterations = iterations
        self.batchsize = batchsize

        noise_input = None
        if save_interval > 0:
            noise_input = np.random.uniform(-1.0, 1.0, size=[16, 100])
        for i in range(iterations):
            # real images
            images_train = self.next_batch(batchsize)

            # fake images
            noise = np.random.uniform(-1.0, 1.0, size=[batchsize, 100])
            images_fake = self.generator.predict(noise)

            x = np.concatenate((images_train, images_fake))
            y = np.ones([2*batchsize, 1])
            y[batchsize:, :] = 0
            d_loss = self.discriminator.train_on_batch(x, y)

            y = np.ones([batchsize, 1])
            noise = np.random.uniform(-1.0, 1.0, size=[batchsize, 100])
            a_loss = self.adversarial.train_on_batch(noise, y)
            log_mesg = "%d: [D loss: %f, acc: %f]" % (i, d_loss[0], d_loss[1])
            log_mesg = "%s  [A loss: %f, acc: %f]" % (log_mesg, a_loss[0], a_loss[1])
            print(log_mesg)
            if save_interval>0:
                if (i+1)%save_interval==0:
                    self.plot_images(save2file=True, fake=True, samples=noise_input.shape[0], noise=noise_input, step=(i+1))

    def plot_images(self, save2file, fake, samples, noise, step=None):
        attributes = {
             'batchsize': self.batchsize,
              'realness': 'fake' if fake else 'real',
               'samples': samples,
                  'step': step if not step is None else self.iterations,
                 'noise': 'some' if not noise is None else 'none'
        }

        filename = self.name + '_' + '_'.join([ '%s=%s' % (k,v) for (k,v) in attributes.items() ])

        # choose images
        if fake:
            if noise is None: noise = np.random.uniform(-1.0, 1.0, size=[samples, 100])
            images = self.generator.predict(noise)
        else:
            i = np.random.randint(0, self.images.shape[0], samples)
            images = self.images[i, :, :, :]

        plt.figure(figsize=(10,10))
        for i in range(images.shape[0]):
            plt.subplot(4, 4, i+1)
            image = images[i, :, :, :]
            image = np.reshape(image, [self.img_rows, self.img_cols])
            plt.imshow(image, cmap='gray')
            plt.axis('off')
        plt.tight_layout()
        if save2file:
            plt.savefig('%s.png' % filename)
            plt.close('all')
        else:
            plt.show()

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

if __name__ == '__main__':
    custom_dcgan = CUSTOM_DCGAN("solidcolor_1")

    timer = ElapsedTimer()
    custom_dcgan.train(iterations=1000, batchsize=32, save_interval=5)
    # custom_dcgan.train(iterations=10000, batchsize=256, save_interval=500)
    timer.elapsed_time()

    custom_dcgan.plot_images(save2file=True, fake=True,  samples=16, noise=None)
    custom_dcgan.plot_images(save2file=True, fake=False, samples=16, noise=None)
