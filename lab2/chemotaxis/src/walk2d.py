import matplotlib.pyplot as plt
import numpy as np
import random
random.seed()

from PIL import Image
from PIL import ImageDraw

from colors import COLORS
from la import *
from util import *
from tqdm import tqdm

# TRIALS = 10000
# STEPS  = 1000
TRIALS = 10000
STEPS = 1000

STEP_ABS_MAX = 1

BINS = 100

def main():

  endpoints_x = []
  endpoints_y = []
  for trial_i in tqdm(range(TRIALS)):
    x, y = 0, 0 # start at origin
    for step_i in range(STEPS):
      x += random.uniform(-STEP_ABS_MAX, STEP_ABS_MAX)
      y += random.uniform(-STEP_ABS_MAX, STEP_ABS_MAX)
    endpoints_x.append(x)
    endpoints_y.append(y)

  plt.figure(figsize=(8, 8), dpi=80, facecolor='w')
  plt.hist2d(endpoints_x, endpoints_y, bins = BINS)

  plt.show()

main()
