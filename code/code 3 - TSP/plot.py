import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

data = []
x_labels = []

with open('csvreport.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[1]), float(row[2]), float(row[3])])
            x_labels.append(row[0])

data = np.array(data)

data_std = np.array([[1, 2, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1], [1, 2, 1],  [1, 2, 1], [1, 2, 1]])

length = len(data)

# Set plot parameters
fig, ax = plt.subplots()
width = 0.2 # width of bar
x = np.arange(length)

ax.bar(x, data[:,0], width, color='goldenrod', label='Optimal Cost Known')
ax.bar(x + width, data[:,1], width, color='indianred', label='Cheapest Insertion Cost')
ax.bar(x + (2 * width), data[:,2], width, color='midnightblue', label='Nearest Neighbour Cost')

ax.set_ylabel('Cost')
ax.set_ylim(0, np.amax(data) + 1)
ax.set_xticks(x + width + width/2)
ax.set_xticklabels(x_labels)
ax.set_xlabel('Filename')
ax.set_title('Cost between methods in all cities')
ax.legend()
plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)

fig.tight_layout()
plt.show()
