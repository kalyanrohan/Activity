import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
import statistics


f= pd.read_csv('activity.csv')
my_dict={}
for row in f:
    if row[0] != '0' and row[1] != 'date' and row [0] != 'NA':
        if row[1] not in my_dict:
            my_dict[row[1]] = [int(row[0])]
        else:
            my_dict[row[1]].append(int(row[0]))

total = {}
mean ={}
median= {}
for key, value in my_dict.items():
    total[key] = sum(value)
    mean[key] = round(mean(value),2)
    median[key] = median(value)

print(total)
print(mean)
print(median)

num = len(my_dict)
meantotalperday = tuple(mean.values())
groups = np.arange(num)   
width = 0.6     

plotting = plt.bar(groups, meantotalperday, width)
plt.ylabel('Numbers of Steps ')
plt.title('Mean Total Step a Day')
plt.xticks(groups, tuple(mean.keys()))
plt.yticks(np.arange(0, 300, 20))
plt.show()


