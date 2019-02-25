import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import random
random.seed()

from PIL import Image
from PIL import ImageDraw

from colors import COLORS
from la import *
from util import *
from tqdm import tqdm

TRIALS = 10000
STEPS  = 1000

STEP_ABS_MAX = 1

BINS = 100

def main():

  endpoints = []
  for trial_i in tqdm(range(TRIALS)):
    x = 0 # start at origin
    for step_i in range(STEPS):
      dx = random.uniform(-STEP_ABS_MAX, STEP_ABS_MAX)
      x += dx
    endpoints.append(x)

  plt.figure(figsize=(8, 8), dpi=80, facecolor='w')
  plt.hist(endpoints,
    bins      = BINS,
    histtype  = "bar",
    facecolor = "blue",
    density   = True)

  plt.show()

main()
