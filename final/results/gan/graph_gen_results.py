import matplotlib.pyplot as plt
import numpy as np
import os

##############################################################################################################################
# read data

def parse_percent(s):
    s = s.replace('%','')
    s = s.replace(',','')
    return float(s)/100

# read validation accuracies
discriminator_accuracies = []
generator_accuracies = []

experiments = ['solidcolor', 'reflection', 'simpleshape', 'matching']

for name in experiments:
    fn = '%s_1__log.txt' % name
    dis_loses = []
    dis_accus = []
    gen_loses = []
    gen_accus = []
    with open(fn, 'r+') as file:
        lines = [l for l in file]
        lines = lines[:1000]
        lines = [ lines[i] for i in range(0, len(lines), 50) ]
        for line in lines:
            line = line.split()
            dis_loses.append( float(line[3][:-1]) )
            dis_accus.append( float(line[5][:-1]) )
            gen_loses.append( float(line[8][:-1]) )
            gen_accus.append( float(line[10][:-1]) )
    discriminator_accuracies.append((name, dis_accus))
    generator_accuracies.append((name, gen_accus))

##############################################################################################################################
# plot data

# setup
fig, ax = plt.subplots()

# labels
plt.title('GAN Training Progress - Generator')
plt.ylabel('generator accuracy')
plt.xlabel('epoch')

# data
step = 1
max_i = len(generator_accuracies[0][1])*step
epochs = np.arange(0, max_i, step)
print(epochs)

for name, gen_accus in generator_accuracies:
    ax.plot(epochs, gen_accus, label=name)
plt.axis([1, epochs[-1],  0, 1.05])

# new_labels = epochs
# ax.set_xticklabels(new_labels)

# legend
legend = ax.legend(loc='lower center')

# show
plt.show()
