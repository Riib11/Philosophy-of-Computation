"""
makes a random language with the following parameters:

"""

import sys
import random
import numpy.random
random.seed()


A = \
  [ 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p',
    'q', 'r', 's', 't',
    'u', 'v', 'w', 'x',
    'y', 'z']


A_dist = \
  [ 0.1116, 0.0849, 0.0758, 0.0754,
    0.0716, 0.0695, 0.0665, 0.0574,
    0.0549, 0.0453, 0.0363, 0.0338,
    0.0317, 0.0301, 0.0300, 0.0247,
    0.0207, 0.0181, 0.0178, 0.0129, 
    0.0110, 0.0101, 0.0029, 0.003,
    0.0020, 0.0020 ]

def main():
  argv = sys.argv
  argl = len(argv)
  length        = int(argv[1]) if argl > 1 else 1000
  spaces_chance = float(argv[2]) if argl > 2 else 0.1
  make_tsv(length, spaces_chance)

def make_tsv(length, spaces_chance):
  filename = (
    "randenlang/randenlang"
    + "_len=" + str(length)
    + "_sc=" + str(spaces_chance)
    + ".txt"
  )

  print("[*] selecting choices...")
  choices = iter(numpy.random.choice(A,
    int(((1-spaces_chance) + 0.05) * length),
    p=A_dist))
  print("[*] finished!")
  i = [0]
  def next_letter():
    i[0] += 1
    return choices[i[0]]
  
  with open(filename, "w+") as file:
    s = ""
    for _ in range(length):
      # choose letter
      if random.uniform(0,1) > spaces_chance:
        s += choices.__next__()
      # choose space
      else:
        s += " "
    file.write(s)


main()
