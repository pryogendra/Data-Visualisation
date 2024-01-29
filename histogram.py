import numpy as np 
import matplotlib.pyplot as plt 

data=np.random.randn(1000)

plt.hist(data,bins=10,edgecolor='green')
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()