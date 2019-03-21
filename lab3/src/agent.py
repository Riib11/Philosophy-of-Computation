from math import *
import random
random.seed()

from la import *

RUN_MAX = 20.0

# represents a bacteria that can move via chemotaxi
class Agent:
  def __init__(self,
    surface,    # vec2 -> vec2
    position,   # vec2
    orientation # vec2
  ):
    self.surface     = surface    
    self.position    = position    
    self.orientation = orientation

  # process next move
  # update to new position
  def step(self):
    self.tumble()
    self.run()

  # turn randomly
  def tumble(self):
    # theta = pi/8
    # noise = 1
    # # constant rotate CC pi/a radians
    # nt = random.uniform(-theta*noise, theta*noise)
    # self.orientation = rotate(theta + nt, self.orientation).normalized()
    
    t = random.uniform(0, 2*pi)
    x, y = cos(t), sin(t)
    self.orientation = vec2([x,y]).normalized()

  # run forward
  # distance weighted by how closely oriented to surface
  def run(self):
    # TODO: calculate run distance from (orientation, surface)

    # gradient at agent's position : vec2
    gra = self.surface.gradient(self.position)
    # how well oriented along gradient?
    ori  = self.orientation
    cos = gra.dot(ori) / (gra.mag() * ori.mag())
    # note that cos = cos(t)
    # cos ranges between in [-1,1], so adjust to make
    # negative values just a fraction of the step distance
    distance = RUN_MAX * (cos + 1) / 2

    # move forward by distance
    move = distance * self.orientation
    self.position = self.position + move
