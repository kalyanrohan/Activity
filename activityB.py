import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
import statistics

f = pd.read_csv('activity.csv')
interval = []
steps = []
for i in f['interval'].unique():
    interval.append(i)
    steps.append(df.loc[df['interval']==i, 'steps'].dropna().mean())

dfB = pd.DataFrame({'Interval':interval, 'Steps':steps})
dfB.plot(x ='Interval', y='Steps', kind = 'line')
plt.title('Average number of steps taken in 5-minute intervals')
plt.xticks(np.linspace(0,2355,15))
plt.show()
print(f"Interval with max number of average steps is {dfB.loc[dfB['Steps']==dfB['Steps'].max(), 'Interval'].item()}.")

