import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("csvreport.csv")

df.pivot("m", "instance", "seconds").plot(kind='bar')
plt.xlabel('m size')
plt.ylabel('seconds')

# df.pivot("m", "instance", "cost").plot(kind='bar')
# plt.xlabel('m size')
# plt.ylabel('total cost')
plt.show()
