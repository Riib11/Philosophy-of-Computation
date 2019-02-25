L_dist = [(1, 47889), (2, 170320), (3, 223516), (4, 180414), (5, 97926), (6, 61283), (7, 45283), (8, 27635), (9, 17996), (10, 9731), (11, 5588), (12, 2071), (13, 1007), (14, 348), (15, 89), (16, 15), (17, 4), (18, 2)]

total = 0
for (length, count) in L_dist: total += count

# print(total)

L_dist_norm = []
for (length, count) in L_dist:
  L_dist_norm.append((length, count/total))

# print(L_dist_norm)

x,y = [], []
for (length, count) in L_dist_norm:
  x.append(length)
  y.append(count)

print(x)
print(y)
