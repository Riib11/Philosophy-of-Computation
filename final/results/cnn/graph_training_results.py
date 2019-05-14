import matplotlib.pyplot as plt
import os

##############################################################################################################################
# read data

def parse_percent(s):
    s = s.replace('%','')
    s = s.replace(',','')
    return float(s)/100

# read validation accuracies
validation_accuracies = []

experiments = ['solidcolor', 'reflection', 'simpleshape', 'matching']


for exp in experiments:
    fn = '%s.txt' % exp
    valaccs = []
    with open(fn, 'r+') as file:
        for line in file:
            train_acc = parse_percent(line.split()[6])
            valacc   = parse_percent(line.split()[9])
            valaccs.append(train_acc)

    name = fn.replace('.txt', '')
    validation_accuracies.append((name,valaccs))

##############################################################################################################################
# plot data

# setup
fig, ax = plt.subplots()

# labels
plt.title('CNN Training Progress')
plt.ylabel('training accuracy')
plt.xlabel('epoch')

# data
epochs = range(1, len(validation_accuracies[0][1])+1)
for name, valaccs in validation_accuracies:
    ax.plot(epochs, valaccs, label=name)
plt.axis([1, epochs[-1],  0, 1.05])

# legend
legend = ax.legend(loc='lower center') #fontsize='x-large')

# show
plt.show()
