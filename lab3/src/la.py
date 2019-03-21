from math import *

class vec2:
  def __init__(self, xs):
    self.xs = list(xs)
    self.x = self.xs[0]
    self.y = self.xs[1]

  def __getitem__(self, i): return self.xs[i]

  def tostring(self): return "V" + str(self.xs)
  __str__ = tostring
  __repr__ = tostring

  # make a new vector by mapping the elements f over zipped v1,v2
  @classmethod
  def combine(cls, f, v1, v2): return cls(
    map(lambda xy: f(xy[0], xy[1]), zip(v1.xs, v2.xs)))

  # make a new vector by mapping f over v
  @classmethod
  def map(cls, f, v): return cls(map(lambda x: f(x), v.xs))

  def __add__(v, w): return vec2.combine(lambda x,y: x + y, v, w)
  def __sub__(v, w): return vec2.combine(lambda x,y: x - y, v, w)

  def __rmul__(v, a): return vec2.map(lambda x: a * x, v)

  # dot product
  def dot(v, w): return (v[0] * w[0]) + (v[1] * w[1])

  # magnitude
  def mag(v): return sqrt(v.dot(v))

  def normalized(v): return (1/v.mag()) * v

  def int(v): return vec2.map(int, v)

  def tup(v): return (v[0], v[1])

def rotate(t, v):
  a, b, c, d = cos(t), -sin(t), sin(t), cos(t)
  x, y = v.tup()
  return vec2([ a*x + b*y, c*x + d*y ])

def distance_between(v, w): return (v - w).mag()

if __name__ == "__main__":
  v = vec2([1,2])
  w = vec2([3,4])

  print(10 * v)
  print(v + v + w)
