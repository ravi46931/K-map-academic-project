import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x=np.arange(0,1.01,0.01)
y=np.zeros(101)
z=np.zeros(101)
mu=4.1
for i in range(101):
    k= mu*x[i]*(1-x[i])/(1+x[i])
    y[i]=mu*k*(1-k)/(1+k)
    z[i]=x[i]
plt.plot(x,y,color="black")
#plt.plot(x=0.6078,marker='o')
plt.plot(x,z)
for r in x:
    if r==0.61:
        plt.scatter(r,r,marker='o',facecolor='white', edgecolors='black')
plt.xlim(0,1)
plt.ylim(0,1)

plt.xlabel("$x$")
plt.ylabel("$K^2(x)$",rotation ='horizontal')
plt.grid(False)
plt.xticks([0,1])
plt.yticks([1,1])
plt.legend()
plt.show()