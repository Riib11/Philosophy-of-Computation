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

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
L_dist = [0.05374041792491895, 0.1911309064915157, 0.25082677134427916, 0.20245826305636633, 0.1098912937358394, 0.06877099191239759, 0.050815998348140594, 0.03101164044676513, 0.020194879011398055, 0.01092000264836155, 0.0062707815023167555, 0.0023240494794735146, 0.0011300424074504247, 0.00039052111002258963, 9.987465170117953e-05, 1.6832806466490933e-05, 4.488748391064249e-06, 2.2443741955321245e-06]


def main():
  argv = sys.argv
  argl = len(argv)
  assert argl == 2

  length = int(argv[1])
  
  make_tsv(length)

def make_tsv(length):
  filename = (
    "randlengths/randlengths"
    + "_len=" + str(length)
    + ".txt"
  )

  print("[*] selecting letters...")
  letters = iter(numpy.random.choice(A, length * 10, p=A_dist))
  print("[*] finished!")

  print("[*] selecting word lengths...")
  lengths = iter(numpy.random.choice(L, length, p=L_dist))
  print("[*] finished!")
  
  with open(filename, "w+") as file:
    s = ""
    for _ in range(length):
      # choose word length
      l = lengths.__next__()
      for _ in range(l):
        # choose letter
        s += letters.__next__()
      # end word
      s += " "
    file.write(s)

main()
