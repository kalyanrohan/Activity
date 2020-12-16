import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
import statistics


f = pd.read_csv('activity.csv')
print(pd.isnull(f).sum())
f1 = f.fillna(0)
print(pd.isnull(f1).sum())

days = []
steps = []
for i in f1['date'].unique():
    days.append(i)
    steps.append(f1.loc[f['date']==i, 'steps'].sum())


plot1 = pd.DataFrame({'Days':days, 'Steps':steps})
ax = plot1.plot.bar(x='Days', y='Steps', width=0.5 , color='g')
plt.title('Total Number of Steps Per Day')
plt.xlabel('Days')
plt.ylabel('Steps')
plt.xticks(rotation = 45, size=7)
plt.show()
print("Report:")
print(f"Mean: {plot1.mean().item()}")
print(f"Median: {plot1.median().item()}")