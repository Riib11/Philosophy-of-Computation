"""
makes a random language with the following parameters:

"""

import sys
import random
import numpy
random.seed()


A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
  argv = sys.argv
  argl = len(argv)
  length        = int(argv[1]) if argl > 1 else 1000
  spaces_chance = float(argv[2]) if argl > 2 else 0.1
  make_tsv(length, spaces_chance)

def make_tsv(length, spaces_chance):
  filename = (
    "randlang/randlang"
    + "_len=" + str(length)
    + "_sc=" + str(spaces_chance)
    + ".txt"
  )
  
  def next_letter():
    return random.choice(A)
  
  with open(filename, "w+") as file:
    s = ""
    for _ in range(length):
      # choose letter
      if random.uniform(0,1) > spaces_chance:
        s += next_letter()
      # choose space
      else:
        s += " "
    file.write(s)


main()
