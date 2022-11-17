import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

result1 = pd.read_csv('result1_stats_history.csv')
result2 = pd.read_csv('result2_stats_history.csv')
result3 = pd.read_csv('result3_stats_history.csv')
result4 = pd.read_csv('result4_stats_history.csv')


request1 = result1['Requests/s'].to_numpy()
request2 = result2['Requests/s'].to_numpy()
request3 = result3['Requests/s'].to_numpy()
request4 = result4['Requests/s'].to_numpy()

num = len(request1)
x = np.arange(num)
print(x)
plt.plot(x, request1, label="local vm")
plt.plot(x, request2, label="vm scale set")
plt.plot(x, request3, label="web app")
plt.plot(x, request4, label="function app")

plt.legend()
plt.show()
