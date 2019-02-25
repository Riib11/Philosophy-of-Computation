from math import *
from la import *

# generic surface in R3 with provided gradient
class Surface:
  def __init__(self,
    offset,  # vec2
    height,  # vec2 -> int
    gradient # vec2 -> vec2
  ):
    self.offset   = offset
    self.height   = lambda v: height(v - offset)
    self.gradient = lambda v: gradient(v - offset)

# parabola in R2 centered at `offset` with z=0
class Parabaloid(Surface):
  def __init__(self, offset):
    height   = lambda v: - (v.x**2 + v.y**2)
    gradient = lambda v: vec2([ 2*x.v, 2*v.y ])
    super().__init__(offset, height, gradient)

# parabola in R2 centered at `center` with z=0
# but, has to 4th power instead of 2nd
class Parabaloid4(Surface):
  def __init__(self, offset):
    height   = lambda v: - (v.x**4 + v.y**4)
    gradient = lambda v: vec2([ 4*x.v, 4*v.y ])
    super().__init__(offset, height, gradient)

class Cone(Surface):
  def __init__(self, offset):
    height   = lambda v: - sqrt(v.x**2 + v.y**2)
    gradient = lambda v: vec2 \
      ([ - (1/2) * (v.x**2 + v.y**2)**(-1/2) * 2*v.x,
         - (1/2) * (v.x**2 + v.y**2)**(-1/2) * 2*v.y ])
    super().__init__(offset, height, gradient)

class Laplace(Surface):
  def __init__(self, offset, r=2):
    height = lambda v: - (v.x**2 + v.y**2)**(1/r)
    gradient = lambda v: vec2 \
      ([ - (1/r) * (v.x**2 + v.y**2)**(-1/r) * 2*v.x,
         - (1/r) * (v.x**2 + v.y**2)**(-1/r) * 2*v.y ])
    super().__init__(offset, height, gradient)
