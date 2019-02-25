from sys import argv

if len(argv) > 1:
  assert (argv[1].endswith(".tsv"))
  infile = open(argv[1], "r")
  
  lengths = []
  with open(argv[1], "r") as infile:
    for line in infile:
      xs = line.split()
      if len(xs) != 2:
        print(xs)
        continue
      lengths += [str(len(xs[0]))] * int(xs[1])

  with open(argv[1].replace(".tsv",".lengths.tsv"), "w+") as outfile:
    for l in lengths: outfile.write(l + "\n")

# if len(argv) > 1:
#   assert (argv[1].endswith(".tsv"))
#   infile = open(argv[1], "r")
  
#   lengths = {}
#   def add_length(word, count):
#     length = len(word)
#     if length not in lengths: lengths[length] = 0
#     lengths[length] += count

#   with open(argv[1], "r") as infile:
#     for line in infile:
#       xs = line.split()
#       if len(xs) != 2:
#         print(xs)
#         continue
#       add_length(xs[0], int(xs[1]))

#   lengths = sorted(lengths.items(), key=lambda x: x[0])
#   print(lengths)
  
#   with open(argv[1].replace(".tsv",".lengths.tsv"), "w+") as outfile:
#     for length, count in lengths:
#       outfile.write(str(length) + "\t" + str(count) + "\n")
